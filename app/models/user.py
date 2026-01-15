from sqlalchemy import Column, Integer, String, Date
from app.db.base import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(255), nullable=False)  # Added length
    # FIXED: Added (255) to allow indexing
    email = Column(String(255), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False) # Added length
    date_of_birth = Column(Date, nullable=False)