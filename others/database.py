from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

url_db = 'postgresql://postgres:root123@127.0.0.1:5432/blog'
engine = create_engine(url_db, echo=True)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Session = sessionmaker()

      
