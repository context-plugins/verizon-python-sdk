
# Contact Info Update Request

Request to update contact information.

## Structure

`ContactInfoUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `primary_place_of_use` | [`PlaceOfUse`](../../doc/models/place-of-use.md) | Required | The customer name and the address of the device's primary place of use. Leave these fields empty to use the account profile address as the primary place of use. These values will be applied to all devices in the request.If the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also be used to derive the MDN for the device. |
| `account_name` | `str` | Optional | The name of the billing account that the devices belong to. An account name is usually numeric, and must include any leading zeros. |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Optional | A list of the devices that you want to change, specified by device identifier. You only need to provide one identifier per device. Do not include accountName, groupName, customFields, or servicePlan if you use this parameter. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.address import Address
from verizon.models.contact_info_update_request import ContactInfoUpdateRequest
from verizon.models.customer_name import CustomerName
from verizon.models.device_id import DeviceId
from verizon.models.place_of_use import PlaceOfUse

contact_info_update_request = ContactInfoUpdateRequest(
    primary_place_of_use=PlaceOfUse(
        address=Address(
            address_line_1='9868 Scranton Rd',
            city='San Diego',
            state='CA',
            zip='92121',
            country='USA',
            address_line_2='Suite A',
            zip_4='0001',
            phone='1234567890',
            phone_type='H',
            email_address='zaffod@theinternet.com'
        ),
        customer_name=CustomerName(
            first_name='Zaffod',
            last_name='Beeblebrox',
            title='President',
            middle_name='P',
            suffix='I'
        )
    ),
    account_name='0212345678-00001',
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='19110173057',
                    kind='ESN'
                ),
                DeviceId(
                    id='19110173057',
                    kind='ESN'
                )
            ],
            ipaddress='ipAddress4'
        )
    ]
)
```

