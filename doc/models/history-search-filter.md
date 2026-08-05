
# History Search Filter

The selected device and attributes for which a request should retrieve data.

## Structure

`HistorySearchFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Required | Account name identifier. |
| `device` | [`Device`](../../doc/models/device.md) | Required | Identifies a particular IoT device. |
| `attributes` | [`HistorySearchFilterAttributes`](../../doc/models/history-search-filter-attributes.md) | Optional | Streaming RF parameters for which you want to retrieve history data. |

## Example

```python
from verizon.models.attribute_identifier_enum import AttributeIdentifierEnum
from verizon.models.device import Device
from verizon.models.history_search_filter import HistorySearchFilter
from verizon.models.history_search_filter_attributes import HistorySearchFilterAttributes

history_search_filter = HistorySearchFilter(
    account_name='0000123456-00001',
    device=Device(
        id='15-digit IMEI',
        kind='IMEI'
    ),
    attributes=HistorySearchFilterAttributes(
        name=AttributeIdentifierEnum.LINK_QUALITY
    )
)
```

