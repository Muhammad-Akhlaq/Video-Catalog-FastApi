# -*- coding: utf-8 -*-
from typing import Optional

from sqlalchemy.orm import Session

from api.v1.video.schemas import (
    VideoCreateRequest,
    VideoUpdateRequest,
    VideoResponse,
    VideoPaginatedResponse,
)
from models.video import VideoModel


class VideoCRUD:
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
        """
        db_video = VideoModel(**video.model_dump())
        db.add(db_video)
        db.commit()
        db.refresh(db_video)
        return db_video

    async def get_video(self, db: Session, video_id: str) -> Optional[VideoResponse]:
        """
        Get a video by ID.

        Args:
            db (Session): The database session.
            video_id (str): The ID of the video.

        Returns:
            Optional[VideoResponse]: The retrieved video or None if not found.
        """
        return db.query(VideoModel).filter_by(id=video_id).first()

    async def update_video(
        self, db: Session, video_id: str, video: VideoUpdateRequest
    ) -> Optional[VideoResponse]:
        """
        Update a video.

        Args:
            db (Session): The database session.
            video_id (str): The ID of the video to update.
            video (VideoUpdateRequest): The updated video data.

        Returns:
            Optional[VideoResponse]: The updated video or None if not found.
        """
        db_video = db.query(VideoModel).filter_by(id=video_id).first()
        if not db_video:
            return
        for field, value in video.model_dump(exclude_unset=True).items():
            setattr(db_video, field, value)
        db.commit()
        db.refresh(db_video)
        return db_video

    async def delete_video(self, db: Session, video_id: str):
        """
        Delete a video.

        Args:
            db (Session): The database session.
            video_id (str): The ID of the video to delete.

        Returns:
            None
        """
        db_video = db.query(VideoModel).filter_by(id=video_id).first()
        if not db_video:
            return
        db.delete(db_video)
        db.commit()
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
        """
        videos = db.query(VideoModel).offset(offset).limit(limit).all()
        total_videos = db.query(VideoModel).count()
        return VideoPaginatedResponse(
            data=videos,
            offset=offset,
            limit=limit,
            total_count=total_videos,
        )
