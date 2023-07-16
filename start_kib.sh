#!/usr/bin/env bash

docker rm -f kib-01
docker pull docker.elastic.co/kibana/kibana:8.8.2
docker run --name kib-01 --net elastic -p 5601:5601 docker.elastic.co/kibana/kibana:8.8.2
