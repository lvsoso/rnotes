from typing import Any
from fastapi import APIRouter

router = APIRouter()

@router.get("/", summary="Get data", description="Get data")
async def get_data() -> Any:
    return {"message": "Hello World"}

@router.post("/", summary="Create data", description="Create data")
async def create_data() -> Any:
    return {"message": "Hello World"}

@router.get("/deprecated", deprecated=True)
async def deprecated() -> Any:
    return {"message": "Hello World"}