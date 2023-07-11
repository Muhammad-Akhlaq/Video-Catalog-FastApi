#!/bin/bash

# Upgrade pip
echo "Upgrading pip..."
python -m pip install --upgrade pip

# Create and Activate Virtual env
echo "Creating virtual env..."
python -m venv venv
source venv/bin/activate

# Install pipenv using pip
echo "Installing pipenv..."
pip install pipenv

# Install dependencies using pipenv
echo "Installing dependencies..."
pipenv install

# Install pre-commit hooks
echo "Installing pre-commit hooks..."
pipenv run pre-commit install

# Migrate Database
echo "Installing pre-commit hooks..."
alembic upgrade head

# Run the FastAPI server
echo "Starting FastAPI server..."
pipenv run uvicorn main:app --reload
