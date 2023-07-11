# -*- coding: utf-8 -*-
from contextvars import ContextVar

from db.database import SessionLocal

db_session: ContextVar[SessionLocal] = ContextVar("db_session", default=SessionLocal)


def context_aware_session():
    return db_session.get()


def get_db() -> SessionLocal:
    session = SessionLocal()
    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
