from typing import List
from src.features.memory.dataModels.semantic_memory_dto import learnSemanticMemoryDataModel, retrievalSemanticMemoryDataModel
from src.features.memory.services.semantic_memory_services.extract_semantic_memory_service import extract_semantic_memory
from src.features.memory.services.semantic_memory_services.patch_semantic_memory_service import patch_semantic_memories
from src.features.memory.services.semantic_memory_services.get_semantic_memory_service import get_user_semantic_memories
from src.features.memory.services.semantic_memory_services.update_semantic_memory_service import update_semantic_memory

def learningSemanticMemoryController(conversation: learnSemanticMemoryDataModel):
    """
    This function is used to learn new information from the conversation and update the semantic memory.
    """   
    new_memories = extract_semantic_memory(conversation.messages, conversation.schema)
    current_memories = get_user_semantic_memories(conversation.user_id)
    patched_memories = patch_semantic_memories(current_memories, new_memories, conversation.schema)
    result = update_semantic_memory(conversation.user_id, patched_memories)
    
    return result

def retrievalSemanticMemoryController(request: retrievalSemanticMemoryDataModel):
    """
    This function is used to retrieve information from the semantic memory.
    now it returns all the memories, but we can improve this by adding a query to the semantic memory.
    """
    ## TODO: Add a query to the semantic memory.
    user_semantic_memories = get_user_semantic_memories(request.user_id)
    return user_semantic_memories