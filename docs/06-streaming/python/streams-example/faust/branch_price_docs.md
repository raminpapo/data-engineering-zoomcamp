# branch_price.py

**Path**: `06-streaming/python/streams-example/faust/branch_price.py`
**Size**: 710 bytes
**Lines**: 22

## Source Code

```python
import faust
from taxi_rides import TaxiRide
from faust import current_event

app = faust.App('datatalksclub.stream.v3', broker='kafka://localhost:9092', consumer_auto_offset_reset="earliest")
topic = app.topic('datatalkclub.yellow_taxi_ride.json', value_type=TaxiRide)

high_amount_rides = app.topic('datatalks.yellow_taxi_rides.high_amount')
low_amount_rides = app.topic('datatalks.yellow_taxi_rides.low_amount')


@app.agent(topic)
async def process(stream):
    async for event in stream:
        if event.total_amount >= 40.0:
            await current_event().forward(high_amount_rides)
        else:
            await current_event().forward(low_amount_rides)

if __name__ == '__main__':
    app.main()

```

## Analysis

File type: `.py`

---
*Generated: 2025-11-15T20:48:44.417809*
