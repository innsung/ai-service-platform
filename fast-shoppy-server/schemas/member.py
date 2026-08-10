from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional
from datetime import datetime

# MemberItem class
class MemberItem(BaseModel):
    id: str
    pwd: str
    name: str
    phone: str
    email: str

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "id": "test1",
                    "pwd": "pw1234",
                    "name": "홍길동",
                    "phone": "010-1234-1234",
                    "email": "test@a.com" 
                }
            ]
        }
    )

# Member class
class Member(BaseModel):
    id: str
    pwd: str
    name: str
    phone: str
    email: str
    role: str
    created_at: datetime