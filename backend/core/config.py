import os
from dotenv import load_dotenv
load_dotenv()


class Settings:
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))


    LLM_BACKEND: str = os.getenv("LLM_BACKEND", "mock") # openai | ollama | mock


    OPENAI_API_KEY: str | None = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


    OLLAMA_BASE_URL: str = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL: str = os.getenv("OLLAMA_MODEL", "llama3.1:8b")


    CHROMA_DIR: str = os.getenv("CHROMA_DIR", "./.chroma")
    EMBED_MODEL: str = os.getenv("EMBED_MODEL", "text-embedding-3-small")


settings = Settings()