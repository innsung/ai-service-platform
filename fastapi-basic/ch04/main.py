from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from routers.todo import todo_router
from routers.book import book_router

from database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

# 리액트 프론트엔드 접속 허용
app.add_middleware(
    CORSMiddleware,
        allow_origins=[
            "http://localhost:5173",
            "http://127.0.0.1:5173",
            "http://192.168.7.25:5173"
        ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# app.include_router(todo_router) # todo 애플리케이션
app.include_router(book_router, prefix="/api") # 도서관리 애플리케이션