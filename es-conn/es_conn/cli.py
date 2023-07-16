import os
import argparse


def parse_cli(args=None):
    # parse CLI
    parser = argparse.ArgumentParser(
        prog='python3 main.py',
        description='Toolkit for ElasticSearch connection',
        epilog='humm....foo bar?')

    env_url = os.environ.get("ES_URL", "https://localhost:9200")
    env_pass = os.environ.get("ES_PASSWORD", "your-password-here")
    env_finger = os.environ.get("ES_FINGERPRINT", "your-cert_fingerprint")

    parser.add_argument('-u', '--es_url', type=str, help='ElasticSearch URL',
                        default=env_url)

    parser.add_argument('-p', '--es_pass', type=str, help='ElasticSearch Password',
                        default=env_pass)

    parser.add_argument('-f', '--es_finger', type=str, help='ElasticSearch Certificate Fingerprint',
                        default=env_finger)

    return parser.parse_args(args)
