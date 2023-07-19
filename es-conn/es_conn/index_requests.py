import json
import requests
import os

# Elasticsearch configuration
ELASTICSEARCH_HOST = 'https://localhost:9200'
INDEX_NAME = 'my_index_2'
CA_CERT_FILE = 'http_ca.crt'  # Path to your CA certificate file

# API-Key for authentication
API_KEY = os.environ.get("API_KEY")

# Define the index settings and mappings
index_body = {
    'settings': {
        'number_of_shards': 1,
        'number_of_replicas': 0,
    },
    'mappings': {
        'properties': {
            'title': {'type': 'text'},
            'content': {'type': 'text'},
        }
    }
}

# Elasticsearch request headers
headers = {
    'Authorization': f'ApiKey {API_KEY}',
    'Content-Type': 'application/json',
}

# Create the Elasticsearch index
url = f'{ELASTICSEARCH_HOST}/{INDEX_NAME}'
response = requests.put(url, headers=headers, data=json.dumps(index_body), verify=CA_CERT_FILE)


if response.status_code == 200:
    print('Index created successfully.')
elif response.status_code == 400:
    print('Index creation failed. The index may already exist.')
else:
    print(f'Index creation failed with status code: {response.status_code}.')
    print(response.text)
