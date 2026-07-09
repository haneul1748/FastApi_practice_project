
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app.core.exception.app_error import AppError

async def app_error_handler(request: Request, exc: AppError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message},
    )

def register_exception_handlers(app: FastAPI) -> None:
    # 부모(AppError)만 등록하면 모든 자식 예외를 한 핸들러가 처리함.
    app.add_exception_handler(AppError, app_error_handler)