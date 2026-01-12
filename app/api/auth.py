from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth import SignUpSchema, SignInSchema, TokenSchema
from app.db.base import get_db
from app.models.user import User
from app.models.token import Token
from app.core.security import hash_password, verify_password, create_jwt

router = APIRouter()

@router.post("/signup", response_model=TokenSchema)
def signup(user: SignUpSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_pwd = hash_password(user.password)
    new_user = User(full_name=user.full_name, email=user.email, hashed_password=hashed_pwd)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    token = create_jwt(new_user.id)
    token_entry = Token(user_id=new_user.id, token=token)
    db.add(token_entry)
    db.commit()

    return {"access_token": token}

@router.post("/signin", response_model=TokenSchema)
def signin(user: SignInSchema, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail="Email does not exist")
    if not verify_password(user.password, db_user.hashed_password):
        raise HTTPException(status_code=400, detail="Incorrect password")

    token = create_jwt(db_user.id)
    token_entry = Token(user_id=db_user.id, token=token)
    db.add(token_entry)
    db.commit()

    return {"access_token": token}
