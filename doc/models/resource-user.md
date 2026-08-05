
# Resource User

## Structure

`ResourceUser`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountclientid` | `str` | Optional | Not used in this release, future functionality |
| `ackterms` | `bool` | Optional | Indicates if terms are agreed to (true) or not |
| `acktermson` | `datetime` | Optional | - |
| `billingaccountid` | `str` | Optional | The billing account ID. This is the same value as the Account ID |
| `createdon` | `datetime` | Required | Timestamp of the record |
| `credentialsid` | `str` | Optional | User credentials. The only valid value is an email address |
| `credentialstype` | `str` | Required | The type of credential represented by the ID. The only valid value is `email` |
| `customdata` | `Dict[str, Any]` | Optional | Name/value pair, where the value is client defined.  The purpose is to keep track of current state per device action. |
| `description` | `str` | Optional | a short description |
| `displayname` | `str` | Optional | the user name value to display |
| `email` | `str` | Optional | Contact email for the group |
| `firstname` | `str` | Optional | The first name in the user record |
| `foreignid` | `str` | Required | UUID of the ECPD account the user belongs to |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `lastname` | `str` | Optional | The last name in the user record |
| `lastupdated` | `datetime` | Required | Timestamp of the record |
| `mdn` | `str` | Optional | The Mobile Directory Number |
| `middlename` | `str` | Optional | optional field for middle name or initial |
| `name` | `str` | Optional | User defined name of the record |
| `secondarybillingaccountids` | `List[str]` | Optional | Virtual field; will not be used in this implementation<br><br>**Constraints**: *Maximum Items*: `100` |
| `state` | `str` | Optional | The current status of the device or transaction and will be `success` or `failed` |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Required | The UUID of the resource version |

## Example

```python
import dateutil.parser

from verizon.models.resource_user import ResourceUser

resource_user = ResourceUser(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    credentialstype='email',
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
    accountclientid='null',
    ackterms=True,
    acktermson=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    billingaccountid='0000123456-00001',
    credentialsid='email@domain.com',
    description='a short description',
    displayname='User name',
    email='email@domain.com',
    firstname='First name',
    lastname='Last name or Surname',
    mdn='908-555-1234',
    middlename='Middle name or initial',
    name='name of the record',
    state='success',
    version='1.0'
)
```

