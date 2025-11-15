# stream_count_vendor_trips.py

**Path**: `06-streaming/python/streams-example/faust/stream_count_vendor_trips.py`
**Size**: 446 bytes
**Lines**: 18

## Source Code

```python
import faust
from taxi_rides import TaxiRide


app = faust.App('datatalksclub.stream.v2', broker='kafka://localhost:9092')
topic = app.topic('datatalkclub.yellow_taxi_ride.json', value_type=TaxiRide)

vendor_rides = app.Table('vendor_rides', default=int)


@app.agent(topic)
async def process(stream):
    async for event in stream.group_by(TaxiRide.vendorId):
        vendor_rides[event.vendorId] += 1

if __name__ == '__main__':
    app.main()

```

## Analysis

File type: `.py`

---
*Generated: 2025-11-15T20:48:44.412202*
