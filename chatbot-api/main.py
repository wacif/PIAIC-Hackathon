import os
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

app = FastAPI(
    title="RAG Chatbot API",
    description="AI-powered chatbot with RAG capabilities for PIAIC Hackathon Book",
    version="1.0.0"
)

# CORS middleware for frontend integration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify your Docusaurus domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Environment variables
QDRANT_URL = os.getenv("QDRANT_URL")
QDRANT_API_KEY = os.getenv("QDRANT_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
QDRANT_COLLECTION_NAME = "book_content"

# Initialize clients
qdrant_client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
    prefer_grpc=False,
)

openai_client = OpenAI(api_key=OPENAI_API_KEY) if OPENAI_API_KEY else None

# Request models
class QueryRequest(BaseModel):
    question: str
    max_results: int = 5

class TextSelectionRequest(BaseModel):
    question: str
    selected_text: str

# Response models
class QueryResponse(BaseModel):
    answer: str
    sources: list[dict]

@app.get("/")
async def root():
    return {
        "message": "RAG Chatbot API for PIAIC Hackathon",
        "status": "running",
        "endpoints": {
            "health": "/health",
            "query": "/query",
            "query_selection": "/query-selection",
            "collections": "/collections"
        }
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    try:
        collections = qdrant_client.get_collections()
        qdrant_status = "connected"
        collection_exists = any(c.name == QDRANT_COLLECTION_NAME for c in collections.collections)
    except Exception as e:
        qdrant_status = f"error: {str(e)}"
        collection_exists = False
    
    return {
        "status": "healthy",
        "qdrant": qdrant_status,
        "collection_exists": collection_exists,
        "openai_configured": OPENAI_API_KEY is not None
    }

@app.get("/collections")
async def list_collections():
    """List all Qdrant collections."""
    try:
        collections = qdrant_client.get_collections()
        return {
            "collections": [c.name for c in collections.collections]
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to fetch collections: {str(e)}")

@app.post("/query", response_model=QueryResponse)
async def query_book(request: QueryRequest):
    """Query the book content using RAG."""
    if not openai_client:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        # Search for relevant content in Qdrant using FastEmbed
        search_results = qdrant_client.query(
            collection_name=QDRANT_COLLECTION_NAME,
            query_text=request.question,
            limit=request.max_results,
        )
        
        if not search_results:
            return QueryResponse(
                answer="I couldn't find any relevant information in the book to answer your question.",
                sources=[]
            )
        
        # Prepare context from search results
        context_parts = []
        sources = []
        
        for result in search_results:
            context_parts.append(result.document)
            sources.append({
                "source": result.metadata.get("source", "unknown"),
                "type": result.metadata.get("type", "unknown"),
                "score": result.score
            })
        
        context = "\n\n".join(context_parts)
        
        # Generate answer using OpenAI
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions based on the provided book content. Use only the information from the context to answer questions. If the context doesn't contain enough information, say so."
                },
                {
                    "role": "user",
                    "content": f"Context from the book:\n\n{context}\n\nQuestion: {request.question}\n\nPlease provide a clear and concise answer based on the context above."
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        
        return QueryResponse(
            answer=answer,
            sources=sources
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

@app.post("/query-selection", response_model=QueryResponse)
async def query_selected_text(request: TextSelectionRequest):
    """Answer questions based on user-selected text from the book."""
    if not openai_client:
        raise HTTPException(status_code=500, detail="OpenAI API key not configured")
    
    try:
        # Generate answer using only the selected text as context
        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant that answers questions based on the provided text selection. Use only the information from the selected text to answer questions."
                },
                {
                    "role": "user",
                    "content": f"Selected text:\n\n{request.selected_text}\n\nQuestion: {request.question}\n\nPlease provide a clear and concise answer based on the selected text above."
                }
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        answer = response.choices[0].message.content
        
        return QueryResponse(
            answer=answer,
            sources=[{"source": "selected_text", "type": "selection", "score": 1.0}]
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")
