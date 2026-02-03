# Need to migrate to Alembic later for database scaling in production
# CORS security to be enhanced in production
# Need to switch to Async SQLAlchemy (AsyncSession) using aiosqlite or asyncpg instead of synchronous Session with psycopg2 for database calls as userbase grows
# Python's logging module to be implemented fo better error logs

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base, engine
from app.api.auth import router as auth_router
from app.api.user import router as user_router

# DEV ONLY: auto-create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="micro2move Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # dev only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(user_router, prefix="/users", tags=["user"])

@app.get("/health")
def health():
    return {"status": "ok"}
