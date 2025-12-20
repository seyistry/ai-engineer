from sqlmodel import Field, Session, SQLModel, create_engine
from . import models

DATABASE_URL = "postgresql://postgres:dracula11%40@localhost/fastapi"

engine = create_engine(DATABASE_URL)

SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session