from app.core.exception.app_error import AppError


class CustomerNotFoundError(AppError):

    status_code = 404

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"customer {customer_id} not found") # customer_id를 찾지못했다.

class CustomerAuthenticationError(AppError):

    status_code = 401

    def __init__(self, customer_id: int):
        self.customer_id = customer_id
        super().__init__(f"customer {customer_id} not authenticated") # 인증된 사용자가 아니다.