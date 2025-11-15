# VendorInfo.java

**Path**: `06-streaming/java/kafka_examples/src/main/java/org/example/data/VendorInfo.java`
**Size**: 540 bytes
**Lines**: 22

## Source Code

```java
package org.example.data;

import java.time.LocalDateTime;

public class VendorInfo {

    public VendorInfo(String vendorID, long PULocationID, LocalDateTime pickupTime, LocalDateTime lastDropoffTime) {
        VendorID = vendorID;
        this.PULocationID = PULocationID;
        this.pickupTime = pickupTime;
        this.lastDropoffTime = lastDropoffTime;
    }

    public VendorInfo() {
    }

    public String VendorID;
    public long PULocationID;
    public LocalDateTime pickupTime;
    public LocalDateTime lastDropoffTime;
}

```

## Analysis

File type: `.java`

---
*Generated: 2025-11-15T20:48:44.512737*
