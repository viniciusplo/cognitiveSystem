from dependencies import get_token_header
from fastapi import Depends
from fastapi.routing import APIRouter
from dotenv import load_dotenv

from src.features.memory.controllers.semantic_memory_controller import learningSemanticMemoryController, retrievalSemanticMemoryController
from src.features.memory.dataModels.semantic_memory_dto import learnSemanticMemoryDataModel, retrievalSemanticMemoryDataModel
load_dotenv()

memoryRouter = APIRouter(
    prefix="/memory",
    tags=["memory"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@memoryRouter.post("/learnSemanticMemory")
async def learnSemanticMemory(request: learnSemanticMemoryDataModel):
    learningSemanticMemoryController(request)
    
    return True

@memoryRouter.post("/retrieveSemanticMemory")
async def retrieveSemanticMemory(request: retrievalSemanticMemoryDataModel):
    retrieved_memories = retrievalSemanticMemoryController(request.user_id, request.query)
    return retrieved_memories