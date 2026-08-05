
# Resource Rule

## Structure

`ResourceRule`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountclientid` | `str` | Optional | Not used in this release, future functionality |
| `billingaccountid` | `str` | Optional | The billing account ID. This is the same value as the Account ID |
| `createdon` | `datetime` | Required | Timestamp of the record |
| `description` | `str` | Optional | a short description |
| `deviceid` | `str` | Optional | This is a UUID value of the device created when the device is onboarded |
| `disabled` | `bool` | Optional | - |
| `foreignid` | `str` | Required | UUID of the ECPD account the user belongs to |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `lastupdated` | `datetime` | Required | Timestamp of the record |
| `name` | `str` | Optional | User defined name of the record |
| `rulechain` | `Any` | Required | - |
| `rulesyntax` | `str` | Optional | The syntax of the rule and supports camel and json style syntaxes |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Required | The UUID of the resource version |

## Example

```python
import dateutil.parser
import jsonpickle

from verizon.models.resource_rule import ResourceRule

resource_rule = ResourceRule(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    rulechain=jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
    accountclientid='null',
    billingaccountid='0000123456-00001',
    description='a short description',
    deviceid='The UUID of the device',
    disabled=False,
    name='name of the record',
    rulesyntax='The rule syntax',
    version='1.0'
)
```

