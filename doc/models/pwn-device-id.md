
# PWN Device Id

## Structure

`PWNDeviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Required | - |
| `kind` | `str` | Required | - |

## Example

```python
from verizon.models.pwn_device_id import PWNDeviceId

pwn_device_id = PWNDeviceId(
    id='99948099913024600001',
    kind='iccid'
)
```

