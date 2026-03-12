from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_models import Base

db_url = "postgresql://postgres:malar@localhost:5432/dep"

engine = create_engine(db_url, pool_pre_ping=True)

SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()