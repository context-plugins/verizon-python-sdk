
# Domestic 4 G and 5G Nationwide Network Coverage Body

## Data Type

`GetWirelessCoverageRequest | GetWirelessCoverageRequestFWA`

## Cases

| Type |
|  --- |
| [`GetWirelessCoverageRequest`](../../../doc/models/get-wireless-coverage-request.md) |
| [`GetWirelessCoverageRequestFWA`](../../../doc/models/get-wireless-coverage-request-fwa.md) |

## GetWirelessCoverageRequest

### Initialization Code

#### Example

```python
value = GetWirelessCoverageRequest(
    account_name='0000123456-00001',
    request_type='NW',
    location_type='LONGLAT',
    locations=Locationscoord(),
    network_types_list=[
        NetworkTypeObject(
            network_type='LTE'
        )
    ]
)
```

## GetWirelessCoverageRequestFWA

### Initialization Code

#### Example

```python
value = GetWirelessCoverageRequestFWA(
    account_name='0000123456-00001',
    request_type='NW',
    location_type='ADDRESS',
    locations=Locations(),
    network_types_list=[
        NetworkTypeObject(
            network_type='LTE'
        )
    ]
)
```

