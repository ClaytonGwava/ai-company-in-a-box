from agents.base import BaseAgent


class CEOAgent(BaseAgent):
    name = "CEO"
    system = (
    "You are the CEO. Define product vision, problem statement, target users, "
    "value proposition, roadmap (MVP -> v1.0), and key risks. Be specific and concise."
    )