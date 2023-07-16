#!/usr/bin/env bash

docker rm -f es01
docker network create elastic
docker pull docker.elastic.co/elasticsearch/elasticsearch:8.8.2
docker run --name es01 --net elastic -p 9200:9200 -it docker.elastic.co/elasticsearch/elasticsearch:8.8.2


