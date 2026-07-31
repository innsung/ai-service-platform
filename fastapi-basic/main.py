from fastapi import FastAPI
from routers.hello import hello_router
from routers.todo import todo_router
from routers.book import book_router

app = FastAPI() # FastAPI 서버 생성

@app.get("/") # http://127.0.0.1:8000
async def welcome() -> dict:
    return {
        "message" : "GET:: welcome to FastAPI wolrd!!"
    }

@app.post("/") # http://127.0.0.1:8000
async def welcome() -> dict:
    return {
        "message" : "POST:: welcome to FastAPI wolrd!!"
    }

app.include_router(hello_router)
app.include_router(todo_router)
app.include_router(book_router)