# Documentation: producer.py

## File Metadata

- **Path**: `06-streaming/python/avro_example/producer.py`
- **Size**: 4,039 bytes
- **Lines**: 94
- **Extension**: `.py`
- **Last Modified**: 2025-11-15T19:46:38.177125

## Original Source

```python
import os
import csv
from time import sleep
from typing import Dict

from confluent_kafka import Producer
from confluent_kafka.schema_registry import SchemaRegistryClient
from confluent_kafka.schema_registry.avro import AvroSerializer
from confluent_kafka.serialization import SerializationContext, MessageField

from ride_record_key import RideRecordKey, ride_record_key_to_dict
from ride_record import RideRecord, ride_record_to_dict
from settings import RIDE_KEY_SCHEMA_PATH, RIDE_VALUE_SCHEMA_PATH, \
    SCHEMA_REGISTRY_URL, BOOTSTRAP_SERVERS, INPUT_DATA_PATH, KAFKA_TOPIC


def delivery_report(err, msg):
    if err is not None:
        print("Delivery failed for record {}: {}".format(msg.key(), err))
        return
    print('Record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


class RideAvroProducer:
    def __init__(self, props: Dict):
        # Schema Registry and Serializer-Deserializer Configurations
        key_schema_str = self.load_schema(props['schema.key'])
        value_schema_str = self.load_schema(props['schema.value'])
        schema_registry_props = {'url': props['schema_registry.url']}
        schema_registry_client = SchemaRegistryClient(schema_registry_props)
        self.key_serializer = AvroSerializer(schema_registry_client, key_schema_str, ride_record_key_to_dict)
        self.value_serializer = AvroSerializer(schema_registry_client, value_schema_str, ride_record_to_dict)

        # Producer Configuration
        producer_props = {'bootstrap.servers': props['bootstrap.servers']}
        self.producer = Producer(producer_props)

    @staticmethod
    def load_schema(schema_path: str):
        path = os.path.realpath(os.path.dirname(__file__))
        with open(f"{path}/{schema_path}") as f:
            schema_str = f.read()
        return schema_str

    @staticmethod
    def delivery_report(err, msg):
        if err is not None:
            print("Delivery failed for record {}: {}".format(msg.key(), err))
            return
        print('Record {} successfully produced to {} [{}] at offset {}'.format(
            msg.key(), msg.topic(), msg.partition(), msg.offset()))

    @staticmethod
    def read_records(resource_path: str):
        ride_records, ride_keys = [], []
        with open(resource_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # skip the header
            for row in reader:
                ride_records.append(RideRecord(arr=[row[0], row[3], row[4], row[9], row[16]]))
                ride_keys.append(RideRecordKey(vendor_id=int(row[0])))
        return zip(ride_keys, ride_records)

    def publish(self, topic: str, records: [RideRecordKey, RideRecord]):
        for key_value in records:
            key, value = key_value
            try:
                self.producer.produce(topic=topic,
                                      key=self.key_serializer(key, SerializationContext(topic=topic,
                                                                                        field=MessageField.KEY)),
                                      value=self.value_serializer(value, SerializationContext(topic=topic,
                                                                                              field=MessageField.VALUE)),
                                      on_delivery=delivery_report)
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Exception while producing record - {value}: {e}")

        self.producer.flush()
        sleep(1)


if __name__ == "__main__":
    config = {
        'bootstrap.servers': BOOTSTRAP_SERVERS,
        'schema_registry.url': SCHEMA_REGISTRY_URL,
        'schema.key': RIDE_KEY_SCHEMA_PATH,
        'schema.value': RIDE_VALUE_SCHEMA_PATH
    }
    producer = RideAvroProducer(props=config)
    ride_records = producer.read_records(resource_path=INPUT_DATA_PATH)
    producer.publish(topic=KAFKA_TOPIC, records=ride_records)

```

## High-Level Overview

Python module containing 6 functions and 1 classes.

## Detailed Analysis

### Functions
- **`delivery_report(err, msg)`**
- **`__init__(self, props: Dict)`**
- **`load_schema(schema_path: str)`**
- **`delivery_report(err, msg)`**
- **`read_records(resource_path: str)`**
- **`publish(self, topic: str, records: [RideRecordKey, RideRecord])`**

### Classes
- **`RideAvroProducer`**

### Dependencies
- `os`
- `csv`
- `sleep`
- `Dict`
- `Producer`
- `SchemaRegistryClient`
- `AvroSerializer`
- `SerializationContext, MessageField`
- `RideRecordKey, ride_record_key_to_dict`
- `RideRecord, ride_record_to_dict`
- `RIDE_KEY_SCHEMA_PATH, RIDE_VALUE_SCHEMA_PATH, \`


## Usage & Examples

*No explicit usage examples found in file.*


## Dependencies & Related Files

### Imported Modules

- `confluent_kafka`
- `time`
- `SchemaRegistryClient`
- `typing`
- `confluent_kafka.serialization`
- `Dict`
- `Producer`
- `ride_record_key`
- `os`
- `RIDE_KEY_SCHEMA_PATH`
- `confluent_kafka.schema_registry.avro`
- `sleep`
- `confluent_kafka.schema_registry`
- `SerializationContext`
- `RideRecordKey`
- `csv`
- `RideRecord`
- `AvroSerializer`
- `settings`
- `ride_record`


## Performance & Security Notes

*No specific performance or security issues detected.*


## Testing & Validation

*No test framework detected. Manual testing may be required.*


---
*Generated by Repo Book Generator v1.0.0*
