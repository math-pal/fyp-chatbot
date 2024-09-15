####################################################
# I think this module is extra
####################################################
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
        qdrant_end = os.getenv('QDRANT_URL')
        qdrant_api_key = os.getenv('QDRANT_API_KEY')
                
        embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

        qdrant = Qdrant.from_documents(
            texts,
            embeddings_model,
            url=qdrant_end,
            prefer_grpc=True,
            api_key=qdrant_api_key,
            collection_name="university-rules-chatbot",
            quantization_config=models.BinaryQuantization(
                binary=models.BinaryQuantizationConfig(
                    always_ram=True,
                ),
            )
        )
        
        logger.info("Documents stored in Qdrant successfully")

        return qdrant
    
    except Exception as e:
        raise CustomException(e, sys)