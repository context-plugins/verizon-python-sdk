
# GIO Profile Request

## Structure

`GIOProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[GIODeviceList]`](../../doc/models/gio-device-list.md) | Required | **Constraints**: *Maximum Items*: `100` |
| `account_name` | `str` | Required | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[0-9\-]{3,32}$` |
| `smrs_oid` | `str` | Optional | The Subscription Manager Secure Router Object ID, used for remote SIM provisioning. SMSR securely routes the download and management of eSIM profiles. |
| `mdn_zip_code` | `str` | Optional | **Constraints**: *Minimum Length*: `5`, *Maximum Length*: `5`, *Pattern*: `^[0-9]{5,5}$` |
| `service_plan` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9 ]{3,32}$` |

## Example

```python
from verizon.models.gio_device_id import GIODeviceId
from verizon.models.gio_device_list import GIODeviceList
from verizon.models.gio_profile_request import GIOProfileRequest

gio_profile_request = GIOProfileRequest(
    devices=[
        GIODeviceList(
            device_ids=[
                GIODeviceId(
                    kind='kind8',
                    id='id0'
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    smrs_oid='1.3.6.1.4.1.#####.1.500.200.101.5',
    mdn_zip_code='12345',
    service_plan='service plan name'
)
```

