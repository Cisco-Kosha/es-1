# Elasticsearch Connector

ElasticSearch has two authentication domains if you will. Client API will try 
to verify server certificate and also authenticate with one of: 

* username and password
* Bearer token
* API key

## Start ES and Kibana

Start ES server with ```./start_server.sh```

Start Kibana with ```./start.kib.sh```

## CA certificate File

Retrieve CA certificate from Docker ES server with ```./get_ca_cert.sh```

