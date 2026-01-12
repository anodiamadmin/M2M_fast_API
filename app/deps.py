from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from app.db.base import SessionLocal
from app.models.token import Token
from app.models.user import User
from app.core.security import decode_jwt

security = HTTPBearer()

def auth_guard(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(lambda: SessionLocal())
) -> User:
    token_str = credentials.credentials

    try:
        payload = decode_jwt(token_str)
        user_id = payload.get("user_id")
        if not user_id:
            raise HTTPException(status_code=401, detail="Invalid token payload")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

    token_in_db = db.query(Token).filter(Token.token == token_str).first()
    if not token_in_db:
        raise HTTPException(status_code=401, detail="Token revoked or invalid")

    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    return user
