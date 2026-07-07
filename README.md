# Fleet-Back

FastAPI 백엔드 프로토타입. 패키지·가상환경·Python 버전은 모두 [uv](https://docs.astral.sh/uv/)로 관리합니다.

## 요구사항

- [uv](https://docs.astral.sh/uv/) (Python 3.13은 uv가 자동 설치)

## 시작하기

```bash
# 의존성 설치 (.venv 자동 생성)
uv sync

# 환경변수 파일 준비
cp .env.example .env

# 개발 서버 실행 (자동 리로드)
uv run uvicorn app.main:app --reload

# 또는 엔트리 스크립트로 실행
uv run python main.py
```

- API 문서(Swagger): http://127.0.0.1:8000/docs
- 헬스체크: http://127.0.0.1:8000/api/v1/health

## 개발

```bash
uv run pytest        # 테스트
uv run ruff check .  # 린트
uv run ruff format . # 포맷
```

## 구조

```
app/
  main.py              # 앱 팩토리 (create_app), 미들웨어, 라우터 등록
  core/config.py       # 설정 (환경변수 / .env)
  api/
    router.py          # v1 라우터 집계
    routes/health.py   # 헬스체크 엔드포인트
tests/                 # pytest 테스트
main.py                # uvicorn 실행 엔트리포인트
```

새 엔드포인트는 `app/api/routes/` 에 라우터를 추가하고 `app/api/router.py` 에 등록하세요.
