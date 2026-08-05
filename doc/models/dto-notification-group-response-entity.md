
# Dto Notification Group Response Entity

## Structure

`DtoNotificationGroupResponseEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `createdon` | `datetime` | Optional | Timestamp of the record |
| `description` | `str` | Optional | a short description |
| `foreignid` | `str` | Optional | UUID of the ECPD account the user belongs to |
| `groupemail` | `str` | Optional | Contact email for the group |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `lastupdated` | `datetime` | Optional | Timestamp of the record |
| `name` | `str` | Optional | User defined name of the record |
| `users` | [`List[DtoUserDTO]`](../../doc/models/dto-user-dto.md) | Optional | **Constraints**: *Maximum Items*: `100` |
| `version` | `str` | Optional | The resource version |
| `versionid` | `str` | Optional | The UUID of the resource version |

## Example

```python
import dateutil.parser

from verizon.models.dto_notification_group_response_entity import DtoNotificationGroupResponseEntity

dto_notification_group_response_entity = DtoNotificationGroupResponseEntity(
    createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    description='a short description',
    foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
    groupemail='email@domain.com',
    id='id4',
    lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
    name='name of the record',
    version='1.0',
    versionid='337bd2e8-eeee-ffff-gggg-5207992fd395'
)
```

