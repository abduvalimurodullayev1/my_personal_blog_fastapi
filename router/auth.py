import httpx
from fastapi import APIRouter, Depends, HTTPException, Body, status
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from others.database import SessionLocal
from others.jwt_handler import signJWT
from others.models import *
from others.schemas import *

github_client_id = 'Ov23liytqPPjfiRWNxv1'
github_secret_id = '94892adaf1fafa80e7cdfe21ec7c837cacca1d64'
router = APIRouter(
    prefix='/user',
    tags=['user']
)


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("register", )
def user_signup(user: UserSchema = Body(...), db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Bu foydalanuvchi allaqachon mavjud")

    hashed_password = pwd_context.hash(user.password)
    new_user = User(email=user.email, hashed_password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return signJWT(new_user.email)
    


def check_user(data: UserLoginSchema, db: Session):
    user = db.query(User).filter(User.email == data.email).first()
    if user and pwd_context.verify(data.password, user.hashed_password):
        return True
    return False


@router.post("login", )
def user_login(user: UserLoginSchema = Body(...), db: Session = Depends(get_db)):
    if check_user(user, db):
        return signJWT(user.email)
    else:
        raise HTTPException(status_code=400, detail="Parol yoki email ma'lumotlari noto'g'ri")


@router.get("/login_github")
async def github_login():
    return RedirectResponse(f"https://github.com/login/oauth/authorize?client_id={github_client_id}",
                            status_code=status.HTTP_302_FOUND)


@router.get("/github-code")
async def github_code(code: str):
    params = {
        "client_id": github_client_id,
        "client_secret": github_secret_id,
        "code": code
    }
    header = {"Accept": "application/json"}
    async with httpx.AsyncClient() as client:
        response = await client.post(url="https://github.com/login/oauth/access_token", params=params, headers=header)
    response_json = response.json()
    access_token = response_json.get("access_token")
    async with httpx.AsyncClient() as client:
        header.update({"Authorization": f"token {access_token}"})
        response = await client.get(url="https://api.github.com/user", headers=header)
    response_json = response.json()
    return response_json

