from fastapi import APIRouter

from .detail import router as detail_router

main_router = APIRouter()

main_router.include_router(detail_router, prefix="/details", tags=["details"])
