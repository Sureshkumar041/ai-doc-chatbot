import os
import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from app.api.v1.router import api_router
from app.core.config import settings
from app.core.logging import setup_logging
import logging
from app.core.database import Base, engine

setup_logging()

logger = logging.getLogger(__name__)
logging.info("AI Document Chatbot API started")

# Load environment variables
load_dotenv()


# Create database tables
Base.metadata.create_all(bind=engine)

# Get host and port from .env
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", 8004))

app = FastAPI(
    title=settings.APP_NAME,
    description="Chat with your documents using AI",
    version=settings.APP_VERSION,
)

app.include_router(api_router, prefix="/api/v1")


if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.HOST, port=settings.PORT, reload=True)
