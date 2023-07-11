# -*- coding: utf-8 -*-
import uuid

import pytest

from api.v1.video.schemas import (
    VideoBase,
    VideoCreateRequest,
    VideoUpdateRequest,
    VideoResponse,
    VideoPaginatedResponse,
)


class TestVideoBase:
    def test_video_base_valid(self):
        data = {"title": "Test Video", "description": "A test video", "duration": 120}
        video = VideoBase(**data)
        assert video.title == data["title"]
        assert video.description == data["description"]
        assert video.duration == data["duration"]

    def test_video_base_invalid(self):
        data = {
            "title": "Test Video" * 20,
            "description": "A test video",
            "duration": 120,
        }
        with pytest.raises(ValueError):
            VideoBase(**data)


class TestVideoCreateRequest:
    def test_video_create_request_valid(self):
        data = {"title": "Test Video", "description": "A test video", "duration": 120}
        video = VideoCreateRequest(**data)
        assert video.title == data["title"]
        assert video.description == data["description"]
        assert video.duration == data["duration"]

    def test_video_create_request_invalid(self):
        data = {
            "title": "Test Video" * 20,
            "description": "A test video",
            "duration": 120,
        }
        with pytest.raises(ValueError):
            VideoCreateRequest(**data)


class TestVideoUpdateRequest:
    def test_video_update_request_valid(self):
        data = {"title": "Test Video", "description": "A test video", "duration": 120}
        video = VideoUpdateRequest(**data)
        assert video.title == data["title"]
        assert video.description == data["description"]
        assert video.duration == data["duration"]

    def test_video_update_request_invalid(self):
        data = {
            "title": "Test Video" * 100,
            "description": "A test video",
            "duration": 120,
        }
        with pytest.raises(ValueError):
            VideoUpdateRequest(**data)


class TestVideoResponse:
    def test_video_response_valid(self):
        data = {
            "title": "Test Video",
            "description": "A test video",
            "duration": 120,
            "id": uuid.uuid4(),
        }
        video = VideoResponse(**data)
        assert video.title == data["title"]
        assert video.description == data["description"]
        assert video.duration == data["duration"]
        assert video.id == data["id"]

    def test_video_response_invalid(self):
        data = {
            "title": "Test Video" * 20,
            "description": "A test video",
            "duration": 120,
            "id": uuid.uuid4(),
        }
        with pytest.raises(ValueError):
            VideoResponse(**data)


class TestVideoPaginatedResponse:
    def test_video_paginated_response_valid(self):
        data = {
            "data": [
                {
                    "title": "Video 1",
                    "description": "Description 1",
                    "duration": 120,
                    "id": uuid.uuid4(),
                },
                {
                    "title": "Video 2",
                    "description": "Description 2",
                    "duration": 180,
                    "id": uuid.uuid4(),
                },
            ],
            "offset": 0,
            "limit": 10,
            "total_count": 2,
        }
        paginated_response = VideoPaginatedResponse(**data)
        assert paginated_response.data[0].model_dump() == data["data"][0]
        assert paginated_response.limit == data["limit"]
        assert paginated_response.offset == data["offset"]
        assert paginated_response.total_count == data["total_count"]

    def test_video_paginated_response_invalid(self):
        data = {
            "data": [
                {
                    "title": "Video 1",
                    "description": "Description 1",
                    "duration": 120,
                    "id": uuid.uuid4(),
                },
                {
                    "title": "Video 2",
                    "description": "Description 2",
                    "duration": 180,
                    "id": uuid.uuid4(),
                },
            ],
            "offset": 0,
            "limit": 10,
            "total_count": 2,
        }
        data["data"].append(
            {
                "title": "Video 3" * 20,
                "description": "Description 3",
                "duration": 240,
                "id": uuid.uuid4(),
            }
        )
        with pytest.raises(ValueError):
            VideoPaginatedResponse(**data)
