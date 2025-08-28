from agents.base import BaseAgent


class DesignerAgent(BaseAgent):
    name = "Designer"
    system = (
    "You are a product designer. Create a UX brief: user personas, primary user flows, "
    "and 3 UI mockup prompts for an image model (concise, structured)."
    )