#!/usr/bin/env bash

# This script starts the development environment using Docker
# Launch as: source tools/dev.sh from the project's root

DOCKER_COMPOSE_FILE="./docker-compose.yml"
docker-compose  stop
docker-compose  rm

docker-compose  stop
docker-compose up -d



