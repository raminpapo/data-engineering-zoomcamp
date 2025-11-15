# taxi_rides.py

**Path**: `06-streaming/python/streams-example/faust/taxi_rides.py`
**Size**: 176 bytes
**Lines**: 10

## Source Code

```python
import faust


class TaxiRide(faust.Record, validation=True):
    vendorId: str
    passenger_count: int
    trip_distance: float
    payment_type: int
    total_amount: float

```

## Analysis

**Classes (1)**: TaxiRide

---
*Generated: 2025-11-15T20:48:44.416226*
