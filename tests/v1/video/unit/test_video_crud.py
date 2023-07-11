# -*- coding: utf-8 -*-
import pytest
from sqlalchemy.orm import Session

from api.v1.video.crud import VideoCRUD
from api.v1.video.schemas import VideoCreateRequest, VideoUpdateRequest


@pytest.fixture
def video_crud():
    return VideoCRUD()


class TestVideoCRUD:
    @pytest.mark.asyncio
    async def test_create_video(self, video_crud: VideoCRUD, db_session: Session):
        video_data = VideoCreateRequest(
            title="Test Video", description="A test video", duration=120
        )
        video = await video_crud.create_video(db=db_session, video=video_data)
        assert video is not None
        assert video.title == video_data.title
        assert video.description == video_data.description
        assert video.duration == video_data.duration

    @pytest.mark.asyncio
    async def test_get_video(self, video_crud: VideoCRUD, db_session: Session):
        video_data = VideoCreateRequest(
            title="Test Video", description="A test video", duration=120
        )
        video = await video_crud.create_video(db=db_session, video=video_data)
        retrieved_video = await video_crud.get_video(
            db=db_session, video_id=str(video.id)
        )
        assert retrieved_video is not None
        assert retrieved_video.title == video_data.title
        assert retrieved_video.description == video_data.description
        assert retrieved_video.duration == video_data.duration

    @pytest.mark.asyncio
    async def test_update_video(self, video_crud: VideoCRUD, db_session: Session):
        video_data = VideoCreateRequest(
            title="Test Video", description="A test video", duration=120
        )
        video = await video_crud.create_video(db=db_session, video=video_data)
        updated_video_data = VideoUpdateRequest(title="Updated Video", duration=180)
        updated_video = await video_crud.update_video(
            db=db_session, video_id=str(video.id), video=updated_video_data
        )
        assert updated_video is not None
        assert updated_video.title == updated_video_data.title
        assert updated_video.description == video_data.description
        assert updated_video.duration == updated_video_data.duration

    @pytest.mark.asyncio
    async def test_delete_video(self, video_crud: VideoCRUD, db_session: Session):
        video_data = VideoCreateRequest(
            title="Test Video", description="A test video", duration=120
        )
        video = await video_crud.create_video(db=db_session, video=video_data)
        await video_crud.delete_video(db=db_session, video_id=str(video.id))
        deleted_video = await video_crud.get_video(
            db=db_session, video_id=str(video.id)
        )
        assert deleted_video is None

    @pytest.mark.asyncio
    async def test_get_videos(self, video_crud: VideoCRUD, db_session: Session):
        video_data1 = VideoCreateRequest(
            title="Video 1", description="Description 1", duration=120
        )
        video_data2 = VideoCreateRequest(
            title="Video 2", description="Description 2", duration=180
        )
        await video_crud.create_video(db=db_session, video=video_data1)
        await video_crud.create_video(db=db_session, video=video_data2)
        videos = await video_crud.get_videos(db=db_session, limit=10, offset=0)
        assert len(videos.data) == 2
