# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from graph import graph

app = FastAPI()

class ChatInput(BaseModel):
    messages: list[str]
    thread_id: str

@app.post("/chat")
async def chat(input: ChatInput):
    config = {"configurable": {"thread_id": input.thread_id}}
    response = await graph.ainvoke({"messages": input.messages}, config=config)
    return {"response": response["messages"][-1].content}