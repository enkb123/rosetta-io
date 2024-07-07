from bitnami/dotnet-sdk:8

WORKDIR /app

# Create a new blank project and build it, so that building in future steps is faster
RUN dotnet new console --name RosettaIO --output . && \
    dotnet build

COPY ./ /app

RUN dotnet build
