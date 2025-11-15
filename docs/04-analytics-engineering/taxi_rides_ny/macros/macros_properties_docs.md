# macros_properties.yml

**Path**: `04-analytics-engineering/taxi_rides_ny/macros/macros_properties.yml`
**Size**: 358 bytes
**Lines**: 12

## Source Code

```yaml
version: 2

macros:
  - name: get_payment_type_description
    description: >
      This macro receives a payment_type and returns the corresponding description.
    arguments:
      - name: payment_type
        type: int
        description: > 
          payment_type value.
          Must be one of the accepted values, otherwise the macro will return null
```

## Analysis

File type: `.yml`

---
*Generated: 2025-11-15T20:48:44.335308*
