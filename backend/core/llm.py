from __future__ import annotations
from typing import Dict, Any, List
from dataclasses import dataclass
import httpx
from openai import OpenAI
from .config import settings


@dataclass
class ChatMessage:
    role: str
    content: str


class LLMClient:
    async def chat(self, messages: List[ChatMessage], **kwargs) -> str:
        raise NotImplementedError


class OpenAIClient(LLMClient):
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
        self.model = settings.OPENAI_MODEL


    async def chat(self, messages: List[ChatMessage], **kwargs) -> str:
        resp = self.client.chat.completions.create(
        model=self.model,
        messages=[{"role": m.role, "content": m.content} for m in messages],
        temperature=kwargs.get("temperature", 0.3)
        )
        return resp.choices[0].message.content


class OllamaClient(LLMClient):
    def __init__(self):
        self.base = settings.OLLAMA_BASE_URL
        self.model = settings.OLLAMA_MODEL


    async def chat(self, messages: List[ChatMessage], **kwargs) -> str:
        async with httpx.AsyncClient(timeout=120) as client:
            payload = {
            "model": self.model,
            "messages": [{"role": m.role, "content": m.content} for m in messages],
            "options": {"temperature": kwargs.get("temperature", 0.3)}
            }
            r = await client.post(f"{self.base}/v1/chat/completions", json=payload)
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"]


class MockClient(LLMClient):
    async def chat(self, messages: List[ChatMessage], **kwargs) -> str:
        # Simple, deterministic mock for local dev & tests
        last = messages[-1].content if messages else ""
        return f"[MOCK RESPONSE] {last[:300]}"




def get_llm() -> LLMClient:
    if settings.LLM_BACKEND == "openai":
        return OpenAIClient()
    if settings.LLM_BACKEND == "ollama":
        return OllamaClient()
    return MockClient()
