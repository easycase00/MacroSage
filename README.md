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
brew install ollama
ollama pull deepseek-coder:8b-instruct
```

> 🔁 Replace with any other Ollama-supported LLM if desired.

### 2. Set Up Python Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3. Run the Crawler 🚀

```bash
python smart_crawler.py
```

This will:
- Crawl economic articles,
- Process them through your local DeepSeek LLM,
- Save results to `smart_results.json`.

---

## 📸 Screenshots

### 🧠 Ollama LLM Server Running Locally

Local DeepSeek model served via Ollama — fully offline.

![Ollama Server Running](SS/Screenshot%202025-03-29%20at%204.56.03%E2%80%AFPM.png)

---

### 🧩 Knowledge Graph: Entity-Relationship View in Neo4j

Graph output showing entities and their relationships inferred from economic news.

![Neo4j Entity Graph](SS/Screenshot%202025-03-29%20at%206.31.08%E2%80%AFPM.png)

---

### 📄 Article-Section Graph View

Shows semantic article structure as graph nodes and relationships.

![Article Graph View](SS/Screenshot%202025-03-29%20at%207.42.30%E2%80%AFPM.png)

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
| `smart_crawler.py` | Crawls articles, queries local LLM, extracts insights |
| `crawl_commands.py` | Source URL definitions and keyword filters |
| `knowledge_graph.py` | Builds entity-relation graph and exports Cypher queries |
| `convert_to_cypher.py` | (Legacy) Graph format transformer |
| `cpi_report1.json` | CPI data for inflation benchmarking |
| `kb_results1.json` | Final extracted entity-relation dataset |
| `smart_results.json` | Final output: structured article summaries |
| `neo4j_query_*.cypher` | Neo4j queries for graph insertion |

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

Created by **Hrishikesh M Bharadwaj**  
🔗 [linkedin.com/in/hrishikeshmb](https://linkedin.com/in/hrishikeshmb)

Questions, ideas, or hiring inquiries? Open an issue or reach out!

---

## 🪪 License

MIT License — use freely, modify openly, give credit if you find it valuable!
