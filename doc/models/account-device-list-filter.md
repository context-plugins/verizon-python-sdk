
# Account Device List Filter

Filter for a list of devices.

## Structure

`AccountDeviceListFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_identifier_filters` | [`List[DeviceIdSearch]`](../../doc/models/device-id-search.md) | Required | Specify the kind of the device identifier, the type of match, and the string that you want to match. |

## Example

```python
from verizon.models.account_device_list_filter import AccountDeviceListFilter
from verizon.models.device_id_search import DeviceIdSearch

account_device_list_filter = AccountDeviceListFilter(
    device_identifier_filters=[
        DeviceIdSearch(
            contains='4259',
            kind='iccid',
            startswith='startswith8',
            endswith='endswith0'
        )
    ]
)
```

