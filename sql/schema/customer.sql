-- customer 테이블 스키마 (MySQL)
-- 원본 스펙은 PostgreSQL 타입(BIGSERIAL, TIMESTAMPTZ)이라 MySQL 타입으로 변환함.
--   BIGSERIAL   -> BIGINT AUTO_INCREMENT
--   INTEGER     -> INT
--   TIMESTAMPTZ -> DATETIME (타임존 미보관 / 앱에서 UTC or KST 통일 권장)
--   NOW()       -> CURRENT_TIMESTAMP

CREATE TABLE customer (
    id                  BIGINT       NOT NULL AUTO_INCREMENT               COMMENT '고객 ID',
    name                VARCHAR(40)  NOT NULL                              COMMENT '이름',
    phone               VARCHAR(20)  NOT NULL                              COMMENT '연락처 (예약 식별 키)',
    emergency_phone     VARCHAR(20)  NULL                                  COMMENT '긴급연락처',
    gender              VARCHAR(2)   NULL                                  COMMENT '성별 (남/여)',
    age                 INT          NULL                                  COMMENT '나이',
    company_id          VARCHAR(80)  NULL                                  COMMENT '주이용 기업 (집계 캐시)',
    top_branch          VARCHAR(40)  NULL                                  COMMENT '주이용 지점 (집계 캐시)',
    last_used_at        DATE         NULL                                  COMMENT '최근 이용일 (표시 캐시)',
    last_vehicle_number VARCHAR(20)  NULL                                  COMMENT '최근 이용 차량 (표시 캐시)',
    total_count         INT          NOT NULL DEFAULT 0                    COMMENT '총 예약수',
    done_count          INT          NOT NULL DEFAULT 0                    COMMENT '이용 완료',
    cancel_count        INT          NOT NULL DEFAULT 0                    COMMENT '취소',
    noshow_count        INT          NOT NULL DEFAULT 0                    COMMENT '노쇼',
    upcoming_count      INT          NOT NULL DEFAULT 0                    COMMENT '예정',
    customer_grade      VARCHAR(20)  NOT NULL DEFAULT '예약보통'           COMMENT '고객등급 (예약보통/예약주의/예약금지)',
    safety_score        DECIMAL(5,2) NULL                                  COMMENT '안전 점수 (0~100)',
    memo                TEXT         NULL                                  COMMENT '메모',
    created_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP    COMMENT '생성일시',
    updated_at          DATETIME     NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '수정일시',
    deleted_at          DATETIME     NULL                                  COMMENT '삭제일시 (soft delete)',
    PRIMARY KEY (id),
    UNIQUE KEY uq_customer_phone (phone),
    KEY idx_customer_grade (customer_grade),
    KEY idx_customer_last_used_at (last_used_at),
    KEY idx_customer_deleted_at (deleted_at)
) ENGINE=InnoDB
  DEFAULT CHARSET=utf8mb4
  COLLATE=utf8mb4_unicode_ci
  COMMENT='고객';
