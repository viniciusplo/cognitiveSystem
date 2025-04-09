from features.conversation.dataModels.endpoint_datamodels import ChatRequest, ChatResponse
from src.features.conversation.services.build_graph_service import build_app

def speechToTextController(chat_request: ChatRequest):
    return "test transcription!"
