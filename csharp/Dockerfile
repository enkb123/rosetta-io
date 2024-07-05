from bitnami/dotnet-sdk:8

WORKDIR /app

RUN dotnet tool install -g dotnet-script
ENV PATH="$PATH:/app/.dotnet/tools"

COPY ./ /app

# prevent bitnami marketing message from being printed
# ENTRYPOINT ["/bin/sh", "-c"]
# CMD ["/bin/bash"]
