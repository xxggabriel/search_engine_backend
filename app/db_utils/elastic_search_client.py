from elasticsearch_async import AsyncElasticsearch
from app.app import app


async def get_elasticsearch() -> AsyncElasticsearch:
    es_client = AsyncElasticsearch(
        hosts=[{"host": "your-elasticsearch-host", "port": 9200}],
    )
    try:
        # Verificar la conexión
        if not await es_client.ping():
            raise ValueError("Conexión fallida")
    except Exception as e:
        print(f"Error: {e}")
        raise e
    return es_client


@app.on_event("startup")
async def startup_event():
    # Inicializar la conexión a Elasticsearch en el inicio de la aplicación
    app.state.elasticsearch = await get_elasticsearch()


@app.on_event("shutdown")
async def shutdown_event():
    await app.state.elasticsearch.close()

