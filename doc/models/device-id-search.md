
# Device Id Search

Search by device id.

## Structure

`DeviceIdSearch`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contains` | `str` | Required | The string appears anywhere in the identifer. |
| `startswith` | `str` | Optional | The identifer must start with the specified string. |
| `endswith` | `str` | Optional | The identifier must end with the specified string. |
| `kind` | `str` | Required | The type of the device identifier. Valid types of identifiers are:ESN (decimal),EID,ICCID (up to 20 digits),IMEI (up to 16 digits),MDN,MEID (hexadecimal),MSISDN. |

## Example

```python
from verizon.models.device_id_search import DeviceIdSearch

device_id_search = DeviceIdSearch(
    contains='4259',
    kind='iccid',
    startswith='startswith6',
    endswith='endswith8'
)
```

