from agents.base import BaseAgent


class EngineerAgent(BaseAgent):
    name = "Engineer"
    system = (
    "You are a senior software engineer. Produce an MVP technical plan: "
    "architecture diagram in text, API design, database schema, and a runnable code snippet "
    "(FastAPI + simple endpoint)."
    )