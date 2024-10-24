import os
import sys
from dotenv import load_dotenv

from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI


load_dotenv()

# Access environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")


def llm_chat(query, k=4):
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    index = FAISS.load_local("faiss_index", embeddings)

    # By default the retriever uses the similarity search, but we can also use the
    # maximum mean relevance (MMR) search by setting search_type="mmr"
    retriever = index.as_retriever(search_type="mmr", search_kwargs={"k": k})

    # create the chain to answer questions
    qa_chain = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
    )

    llm_response = qa_chain(query)

    return llm_response


if __name__ == "__main__":
    print(llm_chat(sys.argv[1]))
