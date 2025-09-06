#!/bin/bash

# Script to run the TBYA portal

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Start PostgreSQL with Docker
echo "Starting PostgreSQL with Docker..."
docker-compose up -d

# Wait for PostgreSQL to start
echo "Waiting for PostgreSQL to start..."
sleep 10

# Initialize database
echo "Initializing database..."
python init_db.py

# Run Django development server
echo "Starting Django development server..."
python manage.py runserver