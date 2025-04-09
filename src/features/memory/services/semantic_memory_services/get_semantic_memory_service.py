import os
import json
from typing import List
from pydantic import BaseModel

from src.features.memory.services.memory_name_service import MemoryType, build_memory_name

def get_user_semantic_memories(type: MemoryType, user_id: str, memory_schema: BaseModel):
    semantic_memory_name = build_memory_name(type, user_id, memory_schema.get_model_name())
    # get json file from memory_storage folder se existir, se nao existir, retorna None  
    file_path = os.path.join(os.path.dirname(__file__), "memory_storage", f"{semantic_memory_name}.json")
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            return json.load(file)
    else:
        return []