from dataclasses import dataclass
from typing import List


@dataclass
class DataItem:
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


@dataclass
class Support:
    text: str
    url: str


@dataclass
class UsersResponse:
    per_page: int
    total: int
    data: List[DataItem]
    page: int
    total_pages: int
    support: Support
