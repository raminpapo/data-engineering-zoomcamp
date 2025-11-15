# taxi_ride_value.avsc

**Path**: `06-streaming/python/resources/schemas/taxi_ride_value.avsc`
**Size**: 425 bytes
**Lines**: 27

## Source Code

```
{
  "namespace": "com.datatalksclub.taxi",
  "type": "record",
  "name": "RideRecord",
  "fields": [
    {
      "name": "vendor_id",
      "type": "int"
    },
    {
      "name": "passenger_count",
      "type": "int"
    },
    {
      "name": "trip_distance",
      "type": "float"
    },
    {
      "name": "payment_type",
      "type": "int"
    },
    {
      "name": "total_amount",
      "type": "float"
    }
  ]
}
```

## Analysis

File type: `.avsc`

---
*Generated: 2025-11-15T20:48:44.384952*
