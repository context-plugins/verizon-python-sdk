
# Profile Request

## Structure

`ProfileRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | - |
| `devices` | [`List[DeviceList]`](../../doc/models/device-list.md) | Required | **Constraints**: *Maximum Items*: `100` |
| `carrier_name` | `str` | Optional | - |
| `service_plan` | `str` | Optional | - |
| `mdn_zip_code` | `str` | Optional | - |
| `primary_place_of_use` | List[[customernamequery](../../doc/models/customernamequery.md) \| [addressquery](../../doc/models/addressquery.md)] \| None | Optional | This is List of a container for any-of cases.<br><br>**Constraints**: *Maximum Items*: `25` |
| `smsr_oid` | `str` | Optional | **Constraints**: *Minimum Length*: `3`, *Maximum Length*: `46`, *Pattern*: `^[0-9.]{3,46}$` |
| `carrier_ip_pool_name` | `str` | Optional | The name of the pool of IP addresses assigned to the profile. |

## Example

```python
from verizon.models.customer_name import CustomerName
from verizon.models.customernamequery import Customernamequery
from verizon.models.device_id import DeviceId
from verizon.models.device_list import DeviceList
from verizon.models.profile_request import ProfileRequest

profile_request = ProfileRequest(
    account_name='0000123456-00001',
    devices=[
        DeviceList(
            device_ids=[
                DeviceId(
                    id='id0',
                    kind='kind8'
                )
            ]
        )
    ],
    carrier_name='the name of the mobile service provider',
    service_plan='The service plan name',
    mdn_zip_code='five digit zip code',
    primary_place_of_use=[
        Customernamequery(
            customer_name=[
                CustomerName(
                    first_name='firstName4',
                    last_name='lastName4',
                    title='title4',
                    middle_name='middleName8',
                    suffix='suffix0'
                ),
                CustomerName(
                    first_name='firstName4',
                    last_name='lastName4',
                    title='title4',
                    middle_name='middleName8',
                    suffix='suffix0'
                )
            ]
        ),
        Customernamequery(
            customer_name=[
                CustomerName(
                    first_name='firstName4',
                    last_name='lastName4',
                    title='title4',
                    middle_name='middleName8',
                    suffix='suffix0'
                ),
                CustomerName(
                    first_name='firstName4',
                    last_name='lastName4',
                    title='title4',
                    middle_name='middleName8',
                    suffix='suffix0'
                )
            ]
        )
    ],
    smsr_oid='smsrOid4'
)
```

