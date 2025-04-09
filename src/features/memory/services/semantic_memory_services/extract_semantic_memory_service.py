from typing import List

from src.llm_services.model_manager import select_model
from features.memory.services.prompt_manager_service import systemPrompt_semantic_memory_extraction
from pydantic import BaseModel


def extract_semantic_memory(chat_history: List[str], memorySchema: BaseModel):
    model = select_model("gpt-4o").with_structured_output(memorySchema)
    prompt = systemPrompt_semantic_memory_extraction()
    messages = [
        {"role": "system", "content": prompt},
        {"role": "user", "content": chat_history}
    ]
    new_memories = model.invoke(messages)
    return new_memories