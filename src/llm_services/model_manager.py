from langchain_openai import ChatOpenAI

def select_model(model_name: str):
    if model_name == "gpt-4o-mini":
        return ChatOpenAI(model="gpt-4o-mini", temperature=0)
    elif model_name == "gpt-4o":
        return ChatOpenAI(model="gpt-4o", temperature=0)
    elif model_name == "gpt-3.5-turbo":
        return ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    else:
        raise ValueError(f"Model {model_name} not found")
