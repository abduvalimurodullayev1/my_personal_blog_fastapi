
from fastapi import Depends, status, APIRouter
from fastapi.openapi.models import Response
from sqlalchemy.orm import Session
from others.database import SessionLocal
from repo.post import get_posts, show_posts, create_post, delete_post, update_post
from others.schemas import PostSchema
from others.jwt_bearer import JWTBearer

router = APIRouter(
    tags=['posts'],
    prefix="/posts"
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", dependencies=[Depends(JWTBearer)], )
def get_posts_all(db: Session = Depends(get_db)):
    return get_posts(db)


@router.get('/{id}', status_code=200, response_model=PostSchema, dependencies=[Depends(JWTBearer())])
def show(id: int, response: Response, db: Session = Depends(get_db)):
    return show_posts(id, db)


@router.post("/", dependencies=[Depends(JWTBearer())], )
def create(request: PostSchema, db: Session = Depends(get_db)):
    return create_post(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(JWTBearer())])
def destroy(id: int, db: Session = Depends(get_db)):
    return delete_post(id, db)


@router.put("/{id}", status_code=status.HTTP_202_ACCEPTED)
def update_posts(id: int, request: PostSchema, db: Session = Depends(get_db)):
    return update_post(id, db, request)
