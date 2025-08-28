from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio
from driver import CompanyInABox
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(title="Multi-Agent Company In A Box")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Request body model
class ProjectIdea(BaseModel):
    idea: str

# Instantiate orchestrator
company = CompanyInABox()

@app.get("/")
async def root():
    return {"message": "Welcome to Multi-Agent Company In A Box API. Use POST /run to execute workflow."}

@app.post("/run")
async def run_workflow(project: ProjectIdea):
    try:
        result = await company.run(project.idea)
        return {"status": "success", "output": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
