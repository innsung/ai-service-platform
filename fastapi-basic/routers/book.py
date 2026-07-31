# /books or /book => CRUD

from fastapi import APIRouter, Path
from pydantic import BaseModel

book_router = APIRouter()

class BookItem(BaseModel):
    title: str
    publisher: str
    price: int
    isbn: int

class Book(BaseModel):
    id: int
    item: BookItem

book_list = []

# C : Create(post)
@book_router.post("/book") # http://127.0.0.1:8000
async def create_book(book: Book) -> dict:
    book_list.append(book)
    return {
        "message" : "Create book",
        "book_list": book_list
    }

# R : Read(get)
# R: Read-all
@book_router.get("/book/all") # http://127.0.0.1:8000
async def read_book() -> dict:
    return {
        "message:All" : book_list
    }

# R: Read - id별 조회
@book_router.get("/book/{id}") # http://127.0.0.1:8000
async def read_book(id: int) -> dict:
    for book in book_list:
        if book.id == id:
            return{
                "book": book
            }
    return {
        "message:All" : "read!!"
    }

# U : Update(put)
@book_router.put("/book/{id}") # http://127.0.0.1:8000
async def update_book(new_item:BookItem, id:int = Path(..., title="")) -> dict:
    for book in book_list:
        if book.id == id:
            book.item = new_item
            return {"message": "업데이트 성공", "book": book}
    return {
        "message" : "id 확인!!"
    }

# D : Delete(delete)
# D : Delete 전체 삭제
@book_router.delete("/book") # http://127.0.0.1:8000
async def delete_book() -> dict:
    if len(book_list) > 0:
        book_list.clear()
        return {"message": "삭제 성공!!"}
    return {
        "message" : "데이터 없음!!"
    }

# D : Delete id 삭제
@book_router.delete("/book/{id}") # http://127.0.0.1:8000
async def delete_book(id: int) -> dict:
    for index in range (len(book_list)):
        book = book_list[index]
        if book.id == id:
            book_list.pop(index)
            return {"message": "삭제 성공!!"}
    return {
        "message" : "id 확인!!"
    }
