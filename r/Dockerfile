FROM r-base:4.3.1

RUN R -e "install.packages('jsonlite')"
RUN R -e "install.packages('base64enc')"

WORKDIR /app
COPY ./ /app
