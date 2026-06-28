from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router
from app.api.upload import router as upload_router
from app.api.chat import router as chat_router
from app.database.db import init_db
app = FastAPI(title="Insurance Policy Q&A Assistant",version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173", "*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)
app.include_router(upload_router)
app.include_router(chat_router)


@app.on_event("startup")
def on_startup():
    init_db()
    
    # Pre-load ML models to speed up first requests
    import logging
    logging.info("Pre-loading ML models into memory...")
    try:
        from app.rag.embedding import get_model as get_embedding_model
        from app.rag.reranker import get_model as get_reranking_model
        get_embedding_model()
        get_reranking_model()
        logging.info("Models loaded successfully.")
    except Exception as e:
        logging.error(f"Failed to load models during startup: {e}")

@app.get("/")
def root():
    return {
        "message": "Insurance Policy Q&A Assistant API"
    }

@app.get("/test")
def test():
    from app.rag.retriever import retrieve_chunks

    chunks = retrieve_chunks("What is the sum insured?")

    return {
        "chunks": chunks
    }
