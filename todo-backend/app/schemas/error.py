from pydantic import BaseModel
from typing import Optional


class ErrorDetail(BaseModel):
    """
    Schema for error responses with code, message, and optional details.
    """
    code: str
    message: str
    details: Optional[str] = None