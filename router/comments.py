from click.shell_completion import add_completion_class
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import others.models
import others.schemas
from others.database import SessionLocal
from others.jwt_bearer import JWTBearer
from others.models import User, Comment, Post
from repo.comments import create_comment, delete_comment, get_comment
from others.schemas import CommentSchema


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


router = APIRouter(
    prefix="/comments",
    tags=['comments']
)


@router.post("/")
def create(request: CommentSchema, db: Session = Depends(get_db)):
    return create_comment(request, db)


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_comments(id: int, db: Session = Depends(get_db)):
    return delete_comment(id, db)


@router.get("/", dependencies=[Depends(JWTBearer)], )
def get_posts_all(db: Session = Depends(get_db)):
    return get_comment(db)
