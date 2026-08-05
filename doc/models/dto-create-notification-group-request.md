
# Dto Create Notification Group Request

## Structure

`DtoCreateNotificationGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `group` | [`DtoNotificationGroupRequestEntity`](../../doc/models/dto-notification-group-request-entity.md) | Required | - |
| `userids` | `List[str]` | Optional | - |

## Example

```python
from verizon.models.dto_create_notification_group_request import DtoCreateNotificationGroupRequest
from verizon.models.dto_notification_group_request_entity import DtoNotificationGroupRequestEntity

dto_create_notification_group_request = DtoCreateNotificationGroupRequest(
    group=DtoNotificationGroupRequestEntity(
        description='a short description',
        groupemail='email@domain.com',
        name='name of the record'
    ),
    accountname='0000123456-00001',
    userids=[
        'userids6'
    ]
)
```

