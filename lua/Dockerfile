FROM nickblah/lua:5.4-luarocks

# Set the working directory inside the container
WORKDIR /app

# Install Lua and luarocks
RUN luarocks install dkjson
RUN luarocks install base64

# Copy the current directory contents into the container at /app
COPY ./ /app
