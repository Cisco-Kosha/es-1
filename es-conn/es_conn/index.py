import json
import requests
from elasticsearch import Elasticsearch

API_KEY = 'your-api-key'
INDEX_NAME = 'my_index'
DOC_TYPE = 'my_document'


def create_index(es):
    # Define the document to be uploaded
    document = {
        'title': 'Example Document',
        'content': 'This is an example document for Elasticsearch.',
    }

    # Index the document
    response = es.index(index=INDEX_NAME, doc_type=DOC_TYPE, body=document)
    if response['result'] == 'created':
        print('Document indexed successfully.')

    # Create an index
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
    response = es.indices.create(index=INDEX_NAME, body=index_body)
    if response['acknowledged']:
        print('Index created successfully.')


def search(es):
    # Search for a string
    search_query = {
        'query': {
            'match': {
                'content': 'example'
            }
        }
    }
    response = es.search(index=INDEX_NAME, body=json.dumps(search_query))
    if response['hits']['total']['value'] > 0:
        hits = response['hits']['hits']
        print(f'{len(hits)} documents found.')
        for hit in hits:
            print(hit['_source'])
    else:
        print('No documents found.')
