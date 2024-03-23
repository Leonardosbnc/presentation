from fastapi import APIRouter

from api.serializers.detail import DetailResponse
from api.utils.details import get_personal_data

router = APIRouter()


@router.get("/", response_model=DetailResponse, status_code=200)
async def me():
    res_data = get_personal_data()
    return res_data
