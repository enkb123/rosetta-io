FROM mileschou/lua:5.4

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./ /app

# Install Lua and luarocks
RUN apt-get update && \
    apt-get install -y lua5.1 luarocks
RUN luarocks install lua-cjson
RUN luarocks install base64



