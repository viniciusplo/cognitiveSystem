from typing import List, Literal, Optional, Union
from pydantic import BaseModel

class QueryRequest(BaseModel):
    query: str