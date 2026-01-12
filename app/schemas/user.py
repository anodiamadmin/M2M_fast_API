from pydantic import BaseModel, EmailStr

class UserSchema(BaseModel):
    id: int
    full_name: str
    email: EmailStr

    class Config:
        orm_mode = True
