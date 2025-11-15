# PickupLocation.java

**Path**: `06-streaming/java/kafka_examples/src/main/java/org/example/data/PickupLocation.java`
**Size**: 396 bytes
**Lines**: 17

## Source Code

```java
package org.example.data;

import java.time.LocalDateTime;

public class PickupLocation {
    public PickupLocation(long PULocationID, LocalDateTime tpep_pickup_datetime) {
        this.PULocationID = PULocationID;
        this.tpep_pickup_datetime = tpep_pickup_datetime;
    }

    public PickupLocation() {
    }

    public long PULocationID;
    public LocalDateTime tpep_pickup_datetime;
}

```

## Analysis

File type: `.java`

---
*Generated: 2025-11-15T20:48:44.514784*
