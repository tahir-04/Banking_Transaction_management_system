from fastapi import APIRouter
from fastapi import Depends

from backend.app.dependencies.auth import (
    get_current_user,
    admin_required
)

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)


@router.get("/profile")
def profile(
    current_user=Depends(
        get_current_user
    )
):
    return {
        "id": str(current_user.customer_id),
        "email": current_user.email,
        "first_name": current_user.first_name,
        "last_name": current_user.last_name,
        "role": current_user.role
    }


@router.get("/admin")
def admin_dashboard(
    current_user=Depends(
        admin_required
    )
):
    return {
        "message": "Welcome Admin"
    }