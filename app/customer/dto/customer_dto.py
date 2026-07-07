from datetime import date, datetime

from pydantic import BaseModel

class CustomerResponse(BaseModel):
    """고객 조회 응답 형태."""

    id: int
    name: str
    phone: str
    emergency_phone: str | None = None
    gender: str | None = None
    age: int | None = None
    company_id: str | None = None
    top_branch: str | None = None
    last_used_at: date | None = None
    last_vehicle_number: str | None = None
    total_count: int
    done_count: int
    cancel_count: int
    noshow_count: int
    upcoming_count: int
    customer_grade:str
    safety_score: float | None = None
    memo: str | None = None
    created_at: datetime
    updated_at: datetime