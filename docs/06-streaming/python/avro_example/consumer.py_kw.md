# Keywords: consumer.py

**File**: `06-streaming/python/avro_example/consumer.py`

## Keyword Index

### AvroDeserializer

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from confluent_kafka.schema_registry.avro import AvroDeserializer

### BOOTSTRAP_SERVERS

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from settings import BOOTSTRAP_SERVERS, SCHEMA_REGISTRY_URL, \

### Consumer

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from confluent_kafka import Consumer

### Dict

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from typing import Dict, List

### RideAvroConsumer

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: class RideAvroConsumer:

### SchemaRegistryClient

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from confluent_kafka.schema_registry import SchemaRegistryClient

### SerializationContext

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from confluent_kafka.serialization import SerializationContext, MessageField

### __init__

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: def __init__(self, props: Dict):

### confluent_kafka

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from confluent_kafka import Consumer

### consume_from_kafka

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: def consume_from_kafka(self, topics: List[str]):

### dict_to_ride_record

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from ride_record import dict_to_ride_record

### dict_to_ride_record_key

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from ride_record_key import dict_to_ride_record_key

### load_schema

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: key_schema_str = self.load_schema(props['schema.key'])

### ride_record

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from ride_record import dict_to_ride_record

### ride_record_key

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from ride_record_key import dict_to_ride_record_key

### settings

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from settings import BOOTSTRAP_SERVERS, SCHEMA_REGISTRY_URL, \

### typing

- **Defined in**: [06-streaming/python/avro_example/consumer.py](./consumer.py_docs.md)
- **Context**: from typing import Dict, List


---
*Total keywords: 17*
