import logfire
import os
from dotenv import load_dotenv
logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))

from fastapi import FastAPI,Response

from contextlib import asynccontextmanager
from app.agents.graph import rag_agent
from app.guardrails.rails import initialize_rails, guard

from pydantic import BaseModel
from typing import Optional

# @asynccontextmanager # This function will manage something that happens when my application starts and when it stops
# async def lifespan(app: FastAPI):
#     initialize_rails()
#     yield



# BEFORE yield  → STARTUP
# AFTER yield   → SHUTDOWN


app=FastAPI(title="Enterprise Agentic Rag API", version="0.1.0")

@app.on_event("startup")
def startup_event():
    initialize_rails()

class QueryRequest(BaseModel):
    query: str
    user_id: Optional[str] = "default_user"

@app.get("/")
def get_graph_image():
    try:
        png_bytes = rag_agent.get_graph().draw_mermaid_png()
        return Response(content=png_bytes, media_type="image/png")
    except Exception as e:
        return {"error": f"Could not generate graph image: {e}"}

@app.post("/query")
def query(request: QueryRequest):
        
    initial_state = {
    "messages": [{"role": "user", "content": request.query}],
    "current_query": request.query,
    "documents": [],
    "plan": ["Start"],
    "status": "Initializing Graph...",
    }
    config = {"configurable": {"thread_id": request.user_id}}

    try:
        # Gate 1: NeMo Guardrails — blocks off-topic / jailbreaks
        rail_fired, rail_response = guard(request.query)
        # return rail_fired, rail_response
        if rail_fired:
            logfire.info(f"Request blocked by guardrails | thread={request.user_id}")
            return {
                "question": request.query,
                "answer": rail_response,
                "thought_process": ["Intent: Guardrails Fired", "Retrieval: Skipped"],
                "status": "Blocked by guardrails.",
                "sources": [],
            }
        
        result = rag_agent.invoke(initial_state, config=config)
        return {"question": request.query,
                "answer": result.get("final_answer"),
                "thought_process": result.get("plan"),
                "status": result.get("status"),
                "sources": result.get("documents", [])
                }
    except Exception as e:
        logfire.error(f"Backend Execution Failed: {e}")
        return {
            "question": request.query,
            "answer": "I apologize, but I encountered an internal error. Please try again.",
            "thought_process": ["Error encountered during execution."],
            "status": "error",
            "sources": [],
        }
    
