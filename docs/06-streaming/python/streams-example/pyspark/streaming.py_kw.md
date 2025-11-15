# Keywords: streaming.py

**File**: `06-streaming/python/streams-example/pyspark/streaming.py`

## Keyword Index

### RIDE_SCHEMA

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: from settings import RIDE_SCHEMA, CONSUME_TOPIC_RIDES_CSV, TOPIC_WINDOWED_VENDOR_I

### SparkSession

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: from pyspark.sql import SparkSession

### op_groupby

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def op_groupby(df, column_names):

### op_windowed_groupby

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def op_windowed_groupby(df, window_duration, slide_duration):

### parse_ride_from_kafka_message

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def parse_ride_from_kafka_message(df, schema):

### prepare_df_to_kafka_sink

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def prepare_df_to_kafka_sink(df, value_columns, key_column=None):

### pyspark

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: from pyspark.sql import SparkSession

### read_from_kafka

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def read_from_kafka(consume_topic: str):

### settings

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: from settings import RIDE_SCHEMA, CONSUME_TOPIC_RIDES_CSV, TOPI

### sink_console

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def sink_console(df, output_mode: str = 'complete', processing_tim

### sink_kafka

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def sink_kafka(df, topic):

### sink_memory

- **Defined in**: [06-streaming/python/streams-example/pyspark/streaming.py](./streaming.py_docs.md)
- **Context**: def sink_memory(df, query_name, query_template):


---
*Total keywords: 12*
