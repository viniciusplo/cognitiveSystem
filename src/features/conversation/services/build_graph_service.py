from typing import Annotated

from langchain_anthropic import ChatAnthropic
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool
from typing_extensions import TypedDict

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition

from langgraph.types import Command, interrupt

from llm_services.model_manager import select_model
from src.features.conversation.services.graph_state_service import State
from langgraph.checkpoint.memory import MemorySaver
from src.features.conversation.services.prompt_manager import systemPrompt_conversation
from features.conversation.services.tools.search_library_tool import rag_tool

def build_graph():
    graph_builder = StateGraph(State)

    ## tools
    tools = [rag_tool]

    ## llm
    llm = select_model("gpt-4o-mini")
    llm_with_tools = llm.bind_tools(tools)
    
    ## llmNode
    def chatNode(state: State):
        return {"messages": [llm_with_tools.invoke(
            [
                {
                    "role": "system",
                    "content": systemPrompt_conversation(state["memoria_semantica"]),
                },
                *state["messages"],
            ],
            state["messages"])]}

    ## build graph
    tool_node = ToolNode(tools=tools)

    graph_builder.add_node("chatNode", chatNode)
    graph_builder.add_node("tools", tool_node)
    graph_builder.add_conditional_edges(
        "chatNode",
        tools_condition,
    )
    graph_builder.add_edge("tools", "chatNode")
    graph_builder.add_edge(START, "chatNode")
    
    memory = MemorySaver()
    return graph_builder.compile(memory=memory)