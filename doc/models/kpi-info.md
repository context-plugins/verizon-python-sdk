
# KPI Info

KPI Info Object

## Structure

`KPIInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `value` | `str` | Optional | - |
| `node_name` | `str` | Optional | - |
| `node_type` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `unit` | `str` | Optional | - |
| `category` | `str` | Optional | - |
| `time_of_last_update` | `str` | Optional | - |

## Example

```python
from verizon.models.kpi_info import KPIInfo

kpi_info = KPIInfo(
    name='DOWNLINK_THROUGHPUT',
    value='23.2',
    node_name='132924_ENB_VZ_EULESS_OLTE_RD-01',
    node_type='BASEBAND',
    description='Downlink throughput (4G)',
    unit='Mbps',
    category='Network Performance Radio',
    time_of_last_update='2022-12-07T08:39:59.228Z'
)
```

