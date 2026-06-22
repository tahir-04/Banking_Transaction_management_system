from fastapi import FastAPI

from backend.app.api.v1.auth import (
    router as auth_router
)

from backend.app.api.v1.user import (
    router as user_router
)

from backend.app.core.config import settings

print(settings.DATABASE_URL)

app = FastAPI(
    title="Banking Transaction Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message":
        "Banking Transaction Management System API"
    }


app.include_router(auth_router)
app.include_router(user_router)