
# Usage History

## Structure

`UsageHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bytes_used` | `int` | Optional | - |
| `serviceplan` | `str` | Optional | - |
| `sms_used` | `int` | Optional | - |
| `mo_sms` | `int` | Optional | - |
| `mt_sms` | `int` | Optional | - |
| `source` | `str` | Optional | - |
| `event_date_time` | `datetime` | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.usage_history import UsageHistory

usage_history = UsageHistory(
    bytes_used=3072,
    serviceplan='The serviceplan name',
    sms_used=142,
    mo_sms=36,
    mt_sms=44,
    source='Raw Usage',
    event_date_time=dateutil.parser.parse('2021-08-15T00:00:00Z')
)
```

