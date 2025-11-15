# DataGeneratorHelper.java

**Path**: `06-streaming/java/kafka_examples/src/test/java/org/example/helper/DataGeneratorHelper.java`
**Size**: 857 bytes
**Lines**: 22

## Source Code

```java
package org.example.helper;

import org.example.data.PickupLocation;
import org.example.data.Ride;
import org.example.data.VendorInfo;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class DataGeneratorHelper {
    public static Ride generateRide() {
        var arrivalTime = LocalDateTime.now().format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        var departureTime = LocalDateTime.now().minusMinutes(30).format(DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss"));
        return new Ride(new String[]{"1", departureTime, arrivalTime,"1","1.50","1","N","238","75","2","8","0.5","0.5","0","0","0.3","9.3","0"});
    }

    public static PickupLocation generatePickUpLocation(long pickupLocationId) {
        return new PickupLocation(pickupLocationId, LocalDateTime.now());
    }
}

```

## Analysis

File type: `.java`

---
*Generated: 2025-11-15T20:48:44.479885*
