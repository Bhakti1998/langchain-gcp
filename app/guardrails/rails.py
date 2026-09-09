import logfire
from langchain_groq import ChatGroq
from nemoguardrails import RailsConfig, LLMRails
from app.guardrails.colang_rules import (
    COLANG_CONTENT,
    YAML_CONTENT,
    RAIL_INDICATORS
)
import os
from dotenv import load_dotenv
load_dotenv()
_rails : LLMRails | None = None

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
logfire.configure(token=os.getenv("LOGFIRE_TOKEN"))

def initialize_rails() -> None:
    """
    Build the NeMo LLMRails singleton at app startup.
    Uses gpt-3.5-turbo for fast intent classification at the gate —
    the heavier gpt-4 is reserved for the RAG pipeline.
    """
    global _rails
    
    guard_llm = ChatGroq(
        api_key=OPENAI_API_KEY,
        # model="openai/gpt-oss-120b",
        model="gpt-3.5-turbo",
        temperature=0
    )

    config = RailsConfig.from_content(
        colang_content=COLANG_CONTENT,
        yaml_content=YAML_CONTENT
    )

    _rails = LLMRails(config)
    #, llm=guard_llm)
    logfire.info("NeMo Guardrails initialised (openai / gpt-3.5-turbo).")


def guard(message: str) -> tuple[bool, str | None]:
    """
    Run a user message through the NeMo rails gate.

    Returns:
        (True,  rail_response) — a rail fired; return this response immediately,
                                skip the RAG pipeline entirely.
        (False, None)          — message is clean; proceed to LangGraph.
    """
    if _rails is None:
        logfire.warning("⚠️ Guardrails not initialised — skipping gate.")
        return False, None

    with logfire.span("🛡️ Guardrails Check"):
        result = _rails.generate(messages=[{"role": "user", "content": message}])

        # NeMo returns {'role': 'assistant', 'content': '...'} — extract text
        content = result.get("content", "") if isinstance(result, dict) else str(result)

        fired = any(indicator in content for indicator in RAIL_INDICATORS)

        if fired:
            logfire.info(f"🛡️ Guardrails fired | query='{message[:80]}'")
            return True, content

        logfire.info("✅ Guardrails passed.")
        return False, None

# if __name__ == "__main__":
#     initialize_rails()
#     test_messages = [
#         # "Hello, what can you do?",
#         # "Can you tell me about Kubernetes networking?",
#         "What is your favorite color?",
#         # "Bye!"
#     ]
#     for msg in test_messages:
#         # res=guard(msg)
#         # return res
#         fired, response = guard(msg)
#         print(f"Message: {msg}\nFired: {fired}\nResponse: {response}\n{'-'*40}")