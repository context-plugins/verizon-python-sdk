
# Dto Notification Group Request Entity

## Structure

`DtoNotificationGroupRequestEntity`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | a short description |
| `groupemail` | `str` | Optional | Contact email for the group |
| `name` | `str` | Optional | User defined name of the record |

## Example

```python
from verizon.models.dto_notification_group_request_entity import DtoNotificationGroupRequestEntity

dto_notification_group_request_entity = DtoNotificationGroupRequestEntity(
    description='a short description',
    groupemail='email@domain.com',
    name='name of the record'
)
```

