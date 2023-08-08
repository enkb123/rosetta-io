# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY null_char.py /app

# Run app.py when the container launches

# python null_char.py
CMD ["python", "null_char.py"]
