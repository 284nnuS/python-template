from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
from .settings import settings
from collections.abc import Generator

engine = create_engine(
    str(settings.SQLALCHEMY_DATABASE_URI)
)

def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        try:
            yield session
        except Exception as e:
            session.rollback()
        finally:
            session.close()


Base = declarative_base()

