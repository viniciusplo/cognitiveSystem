from dependencies import get_token_header
from fastapi import Depends
from fastapi.routing import APIRouter
from src.features.conversation.dataModels.endpoint_datamodels import ChatRequest
from src.features.conversation.controllers.conversation_controller import chatController

from dotenv import load_dotenv
load_dotenv()

chatRouter = APIRouter(
    prefix="/chat",
    tags=["chat"],
    dependencies=[Depends(get_token_header)],
    responses={404: {"description": "Not found"}},
)

@chatRouter.post("/chat")
async def chat(request: ChatRequest):
    result = chatController(request.query)

    return result   