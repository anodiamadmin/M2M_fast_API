from pydantic import BaseModel, EmailStr
from datetime import date

class SignUpSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    date_of_birth: date

class SignInSchema(BaseModel):
    email: EmailStr
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
