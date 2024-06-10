FROM eclipse-temurin:22

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# downloaded from https://search.maven.org/remotecontent?filepath=org/json/json/20240303/json-20240303.jar
ENV CLASSPATH=org.json.simple-0.4.jar
