from passlib.context import CryptContext
import bcrypt

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(raw_password: str, hashed_password: str) -> str:
    return bcrypt.checkpw(raw_password.encode(), hashed_password.encode())

