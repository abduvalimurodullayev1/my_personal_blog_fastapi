from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from others.database import SessionLocal
from others.models import User, Post, Comment
from others.schemas import CommentSchema

router = APIRouter(
    prefix="/posts",
    tags=['/posts']
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_comment(comment: CommentSchema, db: Session = Depends(get_db)):
    author = db.query(User).filter(User.id == comment.user_id).first()
    if not author:
        raise HTTPException(status_code=400, detail="Foydalanuvchi topilmadi")

    post = db.query(Post).filter(Post.id == comment.post_id).first()
    if not post:
        raise HTTPException(status_code=400, detail="Kategoriya topilmadi")

    new_comment = Comment(**comment.dict())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return {"message": "Fikr qo'shildi"}


def get_comment(db: Session):
    posts = db.query(Comment).all()
    return posts


def delete_comment(id: int, db: Session):
    comment = db.query(Comment).filter(Comment.id == id)
    if not comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Comment topilmadi")
    comment.delete()
    db.commit()
    return "Fikr o'chirildi"
