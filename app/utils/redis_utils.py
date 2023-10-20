from app.db_utils.redis_client import redis_pool
import json


async def search_in_redis(normalized_query):
    async with redis_pool as redis_client:
        cache_result = await redis_client.get(normalized_query, encoding='utf-8')
        if cache_result:
            # If result is in cache, deserialize it and return it.
            return json.loads(cache_result)


async def store_in_redis(normalized_query, result):
    async with redis_pool as redis_client:
        await redis_client.set(normalized_query, json.dumps(result))
