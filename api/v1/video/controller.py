# -*- coding: utf-8 -*-
from fastapi import HTTPException
from sqlalchemy.orm import Session

from api.v1.video.crud import VideoCRUD
from api.v1.video.schemas import (
    VideoCreateRequest,
    VideoUpdateRequest,
    VideoResponse,
    VideoPaginatedResponse,
)


class VideoController:
    def __init__(self, video_crud=VideoCRUD()):
        """
        VideoController constructor.

        Args:
            video_crud (VideoCRUD): The video CRUD operations instance.
        """
        self.video_crud = video_crud

    async def create_video(
        self, db: Session, video: VideoCreateRequest
    ) -> VideoResponse:
        """
        Create a video.

        Args:
            db (Session): The database session.
            video (VideoCreateRequest): The video data.

        Returns:
            VideoResponse: The created video.

        Raises:
            HTTPException: If the video is not found.
        """
        db_video = await self.video_crud.create_video(db=db, video=video)
        if not db_video:
            raise HTTPException(status_code=404, detail="Video not found")
        return db_video

    async def get_video(self, db: Session, video_id: str) -> VideoResponse:
        """
        Get a video by ID.

        Args:
            db (Session): The database session.
            video_id (str): The ID of the video.

        Returns:
            VideoResponse: The retrieved video.

        Raises:
            HTTPException: If the video is not found.
        """
        db_video = await self.video_crud.get_video(db=db, video_id=video_id)
        if not db_video:
            raise HTTPException(status_code=404, detail="Video not found")
        return db_video

    async def update_video(
        self, db: Session, video_id: str, video: VideoUpdateRequest
    ) -> VideoResponse:
        """
        Update a video.

        Args:
            db (Session): The database session.
            video_id (str): The ID of the video to update.
            video (VideoUpdateRequest): The updated video data.

        Returns:
            VideoResponse: The updated video.

        Raises:
            HTTPException: If the video is not found.
        """
        db_video = await self.video_crud.update_video(
            db=db, video_id=video_id, video=video
        )
        if not db_video:
            raise HTTPException(status_code=404, detail="Video not found")
        return db_video

    async def delete_video(self, db: Session, video_id: str):
        """
        Delete a video.

        Args:
            db (Session): The database session.
            video_id (str): The ID of the video to delete.

        Returns:
            None

        Raises:
            HTTPException: If the video is not found.
        """
        db_video = await self.video_crud.delete_video(db=db, video_id=video_id)
        if not db_video:
            raise HTTPException(status_code=404, detail="Video not found")
        return db_video

    async def get_videos(
        self, db: Session, limit: int = 10, offset: int = 0
    ) -> VideoPaginatedResponse:
        """
        Get a paginated list of videos.

        Args:
            db (Session): The database session.
            limit (int): The number of records per page.
            offset (int): The offset for pagination.

        Returns:
            VideoPaginatedResponse: The paginated list of videos.

        Raises:
            HTTPException: If the video is not found.
        """
        db_video = await self.video_crud.get_videos(db=db, limit=limit, offset=offset)
        if not db_video:
            raise HTTPException(status_code=404, detail="Video not found")
        return db_video
