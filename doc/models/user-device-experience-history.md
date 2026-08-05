
# User Device Experience History

## Structure

`UserDeviceExperienceHistory`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `billingaccountid` | `str` | Optional | The billing account ID. This is the same value as the Account ID |
| `createdon` | `datetime` | Optional | Timestamp of the record |
| `date` | `datetime` | Optional | Timestamp of the record |
| `devicesbad` | `int` | Optional | This is a score based on combination of network coverage and network outage affecting the device's ability to connect to the network. This is a count of devices that have failed |
| `devicesfair` | `int` | Optional | This is a score based on combination of network coverage and network outage affecting the device's ability to connect to the network. This is a count of devices that are impaired |
| `devicesgood` | `int` | Optional | This is a score based on combination of network coverage and network outage affecting the device's ability to connect to the network. This is a count of devices that have no issues |
| `devicestotal` | `int` | Optional | A count of all devices |
| `foreignid` | `str` | Optional | UUID of the ECPD account the user belongs to |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `lastupdated` | `datetime` | Optional | Timestamp of the record |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Optional | The UUID of the resource version |

## Example

```python
import dateutil.parser

from verizon.models.user_device_experience_history import UserDeviceExperienceHistory

user_device_experience_history = UserDeviceExperienceHistory(
    billingaccountid='0000123456-00001',
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    date=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    devicesbad=2,
    devicesfair=2,
    devicesgood=8,
    devicestotal=12,
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    version='1.0',
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395'
)
```

