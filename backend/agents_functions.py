# agents_functions.py
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage
from typing import List
from dotenv import load_dotenv
load_dotenv()

# Create a single LLM instance
llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.3)  

async def analyst_agent(idea: str, context: List[str]) -> str:
    system_prompt = (
        "You are a business analyst. Perform market sizing, competitor scan, pricing options, "
        "and success metrics (leading+lagging)."
    )
    user_prompt = f"Objective: {idea}\nContext:\n- " + "\n- ".join(context)
    result = await llm.agenerate([[
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]])
    return result.generations[0][0].message.content

async def ceo_agent(idea: str, context: List[str]) -> str:
    system_prompt = (
        "You are the CEO. Define product vision, problem statement, target users, "
        "value proposition, roadmap (MVP -> v1.0), and key risks."
    )
    user_prompt = f"Objective: {idea}\nContext:\n- " + "\n- ".join(context)
    result = await llm.agenerate([[
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]])
    return result.generations[0][0].message.content

async def engineer_agent(idea: str, context: List[str]) -> str:
    system_prompt = (
        "You are a senior software engineer. Produce an MVP technical plan: "
        "architecture diagram in text, API design, database schema, and a runnable code snippet."
    )
    user_prompt = f"Objective: {idea}\nContext:\n- " + "\n- ".join(context)
    result = await llm.agenerate([[
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]])
    return result.generations[0][0].message.content

async def designer_agent(idea: str, context: List[str]) -> str:
    system_prompt = (
        "You are a product designer. Create a UX brief: user personas, primary user flows, "
        "and 3 UI mockup prompts for an image model."
    )
    user_prompt = f"Objective: {idea}\nContext:\n- " + "\n- ".join(context)
    result = await llm.agenerate([[
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]])
    return result.generations[0][0].message.content

async def marketing_agent(idea: str, context: List[str]) -> str:
    system_prompt = (
        "You are a growth marketer. Write: positioning statement, 3 ICP profiles, a 7-day launch plan, "
        "and 1 LinkedIn post + 1 email copy."
    )
    user_prompt = f"Objective: {idea}\nContext:\n- " + "\n- ".join(context)
    result = await llm.agenerate([[
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_prompt)
    ]])
    return result.generations[0][0].message.content
