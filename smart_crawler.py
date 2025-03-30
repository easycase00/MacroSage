import asyncio
import json
import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# === CONFIG ===
source_url = "Enter Your URL here"
query = "economic indicators, inflation, consumer confidence, interest rates, tariffs, recession"
top_k = 5

def extract_text_chunks(text, chunk_size=100, step=50):
    words = text.split()
    return [' '.join(words[i:i+chunk_size]) for i in range(0, len(words), step)]

def rank_chunks_with_query(chunks, query):
    vectorizer = TfidfVectorizer(stop_words='english', ngram_range=(1, 2))
    vectors = vectorizer.fit_transform([query] + chunks)
    similarities = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    return [(chunks[i], similarities[i]) for i in range(len(chunks))]

def get_article_links(url):
    print(f"🌐 Fetching from source: {url}")
    response = requests.get(url)
    response.raise_for_status()
    root = ET.fromstring(response.content)
    items = root.findall(".//item")
    links = [item.find("link").text for item in items if item.find("link") is not None]
    print(f"✅ Found {len(links)} links")
    return links

async def main():
    article_links = get_article_links(source_url)
    browser_cfg = BrowserConfig(headless=True)

    async with AsyncWebCrawler(config=browser_cfg) as crawler:
        scored_links = []

        for link in article_links:
            print(f"\n🔗 Crawling: {link}")
            sub_result = await crawler.arun(url=link, config=CrawlerRunConfig(
                extraction_strategy=None,
                cache_mode=CacheMode.BYPASS
            ))

            if not sub_result.success or not sub_result.cleaned_html:
                print(f"⚠️ Failed or empty content at: {link}")
                continue

            soup = BeautifulSoup(sub_result.cleaned_html, "html.parser")
            text = soup.get_text(separator=' ', strip=True)
            if not text:
                print("⚠️ No usable text found.")
                continue

            chunks = extract_text_chunks(text)
            ranked = rank_chunks_with_query(chunks, query)
            if ranked:
                top_score = max(score for _, score in ranked)
                print(f"🧠 Score: {top_score:.4f}")
                if top_score > 0.05:
                    scored_links.append((link, top_score))

        scored_links = sorted(scored_links, key=lambda x: x[1], reverse=True)[:top_k]

        print(f"\n🏆 Top {top_k} relevant pages:")
        for i, (url, score) in enumerate(scored_links, 1):
            print(f"{i}. {url} (score: {score:.4f})")

        # === LLM Extraction ===
        llm_strategy = LLMExtractionStrategy(
            llm_config=LLMConfig(provider="ollama/deepseek-r1:1.5b"),
            instruction="Extract only key economic insights: inflation %, interest rates, recession indicators, consumer sentiment. Return as valid JSON. No boilerplate.",
            extraction_type="text",
            apply_chunking=True,
            chunk_token_threshold=800,
            temperature=0.1
        )

        results = []
        for link, _ in scored_links:
            print(f"\n🤖 Extracting with LLM: {link}")
            result = await crawler.arun(url=link, config=CrawlerRunConfig(
                extraction_strategy=llm_strategy,
                cache_mode=CacheMode.BYPASS
            ))

            if not result.success:
                print(f"❌ Extraction failed: {link}")
                results.append({"url": link, "error": "LLM crawl failed"})
                continue

            try:
                content = result.extracted_content

                if isinstance(content, str):
                    parsed = json.loads(content)
                elif hasattr(content, "choices"):
                    parsed = json.loads(content.choices[0].message.content)
                else:
                    raise ValueError("Unsupported LLM response format")

                results.append({"url": link, "data": parsed})

            except Exception as e:
                print(f"⚠️ Parsing error: {e}")
                results.append({"url": link, "error": str(e)})

        with open("smart_results.json", "w", encoding="utf-8") as f:
            json.dump(results, f, indent=2)
        print("\n✅ Extraction results saved to smart_results.json")

if __name__ == "__main__":
    asyncio.run(main())
