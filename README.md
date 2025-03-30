# 🧠 MacroSage: Economic Insight Extraction with Local LLMs

**MacroSage** is an AI-powered pipeline that crawls financial news and uses a locally deployed large language model (LLM) to extract structured economic insights — all running privately on your own machine.

It integrates a fully offline LLM (DeepSeek R1 8B) via [Ollama](https://ollama.com) to perform real-time semantic tagging and summarization of key macroeconomic signals like inflation, consumer sentiment, interest rates, and recession indicators.

---

## ⚙️ Technological Overview

MacroSage showcases practical local LLM deployment for real-world insight extraction. Built with Python and powered by **DeepSeek R1 8B** via Ollama, it eliminates the need for API keys or cloud-based inference.

Key innovations include:

- 🌍 Dynamic web crawling and filtering for high-signal economic content  
- 🧠 LLM-driven semantic extraction into structured JSON  
- 📊 Optional knowledge graph and CPI enrichment  
- 🔐 Fully private, offline deployment  

It demonstrates expertise in LLM orchestration, data pipelines, knowledge representation, and real-world application of GenAI in financial domains.

---

## 🚀 Features

- 🔍 **Targeted Economic News Scraping** (e.g., CNBC)
- 🧠 **DeepSeek R1 8B LLM Summarization** via Ollama (local)
- 🧾 **Structured JSON Output** with semantic tags
- 📈 **Optional Knowledge Graph Generation** with Cypher output
- 📊 **CPI Comparison Module** for inflation analysis
- 🔐 **100% Private & Offline**

---

## 🌐 Vast Applications of MacroSage

MacroSage is built to be **modular and extensible**, making it valuable across a wide range of domains:

| Use Case | Description |
|----------|-------------|
| 📉 **Market Intelligence** | Track macroeconomic shifts in real time from high-signal sources |
| 🧠 **LLM Evaluation** | Benchmark offline models (DeepSeek, Mistral, etc.) on real-world content |
| 📰 **Newsroom Automation** | Assist journalists in summarizing and tagging financial articles |
| 🧾 **Regulatory Monitoring** | Identify early signals of policy changes and economic indicators |
| 🔄 **Agentic AI Pipelines** | Feed into LangGraph agents for continuous economic reasoning |
| 🧩 **Knowledge Graph Builders** | Populate Neo4j with rich, LLM-extracted entities and relations |
| 🧠 **Economic Research** | Use as a dataset generator or a starting point for academic analysis |

---

### 💡 What I Used It For

In this implementation, I chose to use **MacroSage** as a **local semantic crawler for economic trend analysis**, extracting and structuring insights from **CNBC's Economy section** and aligning them with **CPI reports and knowledge graph generation** — showcasing how local LLMs can be productionized for offline financial intelligence.

---

## 📂 Project Structure

```bash
├── smart_crawler.py          # 🔥 Main LLM-powered crawler pipeline
├── crawl_commands.py         # 🌐 Article sources and filters
├── knowledge_graph.py        # 🧠 Entity-relation extractor and Cypher builder
├── convert_to_cypher.py      # 🗂 Legacy graph transformer
├── smart_results.json        # 📄 Output: LLM-tagged articles
├── cpi_report1.json          # 📊 Official CPI data (for analysis)
├── kb_results1.json          # 🧱 Graph-ready structured knowledge
├── neo4j_query_*.cypher      # 🧩 Neo4j import queries (Cypher)
```

---

## ▶️ Getting Started

### 1. Install Ollama and DeepSeek

```bash
# macOS
brew install ollama

# Download the model
ollama pull deepseek-coder:8b-instruct
```

> 🔁 Replace with any other Ollama-supported LLM if desired.

### 2. Set Up Python Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> Requirements: `requests`, `beautifulsoup4`, `httpx`, `json`, `datetime`, etc.

### 3. Run the Crawler 🚀

```bash
python smart_crawler.py
```

This will:
- Crawl economic articles,
- Process them through your local DeepSeek LLM,
- Save results to `smart_results.json`.

---

## 🧪 Output Example

```json
{
  "url": "https://www.cnbc.com/2025/03/17/retail-sales-increased-0point2percent-in-february-less-than-expected.html",
  "data": [
    {
      "tags": ["inflation"],
      "content": [
        "The retail sales increase was attributed to factors including inflation, which rose by [percentage]."
      ]
    },
    {
      "tags": ["consumer sentiment"],
      "content": [
        "Consumer confidence remained high, reflecting positive trends in spending and purchasing power."
      ]
    }
  ]
}
```

---

## 🧠 Code Explained

| File | Description |
|------|-------------|
| `smart_crawler.py` | **Main pipeline**. Crawls articles, queries local LLM, extracts economic insights into JSON. |
| `crawl_commands.py` | Defines URLs and filters for selecting relevant economic content. |
| `knowledge_graph.py` | Converts extracted insights into entity-relation triples and outputs `.cypher` files for Neo4j. |
| `convert_to_cypher.py` | (Optional/legacy) Transforms structured data into graph-compatible format. |
| `cpi_report1.json` | Sample CPI report for inflation analysis or baseline comparisons. |
| `kb_results1.json` | Output of knowledge graph generator: entities, relationships, and their types. |
| `smart_results.json` | Final LLM-tagged content from articles, ready for analysis or graphing. |
| `neo4j_query_*.cypher` | Generated queries for populating a Neo4j knowledge graph. |

---

## 📚 Use Cases

- 📈 Real-time economic trend detection  
- 📰 AI-assisted financial journalism  
- 🧠 Knowledge graph enrichment (Neo4j-ready)  
- 📬 Newsletter generation or LLM agent input  
- 🔍 Evaluating local LLMs on real-world tasks  

---

## 🗺️ Roadmap

- [ ] 🔄 Multi-source crawler support (WSJ, Bloomberg, etc.)  
- [ ] 🧩 LangGraph-based reasoning chains  
- [ ] 🧠 Named entity extraction with confidence scoring  
- [ ] 📊 Real-time CPI comparison engine  
- [ ] 📉 Economic trend dashboards (Streamlit/Gradio)

---

## 📬 Contact

Created by [Your Name]  
Questions, ideas, or hiring inquiries? Open an issue or reach out on [LinkedIn/GitHub].

---

## 🪪 License

MIT License — use freely, modify openly, give credit if you find it valuable!
