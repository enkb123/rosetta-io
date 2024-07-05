from bitnami/dotnet-sdk:8

WORKDIR /app

RUN dotnet new console --name RosettaIO --output .
RUN dotnet build

COPY ./ /app

RUN dotnet build

# prevent bitnami marketing message from being printed
# ENTRYPOINT ["/bin/sh", "-c"]
# CMD ["/bin/bash"]
