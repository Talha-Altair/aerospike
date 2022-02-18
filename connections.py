import aerospike
from time import sleep
import settings

client = aerospike.client(settings.config)

key = (
    settings.AEROSPIKE_NAMESPACE,
    settings.AEROSPIKE_SET,
    settings.AEROSPIKE_RECORD
)
