
# M5 G Bidevice Id

## Structure

`M5gBideviceId`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | [`M5gBideviceId1`](../../doc/models/m5-g-bidevice-id-1.md) | Optional | - |

## Example

```python
from verizon.models.m_5g_bidevice_id import M5gBideviceId
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1

m_5g_bidevice_id = M5gBideviceId(
    device_id=M5gBideviceId1(
        id='id0',
        kind='kind8'
    )
)
```

