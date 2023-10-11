from typing import List
from app.models.search_models import SearchQuery, SearchResult
from app.utils.query_process import BaseProcessQuery

process = BaseProcessQuery()


# Function tha execute the search of a query
def search(query: SearchQuery) -> List[SearchResult]:
    # Mock search service
    # Use the Methods that are necesary etc.
    return [SearchResult(title="Example Result", url="https://example.com", snippet="This is an example result.")]
