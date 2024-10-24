from fastapi import FastAPI, Query

from retrieve import retrieve_docs
from bot import llm_chat


app = FastAPI(
    title="Retrieve similar documents",
    description="Retrieves k documents most similar to the query.",
    version="v1.0.0",
)


@app.get("/", tags=["ChatbotQA"])
async def chat(
    query: str = Query(..., description="The question or query to be answered")
):
    llm_response = llm_chat(query)
    return llm_response["result"]


@app.get("/api", tags=["RetrieveDocuments"])
async def query_documents(
    query: str = Query(..., description="The question or query to be answered"),
    k: int = Query(..., ge=1, le=10, description="The number of documents to retrieve"),
):
    documents = retrieve_docs(query, k)
    return {"query": query, "documents": documents}
