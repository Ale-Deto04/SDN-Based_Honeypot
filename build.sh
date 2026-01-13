#!/bin/bash

# Build docker containers
docker build -f Dockerfiles/Dockerfile.ryu -t kathara/ryu .
docker build -f Dockerfiles/Dockerfile.host -t kathara/host .
docker build -f Dockerfiles/Dockerfile.server -t kathara/server .

# Make init script executable
chmod +x Kathara/shared/scripts/init.sh
