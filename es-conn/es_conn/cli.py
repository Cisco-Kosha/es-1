import os
import argparse


def parse_cli(args=None):
    # parse CLI
    parser = argparse.ArgumentParser(
        prog='python3 main.py',
        description='Toolkit for ElasticSearch connection',
        epilog='humm....foo bar?')

    es_url = os.environ.get("ES_URL", "https://localhost:9200")
    es_pass = os.environ.get("ES_PASSWORD", "your-password-here")

    parser.add_argument('-u', '--url', type=str, help='ElasticSeach URL',
                        default=es_url)

    parser.add_argument('-p', '--pass', type=str, help='ElasticSeach Password',
                        default=es_pass)

    return parser.parse_args(args)
