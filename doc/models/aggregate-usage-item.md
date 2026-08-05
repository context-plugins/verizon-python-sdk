
# Aggregate Usage Item

Contains usage information per device.

## Structure

`AggregateUsageItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `imei` | `str` | Optional | The International Mobile Equipment Identifier of the device. |
| `number_of_sessions` | `int` | Optional | Number of sessions established by the device reporting usage. |
| `bytes_transferred` | `int` | Optional | The amount of data transferred by the device reporting usage, measured in Bytes. |

## Example

```python
from verizon.models.aggregate_usage_item import AggregateUsageItem

aggregate_usage_item = AggregateUsageItem(
    imei='15-digit IMEI',
    number_of_sessions=1,
    bytes_transferred=2057
)
```

