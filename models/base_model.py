# -*- coding: utf-8 -*-
import uuid
from datetime import datetime

from sqlalchemy import Column, String, DateTime, Boolean

from db.database import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    created_date = Column(DateTime, default=datetime.now)
    updated_date = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    is_active = Column(Boolean, nullable=False, default=True)
