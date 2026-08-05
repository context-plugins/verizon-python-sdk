
# Dto Remove Users from Notification Group Request

## Structure

`DtoRemoveUsersFromNotificationGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `userids` | `List[str]` | Optional | - |

## Example

```python
from verizon.models.dto_remove_users_from_notification_group_request import DtoRemoveUsersFromNotificationGroupRequest

dto_remove_users_from_notification_group_request = DtoRemoveUsersFromNotificationGroupRequest(
    accountname='0000123456-00001',
    id='id8',
    userids=[
        'userids4',
        'userids5',
        'userids6'
    ]
)
```

