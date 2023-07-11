# -*- coding: utf-8 -*-
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from api.v1.video.controller import VideoController
from api.v1.video.schemas import (
    VideoCreateRequest,
    VideoUpdateRequest,
    VideoResponse,
    VideoPaginatedResponse,
)
from db.session import get_db

router = APIRouter(
    prefix="/video",
    tags=["video"],
    responses={404: {"description": "Not found"}},
)
video_controller = VideoController()


@router.post("/", response_model=VideoResponse)
async def create_video_endpoint(
    video: VideoCreateRequest, db: Session = Depends(get_db)
):
    """
    Create a video.

    Args:
        video (VideoCreateRequest): The video data.
        db (Session): The database session.

    Returns:
        VideoResponse: The created video.
    """
    return await video_controller.create_video(db, video)


@router.get("/{video_id}", response_model=VideoResponse)
async def get_video_endpoint(video_id: str, db: Session = Depends(get_db)):
    """
    Get a video by ID.

    Args:
        video_id (str): The ID of the video.
        db (Session): The database session.

    Returns:
        VideoResponse: The retrieved video.
    """
    return await video_controller.get_video(db, video_id)


@router.put("/{video_id}", response_model=VideoResponse)
async def update_video_endpoint(
    video_id: str, video: VideoUpdateRequest, db: Session = Depends(get_db)
):
    """
    Update a video.

    Args:
        video_id (str): The ID of the video to update.
        video (VideoUpdateRequest): The updated video data.
        db (Session): The database session.

    Returns:
        VideoResponse: The updated video.
    """
    return await video_controller.update_video(db, video_id, video)


@router.delete("/{video_id}")
async def delete_video_endpoint(video_id: str, db: Session = Depends(get_db)):
    """
    Delete a video.

    Args:
        video_id (str): The ID of the video to delete.
        db (Session): The database session.

    Returns:
        None
    """
    return await video_controller.delete_video(db, video_id)


@router.get("/", response_model=VideoPaginatedResponse)
async def get_videos_endpoint(
    limit: int = 10, offset: int = 0, db: Session = Depends(get_db)
):
    """
    Get a paginated list of videos.

    Args:
        limit (int): The number of records per page.
        offset (int): The offset for pagination.
        db (Session): The database session.

    Returns:
        VideoPaginatedResponse: The paginated list of videos.
    """
    return await video_controller.get_videos(db, limit, offset)
