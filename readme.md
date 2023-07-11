# Video Catalog FastAPI

This is a simple Video Catalog API built using FastAPI and PostgreSQL. It provides endpoints to perform CRUD operations on video resources. The API handles error handling, input validation, and pagination for retrieving videos.

## Table of Contents

- [Introduction](#introduction)
- [Technologies](#technologies)
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Testing](#testing)
- [Pre-Commits](#pre-commits)
- [API Documentation](#api-documentation)

## Introduction

This project is a Video Catalog API that allows you to manage video resources. It supports creating, retrieving, updating, and deleting videos. The API is built using FastAPI and uses PostgreSQL as the database for storing video records.

## Technologies

- FASTAPI: A modern, fast (high-performance) web framework for building APIs with Python.
- Postgresql: An open-source relational database management system.
- Alembic: Alembic is a database migration tool for SQLAlchemy.
- Docker Compose: Docker Compose is a tool that allows you to define and manage multi-container Docker applications.
- Pytest: A testing framework for Python.
- Swagger: Swagger is an open-source software framework that helps developers design, build, document, and consume RESTful APIs.

## Features

- Video Resource: The API provides a video resource that allows CRUD (Create, Read, Update, Delete) operations on video records. Each video record includes attributes such as title, description, and duration.
- Create Video: Users can create a new video by providing the required information, including title, description, and duration. Upon creation, the API assigns a unique identifier to the video.
- Retrieve Video: Users can retrieve a video by its unique identifier. The API returns the details of the video, including its title, description, and duration.
- Update Video: Users can update the information of an existing video by specifying its unique identifier and providing the updated data. The API allows modifying the title, description, and duration of the video.
- Delete Video: Users can delete a video by its unique identifier. Once deleted, the video record is permanently removed from the database.
- Pagination: The API supports pagination for retrieving videos. Users can specify the number of videos to retrieve (limit) and the offset from the beginning of the video list.
- Error Handling: The API includes robust error handling mechanisms. It validates the input data and returns appropriate error messages in case of invalid requests or missing required fields.

## Requirements

- Python 3.9: The project is developed using Python programming language. Make sure you have Python 3.9 or a compatible version installed on your system. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)
- Postgresql: PostgreSQL: The project uses PostgreSQL as the relational database management system. Make sure you have PostgreSQL installed and running on your system. You can download PostgreSQL from the official website: [PostgreSQL Downloads](https://www.postgresql.org/download/)
- Docker-compose: The project utilizes Docker Compose for containerization and managing the application's services. Docker Compose allows for easy deployment and configuration of multiple containers. You can install Docker Compose by following the official documentation: [Docker Compose Installation](https://docs.docker.com/compose/install/)

## Setup

### Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Muhammad-Akhlaq/Video-Catalog-FastApi.git
    ```
2. Navigate to the project directory:
   ```bash
   cd Video-Catalog-FastApi
   ```
### Note : You can skip below local setup by using this cmd
```bash
sh run_local.sh
```
3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the project dependencies:
    ```bash
   pip install pipenv
   pipenv install
    ```
5. Set Environment Variables:
   1. Copy the .env.sample file to .env:
   ```bash
   cp .env.sample .env
   ```
   2. Open the .env file and update the value of SQLALCHEMY_DATABASE_URL to the appropriate PostgreSQL database URL for your setup:
   ```plaintext
   POSTGRES_USER=<username>
   POSTGRES_PASSWORD=<password>
   POSTGRES_DB=<db_name>
   POSTGRES_HOST=<host>
   POSTGRES_PORT=<port>
   ```
6. Run database migrations:
    ```bash
   alembic upgrade head
    ```
7. Starting the API Server:
    ```bash
   uvicorn main:app --reload
    ```
The API will be accessible at [http://localhost:8000](http://localhost:8000).

## Docker Compose Setup

Before proceeding with the Docker Compose setup, ensure that you have Docker and Docker Compose installed on your system.

1. Clone the repository:
   ```bash
   git clone https://github.com/Muhammad-Akhlaq/Video-Catalog-FastApi.git
    ```
2. Navigate to the project directory:
   ```bash
   cd Video-Catalog-FastApi
   ```
3. Build the Docker containers:
    ```bash
   docker-compose build
    ```
4. Start the Docker containers:
    ```bash
   docker-compose up -d
    ```
The API will be accessible at [http://localhost:8000](http://localhost:8000).
To access the Swagger documentation and test the endpoints, visit [http://localhost:8000/docs](http://localhost:8000/docs) and [http://localhost:8000/redoc](http://localhost:8000/redoc) in your web browser. The Swagger UI provides an interactive interface to explore the API, view the available endpoints, and test their functionalities.

## Running Tests

To run the unit tests for the API endpoints, execute the following command:

1. To run all tests:

```shell
pytest -vv -s
```

2. To run particular file tests

```shell
pytest tests/v1/video/integration/test_video_endpoints.py -vv -s
```

3. To run particular test

```shell
pytest tests/v1/video/integration/test_video_endpoints.py::TestVideoEndpoints::test_update_video_endpoint -vv -s
```

### Note: current tests coverage is 95%.

## Pre-Commits

The project utilizes pre-commit hooks to enforce code quality and maintain consistency in the codebase. This section provides instructions on how to install and use pre-commit in the project.

## Available Pre-commit Hooks

The pre-commit configuration in this project includes the following pre-commit hooks:

- trailing-whitespace: Checks for trailing whitespace at the end of lines.
- end-of-file-fixer: Ensures that files end with a newline character.
- check-json: Validates JSON files for syntax errors.
- check-yaml: Validates YAML files for syntax errors.
- detect-private-key: Scans for private keys accidentally committed to the repository.
- debug-statements: Detects and removes debug statements from code.
- check-added-large-files: Prevents the addition of large files to the repository.
- fix-encoding-pragma: Ensures that source files contain the correct encoding pragma.
- check-case-conflict: Checks for case conflicts in filenames on case-insensitive file systems.
- black: Enforces Python code formatting using the Black formatter.
- autoflake: Removes unused imports and variables from Python code.
- skjold: Performs static analysis of Python code.
- flake8: Performs code linting and static analysis.

### Installation

1. Install as git hook:
   ```bash
   pre-commit install
   ```
### Usage

1. Auto Use: when ever you try to commit then above hooks will run on changed code.
2. Manual Run:
   ```bash
   pre-commit run --all-files
   ```

## API Documentation

The Video Catalog API provides a comprehensive set of endpoints for managing videos. You can explore and interact with the API using any HTTP client, such as curl, Postman, or the Swagger UI.

To access the Swagger documentation and test the endpoints, visit [http://localhost:8000/docs](http://localhost:8000/docs) and [http://localhost:8000/redoc](http://localhost:8000/redoc) in your web browser. The Swagger UI provides an interactive interface to explore the API, view the available endpoints, and test their functionalities.

Make sure the API server is running before accessing the Swagger UI.

## API Endpoints

The Video Catalog API provides the following endpoints:

1. Create a Video

- URL: POST 'api/v1/video/'
- Description: Creates a new video resource.
- Request Body:
```json
{
  "title": "Video Title",
  "description": "Video Description",
  "duration": 120
}
```
- Response:
```json
{
  "id": "62c609b0-c5dd-4c10-8774-dd8efc701381",
  "title": "Video Title",
  "description": "Video Description",
  "duration": 120
}
```

2. Get a Video by ID

- URL: GET 'api/v1/video/{video_id}'
- Description: Retrieves a video resource by its ID.
- Parameters:
  - 'video_id': ID of the video resource.
- Response:
```json
{
  "id": "62c609b0-c5dd-4c10-8774-dd8efc701381"
  "title": "Video Title",
  "description": "Video Description",
  "duration": 120
}
```

3. Update a Video

- URL: PUT 'api/v1/video/{video_id}'
- Description: Updates an existing video resource.
- Parameters:
  - 'video_id': ID of the video resource.
- Request Body:
```json
{
  "title": "Updated Video Title",
  "description": "Updated Video Description",
  "duration": 180
}
```
- Response
```json
{
  "id": "62c609b0-c5dd-4c10-8774-dd8efc701381",
  "title": "Updated Video Title",
  "description": "Updated Video Description",
  "duration": 180
}
```

4. Delete a Video
- URL: DELETE 'api/v1/video/{video_id}'
- Description: Deletes a video resource.
- Parameters:
  - 'video_id': ID of the video resource.
- Response: Show Deleted Record
```json
{
  "description": "Video Title Description",
  "title": "Video Title",
  "id": "62c609b0-c5dd-4c10-8774-dd8efc701381",
  "created_date": "2023-07-11T17:54:09.910158",
  "is_active": true,
  "duration": 0,
  "updated_date": "2023-07-11T17:54:09.910164"
}
```

5. Get Videos with Pagination
- URL: GET 'api/v1/video/'
- Description: Retrieves a list of videos with pagination support.
- Query Parameters:
  - 'limit' (optional): Maximum number of videos to retrieve. Defaults to 10.
  - 'offset' (optional): Number of videos to skip. Defaults to 0.
- Response:
```json
{
  "data": [
    {
      "id": "62c609b0-c5dd-4c10-8774-dd8efc701381",
      "title": "Video Title 1",
      "description": "Video Description 1",
      "duration": 120
    },
    {
      "id": "52c609b0-c5dd-4c10-8774-dd8efc701789",
      "title": "Video Title 2",
      "description": "Video Description 2",
      "duration": 180
    }
  ],
  "offset": 0,
  "limit": 10,
  "total_count": 1
}
```

## I hope this meets your requirements! Thank You
