from typing import Dict, List, Literal, Optional, Union
from pydantic import BaseModel

from src.features.memory.dataModels.user_semantic_memory_dto import DefaultSemanticMemoryDataModel

class learnSemanticMemoryDataModel(BaseModel):
    messages: List[str]
    user_id: str
    schema: Optional[Dict] = DefaultSemanticMemoryDataModel.model_json_schema()

class retrievalSemanticMemoryDataModel(BaseModel):
    query: str
    user_id: str
    
class semanticMemory(BaseModel):
    fact: Union[str, Dict]
    context: Optional[str] = None
    
class retrievalSemanticMemoryResponse(BaseModel):
    user_id: str
    semantic_memories: List[semanticMemory]