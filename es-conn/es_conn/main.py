from elasticsearch import Elasticsearch
from cli import *

args = parse_cli()
if not args:
    exit(1)

# Create the client instance
client = Elasticsearch(
    args.es_url,
    ca_certs="/path/to/http_ca.crt",
    basic_auth=("elastic", args.es_pass)
)

# Successful response!
client.info()
