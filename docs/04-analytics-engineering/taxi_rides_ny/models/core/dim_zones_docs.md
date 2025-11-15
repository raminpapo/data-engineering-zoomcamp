# dim_zones.sql

**Path**: `04-analytics-engineering/taxi_rides_ny/models/core/dim_zones.sql`
**Size**: 178 bytes
**Lines**: 8

## Source Code

```sql
{{ config(materialized='table') }}

select 
    locationid, 
    borough, 
    zone, 
    replace(service_zone,'Boro','Green') as service_zone 
from {{ ref('taxi_zone_lookup') }}
```

## Analysis

File type: `.sql`

---
*Generated: 2025-11-15T20:48:44.350452*
