# graph.py
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver
from llm import llm_model
from context_manager import trim_messages
from search_tool import search_medical_query

class State(TypedDict):
    messages: Annotated[list, add_messages]

def chatbot(state: State):
    messages = state["messages"]
    user_query = messages[-1].content if messages else ""
    
    # Perform search for medical queries
    search_result = search_medical_query(user_query) if user_query else ""
    
    # Trim messages to fit context window
    messages = trim_messages(messages, max_tokens=4000)
    
    # Combine search results with system message
    system_message = (
        "You are a medical assistant providing accurate and concise health information. "
        "Always clarify that you are not a doctor and recommend consulting a healthcare professional. "
        f"Here are relevant search results:\n{search_result}"
    )
    
    # Invoke LLM
    response = llm_model.invoke({"system_message": system_message, "messages": messages})
    return {"messages": [response]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile(checkpointer=MemorySaver())