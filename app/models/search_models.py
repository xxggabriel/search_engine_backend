from typing import Any, Dict
from pydantic import BaseModel


class SearchQuery(BaseModel):
    query: str


class SearchResult(BaseModel):
    # hits: Dict
    # highlight: Dict
    # aggregations: Dict
    results: str
