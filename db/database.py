# -*- coding: utf-8 -*-
import sys

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

from core.config import config


def create_engine_based_on_env():
    # For now, we are using SQLite for tests
    if "pytest" in sys.modules:
        return create_engine(config.SQLALCHEMY_DATABASE_URL)

    return create_engine(
        config.SQLALCHEMY_DATABASE_URL,
        pool_size=10,
        max_overflow=60,
        pool_recycle=1,
    )


engine = create_engine_based_on_env()

SessionLocal = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = declarative_base()


def create_tables():
    """
    Create tables in the database.
    """
    # Just for development purposes.
    # So just to make this clear - this is not an "unused import".
    # Models must be imported before we call create_all method.

    Base.metadata.create_all(bind=engine)
