from sqlmodel import  SQLModel, create_engine, Session

# Database URL
DATABASE_URL = "mysql+mysqlconnector://testuser:testpass@localhost:3306/testdb"

# Create a database engine
engine = create_engine(DATABASE_URL, echo=True)
# Create tables in the database (if not already existing)
def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

# Dependency for getting the DB session
def get_session():
    with Session(engine) as session:
        yield session
