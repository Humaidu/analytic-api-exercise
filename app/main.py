from app.database import create_db_and_tables
from fastapi import FastAPI
from app.routers import queries


# Create a FastAPI instance
app = FastAPI()

# Register a function to run when the application starts
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
    
app.include_router(queries.router)
