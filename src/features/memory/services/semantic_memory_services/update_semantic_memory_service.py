import json
import os
from typing import List

from pydantic import BaseModel

from features.memory.services.memory_name_service import MemoryType, build_memory_name

def update_semantic_memory(user_id: str, 
                           memory_type: MemoryType, 
                           memory_schema: BaseModel,
                           new_memory: dict):
    """
    recebe memoria atualizada e atualiza o banco de dados
    """
    
    semantic_memory_name = build_memory_name(memory_type, user_id, memory_schema.get_model_name())
    ## salva new memory no path, subsitituindo o arquivo existente, se existir, se nao criar arquivo
    file_path = os.path.join(os.path.dirname(__file__), "memory_storage", f"{semantic_memory_name}.json")
    try:
        with open(file_path, "w+") as file:
            json.dump(new_memory, file)
    except Exception as e:
        print(f"Error updating semantic memory: {e}")
        return False

    return True
