
# Billable Usage Report

Bill usage report.

## Structure

`BillableUsageReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account identifier. |
| `usage_for_all_accounts` | `bool` | Optional | The usage is for a single or multiple accounts. |
| `sku_name` | `str` | Optional | SKU Name of the service subscription. |
| `transactions_allowed` | `str` | Optional | The number of location requests included with the subscription type. |
| `total_transaction_count` | `str` | Optional | The total number of billable device location requests during the reporting period from all included accounts. |
| `primary_account` | [`ServiceUsage`](../../doc/models/service-usage.md) | Optional | - |
| `managed_accounts` | [`List[ServiceUsage]`](../../doc/models/service-usage.md) | Optional | Zero or more managed accounts. |

## Example

```python
from verizon.models.billable_usage_report import BillableUsageReport
from verizon.models.service_usage import ServiceUsage

billable_usage_report = BillableUsageReport(
    account_name='1223334444-00001',
    usage_for_all_accounts=False,
    sku_name='TS-LOC-COARSE-CellID-Aggr',
    transactions_allowed='5000',
    total_transaction_count='350',
    primary_account=ServiceUsage(
        account_name='1223334444-00001',
        transactions_count='125'
    ),
    managed_accounts=[]
)
```

