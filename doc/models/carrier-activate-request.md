
# Carrier Activate Request

Request for carrier activation.

## Structure

`CarrierActivateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[AccountDeviceList]`](../../doc/models/account-device-list.md) | Required | Up to 10,000 devices for which you want to activate service, specified by device identifier. |
| `service_plan` | `str` | Required | The service plan code that you want to assign to all specified devices. |
| `mdn_zip_code` | `str` | Required | The Zip code of the location where the line of service will primarily be used, or a Zip code that you have been told to use with these devices. For accounts that are configured for geographic numbering, this is the ZIP code from which the MDN will be derived. |
| `account_name` | `str` | Optional | The name of a billing account. |
| `carrier_ip_pool_name` | `str` | Optional | The private IP pool (Carrier Group Name) from which your device IP addresses will be derived. |
| `carrier_name` | `str` | Optional | The carrier that will perform the activation. |
| `cost_center_code` | `str` | Optional | A string to identify the cost center that the device is associated with. |
| `custom_fields` | [`List[CustomFields]`](../../doc/models/custom-fields.md) | Optional | A user-defined descriptive field, limited to 50 characters. |
| `group_name` | `str` | Optional | If you specify devices by ID in the devices parameters, this is the name of a device group that the devices should be added to.If you don't specify individual devices with the devices parameter, you can provide the name of a device group to activate all devices in that group. |
| `lead_id` | `str` | Optional | The ID of a “Qualified” or “Closed - Won” VPP customer lead, which is used with other values to determine MDN assignment, taxation, and compensation. |
| `primary_place_of_use` | [`PlaceOfUse`](../../doc/models/place-of-use.md) | Optional | The customer name and the address of the device's primary place of use. Leave these fields empty to use the account profile address as the primary place of use. These values will be applied to all devices in the request.If the account is enabled for non-geographic MDNs and the device supports it, the primaryPlaceOfUse address will also be used to derive the MDN for the device. |
| `public_ip_restriction` | `str` | Optional | For devices with static IP addresses on the public network, this specifies whether the devices have general access to the Internet. |
| `sku_number` | `str` | Optional | The Stock Keeping Unit (SKU) of a 4G device type can be used with ICCID device identifiers in lieu of an IMEI when activating 4G devices. The SkuNumber will be used with all devices in the request, so all devices must be of the same type. |

## Example

```python
from verizon.models.account_device_list import AccountDeviceList
from verizon.models.address import Address
from verizon.models.carrier_activate_request import CarrierActivateRequest
from verizon.models.custom_fields import CustomFields
from verizon.models.customer_name import CustomerName
from verizon.models.device_id import DeviceId
from verizon.models.place_of_use import PlaceOfUse

carrier_activate_request = CarrierActivateRequest(
    devices=[
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='990013907835573',
                    kind='imei'
                ),
                DeviceId(
                    id='89141390780800784259',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress4'
        ),
        AccountDeviceList(
            device_ids=[
                DeviceId(
                    id='990013907884259',
                    kind='imei'
                ),
                DeviceId(
                    id='89141390780800735573',
                    kind='iccid'
                )
            ],
            ipaddress='ipAddress4'
        )
    ],
    service_plan='m2m_4G',
    mdn_zip_code='98801',
    account_name='0868924207-00001',
    carrier_ip_pool_name='carrierIpPoolName4',
    carrier_name='carrierName8',
    cost_center_code='costCenterCode4',
    custom_fields=[
        CustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='4G West',
    primary_place_of_use=PlaceOfUse(
        address=Address(
            address_line_1='1600 Pennsylvania Ave NW',
            city='Washington',
            state='DC',
            zip='20500',
            country='USA'
        ),
        customer_name=CustomerName(
            first_name='Zaffod',
            last_name='Beeblebrox',
            title='President'
        )
    )
)
```

