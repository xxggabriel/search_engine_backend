import json
from typing import Any, Dict, List
from fastapi import APIRouter, HTTPException
from app.models.search_models import SearchQuery, SearchResult
from app.services.search_service import search

from fastapi.responses import FileResponse
import os

router = APIRouter()


@router.post("/search")
async def search_endpoint(query: SearchQuery):
    results = search(query.query)
    if not results:
        raise HTTPException(status_code=404, detail="No results found")
    
    return search(query.query)




# Rota para retornar o arquivo index.html
@router.get("/")
async def read_index():
    # Caminho para o arquivo index.html
    index_path = os.path.join(os.path.dirname(__file__), 'static', 'index.html')
    return FileResponse(index_path)