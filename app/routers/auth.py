from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from app.oauth import create_access_token
import app.utils
from app.models.auth import Token


router = APIRouter(tags=['Authentication'])

user = {
    "id": 1,
    "username": "admin",
    "password": "$2b$12$LljMOaUMuuow8i7DifTJauE/Jr8y0LSTMkBCiJpKxP5AlOyZayCfy"
}


@router.post("/login", response_model=Token)
def login(userdetails: OAuth2PasswordRequestForm = Depends()):
    if not utils.verify_password(userdetails.password, user.get("password")):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(data={"user_id": user.get("id")})
    return {"access_token": access_token, "token_type": "bearer"}
