# Use an official Python runtime as the base image
FROM python:3.11-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY arguments.py /app

ENV DOCKER_HOST="ssh://coffee"

# Run script when the container launches
#  This is the 'shell' form of CMD and is executed in `/bin/sh -c`
# See docker docs for more info on how to format CMD:
# https://docs.docker.com/engine/reference/builder/#cmd:~:text=CMD-,%F0%9F%94%97,-The%20CMD%20instruction
CMD python arguments.py "Argument Number 1"
