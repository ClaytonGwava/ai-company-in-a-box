from __future__ import annotations
from typing import List, Dict, Any
from dataclasses import dataclass, field
from core.llm import ChatMessage, get_llm
from core.memory import Memory


@dataclass
class AgentOutput:
    role: str
    content: str
    artifacts: Dict[str, Any] = field(default_factory=dict)
    
class BaseAgent:
    name: str = "BaseAgent"
    system: str = "You are a helpful agent."


    def __init__(self, memory: Memory):
        self.llm = get_llm()
        self.memory = memory


    async def run(self, objective: str, context: List[str]) -> AgentOutput:
        memories = self.memory.query(objective)
        prompt = (
            f"OBJECTIVE: {objective}\n\n"
            f"CONTEXT:\n- " + "\n- ".join(context + memories)
        )
        content = await self.llm.chat([
            ChatMessage(role="system", content=self.system),
            ChatMessage(role="user", content=prompt)
        ])
        # Save to memory
        self.memory.add([content], metadatas=[{"agent": self.name}])
        return AgentOutput(role=self.name, content=content)