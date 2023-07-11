# -*- coding: utf-8 -*-
from sqlalchemy.orm import Session

from db.database import engine


def test_db_session():
    # Create a new session and start a transaction
    session = Session(bind=engine)
    try:
        yield session
        session.rollback()  # Rollback the transaction after the test is done
    finally:
        session.close()
