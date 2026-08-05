
# Resource Event

## Structure

`ResourceEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountclientid` | `str` | Optional | Not used in this release, future functionality |
| `callbackurl` | `str` | Optional | The URL of the callback listener |
| `createdon` | `datetime` | Required | Timestamp of the record |
| `description` | `str` | Optional | a short description |
| `deviceid` | `str` | Optional | This is a UUID value of the device created when the device is onboarded |
| `errmsg` | `str` | Optional | Error message |
| `fieldid` | `str` | Required | - |
| `fields` | [`DtoFields`](../../doc/models/dto-fields.md) | Optional | Fields to return needed by search |
| `fieldvalue` | `List[int]` | Optional | **Constraints**: *Maximum Items*: `100`, `>= 0`, `<= 100` |
| `foreignid` | `str` | Required | UUID of the ECPD account the user belongs to |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `lastupdated` | `datetime` | Required | Timestamp of the record |
| `modelid` | `str` | Optional | The model ID of the device |
| `name` | `str` | Optional | User defined name of the record |
| `sensordataaggregation` | `bool` | Optional | A flag to indicate if sensor data is to be aggregated (true) or not |
| `state` | `str` | Required | The current status of the device or transaction and will be `success` or `failed` |
| `transactionid` | `str` | Optional | The system-generated UUID of the transaction |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Required | The UUID of the resource version |

## Example

```python
import dateutil.parser

from verizon.models.dto_fields import DtoFields
from verizon.models.resource_event import ResourceEvent

resource_event = ResourceEvent(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    fieldid='The field ID',
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    state='success',
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
    accountclientid='null',
    callbackurl='The URL of the callback listener',
    description='a short description',
    deviceid='The UUID of the device',
    errmsg='provider_service_error',
    fields=DtoFields(
        additional_prop_1='string',
        additional_prop_2='string',
        additional_prop_3='string'
    ),
    modelid='The model ID of the device',
    name='name of the record',
    sensordataaggregation=True,
    transactionid='afbcc00d-eeee-ffff-gggg-38b4333fcf06',
    version='1.0'
)
```

