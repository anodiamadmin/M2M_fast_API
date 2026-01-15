from sqlalchemy import Column, Integer, String
from app.db.base import Base

class Token(Base):
    __tablename__ = "tokens"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    # FIXED: Added (255) so unique=True works in MySQL
    token = Column(String(512), unique=True, nullable=False)