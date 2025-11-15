# settings.py

**Path**: `06-streaming/python/avro_example/settings.py`
**Size**: 289 bytes
**Lines**: 9

## Source Code

```python
INPUT_DATA_PATH = '../resources/rides.csv'

RIDE_KEY_SCHEMA_PATH = '../resources/schemas/taxi_ride_key.avsc'
RIDE_VALUE_SCHEMA_PATH = '../resources/schemas/taxi_ride_value.avsc'

SCHEMA_REGISTRY_URL = 'http://localhost:8081'
BOOTSTRAP_SERVERS = 'localhost:9092'
KAFKA_TOPIC = 'rides_avro'

```

## Analysis

File type: `.py`

---
*Generated: 2025-11-15T20:48:44.424520*
