# client.properties

**Path**: `cohorts/2023/week_6_stream_processing/client.properties`
**Size**: 364 bytes
**Lines**: 9

## Source Code

```
# Required connection configs for Kafka producer, consumer, and admin
bootstrap.servers=<CONFLUENT CLOUD KAFKA BROKER>:9092
security.protocol=SASL_SSL
sasl.mechanisms=PLAIN
sasl.username=<CONFLUENT CLOUD API USER NAME>
sasl.password=<CONFLUENT CLOUD API PASSWORD>

# Best practice for higher availability in librdkafka clients prior to 1.7
session.timeout.ms=45000
```

## Analysis

File type: `.properties`

---
*Generated: 2025-11-15T20:48:44.184102*
