# from elasticsearch_async import AsyncElasticsearch
from opensearchpy import OpenSearch
from opensearchpy.helpers import bulk
# from app.app import app


def get_elasticsearch() -> OpenSearch:
    es_client = OpenSearch(
        hosts=["localhost:9200"],
        http_auth=("elastic", "root"),
    )
    try:
        if not es_client.ping():
            raise ValueError("Conexão com o Elasticsearch falhou")
    except Exception as e:
        print(f"Error: {e}")
        raise e
    return es_client


# @app.on_event("startup")
# async def startup_event():
#     # Inicializar la conexión a Elasticsearch en el inicio de la aplicación
#     app.state.elasticsearch = await get_elasticsearch()


# @app.on_event("shutdown")
# async def shutdown_event():
#     await app.state.elasticsearch.close()

