####################################################
# I think this module is extra
####################################################
import time
# import random
import os
import sys
from dotenv import load_dotenv
# from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Qdrant
from langchain.embeddings import HuggingFaceEmbeddings
from qdrant_client.http import models
from qdrant_client import QdrantClient
from custom_logging import logger
from custom_exception import CustomException

load_dotenv()


def store_documents_to_qdrant(texts: list):
    """
    Store documents into Qdrant vector store.

    Args:
        texts (list): List of text chunks.

    Returns:
        Qdrant: Qdrant vector store instance.
    """
    try:
        qdrant_url = os.getenv('QDRANT_URL')
        qdrant_api_key = os.getenv('QDRANT_API_KEY')
                
        embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        qdrant_client = QdrantClient(
            url = qdrant_url,
            api_key = qdrant_api_key
            )
        
        collection_name = "university-rules-chatbot"

        # Check if the collection already exists
        collections = qdrant_client.get_collections()

        collection_names = [collection.name for collection in collections.collections]

        if collection_name in collection_names:
            print("The collection already exists.")
        else:
            # Create the collection if it doesn't exist
            qdrant = Qdrant.from_documents(
                texts,
                embeddings_model,
                url=qdrant_url,
                prefer_grpc=True,
                api_key=qdrant_api_key,
                collection_name=collection_name,
                quantization_config=models.BinaryQuantization(
                    binary=models.BinaryQuantizationConfig(
                        always_ram=True,
                    ),
                )
            )

        print(f"Collection '{collection_name}' has been created.")
        
        logger.info("Documents stored in Qdrant successfully")

        return qdrant
    
    except Exception as e:
        raise CustomException(e, sys)