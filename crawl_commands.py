import os
import json
import asyncio
from typing import List
from pydantic import BaseModel
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode, LLMConfig
from crawl4ai.extraction_strategy import LLMExtractionStrategy

# Define the schema for extracted data
class CPIReport(BaseModel):
    overall_cpi_change: str
    core_cpi_change: str
    energy_index_change: str
    food_index_change: str
    notable_increases: List[str]
    notable_decreases: List[str]

async def main():
    # Configure the LLM extraction strategy
    llm_strat = LLMExtractionStrategy(
        llm_config=LLMConfig(
            provider="ollama/deepseek-r1:8b"
        ),
        schema=CPIReport.model_json_schema(),
        extraction_type="schema",
        instruction=(
            "Extract the following information from the CPI report: "
            "1. Overall CPI change. "
            "2. Core CPI change (excluding food and energy). "
            "3. Energy index change. "
            "4. Food index change. "
            "5. Notable increases in specific categories. "
            "6. Notable decreases in specific categories. "
            "Return the information in JSON format."
        ),
        chunk_token_threshold=800,
        apply_chunking=True,
        input_format="html",
        temperature=0.1,
        max_tokens=1000,
    )

    # Configure the crawler
    crawl_config = CrawlerRunConfig(
        extraction_strategy=llm_strat,
        cache_mode=CacheMode.BYPASS,
    )

    # Initialize the web crawler
    async with AsyncWebCrawler(config=BrowserConfig(headless=True)) as crawler:
        # URL of the CPI report
        url = "https://www.bls.gov/news.release/cpi.nr0.htm"
        result = await crawler.arun(url=url, config=crawl_config)

        if result.success:
            # Save the extracted content to a JSON file
            with open("cpi_report.json", "w", encoding="utf-8") as f:
                f.write(result.extracted_content)
            llm_strat.show_usage()
            print("✅ Extraction complete. Output saved to `cpi_report.json`.")
        else:
            print("❌ Crawl failed:", result.error_message)

# Run the script
if __name__ == "__main__":
    asyncio.run(main())
