```text
ai-document-chatbot/
│
├── backend/
│   ├── app/
│   │   ├── main.py                 # Application entry point
│   │   │
│   │   ├── api/
│   │   │   └── v1/
│   │   │       ├── routes/
│   │   │       │   ├── documents.py
│   │   │       │   ├── chat.py
│   │   │       │   └── health.py
│   │   │       └── api.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── logging.py
│   │   │   └── exceptions.py
│   │   │
│   │   ├── schemas/
│   │   │   ├── document.py
│   │   │   └── chat.py
│   │   │
│   │   ├── services/
│   │   │   ├── document_service.py
│   │   │   ├── chat_service.py
│   │   │   ├── embedding_service.py
│   │   │   └── retrieval_service.py
│   │   │
│   │   ├── infrastructure/
│   │   │   ├── llm/
│   │   │   │   └── ollama_client.py
│   │   │   │
│   │   │   ├── vectorstore/
│   │   │   │   └── chroma_client.py
│   │   │   │
│   │   │   ├── embeddings/
│   │   │   │   └── sentence_transformer.py
│   │   │   │
│   │   │   └── document_loaders/
│   │   │
│   │   └── utils/
│   │
│   └── tests/
│
├── data/
│   ├── uploads/
│   └── chroma_db/
│
├── .env
├── .env.example
├── .gitignore
├── pyproject.toml
├── Dockerfile
└── README.md
```
