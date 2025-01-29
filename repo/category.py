from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from others.database import SessionLocal

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


from others.models import Category
from others.schemas import CategorySchema


def add_category(category: CategorySchema, db: Session = Depends(get_db)):
    new_category = Category(**category.dict())
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return {"message": "Kategoriya yaratildi!", "": new_category}


def update_categories(id: int, db: Session, request: CategorySchema):
    category = db.query(Category).filter(Category.id == id).first()
    if not category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"{id}ga mos kategoriya topilmadi!!")
    category.title = request.title
    category.content = request.content
    db.commit()
    return "Yangilandi"


def delete_category(id: int, db: Session):
    post = db.query(Category).filter(Category.id == id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Category topilmadi")
    post.delete()
    db.commit()
    return "Category o'chirildi"
