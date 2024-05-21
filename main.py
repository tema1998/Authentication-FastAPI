import uuid

from fastapi import FastAPI
from fastapi_users import FastAPIUsers

from api.auth import auth_backend
from api.manager import get_user_manager
from api.schemas import UserRead, UserCreate
from db.database import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app = FastAPI(title="Auth microservice")

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)