import os
import json
import asyncio
from typing import List
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

# === Define the schema ===
class Entity(BaseModel):
    name: str
    description: str

class Relationship(BaseModel):
    entity1: Entity
    entity2: Entity
    description: str
    relation_type: str

class KnowledgeGraph(BaseModel):
    entities: List[Entity]
    relationships: List[Relationship]

# === Main crawl & extract logic ===
async def main():
    # Define LLM extraction strategy using local Ollama
    llm_strat = LLMExtractionStrategy(
        llm_config=LLMConfig(
            provider="ollama/deepseek-r1:8b"
        ),
        schema=KnowledgeGraph.model_json_schema(),
        extraction_type="schema",
        instruction="Extract entities and relationships from the content. Return valid JSON.",
        chunk_token_threshold=800,
        apply_chunking=True,
        input_format="html",
        temperature=0.1,
        max_tokens=1000,
    )

    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strat,
        cache_mode=CacheMode.BYPASS,
    )

    async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
        # 🔗 CNBC Tesla Q4 2024 earnings article
        url = "https://www.washingtonpost.com/business/2025/03/28/trump-auto-tariffs-car-prices/"
        result = await crawler.arun(url=url, config=crawl_config)

        if result.success:
            with open("kb_result.json", "w", encoding="utf-8") as f:
                f.write(result.extracted_content)
            llm_strat.show_usage()
            print("✅ Extraction complete. Output saved to `kb_result.json`.")
        else:
            print("❌ Crawl failed:", result.error_message)

# === Run the script ===
if __name__ == "__main__":
    asyncio.run(main())
