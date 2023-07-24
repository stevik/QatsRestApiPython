from dataclasses import dataclass
from datetime import datetime


@dataclass
class UserResponse:
    name: str
    job: str
    id: int
    createdAt: datetime
