from fastapi import FastAPI

from app.db.session import engine
from app.db.base import Base
from app.models.user import User
from app.api.users import router as user_router

app = FastAPI(title="FastAPI CRUD")

# Create tables
Base.metadata.create_all(bind=engine)

app.include_router(user_router)
