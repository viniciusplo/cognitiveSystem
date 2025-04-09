from fastapi import Depends, FastAPI

from .dependencies import get_query_token, get_token_header

from src.library.routers.qdrant_router import qdrantRouter

from src.features.memory.routers.memory_router import memoryRouter
from src.features.conversation.routers.ask_router import chatRouter
from src.features.speech.routers.speech_router import speechRouter
app = FastAPI(dependencies=[Depends(get_query_token)])

## gerenciador de documentos
app.include_router(qdrantRouter.router,
                   prefix="/library",
                   tags=["library"],
                   dependencies=[Depends(get_token_header)])

## gerenciador de memória
app.include_router(memoryRouter.router,
                   prefix="/memory",
                   tags=["memory"],
                   dependencies=[Depends(get_token_header)])

## conversação com o agente
app.include_router(chatRouter.router,
                   prefix="/chat",
                   tags=["chat"],
                   dependencies=[Depends(get_token_header)])

## conversação com o agente
app.include_router(speechRouter.router,
                   prefix="/speech",
                   tags=["speech"],
                   dependencies=[Depends(get_token_header)])

@app.get("/")
async def root():
    return {"message": "Artificial Brain Operational! 🧠"}