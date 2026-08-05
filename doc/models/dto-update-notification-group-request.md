
# Dto Update Notification Group Request

## Structure

`DtoUpdateNotificationGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `group` | [`DtoNotificationGroupRequestEntity`](../../doc/models/dto-notification-group-request-entity.md) | Required | - |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `userids` | `List[str]` | Optional | - |

## Example

```python
from verizon.models.dto_notification_group_request_entity import DtoNotificationGroupRequestEntity
from verizon.models.dto_update_notification_group_request import DtoUpdateNotificationGroupRequest

dto_update_notification_group_request = DtoUpdateNotificationGroupRequest(
    group=DtoNotificationGroupRequestEntity(
        description='a short description',
        groupemail='email@domain.com',
        name='name of the record'
    ),
    accountname='0000123456-00001',
    id='id0',
    userids=[
        'userids8',
        'userids7',
        'userids6'
    ]
)
```

