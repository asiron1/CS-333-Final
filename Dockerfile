# Use the official Python image as the base
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the source code and test files into the container
COPY . /app

# Define the command to run the application
CMD ["python", "minesweeper.py"]
