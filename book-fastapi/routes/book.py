from fastapi import APIRouter, Depends, HTTPException, status, Path
from schemas.book import BookItem, Book, Books
from models.book import BookModel
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database import get_db

router = APIRouter()

# Middleware 

books = []

# C: Insert
@router.post("/book", response_model=Book)
async def addBook(bookItem: BookItem,                    
                    db: Session=Depends(get_db)) -> dict:
    
    # 1. BookModel 생성 및 입력 데이터 추가
    bookModel = BookModel(
        title = bookItem.title,
        author = bookItem.author,
        publisher = bookItem.publisher,
        year = bookItem.year,
        status = bookItem.status
    )

    # 2. db.add() - SQL 생성 
    db.add(bookModel)

    # 3. db.commit() - Transaction 실행
    db.commit()

    # 4. db.refresh(모델타입) - 실행 결과 가져오기
    db.refresh(bookModel)

    return bookModel


# R: Select All
@router.get("/books", response_model=Books)
async def getAll(db: Session=Depends(get_db)) -> list:
    init_books = db.execute(
        select(BookModel).order_by(BookModel.id)
    )
    books = init_books.scalars().all()  # [{id:1 ...}, {...}...]

    return {
        "books": books
    }


# R : Select ID

# U : Update
@router.put("/book/{id}")
async def updateId(newData: BookItem, 
                    id:int = Path(...),
                    db: Session = Depends(get_db)) -> dict:
    book = db.get(BookModel, id)
    
    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Id does not exist!"
        )
    book.title = newData.title
    book.author = newData.author
    book.publisher = newData.publisher
    book.year = newData.year
    book.status = newData.status

    db.commit()
    
    return {
        "isUpdate": True
    }



# D : Delete ID
@router.delete("/book/{id}")
async def deleteId(id:int, db:Session=Depends(get_db)) -> dict:
    book = db.get(BookModel, id)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Id does not exist!"
        )
    db.delete(book)
    db.commit()

    return {
        "isDelete": True
    }



# D : Delete All