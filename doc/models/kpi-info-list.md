
# KPI Info List

## Structure

`KPIInfoList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `kpi_info_list` | [`List[KPIInfo]`](../../doc/models/kpi-info.md) | Optional | - |

## Example

```python
from verizon.models.kpi_info import KPIInfo
from verizon.models.kpi_info_list import KPIInfoList

kpi_info_list = KPIInfoList(
    kpi_info_list=[
        KPIInfo(
            name='DOWNLINK_THROUGHPUT',
            value='23.2',
            node_name='132924_ENB_VZ_EULESS_OLTE_RD-01',
            node_type='BASEBAND',
            description='Downlink throughput (4G)',
            unit='Mbps',
            category='Network Performance Radio',
            time_of_last_update='2022-12-07T08:39:59.228Z'
        )
    ]
)
```

