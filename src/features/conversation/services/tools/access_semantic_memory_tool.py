from typing import Annotated
from langgraph.graph import InjectedState
from langchain_core.tools import tool

from features.memory.controllers.semantic_memory_controller import retrievalSemanticMemoryController
from features.memory.dataModels.semantic_memory_dto import retrievalSemanticMemoryDataModel

## search in the memory
@tool
def semantic_memory_tool(query: str, state: Annotated[dict, InjectedState]) -> list[str]:
    """
    Ferramenta utilizada para buscar memoria semantica do usuario.
    """
    semantic_memory = retrievalSemanticMemoryController(
        retrievalSemanticMemoryDataModel(
            user_id=state.user_id,
            query=query
        )
    )
    return semantic_memory