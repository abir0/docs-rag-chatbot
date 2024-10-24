import os
import sys
from dotenv import load_dotenv

from langchain.document_loaders import DirectoryLoader, UnstructuredFileLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings


load_dotenv()

# Access environment variables
OPENAI_KEY = os.getenv("OPENAI_KEY")


directory = sys.argv[1]
loader = DirectoryLoader(
    directory,
    glob="**/[!.]*",
    loader_cls=UnstructuredFileLoader,
    load_hidden=False,
    recursive=True,
    #  silent_errors=True,
    use_multithreading=True,
    max_concurrency=8,
    show_progress=True,
)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1024,
    chunk_overlap=128,
    length_function=len,
    is_separator_regex=False,
)
texts = text_splitter.split_documents(docs)

embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)
new_index = FAISS.from_documents(docs, embeddings)

index = FAISS.load_local("faiss_index", embeddings)

index.merge_from(new_index)
index.save_local("faiss_index")
