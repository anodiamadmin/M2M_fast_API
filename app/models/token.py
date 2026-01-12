from sqlalchemy import Column, Integer, String, ForeignKey
from app.db.base import Base

class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    token = Column(String, unique=True, nullable=False)
