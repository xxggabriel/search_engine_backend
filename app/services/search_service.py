from typing import List
from app.models.search_models import SearchQuery, SearchResult
from app.utils.query_process import BaseProcessQuery
from app.db_utils.translate_query import translate_to_dsl

'''
This is a standard implementation.

Integration with elastic search will be explored later in another article.
'''

process = BaseProcessQuery()


# Function tha execute the search of a query
def search(query: SearchQuery) -> List[SearchResult]:
    query_translated = translate_to_dsl(query)
    # Use the Methods from BaseProcessQuery that are necessary etc.
    # Mock search service
    return [SearchResult(title="Example Result", url="https://example.com", snippet="This is an example result.")]
