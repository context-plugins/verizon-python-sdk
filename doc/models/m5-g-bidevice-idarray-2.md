
# M5 G Bidevice Idarray 2

## Structure

`M5gBideviceIdarray2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`List[M5gBideviceId1]`](../../doc/models/m5-g-bidevice-id-1.md) | Optional | - |

## Example

```python
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1
from verizon.models.m_5g_bidevice_idarray_2 import M5gBideviceIdarray2

m_5g_bidevice_idarray_2 = M5gBideviceIdarray2(
    device_id=[
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        )
    ]
)
```

