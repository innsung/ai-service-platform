from fastapi import APIRouter, Depends, HTTPException, status
from core.security import hash_password

from schemas.member import MemberItem, Member
from models.member import MemberModel
from sqlalchemy.orm import Session
from database.connection import get_db

member_router = APIRouter()

# 아이디 중복 체크
@member_router.get("/idCheck/{id}")
async def idCheck(id: str,
                    db: Session = Depends(get_db)) -> dict:
    memberModel = db.get(MemberModel, id)
    db.commit()
    
    if memberModel is None:
        return {
            "isFind": False
        }
        # raise HTTPException(
        #     status_code = status.HTTP_404_NOT_FOUND,
        #     detail= "ID does not exist"
        # )
    return {
        "isFind": True
    }


# 회원가입
@member_router.post("/signup")
async def signup(memberItem:MemberItem,
                    db: Session = Depends(get_db)) -> dict:
    # DB 연동 : 
    # 1. models.MemberModel에 memberItem 저장
    memberModel = MemberModel(
        id = memberItem.id,
        pwd = hash_password(memberItem.pwd),
        name = memberItem.name,
        phone = memberItem.phone,
        email = memberItem.email
    )

    # 2. 연결된 db session의 add() 함수 호출
    db.add(memberModel)

    # 3. commit
    db.commit()

    # 4. refresh 함수를 통해 저장된 데이터 가져오기
    db.refresh(memberModel)

    return {
        "isSignup": True
    }