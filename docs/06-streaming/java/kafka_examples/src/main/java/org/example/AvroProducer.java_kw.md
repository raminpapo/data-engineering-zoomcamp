# Keywords: AvroProducer.java

**File**: `06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java`

## Keyword Index

### AvroProducer

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: public class AvroProducer {

### com

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: import com.opencsv.CSVReader;

### java

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: import java.io.FileReader;

### org

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: package org.example;

### producer

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: import org.apache.kafka.clients.producer.KafkaProducer;

### reader

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: var reader = new CSVReader(new FileReader(ridesStream.getFil

### record

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: var record = kafkaProducer.send(new ProducerRecord<>("rides_

### rideRecords

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: var rideRecords = producer.getRides();

### ridesStream

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: var ridesStream = this.getClass().getResource("/rides.csv");

### schemaregistry

- **Defined in**: [06-streaming/java/kafka_examples/src/main/java/org/example/AvroProducer.java](./AvroProducer.java_docs.md)
- **Context**: import schemaregistry.RideRecord;


---
*Total keywords: 10*
