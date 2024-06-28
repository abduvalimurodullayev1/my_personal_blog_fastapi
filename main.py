
from fastapi import FastAPI

from passlib.context import CryptContext

from others.database import SessionLocal, Base, engine
from router import comments, auth, category, post

github_client_id = 'Ov23liytqPPjfiRWNxv1'
github_secret_id = '94892adaf1fafa80e7cdfe21ec7c837cacca1d64'
app = FastAPI()

Base.metadata.create_all(bind=engine)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


app.include_router(post.router)
app.include_router(auth.router)
app.include_router(comments.router)
app.include_router(category.router)