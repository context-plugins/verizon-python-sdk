# Sensor Insights Smart Alerts

```python
sensor_insights_smart_alerts_controller = client.sensor_insights_smart_alerts
```

## Class Name

`SensorInsightsSmartAlertsController`

## Methods

* [Sensor Insights List Smart Alerts Request](../../doc/controllers/sensor-insights-smart-alerts.md#sensor-insights-list-smart-alerts-request)
* [Sensor Insights Patch Smart Alert Request](../../doc/controllers/sensor-insights-smart-alerts.md#sensor-insights-patch-smart-alert-request)
* [Sensor Insights Bulk Update](../../doc/controllers/sensor-insights-smart-alerts.md#sensor-insights-bulk-update)


# Sensor Insights List Smart Alerts Request

```python
def sensor_insights_list_smart_alerts_request(self,
                                             body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListSmartAlertsRequest`](../../doc/models/dto-list-smart-alerts-request.md) | Body, Required | Retrieve a smart alert |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[UserSmartAlert]`](../../doc/models/user-smart-alert.md).

## Example Usage

```python
body = DtoListSmartAlertsRequest(
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
    resourceidentifier=DtoResourceidentifier(
        id='cb3eea68-eeee-ffff-gggg-ac4463ccd073'
    )
)

result = sensor_insights_smart_alerts_controller.sensor_insights_list_smart_alerts_request(body)

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


# Sensor Insights Patch Smart Alert Request

```python
def sensor_insights_patch_smart_alert_request(self,
                                             body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoPatchSmartAlertRequest`](../../doc/models/dto-patch-smart-alert-request.md) | Body, Required | Partially update a smart alert |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserSmartAlert`](../../doc/models/user-smart-alert.md).

## Example Usage

```python
body = DtoPatchSmartAlertRequest(
    accountname='0000123456-00001',
    resourceidentifier=DtoResourceidentifier(
        id='0b37ab8b-eeee-ffff-gggg-e0149af43f43'
    ),
    smartalert=UserSmartAlert(
        createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
        lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
        versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
        accountclientid='null',
        billingaccountid='0000123456-00001',
        category='telemetry',
        condition=2592000,
        description='a short description',
        deviceid='The UUID of the device',
        foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
        id='fecbe450-eeee-ffff-gggg-aa166fd5f8e3',
        isacknowledged=True,
        iscleared=True,
        isdisabled=False,
        name='User defined name of the record',
        ruleid='The UUID of a rule',
        severity='minor',
        state='success',
        template='The template ID',
        version='1.0'
    )
)

result = sensor_insights_smart_alerts_controller.sensor_insights_patch_smart_alert_request(body)

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


# Sensor Insights Bulk Update

```python
def sensor_insights_bulk_update(self,
                               body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoBulkUpdate`](../../doc/models/dto-bulk-update.md) | Body, Required | Bulk update smart alerts |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`UserSmartAlert`](../../doc/models/user-smart-alert.md).

## Example Usage

```python
body = DtoBulkUpdate(
    accountname='0000123456-00001',
    resourceidentifiers=[
        TheIDresourceandDeviceID(
            id='ee70a869-eeee-ffff-gggg-07c14c31f96e'
        ),
        TheIDresourceandDeviceID(
            deviceid='The UUID of the device'
        )
    ],
    smartalert=BulkUpdateSmartalert(
        name='User defined name of the record'
    )
)

result = sensor_insights_smart_alerts_controller.sensor_insights_bulk_update(body)

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

