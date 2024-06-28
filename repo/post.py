from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from others.database import SessionLocal
from others.models import User, Category, Post
from others.schemas import PostSchema


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_post(post: PostSchema, db: Session = Depends(get_db)):
    author = db.query(User).filter(User.id == post.author_id).first()
    if not author:
        raise HTTPException(status_code=400, detail="Foydalanuvchi topilmadi")

    category = db.query(Category).filter(Category.id == post.category_id).first()
    if not category:
        raise HTTPException(status_code=400, detail="Kategoriya topilmadi")

    new_post = Post(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return {"message": "Post yaratildi!", "": new_post}


def get_posts(db: Session):
    posts = db.query(Post).all()
    return posts


def show_posts(id: int, db: Session, request: PostSchema):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Bu {id}ga mos post topilmadi! ")
    return post


def delete_post(id: int, db: Session):
    post = db.query(Post).filter(Post.id == id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Post topilmadi")
    post.delete()
    db.commit()
    return "Post o'chirildi"


def update_post(id: int, db: Session, request: PostSchema):
    post = db.query(Post).filter(Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{id}ga mos post topilmadi!!")
    post.title = request.title
    post.content = request.content
    db.commit()
    return "Yangilandi"
