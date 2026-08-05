
# Transaction ID

The transaction ID of the request that you want to cancel, from the POST /devicelocations synchronus response.

## Structure

`TransactionID`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | - |

## Example

```python
from verizon.models.transaction_id import TransactionID

transaction_id = TransactionID(
    txid='2c90bd28-eeee-ffff-gggg-7e3bd4fbff33'
)
```

