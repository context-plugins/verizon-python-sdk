
# ESIM Global Device List Device Filter

## Data Type

`ESIMDeviceId | DeviceId2`

## Cases

| Type |
|  --- |
| [`ESIMDeviceId`](../../../doc/models/esim-device-id.md) |
| [`DeviceId2`](../../../doc/models/device-id-2.md) |

## ESIMDeviceId

### Initialization Code

#### Example

```python
value = ESIMDeviceId(
    id='32-digit EID',
    kind='eid'
)
```

## DeviceId2

### Initialization Code

#### Example

```python
value = DeviceId2(
    id='15-digit IMEI',
    kind='imei'
)
```

