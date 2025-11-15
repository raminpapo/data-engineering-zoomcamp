# stream.py

**Path**: `06-streaming/python/streams-example/faust/stream.py`
**Size**: 353 bytes
**Lines**: 17

## Source Code

```python
import faust
from taxi_rides import TaxiRide


app = faust.App('datatalksclub.stream.v2', broker='kafka://localhost:9092')
topic = app.topic('datatalkclub.yellow_taxi_ride.json', value_type=TaxiRide)


@app.agent(topic)
async def start_reading(records):
    async for record in records:
        print(record)


if __name__ == '__main__':
    app.main()

```

## Analysis

File type: `.py`

---
*Generated: 2025-11-15T20:48:44.413457*
