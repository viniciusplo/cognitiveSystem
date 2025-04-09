from typing import Annotated
from langgraph.graph import InjectedState
from langchain_core.tools import tool
from src.library.services.qdrant_service import query_retriever

## search in the library
@tool
def rag_tool(query: str, state: Annotated[dict, InjectedState]) -> list[str]:
    """
    Ferramenta utilizada para buscar informações relevantes no banco de dados.
    """
    index_name = "library_" + state.user_id
    sources = query_retriever(index_name, query)
    return sources