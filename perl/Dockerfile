FROM perl:5.38

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

RUN cpanm JSON

