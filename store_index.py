from dotenv import load_dotenv
import os
from pinecone import Pinecone
from pinecone import ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from src.helper import load_pdf_files, filter_to_minimal_docs, text_split,download_embeddings

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY
os.environ["GROQ_API_KEY"]=GROQ_API_KEY

extracted_data=load_pdf_files(data="data/")
filter_data=filter_to_minimal_docs(extracted_data)
text_chunks=text_split(filter_data)
embeddings_model=download_embeddings()

pinecone_api_key = PINECONE_API_KEY
pc = Pinecone(api_key=pinecone_api_key)

index_name="mediora-index"
if not pc.has_index(index_name):
    pc.create_index(
        name=index_name,
        dimension=384,  # Dimension of the embedding vectors
        metric="cosine",  # Cosine similarity metric
        spec=ServerlessSpec(cloud="aws", region="us-east-1")
    )


docsearch = PineconeVectorStore.from_documents(
    documents = text_chunks,
    embedding=embeddings_model,
    index_name=index_name
)
