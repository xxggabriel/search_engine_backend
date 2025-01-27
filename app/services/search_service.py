from math import ceil
from typing import Dict, List
from app.models.search_models import SearchQuery, SearchResult
from app.utils.query_process import BaseProcessQuery
from app.db_utils.translate_query import translate_to_dsl
# from app.utils.redis_utils import search_in_redis, store_in_redis
from app.db_utils.elastic_search_client import get_elasticsearch
# from app.app import app
process = BaseProcessQuery()


def search(text):

    terms_list, entities, concepts = process.process(text)

    es = get_elasticsearch()
    query = translate_to_dsl(terms_list)
    
    return es.search(
        body=query,
        # index="decisoes"
        index="decisoes_with_ementas"
    )
   
