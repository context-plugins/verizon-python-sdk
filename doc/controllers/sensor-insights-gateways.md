# Sensor Insights Gateways

```python
sensor_insights_gateways_controller = client.sensor_insights_gateways
```

## Class Name

`SensorInsightsGatewaysController`


# Sensor Insights List Gateway Devices Request

```python
def sensor_insights_list_gateway_devices_request(self,
                                                body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListDevicesRequest`](../../doc/models/dto-list-devices-request.md) | Body, Required | Get gateway information |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[ResourceDevice]`](../../doc/models/resource-device.md).

## Example Usage

```python
body = DtoListDevicesRequest(
    accountname='0000123456-00001',
    filter=DtoFilter(
        expand='device detail(s)',
        limitnumber=100,
        nopagination=True,
        page='The number of pages',
        pagenumber=100,
        projection=[
            'specific device fields requested'
        ],
        selection={
            'additionalProp1': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'additionalProp2': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'additionalProp3': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    resourceidentifier=DtoDeviceResourceIdentifier(
        deveui='The unique EUI64 address of the device',
        deviceid='The UUID of the device',
        esn=223372036854775800,
        iccid='The 20-digit Integrated Circuit Card ID (SIM card ID)',
        imei=223372036854775,
        imsi=223372036854775800,
        mac='The Media Access Control address of the device, listed on the device in the format XX-XX-XX-XX-XX-XX or XX:XX:XX:XX:XX:XX',
        manufacturer='REOLINK',
        meid='The 56-bit Mobile Equipment ID',
        msisdn='The Mobile Station International Subscriber Directory Number. In the USA, this is 1+ a 10-digit phone number',
        node_uuid='The UUID of the node the device is associated with',
        qrcode='The Quick Response (QR) code',
        serial='The device\'s serial number'
    )
)

result = sensor_insights_gateways_controller.sensor_insights_list_gateway_devices_request(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 401 | UnAuthorized | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 404 | Not Found | [`M404ManagementErrorException`](../../doc/models/m404-management-error-exception.md) |
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`M500ManagementErrorException`](../../doc/models/m500-management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |

