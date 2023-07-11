# -*- coding: utf-8 -*-
from fastapi import status


class TestVideoEndpoints:
    def test_create_video_endpoint(self, client):
        video_data = {
            "title": "Test Video",
            "description": "A test video",
            "duration": 120,
        }
        response = client.post("/api/v1/video/", json=video_data)
        assert response.status_code == status.HTTP_200_OK
        video = response.json()
        assert video is not None
        assert video["title"] == video_data["title"]
        assert video["description"] == video_data["description"]
        assert video["duration"] == video_data["duration"]

    def test_create_video_endpoint_incomplete_payload(self, client):
        video_data = {"title": "Test Video", "description": "A test video"}
        response = client.post("/api/v1/video/", json=video_data)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_get_video_endpoint(self, client):
        # Create a video for testing
        video_data = {
            "title": "Test Video",
            "description": "A test video",
            "duration": 120,
        }
        response = client.post("/api/v1/video/", json=video_data)
        assert response.status_code == status.HTTP_200_OK
        video = response.json()

        # Retrieve the video
        response = client.get(f"/api/v1/video/{video['id']}")
        assert response.status_code == status.HTTP_200_OK
        retrieved_video = response.json()
        assert retrieved_video is not None
        assert retrieved_video["title"] == video_data["title"]
        assert retrieved_video["description"] == video_data["description"]
        assert retrieved_video["duration"] == video_data["duration"]

    def test_get_video_endpoint_not_found(self, client):
        # Video ID that does not exist
        video_id = 99999
        response = client.get(f"/api/v1/video/{video_id}")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_update_video_endpoint(self, client):
        # Create a video for testing
        video_data = {
            "title": "Test Video",
            "description": "A test video",
            "duration": 120,
        }
        response = client.post("/api/v1/video/", json=video_data)
        assert response.status_code == status.HTTP_200_OK
        video = response.json()

        # Update the video
        updated_video_data = {"title": "Updated Video", "duration": 180}
        response = client.put(f"/api/v1/video/{video['id']}", json=updated_video_data)
        assert response.status_code == status.HTTP_200_OK
        updated_video = response.json()
        assert updated_video is not None
        assert updated_video["title"] == updated_video_data["title"]
        assert updated_video["description"] == video_data["description"]
        assert updated_video["duration"] == updated_video_data["duration"]

    def test_update_video_endpoint_not_found(self, client):
        # Video ID that does not exist
        video_id = 99999
        updated_video_data = {"title": "Updated Video", "duration": 180}
        response = client.put(f"/api/v1/video/{video_id}", json=updated_video_data)
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_delete_video_endpoint(self, client):
        # Create a video for testing
        video_data = {
            "title": "Test Video",
            "description": "A test video",
            "duration": 120,
        }
        response = client.post("/api/v1/video/", json=video_data)
        assert response.status_code == status.HTTP_200_OK
        video = response.json()

        # Delete the video
        response = client.delete(f"/api/v1/video/{video['id']}")
        assert response.status_code == status.HTTP_200_OK

        # Verify that the video has been deleted
        response = client.get(f"/api/v1/video/{video['id']}")
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_get_videos_endpoint(self, client):
        # Create multiple videos for testing
        video_data1 = {
            "title": "Video 1",
            "description": "Description 1",
            "duration": 120,
        }
        video_data2 = {
            "title": "Video 2",
            "description": "Description 2",
            "duration": 180,
        }
        client.post("/api/v1/video/", json=video_data1)
        client.post("/api/v1/video/", json=video_data2)

        # Retrieve the videos
        response = client.get("/api/v1/video/")
        assert response.status_code == status.HTTP_200_OK
        videos = response.json()
        assert len(videos["data"]) == 2
