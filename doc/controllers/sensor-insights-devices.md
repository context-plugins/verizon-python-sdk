# Sensor Insights Devices

```python
sensor_insights_devices_controller = client.sensor_insights_devices
```

## Class Name

`SensorInsightsDevicesController`

## Methods

* [Sensor Insights List Devices Request](../../doc/controllers/sensor-insights-devices.md#sensor-insights-list-devices-request)
* [Sensor Insights Patch Device Request](../../doc/controllers/sensor-insights-devices.md#sensor-insights-patch-device-request)
* [Sensor Insights Last Reported Time Request](../../doc/controllers/sensor-insights-devices.md#sensor-insights-last-reported-time-request)
* [Sensor Insights Device Action Set Request](../../doc/controllers/sensor-insights-devices.md#sensor-insights-device-action-set-request)
* [Sensor Insights List Device Experience History Request](../../doc/controllers/sensor-insights-devices.md#sensor-insights-list-device-experience-history-request)
* [Sensor Insights List Network Experience History Request](../../doc/controllers/sensor-insights-devices.md#sensor-insights-list-network-experience-history-request)


# Sensor Insights List Devices Request

```python
def sensor_insights_list_devices_request(self,
                                        body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListDevicesRequest`](../../doc/models/dto-list-devices-request.md) | Body, Required | List all device details on an account |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[DtoExpandedDeviceResponse]`](../../doc/models/dto-expanded-device-response.md).

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

result = sensor_insights_devices_controller.sensor_insights_list_devices_request(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 401 | UnAuthorized | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 403 | Forbidden | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 404 | Not Found | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |


# Sensor Insights Patch Device Request

```python
def sensor_insights_patch_device_request(self,
                                        body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoPatchDeviceRequest`](../../doc/models/dto-patch-device-request.md) | Body, Required | Partially update a device's details |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResourceDevice`](../../doc/models/resource-device.md).

## Example Usage

```python
body = DtoPatchDeviceRequest(
    accountname='0000123456-00001',
    device=ResourceDevice(
        createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
        foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
        lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
        state='success',
        versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
        accountclientid='null',
        billingaccountid='0000123456-00001',
        chipset='The chipset used by the device',
        customdata={
            'additionalProp1': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'additionalProp2': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'additionalProp3': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        },
        description='The number of days to retaing the event data',
        esn=223372036854775800,
        fields=DtoFields(
            additional_prop_1='string',
            additional_prop_2='string',
            additional_prop_3='string'
        ),
        hardwareversion='1.0',
        iccid='The 20-digit Integrated Circuit Card ID (SIM card ID)',
        id='33e21f61-a44a-44c9-b7a0-a63f5d19bd4f',
        imei=223372036854775,
        imsi=223372036854775800,
        licenses=[
            'licenses assigned to the device'
        ],
        mac='The Media Access Control address of the device, listed on the device in the format XX-XX-XX-XX-XX-XX or XX:XX:XX:XX:XX:XX',
        manufacturer='REOLINK',
        meid='The 56-bit Mobile Equipment ID',
        msisdn='The Mobile Station International Subscriber Directory Number. In the USA, this is 1+ a 10-digit phone number',
        name='User defined name of the record',
        parentdeviceid='BLE device ID',
        productmodel='Model name of the device',
        providerid='Verizon Wireless',
        qrcode='The Quick Response (QR) code',
        refid='P3730-1422323050860',
        refidtype='The type of value represented by `refid`',
        serial='The device\'s serial number',
        services=[
            'configuration'
        ],
        sku='The Stock Keeping Unit (SKU) number',
        softwareversion='the current device software version',
        version='1.0',
        eventretention=90
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

result = sensor_insights_devices_controller.sensor_insights_patch_device_request(body)

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


# Sensor Insights Last Reported Time Request

```python
def sensor_insights_last_reported_time_request(self,
                                              body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoLastReportedTimeRequest`](../../doc/models/dto-last-reported-time-request.md) | Body, Required | Get the last reported information for a device |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DtoLastReportedTimeResponse`](../../doc/models/dto-last-reported-time-response.md).

## Example Usage

```python
body = DtoLastReportedTimeRequest(
    accountname='0000123456-00001',
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

result = sensor_insights_devices_controller.sensor_insights_last_reported_time_request(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 404 | Not Found | [`M404ManagementErrorException`](../../doc/models/m404-management-error-exception.md) |


# Sensor Insights Device Action Set Request

```python
def sensor_insights_device_action_set_request(self,
                                             body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [dto.DeviceActionSetRequest](../../doc/models/dto-device-action-set-request.md) \| [dto.deviceCommand](../../doc/models/dto-device-command.md) | Body, Required | This is a container for any-of cases. |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DtoDeviceActionSetResponse`](../../doc/models/dto-device-action-set-response.md).

## Example Usage

```python
body = DtoDeviceActionSetRequest(
    accountname='0000123456-00001',
    configuration=DtoDeviceActionSetConfiguration(
        device_config=DtoDeviceConfig(
            ble=SensorInsightsBLE(
                data_mode=1,
                manufacturer_id=13200,
                max_num_scan=100,
                min_sig_str=-115,
                monitor_period=300,
                more_manuf_id=[
                    jsonpickle.decode('{}')
                ],
                op_mode=1,
                report_offset=0,
                report_period=300,
                report_type=2,
                scan_duration=20
            )
        )
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

result = sensor_insights_devices_controller.sensor_insights_device_action_set_request(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 404 | Not Found | [`M404ManagementErrorException`](../../doc/models/m404-management-error-exception.md) |


# Sensor Insights List Device Experience History Request

```python
def sensor_insights_list_device_experience_history_request(self,
                                                          body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListDeviceExperienceHistoryRequest`](../../doc/models/dto-list-device-experience-history-request.md) | Body, Required | List the device experience |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[UserDeviceExperienceHistory]`](../../doc/models/user-device-experience-history.md).

## Example Usage

```python
body = DtoListDeviceExperienceHistoryRequest(
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
    )
)

result = sensor_insights_devices_controller.sensor_insights_list_device_experience_history_request(body)

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


# Sensor Insights List Network Experience History Request

```python
def sensor_insights_list_network_experience_history_request(self,
                                                           body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListNetworkExperienceHistoryRequest`](../../doc/models/dto-list-network-experience-history-request.md) | Body, Required | List the network experience |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[UserNetworkExperienceHistory]`](../../doc/models/user-network-experience-history.md).

## Example Usage

```python
body = DtoListNetworkExperienceHistoryRequest(
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
    )
)

result = sensor_insights_devices_controller.sensor_insights_list_network_experience_history_request(body)

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

