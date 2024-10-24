import os
import sys
from dotenv import load_dotenv

from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


load_dotenv()

# Access environment variables
OPENAI_KEY = os.getenv("OPENAI_KEY")


def retrieve_docs(question, k=4):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
    index = FAISS.load_local("faiss_index", embeddings)

    # By default the retriever uses the similarity search, but we can also use the
    # maximum mean relevance (MMR) search by setting search_type="mmr"
    retriever = index.as_retriever(search_type="mmr", search_kwargs={"k": k})

    docs = retriever.get_relevant_documents(question)

    return docs


if __name__ == "__main__":
    print(retrieve_docs(sys.argv[1]))
