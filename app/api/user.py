from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.user import UserSchema
from app.db.base import get_db
from app.models.user import User
from app.deps import auth_guard

router = APIRouter()

@router.get("/user", response_model=UserSchema)
def get_user(current_user: User = Depends(auth_guard), db: Session = Depends(get_db)):
    return current_user
