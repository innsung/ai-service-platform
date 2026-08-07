from fastapi import FastAPI
from routes.book import router

from database import Base, engine

# 테이블 생성
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(router, prefix="/fastapi")