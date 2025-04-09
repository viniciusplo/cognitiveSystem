import logging
from typing import Dict, List
from uuid import uuid4
from qdrant_client import QdrantClient
from qdrant_client.http import models as qmodels
from qdrant_client.models import PointStruct
from qdrant_client import QdrantClient
from file_service import (break_document, 
                        get_embedding_client, 
                        get_raw_document)
import os

## ------ Qdrant ----

def get_qdrant_client():
    QDRANT_HOST = os.getenv("QDRANT_HOST")
    QDRANT_PORT = os.getenv("QDRANT_PORT")
    client = QdrantClient(host=QDRANT_HOST, port=QDRANT_PORT)
    # client = QdrantClient(host="localhost", port=6333)
    return client

def get_all_collections(): 
    try:
        client = get_qdrant_client()
        collections = client.get_collections()
        return collections.collections
    except Exception as e:
        logging.error(f"Problema ao retornar indexes: {e}")
        return []

def get_collection_info(name: str):
    try:
        client = get_qdrant_client()
        collection_info = client.get_collection(name)
        return collection_info
    except Exception as e:
        logging.error(f"Problema ao retornar index {name}: {e}")
        return None

def collection_exists(collection_name: str):
    client = get_qdrant_client()
    return client.collection_exists(collection_name)

def create_vector_store(index_name: str):
    try:
        client = get_qdrant_client()
        if not client.collection_exists(index_name):
            client.create_collection(
                collection_name=index_name,
                vectors_config=qmodels.VectorParams(size=1536, distance=qmodels.Distance.COSINE),
                )
            logging.info(f"Index criado com sucesso: {index_name}")
            return True
        else:
            logging.warning(f"collection com nome {index_name} ja existe!")
            return False
            
    except Exception as e:
        logging.error(f"Problema ao criar index: {e}")
        return False

def update_documents_to_status(collection_name: str, status:bool):
    """
    Atualiza todos os documentos em uma coleção no Qdrant, definindo o campo 'active' como False.

    :param client: Instância do QdrantClient já conectada.
    :param collection_name: Nome da coleção no Qdrant.
    """
    client = get_qdrant_client()
    
    # Recupera todos os pontos da coleção
    all_points = client.scroll(collection_name=collection_name, with_payload=True)

    # Itera sobre os pontos retornados
    for point in all_points[0]:
        point_id = point.id
        updated_payload = point.payload.copy()

        # Define o campo 'active' como False
        updated_payload['active'] = status

        # Atualiza o payload no Qdrant
        client.update_point(
            collection_name=collection_name,
            point_id=point_id,
            payload=updated_payload
        )

    print(f"Todos os documentos na coleção '{collection_name}' foram atualizados para 'active=False'.")

def add_documents(documents: List[Dict], index_name: str):
    try:
        client = get_qdrant_client()
        
        for document in documents:
            document["id"] = str(uuid4())
            document["metadata"]["active"] = True
            document["embedding"] = get_embedding_client().embed_query(document["text"])
        
        client.upsert(
           collection_name=index_name,
           points=[
              PointStruct(
                    id=document["id"],
                    vector=document["embedding"],
                    payload={**document["metadata"]}
              )
              for document in documents
           ]
        )
       
        logging.warning(f"Documentos inseridos com sucesso no index: {index_name}")
        return True
    except Exception as e:
        logging.error(f"Problema ao adicionar documentos: {e}")
        return False
        

def add_file(index_name: str, file):
    try:
        raw_document = get_raw_document(file)
        doc_chunks = break_document(raw_document)

        document_list = list()
        for chunk in doc_chunks:
            doc = {
                "page_content":chunk.page_content,
                "source": file.name
                }
            document_list.append(doc)

        add_documents(document_list, index_name)
        logging.warning(f"Documento inserido com sucesso no index: {index_name}")
    except Exception as e:
        logging.error(f"Problema ao adicionar documento: {e}")

def query_retriever(index_name: str, query: str, k=2):
    try:
        client = get_qdrant_client()
        query_embedding = get_embedding_client().embed_query(query)
                
        results = client.search(
            collection_name=index_name,
            query_vector=query_embedding,
            limit=k
        )
    
        docs = [res.payload["content"] for res in results]
        return docs
    except Exception as e:
        logging.error(f"Erro ao fazer busca no Qdrant index: {index_name}: {e}")
        return None

def delete_index(index_name):
    try:
        client = get_qdrant_client()
        client.delete_collection(index_name)
        logging.info(f"Index deletado com sucesso: {index_name}")
    except Exception as e:
        logging.error(f"Problema ao deletar index {index_name}: {e}")

def delete_inactive_documents(collection_name: str):
    """
    Apaga todos os documentos em uma coleção no Qdrant onde o campo 'active' está definido como False.

    :param client: Instância do QdrantClient já conectada.
    :param collection_name: Nome da coleção no Qdrant.
    """
    client = get_qdrant_client()
    try:
        # Recupera todos os pontos da coleção
        all_points = client.scroll(collection_name=collection_name, with_payload=True)

        # Itera sobre os pontos retornados
        for point in all_points[0]:
            if point.payload.get('active') == False:
                # Remove o ponto do Qdrant
                client.delete_point(
                    collection_name=collection_name,
                    point_id=point.id
                )
        logging.warning(f"Todos os documentos com 'active=False' na coleção '{collection_name}' foram apagados.")
        
        return True
    except Exception as e:
        logging.error(f"Erro ao deletar documentos inativos na '{collection_name}'")
        
        return False
    