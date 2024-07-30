FROM rust:1.79


WORKDIR /app
RUN cargo install cargo-script
COPY Cargo.toml Cargo.lock ./
COPY ./_main.rs .
RUN cargo build
COPY ./ .
