class AppError(Exception):
    """앱 공통 예외의 부모. 자식이 status_code만 지정시 핸들러가 그대로 사용함."""

    status_code: int = 500  # 기본 서버 에러를 500에러로 표기함.

    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
