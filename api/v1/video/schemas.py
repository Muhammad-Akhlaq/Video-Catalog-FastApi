# -*- coding: utf-8 -*-
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, Field


class VideoBase(BaseModel):
    title: str = Field(..., max_length=100)
    description: str = Field(..., max_length=500)
    duration: int

    class Config:
        from_attributes = True


class VideoCreateRequest(VideoBase):
    pass


class VideoUpdateRequest(VideoBase):
    title: Optional[str] = Field(None, max_length=100)
    description: Optional[str] = Field(None, max_length=500)
    duration: Optional[int]


class VideoResponse(VideoBase):
    id: UUID


class VideoPaginatedResponse(BaseModel):
    data: List[VideoResponse]
    offset: int
    limit: int
    total_count: int
