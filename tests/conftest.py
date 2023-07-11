# -*- coding: utf-8 -*-
import os
from unittest import mock

import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from db.database import Base, engine
from db.session import get_db
from main import app
from tests.helper import test_db_session


@pytest.fixture
def db_session():
    return next(test_db_session())


@pytest.fixture(scope="session")
def client():
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = test_db_session
    with mock.patch.dict(os.environ, {"TESTING": "Testing"}):
        yield TestClient(app)
    app.dependency_overrides.clear()


@pytest.fixture(scope="function", autouse=True)
def truncate_db(db_session):
    # Create a new session and start a transaction
    session = Session(bind=engine)
    session.begin_nested()
    # Delete database tables
    for table in reversed(Base.metadata.sorted_tables):
        session.execute(table.delete())
        session.commit()
    yield
    session.rollback()
    session.close()
