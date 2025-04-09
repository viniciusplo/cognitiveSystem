from typing import Dict, List
from pydantic import BaseModel
from trustcall import create_extractor
from src.llm_services.model_manager import select_model
from src.features.memory.dataModels.user_semantic_memory_dto import UserProfileDataModel

def patch_semantic_memories(current_memories: Dict, 
                            new_memories: Dict, 
                            memory_structure: BaseModel):
    llm = select_model("gpt-4o-mini")

    bound = create_extractor(llm, tools=[memory_structure])

    trustcall_result = bound.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": f"""Update the existing memory (JSON doc) to incorporate new following information:
        <new_memory>
        {new_memories}
        </new_memory>""",
                    }
                ],
                "existing memories": {memory_structure.__name__: current_memories},
            }
        )

    trustcall_output = trustcall_result["responses"][0].model_dump()
    return trustcall_output