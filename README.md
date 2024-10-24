# docs-rag-chatbot

## Overview

`docs-rag-chatbot` is a chatbot application designed to leverage Retrieval-Augmented Generation (RAG) with large language models (LLMs) to interact with documents in a meaningful way. The bot allows users to query large datasets and documents by retrieving relevant information and generating natural language responses.

## Features

- **LLM Integration**: Uses a large language model to generate human-like responses.
- **RAG (Retrieval-Augmented Generation)**: The bot first retrieves relevant information from documents and then generates responses, improving accuracy and relevance.
- **FAISS Indexing**: Efficient document embedding storage using FAISS (Facebook AI Similarity Search), enabling fast and scalable search.
- **Customizable Document Querying**: Supports querying documents stored in FAISS-based indexes.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/docs-rag-chatbot.git
   cd docs-rag-chatbot
   ```

2. **Install dependencies**:
   Ensure you have Python 3.8+ installed, then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up FAISS index**:
   Ensure that the `faiss_index/index.pkl` file exists or create a new index using the appropriate scripts.

## Usage

1. **Start the bot**:
   ```bash
   python app.py
   ```
   This will start the chatbot server.

2. **Querying Documents**:
   Once the chatbot is running, you can interact with it via an API or a UI (depending on how the bot is configured). It will retrieve relevant information from the document set based on your queries and use the LLM to generate a response.

## File Structure

```
.
├── faiss_index             # Directory for storing FAISS index
│   └── index.pkl           # Prebuilt FAISS index for document embeddings
├── README.md               # This file
├── agent.py                # Defines the chatbot agent and its behavior
├── app.py                  # Main entry point for running the chatbot server
├── append_index.py         # Script to append new documents to the FAISS index
├── bot.py                  # Chatbot core logic and interaction flow
├── index.py                # Script to build the FAISS index
├── query.py                # Handles querying the FAISS index
├── requirements.txt        # Python dependencies
├── retrieve.py             # Document retrieval logic
└── schema.json             # Schema for OpenAI API interactions
```

## How It Works

1. **Document Indexing**:
   - Documents are preprocessed into embeddings using a transformer-based model and stored in the FAISS index. Use `index.py` to create the index and `append_index.py` to update it with new documents.

2. **Query Handling**:
   - When a user makes a query, the bot first retrieves the most relevant document snippets from the FAISS index (`retrieve.py`). The retrieved context is then passed to the LLM for generating a coherent response (`agent.py`).
