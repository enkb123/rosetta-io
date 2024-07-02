# Use an official Node Docker image as the base
FROM denoland/deno:alpine-1.44.4

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

RUN chmod -R 777 /app

CMD ["deno", "run","--allow-read=/app", "--allow-write=/app", "write_file.mjs"]
