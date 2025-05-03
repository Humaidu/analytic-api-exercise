import os
from sqlmodel import  SQLModel, create_engine, Session
from dotenv import load_dotenv

# Loads from .env file
load_dotenv()  

# Database URL
DATABASE_URL = os.getenv("DATABASE_URL")

# Create a database engine
engine = create_engine(DATABASE_URL, echo=True)
# Create tables in the database (if not already existing)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency for getting the DB session
def get_session():
    with Session(engine) as session:
        yield session
