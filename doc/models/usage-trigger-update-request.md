
# Usage Trigger Update Request

## Structure

`UsageTriggerUpdateRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `trigger_name` | `str` | Optional | Usage trigger name |
| `account_name` | `str` | Required | Account name |
| `threshold_value` | `str` | Optional | The percent of subscribed usage required to activate the trigger, such as 90 or 100. |
| `sms_phone_numbers` | `str` | Optional | Comma-separated list of phone numbers to send SMS alerts to. Digits only; no dashes or parentheses, etc. |
| `email_addresses` | `str` | Optional | Comma-separated list of email addresses to send alerts to. |

## Example

```python
from verizon.models.usage_trigger_update_request import UsageTriggerUpdateRequest

usage_trigger_update_request = UsageTriggerUpdateRequest(
    account_name='0212312345-00001',
    trigger_name='95% usage alert',
    threshold_value='95',
    sms_phone_numbers='5551231234',
    email_addresses='me@theinternet.com, you@theinternet.com'
)
```

