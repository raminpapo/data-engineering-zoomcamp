# Keywords: producer.py

**File**: `06-streaming/python/avro_example/producer.py`

## Keyword Index

### AvroSerializer

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from confluent_kafka.schema_registry.avro import AvroSerializer

### Dict

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from typing import Dict

### Producer

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from confluent_kafka import Producer

### RIDE_KEY_SCHEMA_PATH

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from settings import RIDE_KEY_SCHEMA_PATH, RIDE_VALUE_SCHEMA_PATH, \

### RideAvroProducer

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: class RideAvroProducer:

### RideRecord

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from ride_record import RideRecord, ride_record_to_dict

### RideRecordKey

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from ride_record_key import RideRecordKey, ride_record_key_to_dict

### SchemaRegistryClient

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from confluent_kafka.schema_registry import SchemaRegistryClient

### SerializationContext

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from confluent_kafka.serialization import SerializationContext, MessageField

### __init__

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: def __init__(self, props: Dict):

### confluent_kafka

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from confluent_kafka import Producer

### csv

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: import csv

### delivery_report

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: def delivery_report(err, msg):

### load_schema

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: key_schema_str = self.load_schema(props['schema.key'])

### publish

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: def publish(self, topic: str, records: [RideRecordKey, RideRe

### read_records

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: def read_records(resource_path: str):

### ride_record

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from ride_record import RideRecord, ride_record_to_dict

### ride_record_key

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from ride_record_key import RideRecordKey, ride_record_key_to_dict

### settings

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from settings import RIDE_KEY_SCHEMA_PATH, RIDE_VALUE_SCHEMA_PA

### sleep

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from time import sleep

### time

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from time import sleep

### typing

- **Defined in**: [06-streaming/python/avro_example/producer.py](./producer.py_docs.md)
- **Context**: from typing import Dict


---
*Total keywords: 22*
