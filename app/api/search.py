from fastapi import APIRouter, HTTPException, Status
from app.models.search_models import SearchQuery, SearchResult
from app.services.search_service import search

router = APIRouter()


@router.post("/search/", response_model=list[SearchResult])
async def search_endpoint(query: SearchQuery):
    results = search(query.query)
    if not results:
        raise HTTPException(status_code=Status.HTTP_404_NOT_FOUND, detail="No results found")
    return results
