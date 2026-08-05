# 5G BI Device Actions

```python
m_5g_bi_device_actions_controller = client.m_5g_bi_device_actions
```

## Class Name

`M5gBIDeviceActionsController`

## Methods

* [Business Internetlist Device Information](../../doc/controllers/5g-bi-device-actions.md#business-internetlist-device-information)
* [Business Internetactivate Using POST](../../doc/controllers/5g-bi-device-actions.md#business-internetactivate-using-post)
* [Business Internet Serviceplanchange](../../doc/controllers/5g-bi-device-actions.md#business-internet-serviceplanchange)


# Business Internetlist Device Information

Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's properties.

```python
def business_internetlist_device_information(self,
                                            body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **OR** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`M5gBideviceId`](../../doc/models/m5-g-bidevice-id.md) | Body, Required | Device Profile Query |

## Response Type

**200**: The device's details will be returned from a successful request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`M5gBideviceDetailsresponse`](../../doc/models/m5-g-bidevice-detailsresponse.md).

## Example Usage

```python
body = M5gBideviceId(
    device_id=M5gBideviceId1(
        id='20-digit ICCID',
        kind='iccid'
    )
)

result = m_5g_bi_device_actions_controller.business_internetlist_device_information(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`M5gBiRestErrorResponseException`](../../doc/models/m5-g-bi-rest-error-response-exception.md) |


# Business Internetactivate Using POST

Uses the device's ICCID and IMEI to activate service.

```python
def business_internetactivate_using_post(self,
                                        body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **OR** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`M5gBiactivateRequest`](../../doc/models/m5-g-biactivate-request.md) | Body, Required | Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is required for activating as Public Static. Leave  <code>publicIpRestriction</code> undefined to activate as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile Private Network (MPN). |

## Response Type

**200**: A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`M5gBiRequestResponse`](../../doc/models/m5-g-bi-request-response.md).

## Example Usage

```python
body = M5gBiactivateRequest(
    account_name='0000123456-00001',
    service_plan='service plan name',
    device_list_with_service_address=[
        M5gBideviceIdarray(
            device_id=[
                M5gBideviceId1(
                    id='15-digit IMEI',
                    kind='imei'
                ),
                M5gBideviceId1(
                    id='20-digit ICCID',
                    kind='iccid'
                )
            ]
        ),
        M5gBideviceIdarray()
    ],
    sku_number='VZW Stock Keeping Unit number',
    public_ip_restriction='Unrestricted',
    carrier_name='Verizon Wireless',
    mdn_zip_code='the 5-digit ZIP code of the Mobile Directory Number (MDN)'
)

result = m_5g_bi_device_actions_controller.business_internetactivate_using_post(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "d1f08526-5443-4054-9a29-4456490ea9f8"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`M5gBiRestErrorResponseException`](../../doc/models/m5-g-bi-rest-error-response-exception.md) |


# Business Internet Serviceplanchange

Change a device's service plan to use 5G BI.

```python
def business_internet_serviceplanchange(self,
                                       body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **OR** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`M5gBichangeRequest`](../../doc/models/m5-g-bichange-request.md) | Body, Required | This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service plan can change for an active device up to four times per month but will require address validation for each change. The service plan cannot be changed for a device while its service is suspended. |

## Response Type

**200**: A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`M5gBiRequestResponse`](../../doc/models/m5-g-bi-request-response.md).

## Example Usage

```python
body = M5gBichangeRequest(
    account_name='0000123456-00001',
    service_plan='5G BI service plan name being changed to',
    device_list_with_service_address=[
        M5gBideviceIdarray2(
            device_id=[
                M5gBideviceId1(
                    id='15-digit IMEI',
                    kind='imei'
                )
            ]
        ),
        M5gBideviceIdarray2()
    ],
    current_service_plan='Optional name of the plan being changed from'
)

result = m_5g_bi_device_actions_controller.business_internet_serviceplanchange(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "requestId": "d1f08526-5443-4054-9a29-4456490ea9f8"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`M5gBiRestErrorResponseException`](../../doc/models/m5-g-bi-rest-error-response-exception.md) |

