from agents.base import BaseAgent


class AnalystAgent(BaseAgent):
    name = "Analyst"
    system = (
    "You are a business analyst. Perform lightweight market sizing, competitor scan, pricing options, "
    "and success metrics (leading+lagging)."
    )