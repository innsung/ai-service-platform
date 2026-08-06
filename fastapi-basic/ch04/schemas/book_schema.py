from typing import List
from pydantic import BaseModel, ConfigDict, Field



class BookItem(BaseModel):
    title: str
    price: int
    isbn: int

    model_config = ConfigDict(
            json_schema_extra={
                "examples":[
                    {
                        "title": "HTML",
                        "price": 30000,
                        "isbn": 2312
                    }
                ]
            }
        )

class Book(BaseModel):
    id: int
    title: str
    price: int
    isbn: int

    model_config = ConfigDict(
        json_schema_extra={
            "examples":[
                {
                    "id": 1,
                    "title": "FastAPI",
                    "price": 20000,
                    "isbn": 1234
                }
            ]
        }
    )

class BookItems(BaseModel):
    books: List[BookItem] = Field(default_factory=list)
