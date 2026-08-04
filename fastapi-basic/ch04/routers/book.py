# --------------------------------------------------
# 도서 관리 애플리케이션 - CRUD
# --------------------------------------------------
from fastapi import APIRouter, Path, HTTPException, status
from schemas.book_schema import Book, BookItem

book_router = APIRouter()

book_list = []

# C : Create(post)
@book_router.post("/book") 
async def create_book(book: Book) -> dict:
    book_list.append(book)
    return {
        "message" : "Create book",
        "book_list": book_list
    }

# R : Read(get)
# R: Read-all
@book_router.get("/book/all") 
async def read_book() -> dict:
    return {
        "message:All" : book_list
    }

# R: Read - id별 조회
@book_router.get("/book/{id}") 
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
@book_router.put("/book/{id}") 
async def update_book(new_item:BookItem, id:int = Path(..., title="")) -> dict:
    for book in book_list:
        if book.id == id:
            book.title = new_item.title
            book.price = new_item.price
            book.isbn = new_item.isbn
            return {"message": "업데이트 성공", "book": book}
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
            )

# D : Delete(delete)
# D : Delete 전체 삭제
@book_router.delete("/book") 
async def delete_book() -> dict:
    if len(book_list) > 0:
        book_list.clear()
        return {"message": "삭제 성공!!"}
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
            )

# D : Delete id 삭제
@book_router.delete("/book/{id}") 
async def delete_book(id: int) -> dict:
    for index in range (len(book_list)):
        book = book_list[index]
        if book.id == id:
            book_list.pop(index)
            return {"message": "삭제 성공!!"}
    raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
            )