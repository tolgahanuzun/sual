#!/usr/bin/env bash

# This script starts the development environment using Docker
# Launch as: source tools/dev.sh from the project's root


if [ $1 = "remove" ]; then
    DOCKER_COMPOSE_FILE="./docker-compose.yml"
    docker-compose  stop
    docker-compose  rm
fi

if [ $1 = "start" ]; then
    docker-compose up -d 
    docker-compose  stop

    docker start sual_db_1 
    docker start sual_web_1
fi

if [ $1 = "bash" ]; then
    docker exec -it sual_web_1 bash
fi

