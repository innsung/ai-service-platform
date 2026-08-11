from fastapi import APIRouter, Depends, HTTPException, status, Response
from core.security import hash_password, verify_password, create_access_token, create_refresh_token

from schemas.member import MemberItem, LoginItem
from models.member import MemberModel
from sqlalchemy.orm import Session
from database.connection import get_db

member_router = APIRouter()

# 토큰명, 유효기간 설정
REFRESH_COOKIE_NAME = "refreshToken"
REFRESH_COOKIE_MAX_AGE = 60 * 60 * 24 * 7 

# 로그아웃
@member_router.post("/logout")
async def logout(response: Response) -> dict:
    return{
        "isLogout": True
    }

# 로그인
@member_router.post("/login")
async def login(loginItem: LoginItem,
                response: Response,
                db: Session = Depends(get_db)) -> dict:
    # 1. id를 통해 DB 데이터 가져오기
    memberModel = db.get(MemberModel, loginItem.id)

    if memberModel is None:
        return {
            "isLogin": False
        }
    result = verify_password(loginItem.pwd, memberModel.pwd)

    if result:
        access_token = create_access_token(memberModel.id, memberModel.role)
        refresh_token = create_refresh_token(memberModel.id, memberModel.role)
        response.set_cookie(
            key=REFRESH_COOKIE_NAME,
            value=refresh_token,
            httponly=True,
            # samsite="lax",
            secure=False,
            max_age=REFRESH_COOKIE_MAX_AGE
        )         
        return {
            "isLogin": result,
            "role": memberModel.role,
            "accessToken": access_token
        }


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