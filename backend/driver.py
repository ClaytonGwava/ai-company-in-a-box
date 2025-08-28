import asyncio
from agents.agents_functions import analyst_agent, ceo_agent, engineer_agent, designer_agent, marketing_agent

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

        analyst_out = await analyst_agent(idea, context)
        output["analyst"] = analyst_out
        context.append(analyst_out)

        tasks = [agent_func(idea, context) for name, agent_func in self.agents[1:]]
        results = await asyncio.gather(*tasks)

        for (name, _), res in zip(self.agents[1:], results):
            output[name] = res
            context.append(res)  

        return output

if __name__ == "__main__":
    import asyncio
    company = CompanyInABox()
    idea = "AI-powered personal finance assistant"
    result = asyncio.run(company.run(idea))
    print(result)
