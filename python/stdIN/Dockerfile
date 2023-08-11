# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY stdin.py /app

ENV DOCKER_HOST="ssh://coffee"

# Run script when the container launches
# `python stdin.py <some input>`
CMD ["python", "stdin.py", "hi hello how are you?"]
