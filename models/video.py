# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, String

from models.base_model import BaseModel


class VideoModel(BaseModel):
    __tablename__ = "videos"

    title = Column(String(100), index=True)
    description = Column(String(500))
    duration = Column(Integer)

    def __repr__(self):
        return self.title
