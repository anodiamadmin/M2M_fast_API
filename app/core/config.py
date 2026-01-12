import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
JWT_SECRET = os.getenv("JWT_SECRET", "supersecretkey")
JWT_ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")

if "JWT_ALGORITHM" not in os.environ:
    print("⚠️ Using fallback JWT_ALGORITHM")
