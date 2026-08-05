# Device SMS Messaging

```python
device_sms_messaging_controller = client.device_sms_messaging
```

## Class Name

`DeviceSMSMessagingController`

## Methods

* [Send an Sms Message](../../doc/controllers/device-sms-messaging.md#send-an-sms-message)
* [Get Sms Messages](../../doc/controllers/device-sms-messaging.md#get-sms-messages)
* [Start Sms Message Delivery](../../doc/controllers/device-sms-messaging.md#start-sms-message-delivery)
* [List Sms Message History](../../doc/controllers/device-sms-messaging.md#list-sms-message-history)


# Send an Sms Message

Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible, but they may be delayed due to traffic and routing considerations.

```python
def send_an_sms_message(self,
                       body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GIOSMSSendRequest`](../../doc/models/giosms-send-request.md) | Body, Required | SMS message to an indiividual device. |

## Response Type

**200**: Request ID

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = GIOSMSSendRequest(
    sms_message='the body or text of the message itself',
    account_name='0000123456-00001',
    custom_fields=[
        KvPair(
            key='CustomField1',
            value='value of the field'
        )
    ],
    data_encoding='optional 7 or 8-bit encoding',
    time_to_live='000000010000000R',
    device_ids=[
        GIODeviceId(
            kind='iccid',
            id='20-digit ICCID'
        )
    ]
)

result = device_sms_messaging_controller.send_an_sms_message(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Get Sms Messages

Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

```python
def get_sms_messages(self,
                    account_name,
                    next=None)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | Numeric account name<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9\-]{3,32}$` |
| `next` | `str` | Query, Optional | Continue the previous query from the pageUrl in Location Header<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9]{3,32}$` |

## Response Type

**200**: Successful response

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SmsMessagesResponse`](../../doc/models/sms-messages-response.md).

## Example Usage

```python
account_name = '0000123456-00001'

next = 'TheURLForTheNextQuery'

result = device_sms_messaging_controller.get_sms_messages(
    account_name,
    next=next
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# Start Sms Message Delivery

Starts delivery of SMS messages for the specified account.

```python
def start_sms_message_delivery(self,
                              account_name)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Template, Required | Numeric account name<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `32`, *Pattern*: `^[A-Za-z0-9\-]{3,32}$` |

## Response Type

**200**: Request Success Message

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SuccessResponse`](../../doc/models/success-response.md).

## Example Usage

```python
account_name = '0000123456-00001'

result = device_sms_messaging_controller.start_sms_message_delivery(account_name)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |


# List Sms Message History

Returns a list of sms history for a given device during a specified time frame.

```python
def list_sms_message_history(self,
                            body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SMSEventHistoryRequest`](../../doc/models/sms-event-history-request.md) | Body, Required | Device Query |

## Response Type

**200**: Request ID

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`GIORequestResponse`](../../doc/models/gio-request-response.md).

## Example Usage

```python
body = SMSEventHistoryRequest(
    device_id=GIODeviceId(
        kind='eid',
        id='12345678901234567890123456789012'
    )
)

result = device_sms_messaging_controller.list_sms_message_history(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`GIORestErrorResponseException`](../../doc/models/gio-rest-error-response-exception.md) |

