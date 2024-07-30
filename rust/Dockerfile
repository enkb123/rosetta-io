FROM rust:1.79


WORKDIR /app
RUN cargo install cargo-script
COPY Cargo.toml Cargo.lock ./
COPY ./streaming_pipe_in_and_out.rs .
RUN cargo build
COPY ./ /app
