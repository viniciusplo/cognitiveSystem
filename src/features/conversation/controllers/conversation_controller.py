from src.features.conversation.dataModels.endpoint_datamodels import ChatRequest, ChatResponse
from src.features.conversation.services.build_graph_service import build_app

def chatController(chat_request: ChatRequest):
    query = chat_request.query
    user_id = chat_request.user_id
      
    conversation_app = build_app()
    config = {"configurable": {"thread_id": user_id, "user_id": user_id}}
    events = conversation_app.stream(
        {"messages": [{"role": "user", "content": query}]},
        config,
        stream_mode="values",
    )
    #for event in events:
    #    print(event["messages"][-1].content)
      
    return ChatResponse(message=events["messages"][-1].content)