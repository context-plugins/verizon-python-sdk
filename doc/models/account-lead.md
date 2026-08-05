
# Account Lead

A successful response returns an array of lead objects.

## Structure

`AccountLead`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address`](../../doc/models/address.md) | Optional | The customer address for the line's primary place of use, for line usage taxation. |
| `lead_id` | `str` | Optional | Unique number for each lead. Use this value in the leadId parameter when activating devices to credit the activations to the lead. |
| `lead_state` | `str` | Optional | The current state of the lead, such as “Qualified” or “Closed.” |

## Example

```python
from verizon.models.account_lead import AccountLead
from verizon.models.address import Address

account_lead = AccountLead(
    address=Address(
        address_line_1='1600 Pennsylvania Avenue',
        city='Washington',
        state='DC',
        zip='20500',
        country='USA',
        address_line_2='',
        zip_4='zip40',
        phone='phone4',
        phone_type='phoneType0',
        email_address='emailAddress6'
    ),
    lead_id='L-10001',
    lead_state='Qualified'
)
```

