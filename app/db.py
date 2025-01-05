# app/db.py
from sqlalchemy import create_engine, URL
from sqlalchemy.orm import sessionmaker
from app.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME
from contextlib import contextmanager
from sqlalchemy.pool import QueuePool
from rich.console import Console
from sqlalchemy.ext.declarative import declarative_base

console = Console()

# Use the PostgreSQL connection string from the config
connection_string = URL.create(
    "postgresql+psycopg2",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME,
    port=DB_PORT,
)

# Create the engine for PostgreSQL connection
engine = create_engine(connection_string, poolclass=QueuePool, pool_pre_ping=True, pool_recycle=600, pool_size=10, max_overflow=2, echo=False)

# SessionLocal for DB sessions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@contextmanager
def get_db_raw():
    db = engine.connect()
    try:
        yield db
    finally:
        db.close()

# To create tables if not exist
def recreate_database():
    Base.metadata.create_all(engine)
    console.log("Database tables created successfully", style="green")
