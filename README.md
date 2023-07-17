# Elasticsearch Connector

ElasticSearch has two authentication 'domains' if you will. Client API will try 
to verify server certificate and also authenticate with one of: 

* username and password
* Bearer token
* Service Token
* API key

## 1. Start ES and Kibana

Start ES server with ```./start_server.sh``` and note down password and Kibana token

Start Kibana with ```./start.kib.sh```, go to Webpage and use token to enroll it. 

## 2. CA certificate File

It is mandatory to have a CA certificate file to verify the server certificate unless server is running without 
security enabled or use CertiFi. 

Retrieve CA certificate from Docker ES server with ```./get_ca_cert.sh```

## 3. Run the connector

Make sure you pass CLI arguments to the connector or use environment variables as below

```shell
ES_PASSWORD=changeme \
ES_FINGERPRINT=changeme \
```

Run the connector with ```python3 main.py```

