# Use the official Python base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Install pipenv
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir pipenv

# Copy Pipfile and Pipfile.lock to the container
COPY Pipfile Pipfile.lock /app/

# Install project dependencies
RUN pipenv install --system --deploy

# Copy the project files to the container
COPY . /app

# Expose the port that the FastAPI application listens on
EXPOSE 8000

# Set the entrypoint command to run the application
CMD ["pipenv", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
