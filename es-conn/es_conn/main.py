from elasticsearch import Elasticsearch
from elasticsearch.exceptions import HTTP_EXCEPTIONS

from cli import *


def get_api_key_client(c):
    # API Key client. Use base client to create API Key
    api_key = c.security.create_api_key(body={"name": "my-api-key", "expiration": "1d", "role_descriptors": {}})
    print(api_key)

    api_key_client = Elasticsearch(
        args.es_url,
        ca_certs="./http_ca.crt",
        api_key=(api_key.body["id"], api_key.body["api_key"])
    )

    print(api_key_client.info())
    return api_key_client


def get_bearer_token_client(c):
    try:
        # It will not work with basic license
        test_bearer_token = c.security.get_token(body={"grant_type": "client_credentials"})

        # Adds the HTTP header 'Authorization: Bearer token-value'
        bearer_token_client = Elasticsearch(
            args.es_url,
            ca_certs="./http_ca.crt",
            bearer_auth=test_bearer_token["access_token"]
        )
        return bearer_token_client
    except HTTP_EXCEPTIONS as e:
        print(e)
    return None


def get_basic_client():
    return Elasticsearch(
        args.es_url,
        ca_certs="./http_ca.crt",
        basic_auth=("elastic", args.es_pass)
    )


def get_basic_client_with_fingerprint():
    return Elasticsearch(
        args.es_url,
        ssl_assert_fingerprint=args.es_finger,
        basic_auth=("elastic", args.es_pass)
    )


args = parse_cli()
if not args:
    exit(1)

# Create the client instance
client = get_basic_client()
client_fingerprint = get_basic_client_with_fingerprint()

print(get_api_key_client(client))
print(get_bearer_token_client(client))
