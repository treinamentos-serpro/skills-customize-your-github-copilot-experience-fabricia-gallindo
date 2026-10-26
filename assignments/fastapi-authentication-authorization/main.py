import os
from typing import Annotated

import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jwt.exceptions import InvalidTokenError
from pwdlib import PasswordHash
from pydantic import BaseModel

app = FastAPI(title="Authenticated Books API")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
password_hash = PasswordHash.recommended()
secret_key = os.getenv("JWT_SECRET_KEY")
algorithm = "HS256"


class Token(BaseModel):
    access_token: str
    token_type: str


class UserPublic(BaseModel):
    username: str
    role: str


class Message(BaseModel):
    message: str


def create_demo_user(username: str, password: str, role: str) -> dict[str, str]:
    return {
        "username": username,
        "hashed_password": password_hash.hash(password),
        "role": role,
    }


users: dict[str, dict[str, str]] = {
    "student": create_demo_user("student", "student-demo", "student"),
    "admin": create_demo_user("admin", "admin-demo", "admin"),
}


@app.post("/token", response_model=Token)
def login(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this endpoint",
    )


def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],
) -> dict[str, str]:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this dependency",
    )


def require_admin(
    current_user: Annotated[dict[str, str], Depends(get_current_user)],
) -> None:
    raise HTTPException(
        status_code=status.HTTP_501_NOT_IMPLEMENTED,
        detail="Implement this dependency",
    )


@app.get("/users/me", response_model=UserPublic)
def read_current_user(
    current_user: Annotated[dict[str, str], Depends(get_current_user)],
) -> UserPublic:
    return UserPublic(
        username=current_user["username"],
        role=current_user["role"],
    )


@app.get(
    "/admin",
    response_model=Message,
    dependencies=[Depends(require_admin)],
)
def admin_area() -> Message:
    return Message(message="Acesso administrativo autorizado")