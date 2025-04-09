from enum import Enum

class MemoryType(Enum):
    SEMANTIC = "semantic_memory"
    EPISODIC = "episodic_memory"
    PROCEDURAL = "procedural_memory"

def build_memory_name(type: MemoryType, user_id: str, schema_name: str = "facts"):
    return f"{type.value}_{user_id}_{schema_name}"
