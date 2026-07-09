# Fleet-Back TODO

한 번에 하나씩 진행. 완료하면 `[x]` 체크하고, **완료 날짜 + 무엇이 바뀌었는지**를 함께 기록.

## 진행 중
<!-- 여기에 하나씩 추가 -->

## 예정
- [ ] customer 상세 조회 엔드포인트 (`GET /api/v1/customers/{id}` — repository의 `find_by_id` 연결)
- [ ] 쓰기(INSERT/UPDATE) 기능 추가 시 트랜잭션 커밋 처리 (pymysql autocommit 꺼짐 → `conn.commit()` 필요)
- [ ] controller의 `response_model=list[CustomerResponse]` 다시 부착 (Swagger 응답 스키마 표시)

## 완료
- [x] **customer 조회 API (findAll) + 의존성 주입(DI) 구조** — 2026-07-08
  - customer 테이블 DDL 작성 → `sql/schema/customer.sql` (사용자가 create)
  - aiosql 매퍼 `sql/mappers/customer/customer.sql` — `get_all` / `get_by_id`
  - 계층별 DI 구조로 분리 (자바 스프링 스타일 **생성자 주입**):
    - `app/db/queries.py` — `get_queries()` provider 추가 (전역 import 제거의 교체 지점)
    - `app/db/connection.py` — `get_connection()`을 `yield` 방식으로 변경 (응답 후 커넥션 자동 close → 누수 방지)
    - `app/customer/repository/customer_repository.py` — `CustomerRepository` 클래스 (conn·queries 생성자 주입) + provider
    - `app/customer/service/customer_service.py` — `CustomerService` 클래스 (repository 주입) + provider, row → `CustomerResponse` 변환
    - `app/customer/controller/customer_controller.py` — 라우터, `Annotated`로 service 주입 (`GET /api/v1/customers`)
    - `app/api/router.py`에 customer 라우터 등록
  - 폴더 구조: `app/customer/{controller,service,repository,dto}/` — 새 도메인의 표준 템플릿
  - 동작 확인: `GET /api/v1/customers` → 200, 샘플 2건 조회 성공

- [x] **헬스체크 제거** — 2026-07-08
  - 초기 서버 확인용 임시 엔드포인트라, customer 흐름 완성 후 정리
  - 삭제: `app/api/routes/` 폴더(health.py), `tests/test_health.py`
  - `app/api/router.py`에서 health 등록 제거 (이제 customer 도메인만 집계)

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