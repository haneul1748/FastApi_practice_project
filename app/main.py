from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.core.exception.global_exception_handlers import register_exception_handlers

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 시작 시 실행 (DB 연결 등)
    yield
    # 종료 시 실행 (리소스 정리 등)


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.project_name,
        debug=settings.debug,
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    register_exception_handlers(app)    # main.py에 exception_handler (등록 미들웨어뒤, 라우터 앞 아무데나)

    app.include_router(api_router, prefix=settings.api_v1_prefix)

    @app.get("/")
    async def root() -> dict[str, str]:
        return {"message": f"{settings.project_name} is running"}

    return app


app = create_app()
