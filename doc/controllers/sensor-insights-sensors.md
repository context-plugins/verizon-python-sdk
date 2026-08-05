# Sensor Insights Sensors

```python
sensor_insights_sensors_controller = client.sensor_insights_sensors
```

## Class Name

`SensorInsightsSensorsController`

## Methods

* [Sensor Insights List Sensor Devices Request](../../doc/controllers/sensor-insights-sensors.md#sensor-insights-list-sensor-devices-request)
* [Sensor Insights on Board Sensor Request](../../doc/controllers/sensor-insights-sensors.md#sensor-insights-on-board-sensor-request)
* [Sensor Insights Sensor on Board Status Request](../../doc/controllers/sensor-insights-sensors.md#sensor-insights-sensor-on-board-status-request)
* [Sensor Insights Off Board Sensor Request](../../doc/controllers/sensor-insights-sensors.md#sensor-insights-off-board-sensor-request)
* [Sensor Insights Sensor Off Boarding Status Request](../../doc/controllers/sensor-insights-sensors.md#sensor-insights-sensor-off-boarding-status-request)


# Sensor Insights List Sensor Devices Request

```python
def sensor_insights_list_sensor_devices_request(self,
                                               body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListSensorDevicesRequest`](../../doc/models/dto-list-sensor-devices-request.md) | Body, Required | List details of the sensors |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[ResourceDevice]`](../../doc/models/resource-device.md).

## Example Usage

```python
body = DtoListSensorDevicesRequest(
    accountname='0000123456-00001',
    filter=DtoFilter(
        expand='device detail(s)',
        limitnumber=100,
        nopagination=True,
        page='The number of pages',
        pagenumber=1,
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

result = sensor_insights_sensors_controller.sensor_insights_list_sensor_devices_request(body)

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


# Sensor Insights on Board Sensor Request

```python
def sensor_insights_on_board_sensor_request(self,
                                           body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoOnBoardSensorRequest`](../../doc/models/dto-on-board-sensor-request.md) | Body, Required | Onboarding a sensor |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
body = DtoOnBoardSensorRequest(
    accountname='0000123456-00001',
    payload=Payload(
        addsensor=ResourceOnBoardSensor(
            deveui='The unique EUI64 address of the device',
            appeui='global application ID in IEEE EUI64 address space that uniquely identifies the entity able to process the JoinReq frame',
            appkey='Encryption key used for messages during every over the air activation',
            mclass='A',
            kind='ts.device.sensor.lorawan.radiobridge.RBS301-DWS-US',
            description='used to identify water leaks',
            name='Water Leak sensor',
            customdata={
                'additionalProp1': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                'additionalProp2': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
                'additionalProp3': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    )
)

result = sensor_insights_sensors_controller.sensor_insights_on_board_sensor_request(body)

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
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`M500ManagementErrorException`](../../doc/models/m500-management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |


# Sensor Insights Sensor on Board Status Request

```python
def sensor_insights_sensor_on_board_status_request(self,
                                                  body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoSensorOnBoardStatusRequest`](../../doc/models/dto-sensor-on-board-status-request.md) | Body, Required | Get the sensor's onboarding status |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DtoSensorOnBoardingStatusResponse`](../../doc/models/dto-sensor-on-boarding-status-response.md).

## Example Usage

```python
body = DtoSensorOnBoardStatusRequest(
    accountname='0000123456-00001',
    gatewayidentifier=Gatewayidentifier(
        deviceid='00000000-0000-0000-0000-000000000255'
    ),
    onboarding=Onboarding()
)

result = sensor_insights_sensors_controller.sensor_insights_sensor_on_board_status_request(body)

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


# Sensor Insights Off Board Sensor Request

```python
def sensor_insights_off_board_sensor_request(self,
                                            body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoOffBoardSensorRequest`](../../doc/models/dto-off-board-sensor-request.md) | Body, Required | Offboard a sensor |

## Response Type

**204**: No Content

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
body = DtoOffBoardSensorRequest(
    accountname='0000123456-00001',
    configuration=Sensorinsightsconfig(
        removesensor=DtoOffBoardSensor(
            deveui='The unique EUI64 address of the device'
        )
    )
)

result = sensor_insights_sensors_controller.sensor_insights_off_board_sensor_request(body)

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


# Sensor Insights Sensor Off Boarding Status Request

```python
def sensor_insights_sensor_off_boarding_status_request(self,
                                                      body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoSensorOffBoardStatusRequest`](../../doc/models/dto-sensor-off-board-status-request.md) | Body, Required | Get a sensor's offboarding status |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DtoSensorOffBoardingStatusResponse`](../../doc/models/dto-sensor-off-boarding-status-response.md).

## Example Usage

```python
body = DtoSensorOffBoardStatusRequest(
    accountname='0000123456-00001',
    gatewayidentifier=Gatewayidentifier(
        deviceid='UUID of the Gateway device'
    ),
    offboarding=Offboarding()
)

result = sensor_insights_sensors_controller.sensor_insights_sensor_off_boarding_status_request(body)

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

