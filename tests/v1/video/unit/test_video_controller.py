# -*- coding: utf-8 -*-
import pytest
from fastapi import HTTPException

from api.v1.video.controller import VideoController
from api.v1.video.crud import VideoCRUD
from api.v1.video.schemas import (
    VideoCreateRequest,
    VideoUpdateRequest,
    VideoResponse,
)


@pytest.fixture
def video_crud():
    return VideoCRUD()


class TestVideoController:
    @pytest.fixture
    def video_controller(self, video_crud):
        return VideoController(video_crud)

    @pytest.mark.asyncio
    async def test_create_video(self, video_controller, db_session):
        video_data = VideoCreateRequest(
            title="Test Video", description="A test video", duration=120
        )
        video = await video_controller.create_video(db=db_session, video=video_data)

        assert video is not None
        assert video.title == video_data.title
        assert video.description == video_data.description
        assert video.duration == video_data.duration

    @pytest.mark.asyncio
    async def test_get_video(self, video_controller, db_session):
        video_data1 = VideoCreateRequest(
            title="Video 1", description="Description 1", duration=120
        )
        video = await video_controller.create_video(db=db_session, video=video_data1)
        video_data = VideoResponse(
            id=video.id,
            title=video.title,
            description=video.description,
            duration=video.duration,
        )
        video = await video_controller.get_video(db=db_session, video_id=str(video.id))

        assert video is not None
        assert video.id == video.id
        assert video.title == video_data.title
        assert video.description == video_data.description
        assert video.duration == video_data.duration

    @pytest.mark.asyncio
    async def test_update_video(self, video_controller, db_session):
        video_data1 = VideoCreateRequest(
            title="Video 1", description="Description 1", duration=120
        )
        video = await video_controller.create_video(db=db_session, video=video_data1)
        video_data = VideoResponse(
            id=video.id,
            title=video.title,
            description=video.description,
            duration=video.duration,
        )
        updated_video_data = VideoUpdateRequest(title="Updated Video", duration=180)
        updated_video = await video_controller.update_video(
            db=db_session, video_id=str(video.id), video=updated_video_data
        )

        assert updated_video is not None
        assert updated_video.id == video.id
        assert updated_video.title == updated_video_data.title
        assert updated_video.description == video_data.description
        assert updated_video.duration == updated_video_data.duration

    @pytest.mark.asyncio
    async def test_delete_video(self, video_controller, db_session):
        video_data1 = VideoCreateRequest(
            title="Video 1", description="Description 1", duration=120
        )
        video = await video_controller.create_video(db=db_session, video=video_data1)
        await video_controller.delete_video(db=db_session, video_id=video.id)

        with pytest.raises(HTTPException) as exc_info:
            await video_controller.get_video(db=db_session, video_id=video.id)
        assert exc_info.value.status_code == 404

    @pytest.mark.asyncio
    async def test_get_videos(self, video_controller, db_session):
        video_data1 = VideoCreateRequest(
            title="Video 1", description="Description 1", duration=120
        )
        video_data2 = VideoCreateRequest(
            title="Video 2", description="Description 2", duration=180
        )
        await video_controller.create_video(db=db_session, video=video_data1)
        await video_controller.create_video(db=db_session, video=video_data2)

        videos = await video_controller.get_videos(db=db_session, limit=10, offset=0)

        assert len(videos.data) == 2
        assert videos.offset == 0
        assert videos.limit == 10
        assert videos.total_count == 2
