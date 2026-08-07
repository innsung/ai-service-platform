from pydantic import BaseModel, ConfigDict, Field
from typing import List

class BookItem(BaseModel):
    title: str
    author: str
    publisher: str
    year: str
    status: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "title": "FastAPI 정복",
                    "author": "홍길동",
                    "publisher": "파이썬 출판사",
                    "year": "2026",
                    "status": "대여가능"
                }
            ]
        }
    )

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    year: str
    status: str

class Books(BaseModel):
    books: List[Book] = Field(default_factory=list)