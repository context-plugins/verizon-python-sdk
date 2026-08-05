
# Callback Summary

Registered callback information.

## Structure

`CallbackSummary`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Optional | Callback URL for an subscribed service. |

## Example

```python
from verizon.models.callback_summary import CallbackSummary

callback_summary = CallbackSummary(
    url='http://10.120.102.183:50559/CallbackListener/FirmwareServiceMessages.asmx'
)
```

