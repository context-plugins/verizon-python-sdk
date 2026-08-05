
# User Smart Alert

## Structure

`UserSmartAlert`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountclientid` | `str` | Optional | Not used in this release, future functionality |
| `billingaccountid` | `str` | Optional | The billing account ID. This is the same value as the Account ID |
| `category` | `str` | Optional | The type of alert and will be either `telemetry` or `infrastructure` |
| `condition` | `int` | Optional | The condition or threshold for an alert |
| `createdon` | `datetime` | Required | Timestamp of the record |
| `description` | `str` | Optional | a short description |
| `deviceid` | `str` | Optional | This is a UUID value of the device created when the device is onboarded |
| `foreignid` | `str` | Optional | UUID of the ECPD account the user belongs to |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `isacknowledged` | `bool` | Optional | A flag that indicates if the alarm has been acknowledged |
| `iscleared` | `bool` | Optional | A flag that indicates if the alarm has been cleared |
| `isdisabled` | `bool` | Optional | A flag that indicates if the alarm has been disabled |
| `lastupdated` | `datetime` | Required | Timestamp of the record |
| `name` | `str` | Optional | User defined name of the record |
| `ruleid` | `str` | Optional | The UUID of a rule for alerts |
| `severity` | `str` | Optional | The threshold value to trigger an alert and will be Critical, Major or Minor |
| `state` | `str` | Optional | The current status of the device or transaction and will be `success` or `failed` |
| `template` | `str` | Optional | template of the rule which triggered a given alert |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Required | The UUID of the resource version |

## Example

```python
import dateutil.parser

from verizon.models.user_smart_alert import UserSmartAlert

user_smart_alert = UserSmartAlert(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
    accountclientid='null',
    billingaccountid='0000123456-00001',
    category='telemetry',
    condition=2592000,
    description='a short description',
    deviceid='The UUID of the device',
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    isacknowledged=True,
    iscleared=True,
    isdisabled=False,
    name='name of the record',
    ruleid='The UUID of a rule',
    severity='minor',
    state='success',
    template='The template ID',
    version='1.0'
)
```

