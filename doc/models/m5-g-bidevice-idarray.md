
# M5 G Bidevice Idarray

## Structure

`M5gBideviceIdarray`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | List[[5gbideviceId1](../../doc/models/m5-g-bidevice-id-1.md)] \| None | Optional | This is List of a container for any-of cases. |

## Example

```python
from verizon.models.m_5g_bidevice_id_1 import M5gBideviceId1
from verizon.models.m_5g_bidevice_idarray import M5gBideviceIdarray

m_5g_bidevice_idarray = M5gBideviceIdarray(
    device_id=[
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        ),
        M5gBideviceId1(
            id='id0',
            kind='kind8'
        )
    ]
)
```

