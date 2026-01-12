import jwt
from passlib.context import CryptContext
from app.core.config import JWT_SECRET, JWT_ALGORITHM

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# Password hashing
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# JWT
def create_jwt(user_id: int) -> str:
    payload = {"user_id": user_id}
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

def decode_jwt(token: str) -> dict:
    return jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
