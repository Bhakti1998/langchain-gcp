import logfire
from qdrant_client import QdrantClient
from qdrant_client.http import models
from app.retrieval.embeddings import get_embedding_model , embed_query
import os
from dotenv import load_dotenv
load_dotenv()

QRDANT_url=os.getenv("QUADRANT_EP")
QDRANT_api=os.getenv("QUADRANT_API_KEY")
QDRANT_COLLECTION_name=os.getenv("QDRANT_COLLECTION")

client=QdrantClient(
    url=QRDANT_url,
    api_key=QDRANT_api
)


def search_enterprise_knowledge(query: str, limit: int = 8):
    """
    Performs a high-precision search in the enterprise knowledge base.
    Uses the modern query_points interface.
    """
    try:
        query_vector = embed_query(query)

        # Using query_points - the modern standard for Qdrant
        response = client.query_points(
            collection_name=QDRANT_COLLECTION_name,
            query=query_vector,
            limit=limit,
            with_payload=True # JSON
        )

        results = []
        for res in response.points:
            results.append({
                "content": res.payload.get("text", ""),
                "source": res.payload.get("source", "Unknown"),
                "score": res.score
            })
        
        return results
    except Exception as e:
        logfire.error(f"❌ Qdrant Search Failed: {e}")
        return []
