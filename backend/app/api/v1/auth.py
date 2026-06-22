from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from backend.app.schemas.auth import (
    RegisterRequest,
    LoginRequest
)

from backend.app.services.auth_service import AuthService
from backend.app.dependencies.database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

auth_service = AuthService()


@router.post("/register")
def register(
    request: RegisterRequest,
    db: Session = Depends(get_db)
):
    return auth_service.register(
        db,
        request
    )


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):
    return auth_service.login(
        db,
        request.email,
        request.password
    )