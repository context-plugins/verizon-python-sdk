# SMS

Exchange Short Message Service (SMS) messages with devices.

```python
sms_controller = client.sms
```

## Class Name

`SMSController`

## Methods

* [Send SMS to Device](../../doc/controllers/sms.md#send-sms-to-device)
* [List Devices SMS Messages](../../doc/controllers/sms.md#list-devices-sms-messages)
* [Start Queued SMS Delivery](../../doc/controllers/sms.md#start-queued-sms-delivery)


# Send SMS to Device

The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due to traffic and routing considerations.

```python
def send_sms_to_device(self,
                      body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SMSSendRequest`](../../doc/models/sms-send-request.md) | Body, Required | Request to send SMS. |

## Response Type

**200**: Request ID received on a successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`DeviceManagementResult`](../../doc/models/device-management-result.md).

## Example Usage

```python
body = SMSSendRequest(
    account_name='0000123456-00001',
    sms_message='the body or text of the message itself',
    custom_fields=[
        CustomFields(
            key='CustomField1',
            value='value of the field'
        )
    ],
    data_encoding='optional 7 or 8-bit encoding',
    device_ids=[
        DeviceId(
            id='20-digit ICCID',
            kind='iccid'
        )
    ],
    time_to_live='a000000010000000R'
)

result = sms_controller.send_sms_to_device(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "595f5c44-c31c-4552-8670-020a1545a84d"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# List Devices SMS Messages

When HTTP status is 202, a URL will be returned in the Location header of the form /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

```python
def list_devices_sms_messages(self,
                             aname,
                             next=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |
| `next` | `int` | Query, Optional | Continue the previous query from the URL in Location Header. |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SMSMessagesQueryResult`](../../doc/models/sms-messages-query-result.md).

## Example Usage

```python
aname = '0252012345-00001'

result = sms_controller.list_devices_sms_messages(aname)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "messages": [
    {
      "deviceIds": [
        {
          "id": "09623489171",
          "kind": "esn"
        }
      ],
      "message": "testmessage1",
      "timestamp": "2016-01-01T12:29:49-08:00"
    },
    {
      "deviceIds": [
        {
          "id": "09623489171",
          "kind": "esn"
        }
      ],
      "message": "testmessage2",
      "timestamp": "2016-01-01T12:31:02-08:00"
    }
  ],
  "hasMoreData": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |


# Start Queued SMS Delivery

Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by your application, either by callback or synchronously with GET /sms/{accountName}/history.

```python
def start_queued_sms_delivery(self,
                             aname)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `aname` | `str` | Template, Required | Account name. |

## Response Type

**200**: Successful response.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ConnectivityManagementSuccessResult`](../../doc/models/connectivity-management-success-result.md).

## Example Usage

```python
aname = '0252012345-00001'

result = sms_controller.start_queued_sms_delivery(aname)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "success": true
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Error response. | [`ConnectivityManagementResultException`](../../doc/models/connectivity-management-result-exception.md) |

