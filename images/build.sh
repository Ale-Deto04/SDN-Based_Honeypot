#!/bin/bash

docker build -f Dockerfile.ryu -t kathara/ryu .
docker build -f Dockerfile.host -t kathara/host .
docker build -f Dockerfile.server -t kathara/server .
