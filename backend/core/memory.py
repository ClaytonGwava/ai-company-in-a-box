from __future__ import annotations
import chromadb
from chromadb.config import Settings as ChromaSettings
from typing import List, Dict
from .config import settings

class Memory:
    def __init__(self, collection_name: str = "company_memory"):
        self.client = chromadb.PersistentClient(path=settings.CHROMA_DIR, settings=ChromaSettings())
        self.col = self.client.get_or_create_collection(collection_name)


    def add(self, texts: List[str], metadatas: List[Dict] | None = None):
        ids = [f"doc_{self.col.count()}_{i}" for i in range(len(texts))]
        self.col.add(documents=texts, metadatas=metadatas, ids=ids)


    def query(self, q: str, k: int = 4) -> List[str]:
        res = self.col.query(query_texts=[q], n_results=k)
        return [d for d in res.get("documents", [[]])[0]]