# HPL Device Management

```python
hpl_device_management_controller = client.hpl_device_management
```

## Class Name

`HPLDeviceManagementController`


# Add Devices Hyper Precise

Use this API if you want to manage some device settings before you are ready to activate service for the devices.

```python
def add_devices_hyper_precise(self,
                             body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`HplAddDevicesRequest`](../../doc/models/hpl-add-devices-request.md) | Body, Required | Devices to add to the account. |

## Response Type

**200**: For each device in the request, contains device identifiers and a success or failure response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[HplAddDevicesRequest]`](../../doc/models/hpl-add-devices-request.md).

## Example Usage

```python
body = HplAddDevicesRequest(
    state='preactive',
    devices_to_add=[
        HplAccountDeviceList(
            device_ids=[
                HplDeviceId(
                    kind='imei',
                    id='15-digit IMEI'
                ),
                HplDeviceId(
                    kind='iccid',
                    id='20-digit ICCID'
                )
            ]
        ),
        HplAccountDeviceList(
            device_ids=[
                HplDeviceId(
                    kind='imei',
                    id='15-digit IMEI'
                ),
                HplDeviceId(
                    kind='iccid',
                    id='20-digit ICCID'
                )
            ]
        )
    ],
    account_name='0000123456-00001',
    custom_fields=[
        HplCustomFields(
            key='CustomField2',
            value='SuperVend'
        )
    ],
    group_name='West Region'
)

result = hpl_device_management_controller.add_devices_hyper_precise(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
[
  {
    "deviceIds": [
      {
        "id": "20-digit ICCID",
        "kind": "iccid"
      }
    ],
    "response": "Success"
  }
]
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request. | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 401 | Unauthorized | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 403 | Forbidden | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 404 | Not Found / Does not exist | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 405 | Method Not Allowed | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 406 | Format / Request Unacceptable | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 429 | Too many requests | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| 500 | Internal Server Error | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |
| Default | Error response | [`HyperPreciseLocationResultException`](../../doc/models/hyper-precise-location-result-exception.md) |

