
# Notification Group Name Trigger Attribute

Notification group name trigger attribute.

## Structure

`NotificationGroupNameTriggerAttribute`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `key` | `str` | Optional | If present, the NotificationGroupName will be listed here. |

## Example

```python
from verizon.models.notification_group_name_trigger_attribute import NotificationGroupNameTriggerAttribute

notification_group_name_trigger_attribute = NotificationGroupNameTriggerAttribute(
    key='NotificationGroupName'
)
```

