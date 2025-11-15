# rides_compatible.avsc

**Path**: `06-streaming/java/kafka_examples/src/main/avro/rides_compatible.avsc`
**Size**: 354 bytes
**Lines**: 11

## Source Code

```
{
   "type": "record",
       "name":"RideRecordCompatible",
       "namespace": "schemaregistry",
       "fields":[
         {"name":"vendorId","type":"string"},
         {"name":"passenger_count","type":"int"},
         {"name":"trip_distance","type":"double"},
         {"name":"pu_location_id", "type": [ "null", "long" ], "default": null}
       ]
}
```

## Analysis

File type: `.avsc`

---
*Generated: 2025-11-15T20:48:44.484044*
