# company_in_a_box.py
import asyncio
from agents_functions import analyst_agent, ceo_agent, engineer_agent, designer_agent, marketing_agent

class CompanyInABox:
    def __init__(self):
        self.agents = [
            ("analyst", analyst_agent),
            ("ceo", ceo_agent),
            ("engineer", engineer_agent),
            ("designer", designer_agent),
            ("marketing", marketing_agent),
        ]

    async def run(self, idea: str):
        context = []
        output = {}

        # Step 1: Run Analyst first to create initial context
        analyst_out = await analyst_agent(idea, context)
        output["analyst"] = analyst_out
        context.append(analyst_out)

        # Step 2: Run remaining agents concurrently using the context from Analyst
        tasks = [agent_func(idea, context) for name, agent_func in self.agents[1:]]
        results = await asyncio.gather(*tasks)

        for (name, _), res in zip(self.agents[1:], results):
            output[name] = res
            context.append(res)  # optional if you want to feed subsequent runs

        return output

# Optional test
if __name__ == "__main__":
    import asyncio
    company = CompanyInABox()
    idea = "AI-powered personal finance assistant"
    result = asyncio.run(company.run(idea))
    print(result)
