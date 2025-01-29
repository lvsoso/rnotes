from fastapi import APIRouter
from routers.api_v1.endpoints.user import router as user_router
from routers.api_v1.endpoints.data import router as data_router
from routers.api_v1.endpoints.resp import router as resp_router

router = APIRouter()

router.include_router(user_router, prefix="/user", tags=["user"])
router.include_router(data_router, prefix="/data", tags=["data"])
router.include_router(resp_router, prefix="/resp", tags=["resp"])