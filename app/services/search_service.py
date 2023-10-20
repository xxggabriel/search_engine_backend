from typing import List
from app.models.search_models import SearchQuery, SearchResult
from app.utils.query_process import BaseProcessQuery
from app.db_utils.translate_query import translate_to_dsl
from app.utils.redis_utils import search_in_redis, store_in_redis


process = BaseProcessQuery()


async def search(query: SearchQuery) -> List[SearchResult]:
    # Normalized a proces de query
    # In future could be possible to make more query process.
    normalized_query, _, _ = process.process(query.query)
    # Check in redis cache
    cache_result = await search_in_redis(normalized_query)

    if cache_result:
        # Transform the dictionaries to the SearchResult Schema.
        return [SearchResult(**result_dict) for result_dict in cache_result]

    query_translated = translate_to_dsl(query)
    # db_search() will be the function that consult the DB. Elastic cache is not implemented yet.
    # results = await db_search(query_translated)
    results = [SearchResult(title="Example Result", url="https://example.com", snippet="This is an example result.")]

    # Store the result in Redis for further consults.
    await store_in_redis(normalized_query, results)

    return results
