# --------------------------------------------------
# 도서 관리 애플리케이션 - CRUD
# --------------------------------------------------
from fastapi import APIRouter, Path, HTTPException, status, Depends
from schemas.book_schema import Book, BookItem, BookItems

from sqlalchemy import delete, select
from sqlalchemy.orm import Session
from database import get_db
from models.book_model import BookModel

book_router = APIRouter()

book_list = []

# C : Insert(post)
@book_router.post("/book",
                    response_model=Book,
                    status_code=status.HTTP_201_CREATED) 
async def add_book(book_data: BookItem,
                        db: Session=Depends(get_db)) -> dict:
    bookModel = BookModel(title=book_data.title, price=book_data.price, isbn=book_data.isbn)

    db.add(bookModel)
    db.commit()
    db.refresh(bookModel)

    # return bookModel
    return{
        "message": "등록 성공!!",
        "book": {
                    "id": bookModel.id,
                    "title": bookModel.title,
                    "price": bookModel.price,
                    "isbn": bookModel.isbn
                }
    }



# R : Select(get)
# R: Selecct-all
@book_router.get("/books", response_model=BookItems) 
async def getAll(db:Session=Depends(get_db)) -> dict:
    result = db.execute(
        select(BookModel).order_by(BookModel.id)
    )
    books = result.scalars().all()
    return{"books": books}



# R: Select - id별 조회
@book_router.get("/book/{id}", response_model=Book) 
async def getId(id: int,
                db: Session=Depends(get_db)) -> dict:
    book = db.get(BookModel, id)

    if book is None:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="Todo with supplied ID doesn't exist",
                    )
    return book


# U : Update(put)
@book_router.put("/book/{id}", response_model=Book) 
async def update_book(book_data: BookItem,
                        id: int = Path(...),
                        db: Session=Depends(get_db)) -> dict:
    book = db.get(BookModel, id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Todo with supplied ID doesn't exist",
        )

    book.title = book_data.title  # DB Old item => New item 교체
    book.price = book_data.price
    book.isbn = book_data.isbn
    db.commit() # update 실행 - update books set item=? where id=?
    db.refresh(book) # update 실행 - update books set item='JS' where id=1

    return book
    

# D : Delete(delete)
# D : Delete 전체 삭제
@book_router.delete("/book") 
async def deleteAll(db: Session=Depends(get_db)) -> dict:
    result = db.execute(
            delete(BookModel)
    )
    db.commit()
    
    if result.rowcount == 0:
        return{
            "message": "books 테이블의 데이터가 존재하지 않음"
        }
    return {
        "message": "전체 데이터 삭제 완료!!"
    }


# D : Delete id 삭제
@book_router.delete("/book/{id}") 
async def delete_book(id: int,
                        db: Session=Depends(get_db)) -> dict:
    book = db.get(BookModel, id)
    if book is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Todo with supplied ID doesn't exist",
            )
    db.delete(book)
    db.commit()

    return{
        "message": "삭제 완료!!"
    }

