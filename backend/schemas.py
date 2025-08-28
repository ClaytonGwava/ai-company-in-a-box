from pydantic import BaseModel, Field
from typing import List, Dict, Any


class RunRequest(BaseModel):
    idea: str = Field(..., description="High-level startup idea or problem statement")