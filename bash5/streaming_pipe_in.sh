#!/bin/bash

pipe_in="$1"

tr '[:lower:]' '[:upper:]' < "$pipe_in"
