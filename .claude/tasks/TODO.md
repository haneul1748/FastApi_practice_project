# Fleet-Back TODO

한 번에 하나씩 진행. 완료하면 `[x]` 체크하고, **완료 날짜 + 무엇이 바뀌었는지**를 함께 기록.

## 진행 중
- [ ] **customer 조회 API 흐름 만들기 (A안)** — MyBatis 스타일 aiosql
  - [ ] customer 테이블 CREATE 스키마 작성 (사용자가 컬럼 정보 제공 → Claude가 DDL 생성 → 사용자가 create)
  - [ ] `sql/customer.sql` — 조회 SQL 작성 (aiosql 매퍼)
  - [ ] aiosql로 SQL 로드 + FastAPI 커넥션 주입 (get_db 의존성)
  - [ ] `api/routes/customer.py` — 조회 엔드포인트 + 라우터 등록
  - [ ] 실제 조회 API 동작 확인

## 예정
<!-- 여기에 하나씩 추가 -->

## 완료
- [x] **MySQL 접속 설정** — 2026-07-07
  - 라이브러리 추가: `aiosql`, `pymysql` (동기 방식 / MyBatis 스타일 SQL 매퍼)
  - `app/core/config.py`에 DB 설정 추가 (db_host/port/user/password/name)
  - `.env` / `.env.example`에 DB 접속값 추가
  - `app/db/connection.py` 작성 — `get_connection()` (DictCursor로 결과를 딕셔너리 반환)
  - 접속 테스트 성공: MySQL 8.4.9, database=fleet 확인

- [x] **FastAPI 프로젝트 초기 세팅** — 2026-07-07
  - uv로 프로젝트 초기화 (Python 3.13, 가상환경 `.venv`)
  - 의존성 추가: `fastapi[standard]`, `pydantic-settings` / dev: `ruff`, `pytest`
  - `app/` 구조 생성: `main.py`(앱 팩토리·CORS), `core/config.py`(설정), `api/router.py`, `api/routes/health.py`(헬스체크)
  - `.env` / `.env.example` 추가, `.gitignore`에 `.env` 등 반영
  - `tests/test_health.py` 작성 (2개 통과), `pyproject.toml`에 ruff·pytest 설정
  - `README.md` 작성 (실행법·구조 안내)