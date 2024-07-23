FROM rust:1.79

#Conditional Compilation

WORKDIR /app
COPY ./Cargo.toml .
COPY ./ /app
RUN cargo build --release
