from functools import lru_cache
from typing import Annotated

from pydantic import field_validator
from pydantic_settings import BaseSettings, NoDecode, SettingsConfigDict


class Settings(BaseSettings):
    """애플리케이션 설정. `.env` 파일 또는 환경변수에서 읽어옵니다."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    project_name: str = "Fleet-Back"
    api_v1_prefix: str = "/api/v1"
    debug: bool = False

    # CORS 허용 오리진 (쉼표로 구분: CORS_ORIGINS=http://localhost:3000,https://example.com)
    cors_origins: Annotated[list[str], NoDecode] = ["http://localhost:3000"]

    #--- mysql ---
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    @field_validator("cors_origins", mode="before")
    @classmethod
    def _split_cors_origins(cls, v: object) -> object:
        if isinstance(v, str):
            return [origin.strip() for origin in v.split(",") if origin.strip()]
        return v


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
