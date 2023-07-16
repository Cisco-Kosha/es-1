#!/usr/bin/env bash

rm http_ca.crt
docker cp es01:/usr/share/elasticsearch/config/certs/http_ca.crt ./es-conn/es_conn/http_ca.crt
