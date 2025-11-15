# get_payment_type_description.sql

**Path**: `04-analytics-engineering/taxi_rides_ny/macros/get_payment_type_description.sql`
**Size**: 441 bytes
**Lines**: 17

## Source Code

```sql
{#
    This macro returns the description of the payment_type 
#}

{% macro get_payment_type_description(payment_type) -%}

    case {{ dbt.safe_cast("payment_type", api.Column.translate_type("integer")) }}  
        when 1 then 'Credit card'
        when 2 then 'Cash'
        when 3 then 'No charge'
        when 4 then 'Dispute'
        when 5 then 'Unknown'
        when 6 then 'Voided trip'
        else 'EMPTY'
    end

{%- endmacro %}
```

## Analysis

File type: `.sql`

---
*Generated: 2025-11-15T20:48:44.334121*
