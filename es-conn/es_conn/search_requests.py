import json
import requests
import os

# Elasticsearch configuration
ELASTICSEARCH_HOST = 'https://localhost:9200'
INDEX_NAME = 'my_index_2'
CA_CERT_FILE = 'http_ca.crt'  # Path to your CA certificate file
API_KEY_FILE = 'api_key.txt'  # Path to your API key file

try:
    # Read the API key from the file
    with open(API_KEY_FILE, 'r') as api_key_file:
        API_KEY = api_key_file.read().strip()

    # Rest of the code remains the same...

except FileNotFoundError:
    print(f"API key file '{API_KEY_FILE}' not found.")
except Exception as e:
    print(f"An error occurred while reading the API key: {e}")

# Try with environment variable
API_KEY = os.environ.get("API_KEY", API_KEY)

if not API_KEY:
    print("No API key found. Please set the API_KEY environment variable.")
    exit(1)

# Elasticsearch request headers
headers = {
    'Authorization': f'ApiKey elastic:{API_KEY}',
    'Content-Type': 'application/json',
}

# Document to be uploaded
document = {
    'title': 'Example Document',
    'content': 'This is an example document for Elasticsearch.',
}

# Upload the document
url = f'{ELASTICSEARCH_HOST}/{INDEX_NAME}/_doc/'
response = requests.post(url, headers=headers, data=json.dumps(document), verify=CA_CERT_FILE)

if response.status_code == 201:
    print('Document uploaded successfully.')
else:
    print(f'Failed to upload document with status code: {response.status_code}.')
    print(response.text)

# Search for a string
search_query = {
    'query': {
        'match': {
            'content': 'example'
        }
    }
}
url = f'{ELASTICSEARCH_HOST}/{INDEX_NAME}/_search'
response = requests.get(url, headers=headers, params=json.dumps(search_query), verify=CA_CERT_FILE)

if response.status_code == 200:
    search_results = response.json()
    total_hits = search_results['hits']['total']['value']
    print(f'{total_hits} documents found.')
    for hit in search_results['hits']['hits']:
        print(hit['_source'])
else:
    print(f'Failed to search for the string with status code: {response.status_code}.')
    print(response.text)
