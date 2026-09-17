# Enterprise RAG - AI Knowledge Assistant

## 📌 Project Overview
**Research Question:** *How can cross-lingual retrieval be improved for Vietnamese queries over English educational documents?*

A cross-lingual RAG system built with LangChain and Google Gemini API for English educational documents, supporting Vietnamese queries with English citations.

---

## 🏗️ Project Structure
```text
Enterprise RAG-AI Knowledge Assistant/
├── backend/
│   ├── app/
│   │   ├── ingestion/         # Document loaders & Chunking strategies
│   │   ├── embeddings/        # Embedding services
│   │   ├── query_processing/  # HyDE & Query translation
│   │   ├── retrieval/         # Hybrid search & Cross-encoder reranking
│   │   ├── generation/        # LCEL chains & prompt templates
│   │   ├── evaluation/        # Retrieval metrics, Latency, & RAGAS eval
│   │   └── api/               # FastAPI endpoints
│   ├── data/
│   │   ├── raw/               # Raw input documents (PDF/DOCX)
│   │   └── processed/         # Chunked JSON datasets
│   ├── experiments/           # Logs & evaluation ablation study results
│   ├── Dockerfile             # Container configuration
│   └── requirements.txt       # Python dependencies
├── frontend/                  # Streamlit UI
├── test_gemini.py             # Script testing Gemini API connection
└── README.md
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.10+
- Virtual environment (`venv`) activated

### 2. Environment Setup
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### 3. Installation
```bash
pip install -r backend/requirements.txt
```

---

## 📊 Evaluation & Ablation Study
- Baseline: Dense-only retrieval (ChromaDB + Gemini Embeddings)
- Experiment 1: Semantic Chunking vs. Fixed Recursive Chunking
- Experiment 2: Hybrid Search (BM25 + Dense via HyDE)
- Experiment 3: Cross-Encoder Reranking
