# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the source code and test files into the container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir flake8 pytest

# Run linting and tests
RUN flake8 .
RUN pytest TestBoard.py
RUN pytest TestGame.py
RUN pytest TestPlayer.py
RUN pytest TestIntegration.py

# Define the command to run the application
CMD ["python", "minesweeper.py"]
