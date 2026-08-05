
# Dto Add Users to Notification Group Request

## Structure

`DtoAddUsersToNotificationGroupRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `id` | `str` | Optional | UUID of the user record, assigned at creation |
| `userids` | `List[str]` | Optional | - |

## Example

```python
from verizon.models.dto_add_users_to_notification_group_request import DtoAddUsersToNotificationGroupRequest

dto_add_users_to_notification_group_request = DtoAddUsersToNotificationGroupRequest(
    accountname='0000123456-00001',
    id='id2',
    userids=[
        'userids0',
        'userids1',
        'userids2'
    ]
)
```

