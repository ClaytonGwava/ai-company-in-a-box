from __future__ import annotations
from typing import List
from core.memory import Memory
from agents.roles.ceo import CEOAgent
from agents.roles.engineer import EngineerAgent
from agents.roles.designer import DesignerAgent
from agents.roles.marketing import MarketingAgent
from agents.roles.analyst import AnalystAgent


class Coordinator:
    def __init__(self, memory: Memory):
        self.memory = memory
        self.ceo = CEOAgent(memory)
        self.engineer = EngineerAgent(memory)
        self.designer = DesignerAgent(memory)
        self.marketer = MarketingAgent(memory)
        self.analyst = AnalystAgent(memory)


    async def run_round(self, idea: str, context: List[str]):
        # Round 1: CEO sets vision
        ceo_out = await self.ceo.run(idea, context)
        ctx1 = context + [ceo_out.content]
        # Round 2: Analyst and Engineer
        analyst_out = await self.analyst.run(idea, ctx1)
        eng_out = await self.engineer.run(idea, ctx1 + [analyst_out.content])
        ctx2 = ctx1 + [analyst_out.content, eng_out.content]
        # Round 3: Designer and Marketing
        des_out = await self.designer.run(idea, ctx2)
        mkt_out = await self.marketer.run(idea, ctx2 + [des_out.content])
        outputs = [ceo_out, analyst_out, eng_out, des_out, mkt_out]
        return outputs