from typing import List
from pydantic import BaseModel

class ChatRequest(BaseModel):
    query: str
    user_id: str

class ChatResponse(BaseModel):
    message: str ## agent response
