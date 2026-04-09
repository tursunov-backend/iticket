from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.db.session import get_db
from app.schemas.user import UserRegistration, UserLogin, UserLoginResponse
from app.services.user_service import UserService


router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/register")
async def register_view(
    user_data: Annotated[UserRegistration, Body()],
    db: Annotated[Session, Depends(get_db)],
):
    user_service = UserService(db)
    user = user_service.create_user(user_data)

    return user


@router.post("/login")
async def login_view(
    data: Annotated[UserLogin, Body()], db: Annotated[Session, Depends(get_db)]
):
    user_service = UserService(db)
    login_response = user_service.authenticate_user(data)

    return login_response
