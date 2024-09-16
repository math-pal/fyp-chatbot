import os
import sys
project_root = "E:/Training/Atomcamp/DS6_Bootcamp/Projects/FYP/fyp-chatbot"
sys.path.append(project_root)
from src.preprocess import load_documents, split_documents
from src.index import store_documents_to_qdrant
# from langchain_openai import OpenAIEmbeddings
from src.retriever import retrieve_answer_from_docs
from src.utils import format_docs
from langchain_community.vectorstores import Qdrant
from qdrant_client import QdrantClient
from dotenv import load_dotenv

load_dotenv()

def retriever(question:str, history=None):
    # # Load and preprocess
    directory = "E:/Training/Atomcamp/DS6_Bootcamp/Projects/FYP/Rules_and_Policies"
    directory_path = os.path.join(project_root, directory)
    documents = load_documents(directory_path)
    texts = split_documents(documents)
    
    print('*' * 60)
    print(len(texts))
    print(len(documents))
    print('*' * 60)

    # Index
    qdrant = store_documents_to_qdrant(texts)

    
    # Retrieve
    # question = "What are the documents uploaded in the database?"
    answer = retrieve_answer_from_docs(question)
    
    return answer

# def main():
#     question = "What are the documents uploaded in the database?"
#     answer = retriever(question, 'bot')
#     print(answer)

# if __name__ == "__main__":
#     main()