from json import load
from dotenv import load_dotenv
import os

load_dotenv()

AEROSPIKE_HOST = os.environ.get('AEROSPIKE_HOST')
AEROSPIKE_PORT = os.environ.get('AEROSPIKE_PORT')

config = {
    'hosts': [
        (AEROSPIKE_HOST, int(AEROSPIKE_PORT))
    ]
}

AEROSPIKE_NAMESPACE = 'test'
AEROSPIKE_SET = 'to-do'
AEROSPIKE_RECORD = 'all'
