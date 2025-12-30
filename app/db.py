from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

DB_URL = "sqlite:///./mealgen.db"

engine = create_engine(
    DB_URL,
    connect_args={"check_same_thread": False},  # needed for SQLite + threads
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

class Base(DeclarativeBase):
    pass
