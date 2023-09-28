from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from humanes.infraestructure.entity_mapping import mapper_registry, start_mappers

DATABASE_URL = "sqlite:///./humanes_socies.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
start_mappers()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
mapper_registry.metadata.create_all(engine)


def create_database():
    Base.metadata.create_all(bind=engine)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
