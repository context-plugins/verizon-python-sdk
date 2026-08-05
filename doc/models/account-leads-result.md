
# Account Leads Result

Returns information for all leads associated with an account.

## Structure

`AccountLeadsResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `has_more_data` | `bool` | Optional | False if no more leads.True if there is more data to be retrieved. |
| `leads` | [`List[AccountLead]`](../../doc/models/account-lead.md) | Optional | The leads associated with an account. |

## Example

```python
from verizon.models.account_lead import AccountLead
from verizon.models.account_leads_result import AccountLeadsResult
from verizon.models.address import Address

account_leads_result = AccountLeadsResult(
    has_more_data=False,
    leads=[
        AccountLead(
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
    ]
)
```

