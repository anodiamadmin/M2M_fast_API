from pydantic import BaseModel, EmailStr

class SignUpSchema(BaseModel):
    full_name: str
    email: EmailStr
    password: str

class SignInSchema(BaseModel):
    email: EmailStr
    password: str

class TokenSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"
