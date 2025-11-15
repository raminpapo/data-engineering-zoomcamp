# ride_record_key.py

**Path**: `06-streaming/python/avro_example/ride_record_key.py`
**Size**: 525 bytes
**Lines**: 25

## Source Code

```python
from typing import Dict


class RideRecordKey:
    def __init__(self, vendor_id):
        self.vendor_id = vendor_id

    @classmethod
    def from_dict(cls, d: Dict):
        return cls(vendor_id=d['vendor_id'])

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.__dict__}'


def dict_to_ride_record_key(obj, ctx):
    if obj is None:
        return None

    return RideRecordKey.from_dict(obj)


def ride_record_key_to_dict(ride_record_key: RideRecordKey, ctx):
    return ride_record_key.__dict__

```

## Analysis

**Classes (1)**: RideRecordKey

**Functions (2)**: dict_to_ride_record_key, ride_record_key_to_dict

---
*Generated: 2025-11-15T20:48:44.420591*
