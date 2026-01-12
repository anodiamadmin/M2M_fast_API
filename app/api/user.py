from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserSchema
from app.db.base import get_db
from app.models.user import User
from app.core.auth_session import get_current_user

router = APIRouter()

@router.get("/user", response_model=UserSchema)
def get_user(current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    return current_user
