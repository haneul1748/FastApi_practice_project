-- name: get_all()
-- 전체 고객 조회 (삭제 안 된 것만)
SELECT *
FROM customer
WHERE deleted_at IS NULL
ORDER BY id;


-- name: get_by_id(id)^
-- id로 고객 1명 조회
SELECT *
FROM customer
WHERE id = :id
  AND deleted_at IS NULL;
