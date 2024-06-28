from typing import Optional
import datetime
from pydantic import BaseModel, EmailStr, Field


class UserSchema(BaseModel):
    name: str = Field(default=None)
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        user_schema = {
            "user_example": {
                "name": "abduvali",
                "email": "murodullayevabduvali972@gmail.com",
                "password": "12"

            }
        }


class CommentSchema(BaseModel):
    content: str
    user_id: int
    post_id: int


class PostSchema(BaseModel):
    title: str
    content: str
    author_id: int
    category_id: int

    class Config:
        orm_mode = True


class UserLoginSchema(BaseModel):
    email: EmailStr = Field(default=None)
    password: str = Field(default=None)

    class Config:
        user_schema = {
            "user_example": {
                "email": "murodullayevabduvali972@gmail.com",
                "password": "12"

            }
        }


class CategorySchema(BaseModel):
    id: int = Field(default=None)
    name: str = Field(default=None)

    class Config:
        user_schema = {
            "category_example": {
                "name": "name"

            }
        }

