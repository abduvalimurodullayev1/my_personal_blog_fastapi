import httpx
from fastapi import FastAPI, Body, Depends, HTTPException, status, APIRouter
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

from others.database import engine, SessionLocal, Base
from others.schemas import PostSchema, CategorySchema
from others.jwt_bearer import JWTBearer
from repo.category import add_category, update_categories, delete_category

router = APIRouter(
    prefix="/category",
    tags=['category']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", dependencies=[Depends(JWTBearer())], )
def create(request: CategorySchema, db: Session = Depends(get_db)):
    return add_category(request, db)


@router.put("/", dependencies=[Depends(JWTBearer())])
def update_category(id: int, request: PostSchema, db: Session = Depends(get_db)):
    return update_categories(id, db, request)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def destroy_category(id: int, db: Session = Depends(get_db)):
    return delete_category(id, db)
