from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: str
    service: str


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """서비스 상태 확인용 헬스체크 엔드포인트."""
    return HealthResponse(status="ok", service="fleet-back")
