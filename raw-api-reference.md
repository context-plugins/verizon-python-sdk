# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [VerizonClient](verizon/client.py)

## GbiDeviceActions5

> Source: [GbiDeviceActions5](verizon/apis/gbi_device_actions5.py)

<details>
<summary><code>def business_internet_serviceplanchange(body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GbiRequestResponse5, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change a device's service plan to use 5G BI.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gbi_device_actions5.with_raw_response.business_internet_serviceplanchange(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbiRequestResponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gbi_device_actions5.with_raw_response.business_internet_serviceplanchange(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbiRequestResponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GbichangeRequest5](verizon/models/gbichange_request5.py) \| [GbichangeRequest5Dict](verizon/models/gbichange_request5.py)</code> | This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service plan can change for an active device up to four times per month but will require address validation for each change. The service plan cannot be changed for a device while its service is suspended. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GbiRequestResponse5](verizon/models/gbi_request_response5.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GbiRequestResponse5](verizon/models/gbi_request_response5.py)</code> -- A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_internetactivate_using_post(body: GbiactivateRequest5 | GbiactivateRequest5Dict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GbiRequestResponse5, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the device's ICCID and IMEI to activate service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gbi_device_actions5.with_raw_response.business_internetactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbiRequestResponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gbi_device_actions5.with_raw_response.business_internetactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbiRequestResponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GbiactivateRequest5](verizon/models/gbiactivate_request5.py) \| [GbiactivateRequest5Dict](verizon/models/gbiactivate_request5.py)</code> | Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is required for activating as Public Static. Leave  <code>publicIpRestriction</code> undefined to activate as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile Private Network (MPN). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GbiRequestResponse5](verizon/models/gbi_request_response5.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GbiRequestResponse5](verizon/models/gbi_request_response5.py)</code> -- A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_internetlist_device_information(body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GbideviceDetailsresponse5, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's properties.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gbi_device_actions5.with_raw_response.business_internetlist_device_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbideviceDetailsresponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gbi_device_actions5.with_raw_response.business_internetlist_device_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbideviceDetailsresponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GbideviceId5](verizon/models/gbidevice_id5.py) \| [GbideviceId5Dict](verizon/models/gbidevice_id5.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GbideviceDetailsresponse5](verizon/models/gbidevice_detailsresponse5.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GbideviceDetailsresponse5](verizon/models/gbidevice_detailsresponse5.py)</code> -- The device's details will be returned from a successful request.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AccountDevices

> Source: [AccountDevices](verizon/apis/account_devices.py)

<details>
<summary><code>def get_account_device_information(acc: str, *, last_seen_device_id: str | None = None, protocol: DevicesProtocolOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3AccountDeviceList, GetAccountDeviceInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve account device information such as reported firmware on the devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_devices.with_raw_response.get_account_device_information(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3AccountDeviceList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountDeviceInformationErrorBody
```

**Async**

```python
result = await async_client.account_devices.with_raw_response.get_account_device_information(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3AccountDeviceList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountDeviceInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>last_seen_device_id</code> | <code>str \| None</code> | Last seen device identifier.<br>**Default**: <code>None</code> |
| <code>protocol</code> | <code>[DevicesProtocolOrStr](verizon/models/enums/devices_protocol.py) \| None</code> | Filter to retrieve a specific protocol type used.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3AccountDeviceList](verizon/models/v3_account_device_list.py), [GetAccountDeviceInformationErrorBody](verizon/errors/get_account_device_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3AccountDeviceList](verizon/models/v3_account_device_list.py)</code> -- Returns an array of devices.

**On `Failure`**: `error` is <code>[GetAccountDeviceInformationErrorBody](verizon/errors/get_account_device_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_account_devices_information(acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceListResult, ListAccountDevicesInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve device information for a list of devices on an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_devices.with_raw_response.list_account_devices_information(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountDevicesInformationErrorBody
```

**Async**

```python
result = await async_client.account_devices.with_raw_response.list_account_devices_information(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountDevicesInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[DeviceImei](verizon/models/device_imei.py) \| [DeviceImeiDict](verizon/models/device_imei.py)</code> | Request device list information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceListResult](verizon/models/device_list_result.py), [ListAccountDevicesInformationErrorBody](verizon/errors/list_account_devices_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceListResult](verizon/models/device_list_result.py)</code> -- Get device list information.

**On `Failure`**: `error` is <code>[ListAccountDevicesInformationErrorBody](verizon/errors/list_account_devices_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AccountRequests

> Source: [AccountRequests](verizon/apis/account_requests.py)

<details>
<summary><code>def get_current_asynchronous_request_status(aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AsynchronousRequestResult, GetCurrentAsynchronousRequestStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current status of an asynchronous request that was made for a single device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_requests.with_raw_response.get_current_asynchronous_request_status(aname, request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsynchronousRequestResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCurrentAsynchronousRequestStatusErrorBody
```

**Async**

```python
result = await async_client.account_requests.with_raw_response.get_current_asynchronous_request_status(
    aname, request_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsynchronousRequestResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCurrentAsynchronousRequestStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_id</code> | <code>str</code> | UUID from synchronous response. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AsynchronousRequestResult](verizon/models/asynchronous_request_result.py), [GetCurrentAsynchronousRequestStatusErrorBody](verizon/errors/get_current_asynchronous_request_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AsynchronousRequestResult](verizon/models/asynchronous_request_result.py)</code> -- The asynchronous request status.

**On `Failure`**: `error` is <code>[GetCurrentAsynchronousRequestStatusErrorBody](verizon/errors/get_current_asynchronous_request_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AccountServiceController

> Source: [AccountServiceController](verizon/apis/account_service_controller.py)

<details>
<summary><code>def get_account_information_using_get(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetAccountInformationResponseforplanner, GetAccountInformationUsingGetErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns aaccount information associated with a specified account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_service_controller.with_raw_response.get_account_information_using_get(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAccountInformationResponseforplanner
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountInformationUsingGetErrorBody
```

**Async**

```python
result = await async_client.account_service_controller.with_raw_response.get_account_information_using_get(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAccountInformationResponseforplanner
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountInformationUsingGetErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The account's numeric name, including leading zeroes. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GetAccountInformationResponseforplanner](verizon/models/get_account_information_responseforplanner.py), [GetAccountInformationUsingGetErrorBody](verizon/errors/get_account_information_using_get_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetAccountInformationResponseforplanner](verizon/models/get_account_information_responseforplanner.py)</code> -- The account information related to an account.

**On `Failure`**: `error` is <code>[GetAccountInformationUsingGetErrorBody](verizon/errors/get_account_information_using_get_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 406, 429 | <code>[RestErrorResponseforplanner](verizon/models/rest_error_responseforplanner.py)</code> |
| 401 | <code>[AuthRestErrorResponseforplanner](verizon/models/auth_rest_error_responseforplanner.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AccountSubscriptions

> Source: [AccountSubscriptions](verizon/apis/account_subscriptions.py)

<details>
<summary><code>def list_account_subscriptions(body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict, *, x_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SecuritySubscriptionResult, ListAccountSubscriptionsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the total number of SIM-Secure for IoT subscription licenses purchased for your account by license type, and lists the number of licenses assigned and available for each license type.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.account_subscriptions.with_raw_response.list_account_subscriptions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecuritySubscriptionResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountSubscriptionsErrorBody
```

**Async**

```python
result = await async_client.account_subscriptions.with_raw_response.list_account_subscriptions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecuritySubscriptionResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountSubscriptionsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SecuritySubscriptionRequest](verizon/models/security_subscription_request.py) \| [SecuritySubscriptionRequestDict](verizon/models/security_subscription_request.py)</code> | Request for account subscription. |
| <code>x_request_id</code> | <code>str \| None</code> | Transaction Id.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SecuritySubscriptionResult](verizon/models/security_subscription_result.py), [ListAccountSubscriptionsErrorBody](verizon/errors/list_account_subscriptions_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SecuritySubscriptionResult](verizon/models/security_subscription_result.py)</code> -- Security subscription result.

**On `Failure`**: `error` is <code>[ListAccountSubscriptionsErrorBody](verizon/errors/list_account_subscriptions_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[SecurityResult](verizon/models/security_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Accounts

> Source: [Accounts](verizon/apis/accounts.py)

<details>
<summary><code>def get_account_information(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Account, GetAccountInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about a specified account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.accounts.with_raw_response.get_account_information(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Account
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountInformationErrorBody
```

**Async**

```python
result = await async_client.accounts.with_raw_response.get_account_information(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Account
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Account](verizon/models/account.py), [GetAccountInformationErrorBody](verizon/errors/get_account_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Account](verizon/models/account.py)</code> -- The account information.

**On `Failure`**: `error` is <code>[GetAccountInformationErrorBody](verizon/errors/get_account_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_account_leads(aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountLeadsResult, ListAccountLeadsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

When HTTP status is 202, a URL will be returned in the Location header of the form /leads/{aname}?next={token}. This URL can be used to request the next set of leads.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.accounts.with_raw_response.list_account_leads(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountLeadsResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountLeadsErrorBody
```

**Async**

```python
result = await async_client.accounts.with_raw_response.list_account_leads(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountLeadsResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountLeadsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>next</code> | <code>int \| None</code> | Continue the previous query from the pageUrl in Location Header.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AccountLeadsResult](verizon/models/account_leads_result.py), [ListAccountLeadsErrorBody](verizon/errors/list_account_leads_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountLeadsResult](verizon/models/account_leads_result.py)</code> -- The list of leads associated with the account.

**On `Failure`**: `error` is <code>[ListAccountLeadsErrorBody](verizon/errors/list_account_leads_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_account_states_and_services(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountStatesAndServices, ListAccountStatesAndServicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list and details of all custom services and states defined for a specified account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.accounts.with_raw_response.list_account_states_and_services(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountStatesAndServices
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountStatesAndServicesErrorBody
```

**Async**

```python
result = await async_client.accounts.with_raw_response.list_account_states_and_services(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountStatesAndServices
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountStatesAndServicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AccountStatesAndServices](verizon/models/account_states_and_services.py), [ListAccountStatesAndServicesErrorBody](verizon/errors/list_account_states_and_services_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountStatesAndServices](verizon/models/account_states_and_services.py)</code> -- The account's engagements, services, and states.

**On `Failure`**: `error` is <code>[ListAccountStatesAndServicesErrorBody](verizon/errors/list_account_states_and_services_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AnomalySettings

> Source: [AnomalySettings](verizon/apis/anomaly_settings.py)

<details>
<summary><code>def activate_anomaly_detection(body: AnomalyDetectionRequest | AnomalyDetectionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IntelligenceSuccessResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the subscribed account ID to activate anomaly detection and set threshold values.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_settings.with_raw_response.activate_anomaly_detection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IntelligenceSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_settings.with_raw_response.activate_anomaly_detection(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IntelligenceSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AnomalyDetectionRequest](verizon/models/anomaly_detection_request.py) \| [AnomalyDetectionRequestDict](verizon/models/anomaly_detection_request.py)</code> | Request to activate anomaly detection. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py)</code> -- Success response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_settings(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnomalyDetectionSettings, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the current anomaly detection settings for an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_settings.with_raw_response.list_anomaly_detection_settings(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionSettings
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_settings.with_raw_response.list_anomaly_detection_settings(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionSettings
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The name of the subscribed account. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AnomalyDetectionSettings](verizon/models/anomaly_detection_settings.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnomalyDetectionSettings](verizon/models/anomaly_detection_settings.py)</code> -- Retrieve the settings for anomaly detection.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reset_anomaly_detection_parameters(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IntelligenceSuccessResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Resets the thresholds to zero.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_settings.with_raw_response.reset_anomaly_detection_parameters(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IntelligenceSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_settings.with_raw_response.reset_anomaly_detection_parameters(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IntelligenceSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The name of the subscribed account. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py)</code> -- Success response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AnomalyTriggers

> Source: [AnomalyTriggers](verizon/apis/anomaly_triggers.py)

<details>
<summary><code>def create_anomaly_detection_trigger(body: CreateTriggerRequest | CreateTriggerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnomalyDetectionTrigger, CreateAnomalyDetectionTriggerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This corresponds to the M2M-MC SOAP interface, ``CreateTrigger``.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers.with_raw_response.create_anomaly_detection_trigger(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAnomalyDetectionTriggerErrorBody
```

**Async**

```python
result = await async_client.anomaly_triggers.with_raw_response.create_anomaly_detection_trigger(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAnomalyDetectionTriggerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTriggerRequest](verizon/models/create_trigger_request.py) \| [CreateTriggerRequestDict](verizon/models/create_trigger_request.py)</code> | Create Trigger Request |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py), [CreateAnomalyDetectionTriggerErrorBody](verizon/errors/create_anomaly_detection_trigger_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- Trigger ID

**On `Failure`**: `error` is <code>[CreateAnomalyDetectionTriggerErrorBody](verizon/errors/create_anomaly_detection_trigger_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[IntelligenceResult](verizon/models/intelligence_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_anomaly_detection_trigger(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnomalyDetectionTrigger, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a specific trigger ID

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers.with_raw_response.delete_anomaly_detection_trigger(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_triggers.with_raw_response.delete_anomaly_detection_trigger(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | The trigger ID to be deleted |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- The ID of the deleted trigger is returned

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_trigger_settings(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggerSettingsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This corresponds to the M2M-MC SOAP interface, ``GetTriggers``.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers.with_raw_response.list_anomaly_detection_trigger_settings(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GetTriggerResponseList]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAnomalyDetectionTriggerSettingsErrorBody
```

**Async**

```python
result = await async_client.anomaly_triggers.with_raw_response.list_anomaly_detection_trigger_settings(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GetTriggerResponseList]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAnomalyDetectionTriggerSettingsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | trigger ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[GetTriggerResponseList](verizon/models/get_trigger_response_list.py)&#93;, [ListAnomalyDetectionTriggerSettingsErrorBody](verizon/errors/list_anomaly_detection_trigger_settings_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GetTriggerResponseList](verizon/models/get_trigger_response_list.py)&#93;</code> -- Trigger information associated to a Trigger Id

**On `Failure`**: `error` is <code>[ListAnomalyDetectionTriggerSettingsErrorBody](verizon/errors/list_anomaly_detection_trigger_settings_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[IntelligenceResult](verizon/models/intelligence_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_triggers(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[GetTriggerResponseList], ListAnomalyDetectionTriggersErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This corresponds to the M2M-MC SOAP interface, ``GetTriggers``.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers.with_raw_response.list_anomaly_detection_triggers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GetTriggerResponseList]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAnomalyDetectionTriggersErrorBody
```

**Async**

```python
result = await async_client.anomaly_triggers.with_raw_response.list_anomaly_detection_triggers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[GetTriggerResponseList]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAnomalyDetectionTriggersErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[GetTriggerResponseList](verizon/models/get_trigger_response_list.py)&#93;, [ListAnomalyDetectionTriggersErrorBody](verizon/errors/list_anomaly_detection_triggers_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[GetTriggerResponseList](verizon/models/get_trigger_response_list.py)&#93;</code> -- List of triggers associated to a Contact

**On `Failure`**: `error` is <code>[ListAnomalyDetectionTriggersErrorBody](verizon/errors/list_anomaly_detection_triggers_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[IntelligenceResult](verizon/models/intelligence_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_anomaly_detection_trigger(body: UpdateTriggerRequest | UpdateTriggerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnomalyDetectionTrigger, UpdateAnomalyDetectionTriggerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This corresponds to the M2M-MC SOAP interface, ``UpdateTriggerRequest``.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers.with_raw_response.update_anomaly_detection_trigger(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateAnomalyDetectionTriggerErrorBody
```

**Async**

```python
result = await async_client.anomaly_triggers.with_raw_response.update_anomaly_detection_trigger(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateAnomalyDetectionTriggerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpdateTriggerRequest](verizon/models/update_trigger_request.py) \| [UpdateTriggerRequestDict](verizon/models/update_trigger_request.py)</code> | Update Trigger Request |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py), [UpdateAnomalyDetectionTriggerErrorBody](verizon/errors/update_anomaly_detection_trigger_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- Trigger ID

**On `Failure`**: `error` is <code>[UpdateAnomalyDetectionTriggerErrorBody](verizon/errors/update_anomaly_detection_trigger_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[IntelligenceResult](verizon/models/intelligence_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## AnomalyTriggersV2

> Source: [AnomalyTriggersV2](verizon/apis/anomaly_triggers_v2.py)

<details>
<summary><code>def create_anomaly_detection_trigger_v2(body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnomalyDetectionTrigger, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates the trigger to identify an anomaly.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers_v2.with_raw_response.create_anomaly_detection_trigger_v2(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_triggers_v2.with_raw_response.create_anomaly_detection_trigger_v2(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyDetectionTrigger
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>list&#91;[CreateTriggerRequestOptions](verizon/models/unions/create_trigger_request_options.py) \| [CreateTriggerRequestOptionsDict](verizon/models/unions/create_trigger_request_options.py)&#93;</code> | Request to create an anomaly trigger. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- Result of request to create a trigger for anomaly detection.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_trigger_settings_v2(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AnomalyTriggerResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the values for a specific trigger ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers_v2.with_raw_response.list_anomaly_detection_trigger_settings_v2(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyTriggerResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_triggers_v2.with_raw_response.list_anomaly_detection_trigger_settings_v2(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AnomalyTriggerResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | The trigger ID of a specific trigger. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AnomalyTriggerResult](verizon/models/anomaly_trigger_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AnomalyTriggerResult](verizon/models/anomaly_trigger_result.py)</code> -- Anomaly detection trigger details.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_anomaly_detection_trigger_v2(body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict], *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[IntelligenceSuccessResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing trigger using the account name.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.anomaly_triggers_v2.with_raw_response.update_anomaly_detection_trigger_v2(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IntelligenceSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.anomaly_triggers_v2.with_raw_response.update_anomaly_detection_trigger_v2(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type IntelligenceSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>list&#91;[UpdateTriggerRequestOptions](verizon/models/unions/update_trigger_request_options.py) \| [UpdateTriggerRequestOptionsDict](verizon/models/unions/update_trigger_request_options.py)&#93;</code> | Request to update existing trigger. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py)</code> -- Success response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Billing

> Source: [Billing](verizon/apis/billing.py)

<details>
<summary><code>def add_account(body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ManagedAccountsAddResponse, AddAccountErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to add managed accounts to a primary account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.add_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountsAddResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddAccountErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.add_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountsAddResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ManagedAccountsAddRequest](verizon/models/managed_accounts_add_request.py) \| [ManagedAccountsAddRequestDict](verizon/models/managed_accounts_add_request.py)</code> | Service name and list of accounts to add |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ManagedAccountsAddResponse](verizon/models/managed_accounts_add_response.py), [AddAccountErrorBody](verizon/errors/add_account_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ManagedAccountsAddResponse](verizon/models/managed_accounts_add_response.py)</code> -- Add managed accounts response

**On `Failure`**: `error` is <code>[AddAccountErrorBody](verizon/errors/add_account_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_managed_account_action(body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ManagedAccountCancelResponse, CancelManagedAccountActionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deactivates a managed billing service relationship between a managed account and the primary account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.cancel_managed_account_action(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelManagedAccountActionErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.cancel_managed_account_action(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountCancelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelManagedAccountActionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ManagedAccountCancelRequest](verizon/models/managed_account_cancel_request.py) \| [ManagedAccountCancelRequestDict](verizon/models/managed_account_cancel_request.py)</code> | Service name and list of accounts to add |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ManagedAccountCancelResponse](verizon/models/managed_account_cancel_response.py), [CancelManagedAccountActionErrorBody](verizon/errors/cancel_managed_account_action_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ManagedAccountCancelResponse](verizon/models/managed_account_cancel_response.py)</code> -- Managed account cancel response

**On `Failure`**: `error` is <code>[CancelManagedAccountActionErrorBody](verizon/errors/cancel_managed_account_action_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_managed_account(account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ManagedAccountsGetAllResponse, ListManagedAccountErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to retrieve the list of all accounts managed by a primary account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.list_managed_account(account_name, service_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountsGetAllResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListManagedAccountErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.list_managed_account(account_name, service_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountsGetAllResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListManagedAccountErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Primary account identifier |
| <code>service_name</code> | <code>str</code> | Service name |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ManagedAccountsGetAllResponse](verizon/models/managed_accounts_get_all_response.py), [ListManagedAccountErrorBody](verizon/errors/list_managed_account_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ManagedAccountsGetAllResponse](verizon/models/managed_accounts_get_all_response.py)</code> -- List of managed accounts

**On `Failure`**: `error` is <code>[ListManagedAccountErrorBody](verizon/errors/list_managed_account_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def managed_account_action(body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ManagedAccountsProvisionResponse, ManagedAccountActionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activates a managed billing service relationship between a managed account and the primary account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.billing.with_raw_response.managed_account_action(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountsProvisionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ManagedAccountActionErrorBody
```

**Async**

```python
result = await async_client.billing.with_raw_response.managed_account_action(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ManagedAccountsProvisionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ManagedAccountActionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ManagedAccountsProvisionRequest](verizon/models/managed_accounts_provision_request.py) \| [ManagedAccountsProvisionRequestDict](verizon/models/managed_accounts_provision_request.py)</code> | Service name and list of accounts to add |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ManagedAccountsProvisionResponse](verizon/models/managed_accounts_provision_response.py), [ManagedAccountActionErrorBody](verizon/errors/managed_account_action_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ManagedAccountsProvisionResponse](verizon/models/managed_accounts_provision_response.py)</code> -- Managed account provision response

**On `Failure`**: `error` is <code>[ManagedAccountActionErrorBody](verizon/errors/managed_account_action_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CampaignsV2

> Source: [CampaignsV2](verizon/apis/campaigns_v2.py)

<details>
<summary><code>def cancel_campaign(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV2SuccessResult, CancelCampaignErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to cancel software upgrade. A software upgrade already started can not be cancelled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.cancel_campaign(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelCampaignErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.cancel_campaign(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelCampaignErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Unique identifier of campaign. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py), [CancelCampaignErrorBody](verizon/errors/cancel_campaign_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py)</code> -- Return cancellation status.

**On `Failure`**: `error` is <code>[CancelCampaignErrorBody](verizon/errors/cancel_campaign_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_campaign_information(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CampaignSoftware, GetCampaignInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to get information of a software upgrade.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.get_campaign_information(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignSoftware
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignInformationErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.get_campaign_information(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignSoftware
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Software upgrade identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CampaignSoftware](verizon/models/campaign_software.py), [GetCampaignInformationErrorBody](verizon/errors/get_campaign_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CampaignSoftware](verizon/models/campaign_software.py)</code> -- Return software upgrade information.

**On `Failure`**: `error` is <code>[GetCampaignInformationErrorBody](verizon/errors/get_campaign_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_campaign_firmware_upgrade(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CampaignSoftware, ScheduleCampaignFirmwareUpgradeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to schedule a software upgrade.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.schedule_campaign_firmware_upgrade(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignSoftware
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleCampaignFirmwareUpgradeErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.schedule_campaign_firmware_upgrade(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignSoftware
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleCampaignFirmwareUpgradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CampaignSoftware](verizon/models/campaign_software.py), [ScheduleCampaignFirmwareUpgradeErrorBody](verizon/errors/schedule_campaign_firmware_upgrade_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CampaignSoftware](verizon/models/campaign_software.py)</code> -- Return software upgrade information.

**On `Failure`**: `error` is <code>[ScheduleCampaignFirmwareUpgradeErrorBody](verizon/errors/schedule_campaign_firmware_upgrade_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_file_upgrade(acc: str, body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UploadAndScheduleFileResponse, ScheduleFileUpgradeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can upload configuration files and schedule them in a campaign to devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.schedule_file_upgrade(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UploadAndScheduleFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleFileUpgradeErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.schedule_file_upgrade(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UploadAndScheduleFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleFileUpgradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[UploadAndScheduleFileRequest](verizon/models/upload_and_schedule_file_request.py) \| [UploadAndScheduleFileRequestDict](verizon/models/upload_and_schedule_file_request.py)</code> | Device logging information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UploadAndScheduleFileResponse](verizon/models/upload_and_schedule_file_response.py), [ScheduleFileUpgradeErrorBody](verizon/errors/schedule_file_upgrade_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UploadAndScheduleFileResponse](verizon/models/upload_and_schedule_file_response.py)</code> -- Successful responses.

**On `Failure`**: `error` is <code>[ScheduleFileUpgradeErrorBody](verizon/errors/schedule_file_upgrade_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_sw_upgrade_http_devices(acc: str, body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UploadAndScheduleFileResponse, ScheduleSwupgradeHttpDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Campaign time windows for downloading and installing software are available as long as the device OEM supports this.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.schedule_sw_upgrade_http_devices(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UploadAndScheduleFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleSwupgradeHttpDevicesErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.schedule_sw_upgrade_http_devices(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UploadAndScheduleFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleSwupgradeHttpDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[SchedulesSoftwareUpgradeRequest](verizon/models/schedules_software_upgrade_request.py) \| [SchedulesSoftwareUpgradeRequestDict](verizon/models/schedules_software_upgrade_request.py)</code> | Device logging information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UploadAndScheduleFileResponse](verizon/models/upload_and_schedule_file_response.py), [ScheduleSwupgradeHttpDevicesErrorBody](verizon/errors/schedule_swupgrade_http_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UploadAndScheduleFileResponse](verizon/models/upload_and_schedule_file_response.py)</code> -- Successful responses.

**On `Failure`**: `error` is <code>[ScheduleSwupgradeHttpDevicesErrorBody](verizon/errors/schedule_swupgrade_http_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_campaign_dates(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CampaignSoftware, UpdateCampaignDatesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged should be also provided.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.update_campaign_dates(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignSoftware
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignDatesErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.update_campaign_dates(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CampaignSoftware
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignDatesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Software upgrade information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CampaignSoftware](verizon/models/campaign_software.py), [UpdateCampaignDatesErrorBody](verizon/errors/update_campaign_dates_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CampaignSoftware](verizon/models/campaign_software.py)</code> -- Updated campaign information.

**On `Failure`**: `error` is <code>[UpdateCampaignDatesErrorBody](verizon/errors/update_campaign_dates_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_campaign_firmware_devices(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to Add or Remove devices to an existing software upgrade.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v2.with_raw_response.update_campaign_firmware_devices(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2AddOrRemoveDeviceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignFirmwareDevicesErrorBody
```

**Async**

```python
result = await async_client.campaigns_v2.with_raw_response.update_campaign_firmware_devices(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2AddOrRemoveDeviceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignFirmwareDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Software upgrade information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2AddOrRemoveDeviceResult](verizon/models/v2_add_or_remove_device_result.py), [UpdateCampaignFirmwareDevicesErrorBody](verizon/errors/update_campaign_firmware_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2AddOrRemoveDeviceResult](verizon/models/v2_add_or_remove_device_result.py)</code> -- Result of adding or removing devices to existing software upgrade information.

**On `Failure`**: `error` is <code>[UpdateCampaignFirmwareDevicesErrorBody](verizon/errors/update_campaign_firmware_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CampaignsV3

> Source: [CampaignsV3](verizon/apis/campaigns_v3.py)

<details>
<summary><code>def cancel_campaign2(account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV3SuccessResult, CancelCampaign2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to cancel a firmware campaign. A firmware campaign already started can not be cancelled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v3.with_raw_response.cancel_campaign2(account_name, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelCampaign2ErrorBody
```

**Async**

```python
result = await async_client.campaigns_v3.with_raw_response.cancel_campaign2(account_name, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelCampaign2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Firmware upgrade information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV3SuccessResult](verizon/models/fota_v3_success_result.py), [CancelCampaign2ErrorBody](verizon/errors/cancel_campaign2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV3SuccessResult](verizon/models/fota_v3_success_result.py)</code> -- Returns cancellation status.

**On `Failure`**: `error` is <code>[CancelCampaign2ErrorBody](verizon/errors/cancel_campaign2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_campaign_information2(account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Campaign, GetCampaignInformation2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to retrieve campaign level information for a specified campaign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v3.with_raw_response.get_campaign_information2(account_name, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Campaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignInformation2ErrorBody
```

**Async**

```python
result = await async_client.campaigns_v3.with_raw_response.get_campaign_information2(account_name, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Campaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignInformation2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Firmware upgrade identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Campaign](verizon/models/campaign.py), [GetCampaignInformation2ErrorBody](verizon/errors/get_campaign_information2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[Campaign](verizon/models/campaign.py)</code> -- Returns firmware upgrade information.

**On `Failure`**: `error` is <code>[GetCampaignInformation2ErrorBody](verizon/errors/get_campaign_information2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_campaign_firmware_upgrade2(account_name: str, body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FirmwareCampaign, ScheduleCampaignFirmwareUpgrade2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows a user to schedule a firmware upgrade for a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v3.with_raw_response.schedule_campaign_firmware_upgrade2(account_name, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareCampaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleCampaignFirmwareUpgrade2ErrorBody
```

**Async**

```python
result = await async_client.campaigns_v3.with_raw_response.schedule_campaign_firmware_upgrade2(account_name, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareCampaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleCampaignFirmwareUpgrade2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[CampaignFirmwareUpgrade](verizon/models/campaign_firmware_upgrade.py) \| [CampaignFirmwareUpgradeDict](verizon/models/campaign_firmware_upgrade.py)</code> | Firmware upgrade information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FirmwareCampaign](verizon/models/firmware_campaign.py), [ScheduleCampaignFirmwareUpgrade2ErrorBody](verizon/errors/schedule_campaign_firmware_upgrade2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FirmwareCampaign](verizon/models/firmware_campaign.py)</code> -- Return upgrade information.

**On `Failure`**: `error` is <code>[ScheduleCampaignFirmwareUpgrade2ErrorBody](verizon/errors/schedule_campaign_firmware_upgrade2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_campaign_dates2(acc: str, campaign_id: str, body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FirmwareCampaign, UpdateCampaignDates2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to change campaign dates and time windows. Fields which need to remain unchanged should be also provided.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v3.with_raw_response.update_campaign_dates2(acc, campaign_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareCampaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignDates2ErrorBody
```

**Async**

```python
result = await async_client.campaigns_v3.with_raw_response.update_campaign_dates2(acc, campaign_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareCampaign
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignDates2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Firmware upgrade information. |
| <code>body</code> | <code>[V3ChangeCampaignDatesRequest](verizon/models/v3_change_campaign_dates_request.py) \| [V3ChangeCampaignDatesRequestDict](verizon/models/v3_change_campaign_dates_request.py)</code> | New dates and time windows. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FirmwareCampaign](verizon/models/firmware_campaign.py), [UpdateCampaignDates2ErrorBody](verizon/errors/update_campaign_dates2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FirmwareCampaign](verizon/models/firmware_campaign.py)</code> -- Updated campaign information.

**On `Failure`**: `error` is <code>[UpdateCampaignDates2ErrorBody](verizon/errors/update_campaign_dates2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_campaign_firmware_devices2(acc: str, campaign_id: str, body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3AddOrRemoveDeviceResult, UpdateCampaignFirmwareDevices2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to Add or Remove devices to an existing campaign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.campaigns_v3.with_raw_response.update_campaign_firmware_devices2(acc, campaign_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3AddOrRemoveDeviceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignFirmwareDevices2ErrorBody
```

**Async**

```python
result = await async_client.campaigns_v3.with_raw_response.update_campaign_firmware_devices2(acc, campaign_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3AddOrRemoveDeviceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCampaignFirmwareDevices2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Unique identifier of a campaign. |
| <code>body</code> | <code>[V3AddOrRemoveDeviceRequest](verizon/models/v3_add_or_remove_device_request.py) \| [V3AddOrRemoveDeviceRequestDict](verizon/models/v3_add_or_remove_device_request.py)</code> | Add or remove device to existing upgrade information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3AddOrRemoveDeviceResult](verizon/models/v3_add_or_remove_device_result.py), [UpdateCampaignFirmwareDevices2ErrorBody](verizon/errors/update_campaign_firmware_devices2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3AddOrRemoveDeviceResult](verizon/models/v3_add_or_remove_device_result.py)</code> -- Returns add or remove devices to existing upgrade information.

**On `Failure`**: `error` is <code>[UpdateCampaignFirmwareDevices2ErrorBody](verizon/errors/update_campaign_firmware_devices2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ClientLogging

> Source: [ClientLogging](verizon/apis/client_logging.py)

<details>
<summary><code>def disable_device_logging(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DisableDeviceLoggingErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disables logging for a specific device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.client_logging.with_raw_response.disable_device_logging(account, device_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DisableDeviceLoggingErrorBody
```

**Async**

```python
result = await async_client.client_logging.with_raw_response.disable_device_logging(account, device_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DisableDeviceLoggingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device IMEI identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DisableDeviceLoggingErrorBody](verizon/errors/disable_device_logging_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DisableDeviceLoggingErrorBody](verizon/errors/disable_device_logging_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_logging_for_devices(account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DisableLoggingForDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Turn logging off for a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.client_logging.with_raw_response.disable_logging_for_devices(account, device_ids)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DisableLoggingForDevicesErrorBody
```

**Async**

```python
result = await async_client.client_logging.with_raw_response.disable_logging_for_devices(account, device_ids)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DisableLoggingForDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>device_ids</code> | <code>str</code> | The list of device IDs. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DisableLoggingForDevicesErrorBody](verizon/errors/disable_logging_for_devices_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DisableLoggingForDevicesErrorBody](verizon/errors/disable_logging_for_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_device_logging(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceLoggingStatus, EnableDeviceLoggingErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables logging for a specific device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.client_logging.with_raw_response.enable_device_logging(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLoggingStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EnableDeviceLoggingErrorBody
```

**Async**

```python
result = await async_client.client_logging.with_raw_response.enable_device_logging(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLoggingStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EnableDeviceLoggingErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device IMEI identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py), [EnableDeviceLoggingErrorBody](verizon/errors/enable_device_logging_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceLoggingStatus](verizon/models/device_logging_status.py)</code> -- Device logging status information.

**On `Failure`**: `error` is <code>[EnableDeviceLoggingErrorBody](verizon/errors/enable_device_logging_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_logging_for_devices(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceLoggingStatus], EnableLoggingForDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Each customer may have a maximum of 20 devices enabled for logging.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.client_logging.with_raw_response.enable_logging_for_devices(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLoggingStatus]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EnableLoggingForDevicesErrorBody
```

**Async**

```python
result = await async_client.client_logging.with_raw_response.enable_logging_for_devices(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLoggingStatus]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EnableLoggingForDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py)&#93;, [EnableLoggingForDevicesErrorBody](verizon/errors/enable_logging_for_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py)&#93;</code> -- List containing device logging status information.

**On `Failure`**: `error` is <code>[EnableLoggingForDevicesErrorBody](verizon/errors/enable_logging_for_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_device_logs(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceLog], ListDeviceLogsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets logs for a specific device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.client_logging.with_raw_response.list_device_logs(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLog]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDeviceLogsErrorBody
```

**Async**

```python
result = await async_client.client_logging.with_raw_response.list_device_logs(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLog]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDeviceLogsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device IMEI identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceLog](verizon/models/device_log.py)&#93;, [ListDeviceLogsErrorBody](verizon/errors/list_device_logs_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceLog](verizon/models/device_log.py)&#93;</code> -- List of device logs.

**On `Failure`**: `error` is <code>[ListDeviceLogsErrorBody](verizon/errors/list_device_logs_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_with_logging_enabled(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceLoggingStatus], ListDevicesWithLoggingEnabledErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an array of all devices in the specified account for which logging is enabled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.client_logging.with_raw_response.list_devices_with_logging_enabled(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLoggingStatus]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesWithLoggingEnabledErrorBody
```

**Async**

```python
result = await async_client.client_logging.with_raw_response.list_devices_with_logging_enabled(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLoggingStatus]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesWithLoggingEnabledErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py)&#93;, [ListDevicesWithLoggingEnabledErrorBody](verizon/errors/list_devices_with_logging_enabled_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py)&#93;</code> -- List containing device logging status information.

**On `Failure`**: `error` is <code>[ListDevicesWithLoggingEnabledErrorBody](verizon/errors/list_devices_with_logging_enabled_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CloudConnectorDevices

> Source: [CloudConnectorDevices](verizon/apis/cloud_connector_devices.py)

<details>
<summary><code>def delete_device_from_account(body: RemoveDeviceRequest | RemoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a device from a ThingSpace account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_devices.with_raw_response.delete_device_from_account(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_devices.with_raw_response.delete_device_from_account(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RemoveDeviceRequest](verizon/models/remove_device_request.py) \| [RemoveDeviceRequestDict](verizon/models/remove_device_request.py)</code> | The request body identifies the device to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_device_by_property_values(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FindDeviceByPropertyResponseList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Find devices by property values. Returns an array of all matching device resources.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_devices.with_raw_response.find_device_by_property_values(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FindDeviceByPropertyResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_devices.with_raw_response.find_device_by_property_values(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FindDeviceByPropertyResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[QuerySubscriptionRequest](verizon/models/query_subscription_request.py) \| [QuerySubscriptionRequestDict](verizon/models/query_subscription_request.py)</code> | The request body specifies fields and values to match. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FindDeviceByPropertyResponseList](verizon/models/find_device_by_property_response_list.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[FindDeviceByPropertyResponseList](verizon/models/find_device_by_property_response_list.py)</code> -- A success response includes an array of all matching devices. Each device includes the full device resource definition.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_device_event_history(body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchDeviceEventHistoryResponseList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search device event history to find events that match criteria.Sensor readings, configuration changes, and other device data are all stored as events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_devices.with_raw_response.search_device_event_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchDeviceEventHistoryResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_devices.with_raw_response.search_device_event_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchDeviceEventHistoryResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchDeviceEventHistoryRequest](verizon/models/search_device_event_history_request.py) \| [SearchDeviceEventHistoryRequestDict](verizon/models/search_device_event_history_request.py)</code> | The device identifier and fields to match in the search. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SearchDeviceEventHistoryResponseList](verizon/models/search_device_event_history_response_list.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchDeviceEventHistoryResponseList](verizon/models/search_device_event_history_response_list.py)</code> -- A success response includes an array of all matching devices.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_devices_resources_by_property_values(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchDeviceByPropertyResponseList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for devices by property values. Returns an array of all matching device resources.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_devices.with_raw_response.search_devices_resources_by_property_values(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchDeviceByPropertyResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_devices.with_raw_response.search_devices_resources_by_property_values(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchDeviceByPropertyResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[QuerySubscriptionRequest](verizon/models/query_subscription_request.py) \| [QuerySubscriptionRequestDict](verizon/models/query_subscription_request.py)</code> | The request body specifies fields and values to match. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SearchDeviceByPropertyResponseList](verizon/models/search_device_by_property_response_list.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchDeviceByPropertyResponseList](verizon/models/search_device_by_property_response_list.py)</code> -- A success response includes an array of all matching devices.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_sensor_readings(fieldname: str, body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchSensorHistoryResponseList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the readings of a specified sensor, with the most recent reading first. Sensor readings are stored as events; this request an array of events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_devices.with_raw_response.search_sensor_readings(fieldname, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchSensorHistoryResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_devices.with_raw_response.search_sensor_readings(fieldname, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchSensorHistoryResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>fieldname</code> | <code>str</code> | The name of the sensor. |
| <code>body</code> | <code>[SearchSensorHistoryRequest](verizon/models/search_sensor_history_request.py) \| [SearchSensorHistoryRequestDict](verizon/models/search_sensor_history_request.py)</code> | The device identifier and fields to match in the search. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SearchSensorHistoryResponseList](verizon/models/search_sensor_history_response_list.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchSensorHistoryResponseList](verizon/models/search_sensor_history_response_list.py)</code> -- A success response includes an array of all matching devices.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_devices_configuration_value(body: ChangeConfigurationRequest | ChangeConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChangeConfigurationResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Change configuration values on a device, such as setting how often a device records and reports sensor readings.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_devices.with_raw_response.update_devices_configuration_value(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangeConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_devices.with_raw_response.update_devices_configuration_value(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangeConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ChangeConfigurationRequest](verizon/models/change_configuration_request.py) \| [ChangeConfigurationRequestDict](verizon/models/change_configuration_request.py)</code> | The request body changes configuration values on a device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ChangeConfigurationResponse](verizon/models/change_configuration_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChangeConfigurationResponse](verizon/models/change_configuration_response.py)</code> -- A success response contains the ts.event.configuration event that was created to record the change.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CloudConnectorSubscriptions

> Source: [CloudConnectorSubscriptions](verizon/apis/cloud_connector_subscriptions.py)

<details>
<summary><code>def create_subscription(body: CreateSubscriptionRequest | CreateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Subscription, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a subscription to define a streaming channel that sends data from devices in the account to an endpoint defined in a target resource.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_subscriptions.with_raw_response.create_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Subscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_subscriptions.with_raw_response.create_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Subscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSubscriptionRequest](verizon/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](verizon/models/create_subscription_request.py)</code> | The request body provides the details of the subscription that you want to create. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Subscription](verizon/models/subscription.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Subscription](verizon/models/subscription.py)</code> -- Returns full subscription resource definition.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription(body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a subscription from a ThingSpace account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_subscriptions.with_raw_response.delete_subscription(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_subscriptions.with_raw_response.delete_subscription(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeleteSubscriptionRequest](verizon/models/delete_subscription_request.py) \| [DeleteSubscriptionRequestDict](verizon/models/delete_subscription_request.py)</code> | The request body identifies the subscription to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_subscription(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Subscription], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for subscriptions by property values. Returns an array of all matching subscription resources.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cloud_connector_subscriptions.with_raw_response.query_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Subscription]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cloud_connector_subscriptions.with_raw_response.query_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Subscription]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[QuerySubscriptionRequest](verizon/models/query_subscription_request.py) \| [QuerySubscriptionRequestDict](verizon/models/query_subscription_request.py)</code> | The request body specifies fields and values to match. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[Subscription](verizon/models/subscription.py)&#93;, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Subscription](verizon/models/subscription.py)&#93;</code> -- Returns an array of all matching subscriptions. Each subscription includes the full subscription resource definition.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ConfigurationFiles

> Source: [ConfigurationFiles](verizon/apis/configuration_files.py)

<details>
<summary><code>def get_list_of_files(acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrievesAvailableFilesResponseList, GetListOfFilesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You can retrieve a list of configuration or supplementary of files for an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.configuration_files.with_raw_response.get_list_of_files(acc, distribution_type)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrievesAvailableFilesResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListOfFilesErrorBody
```

**Async**

```python
result = await async_client.configuration_files.with_raw_response.get_list_of_files(acc, distribution_type)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrievesAvailableFilesResponseList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetListOfFilesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>distribution_type</code> | <code>str</code> | Filter the distributionType to only retrieve files for a specific distribution type. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RetrievesAvailableFilesResponseList](verizon/models/retrieves_available_files_response_list.py), [GetListOfFilesErrorBody](verizon/errors/get_list_of_files_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrievesAvailableFilesResponseList](verizon/models/retrieves_available_files_response_list.py)</code> -- Successful responses.

**On `Failure`**: `error` is <code>[GetListOfFilesErrorBody](verizon/errors/get_list_of_files_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upload_config_file(acc: str, *, file_version: str | None = None, make: str | None = None, model: str | None = None, local_target_path: str | None = None, fileupload: bytes | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UploadConfigurationFilesResponse, UploadConfigFileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads a configuration/supplementary file for an account. ThingSpace generates a fileName after the upload and is returned in the response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.configuration_files.with_raw_response.upload_config_file(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UploadConfigurationFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadConfigFileErrorBody
```

**Async**

```python
result = await async_client.configuration_files.with_raw_response.upload_config_file(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UploadConfigurationFilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadConfigFileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>file_version</code> | <code>str \| None</code> | Version of the file.<br>**Default**: <code>None</code> |
| <code>make</code> | <code>str \| None</code> | The software-applicable device make.<br>**Default**: <code>None</code> |
| <code>model</code> | <code>str \| None</code> | The software-applicable device model.<br>**Default**: <code>None</code> |
| <code>local_target_path</code> | <code>str \| None</code> | Local target path on the device.<br>**Default**: <code>None</code> |
| <code>fileupload</code> | <code>bytes \| None</code> | The file to upload.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UploadConfigurationFilesResponse](verizon/models/upload_configuration_files_response.py), [UploadConfigFileErrorBody](verizon/errors/upload_config_file_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UploadConfigurationFilesResponse](verizon/models/upload_configuration_files_response.py)</code> -- Successful responses.

**On `Failure`**: `error` is <code>[UploadConfigFileErrorBody](verizon/errors/upload_config_file_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ConnectivityCallbacks

> Source: [ConnectivityCallbacks](verizon/apis/connectivity_callbacks.py)

<details>
<summary><code>def deregister_callback(aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CallbackActionResult, DeregisterCallbackErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Stops ThingSpace from sending callback messages for the specified account and service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.connectivity_callbacks.with_raw_response.deregister_callback(aname, sname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackActionResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallbackErrorBody
```

**Async**

```python
result = await async_client.connectivity_callbacks.with_raw_response.deregister_callback(aname, sname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackActionResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>sname</code> | <code>str</code> | Service name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CallbackActionResult](verizon/models/callback_action_result.py), [DeregisterCallbackErrorBody](verizon/errors/deregister_callback_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CallbackActionResult](verizon/models/callback_action_result.py)</code> -- Response for a request to deregister a callback.

**On `Failure`**: `error` is <code>[DeregisterCallbackErrorBody](verizon/errors/deregister_callback_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_registered_callbacks(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ConnectivityManagementCallback], ListRegisteredCallbacksErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the name and endpoint URL of the callback listening services registered for a given account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.connectivity_callbacks.with_raw_response.list_registered_callbacks(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ConnectivityManagementCallback]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacksErrorBody
```

**Async**

```python
result = await async_client.connectivity_callbacks.with_raw_response.list_registered_callbacks(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ConnectivityManagementCallback]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacksErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ConnectivityManagementCallback](verizon/models/connectivity_management_callback.py)&#93;, [ListRegisteredCallbacksErrorBody](verizon/errors/list_registered_callbacks_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ConnectivityManagementCallback](verizon/models/connectivity_management_callback.py)&#93;</code> -- A list of callback listeners.

**On `Failure`**: `error` is <code>[ListRegisteredCallbacksErrorBody](verizon/errors/list_registered_callbacks_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_callback(aname: str, body: RegisterCallbackRequest | RegisterCallbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CallbackActionResult, RegisterCallbackErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

You are responsible for creating and running a listening process on your server at that URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.connectivity_callbacks.with_raw_response.register_callback(aname, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackActionResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallbackErrorBody
```

**Async**

```python
result = await async_client.connectivity_callbacks.with_raw_response.register_callback(aname, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackActionResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>body</code> | <code>[RegisterCallbackRequest](verizon/models/register_callback_request.py) \| [RegisterCallbackRequestDict](verizon/models/register_callback_request.py)</code> | Request to register a callback. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CallbackActionResult](verizon/models/callback_action_result.py), [RegisterCallbackErrorBody](verizon/errors/register_callback_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CallbackActionResult](verizon/models/callback_action_result.py)</code> -- A success response for registering a callback.

**On `Failure`**: `error` is <code>[RegisterCallbackErrorBody](verizon/errors/register_callback_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## CreatePricePlanTriggers

> Source: [CreatePricePlanTriggers](verizon/apis/create_price_plan_triggers.py)

<details>
<summary><code>def create_trigger_rules(body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TriggerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a usage trigger at the account level, device level or a price plan trigger for all devices on the account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.create_price_plan_triggers.with_raw_response.create_trigger_rules(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.create_price_plan_triggers.with_raw_response.create_trigger_rules(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V2TriggersRequest](verizon/models/unions/v2_triggers_request.py) \| [V2TriggersRequestDict](verizon/models/unions/v2_triggers_request.py)</code> | Create a trigger |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TriggerResponse](verizon/models/trigger_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TriggerResponse](verizon/models/trigger_response.py)</code> -- Successful request

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceActions

> Source: [DeviceActions](verizon/apis/device_actions.py)

<details>
<summary><code>def account_information(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountDetails, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve all of the service plans, features and carriers associated with the account specified.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.account_information(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.account_information(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AccountDetails](verizon/models/account_details.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountDetails](verizon/models/account_details.py)</code> -- Account details **Note:** The response will have placeholders. You can identify the placeholders by `"sizeKb":0` and that the record will only have `name` and `sizeKb` values.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def aggregate_usage(body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the aggregate usage for a device or a number of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.aggregate_usage(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.aggregate_usage(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AggregateUsage](verizon/models/aggregate_usage.py) \| [AggregateUsageDict](verizon/models/aggregate_usage.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def daily_usage(body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DailyUsageResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the daily usage for a device, for a specified period of time, segmented by day

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.daily_usage(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DailyUsageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.daily_usage(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DailyUsageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DailyUsage](verizon/models/daily_usage.py) \| [DailyUsageDict](verizon/models/daily_usage.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DailyUsageResponse](verizon/models/daily_usage_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DailyUsageResponse](verizon/models/daily_usage_response.py)</code> -- Syncronous response of device usage

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_asynchronous_request_status(account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StatusResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the status of an asynchronous request made with the Device Actions.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.get_asynchronous_request_status(account_name, request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.get_asynchronous_request_status(account_name, request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Value sent with the request. |
| <code>request_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[StatusResponse](verizon/models/status_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StatusResponse](verizon/models/status_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_device_provisioning_history(body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the provisioning history of a specific device or devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.retrieve_device_provisioning_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.retrieve_device_provisioning_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProvhistoryRequest](verizon/models/provhistory_request.py) \| [ProvhistoryRequestDict](verizon/models/provhistory_request.py)</code> | Device Provisioning History |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_the_global_device_list(body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows the profile to fetch the complete device list. This works with Verizon US and Global profiles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.retrieve_the_global_device_list(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.retrieve_the_global_device_list(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetDeviceListWithProfilesRequest](verizon/models/get_device_list_with_profiles_request.py) \| [GetDeviceListWithProfilesRequestDict](verizon/models/get_device_list_with_profiles_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_plan_list(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountDetails, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve all of the service plans, features and carriers associated with the account specified.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_actions.with_raw_response.service_plan_list(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_actions.with_raw_response.service_plan_list(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountDetails
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AccountDetails](verizon/models/account_details.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountDetails](verizon/models/account_details.py)</code> -- Account details **Note:** The response will have placeholders. You can identify the placeholders by `"sizeKb":0` and that the record will only have `name` and `sizeKb` values.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceCredentialManagement

> Source: [DeviceCredentialManagement](verizon/apis/device_credential_management.py)

<details>
<summary><code>def drop_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DropResponse, DropCredentialsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_credential_management.with_raw_response.drop_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DropResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DropCredentialsErrorBody
```

**Async**

```python
result = await async_client.device_credential_management.with_raw_response.drop_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DropResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DropCredentialsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CredentialsRequest](verizon/models/credentials_request.py) \| [CredentialsRequestDict](verizon/models/credentials_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DropResponse](verizon/models/drop_response.py), [DropCredentialsErrorBody](verizon/errors/drop_credentials_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DropResponse](verizon/models/drop_response.py)</code> -- Credentials dropped successfully

**On `Failure`**: `error` is <code>[DropCredentialsErrorBody](verizon/errors/drop_credentials_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](verizon/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateResponse, GenerateCredentialsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_credential_management.with_raw_response.generate_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateCredentialsErrorBody
```

**Async**

```python
result = await async_client.device_credential_management.with_raw_response.generate_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GenerateCredentialsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CredentialsRequest](verizon/models/credentials_request.py) \| [CredentialsRequestDict](verizon/models/credentials_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GenerateResponse](verizon/models/generate_response.py), [GenerateCredentialsErrorBody](verizon/errors/generate_credentials_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateResponse](verizon/models/generate_response.py)</code> -- Credentials generated successfully

**On `Failure`**: `error` is <code>[GenerateCredentialsErrorBody](verizon/errors/generate_credentials_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](verizon/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reset_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateResponse, ResetCredentialsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_credential_management.with_raw_response.reset_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ResetCredentialsErrorBody
```

**Async**

```python
result = await async_client.device_credential_management.with_raw_response.reset_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ResetCredentialsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CredentialsRequest](verizon/models/credentials_request.py) \| [CredentialsRequestDict](verizon/models/credentials_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GenerateResponse](verizon/models/generate_response.py), [ResetCredentialsErrorBody](verizon/errors/reset_credentials_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateResponse](verizon/models/generate_response.py)</code> -- Credentials reset successfully

**On `Failure`**: `error` is <code>[ResetCredentialsErrorBody](verizon/errors/reset_credentials_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](verizon/models/error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveResponse, RetrieveCredentialsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_credential_management.with_raw_response.retrieve_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveCredentialsErrorBody
```

**Async**

```python
result = await async_client.device_credential_management.with_raw_response.retrieve_credentials(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveCredentialsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CredentialsRequest](verizon/models/credentials_request.py) \| [CredentialsRequestDict](verizon/models/credentials_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RetrieveResponse](verizon/models/retrieve_response.py), [RetrieveCredentialsErrorBody](verizon/errors/retrieve_credentials_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveResponse](verizon/models/retrieve_response.py)</code> -- Successful retrieval

**On `Failure`**: `error` is <code>[RetrieveCredentialsErrorBody](verizon/errors/retrieve_credentials_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ErrorResponse](verizon/models/error_response.py)</code> |
| 401 | <code>[RawError](verizon/core/results.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceDiagnostics

> Source: [DeviceDiagnostics](verizon/apis/device_diagnostics.py)

<details>
<summary><code>def device_reachability_status_using_post(body: NotificationReportStatusRequest | NotificationReportStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, DeviceReachabilityStatusUsingPostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

If the devices do not already exist in the account, this API resource adds them before activation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_diagnostics.with_raw_response.device_reachability_status_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceReachabilityStatusUsingPostErrorBody
```

**Async**

```python
result = await async_client.device_diagnostics.with_raw_response.device_reachability_status_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceReachabilityStatusUsingPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[NotificationReportStatusRequest](verizon/models/notification_report_status_request.py) \| [NotificationReportStatusRequestDict](verizon/models/notification_report_status_request.py)</code> | Retrieve Reachability Report Status for a device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [DeviceReachabilityStatusUsingPostErrorBody](verizon/errors/device_reachability_status_using_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[DeviceReachabilityStatusUsingPostErrorBody](verizon/errors/device_reachability_status_using_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_active_monitors_using_post(body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, RetrieveActiveMonitorsUsingPostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve all the active monitors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_diagnostics.with_raw_response.retrieve_active_monitors_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveActiveMonitorsUsingPostErrorBody
```

**Async**

```python
result = await async_client.device_diagnostics.with_raw_response.retrieve_active_monitors_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveActiveMonitorsUsingPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RetrieveMonitorsRequest](verizon/models/retrieve_monitors_request.py) \| [RetrieveMonitorsRequestDict](verizon/models/retrieve_monitors_request.py)</code> | Retrieve Monitor Request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [RetrieveActiveMonitorsUsingPostErrorBody](verizon/errors/retrieve_active_monitors_using_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[RetrieveActiveMonitorsUsingPostErrorBody](verizon/errors/retrieve_active_monitors_using_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceGroups

> Source: [DeviceGroups](verizon/apis/device_groups.py)

<details>
<summary><code>def create_device_group(body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectivityManagementSuccessResult, CreateDeviceGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new device group and optionally add devices to the group. Device groups can make it easier to manage similar devices and to get reports on their usage.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_groups.with_raw_response.create_device_group(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateDeviceGroupErrorBody
```

**Async**

```python
result = await async_client.device_groups.with_raw_response.create_device_group(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateDeviceGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateDeviceGroupRequest](verizon/models/create_device_group_request.py) \| [CreateDeviceGroupRequestDict](verizon/models/create_device_group_request.py)</code> | A request to create a new device group. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py), [CreateDeviceGroupErrorBody](verizon/errors/create_device_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response, Creates a new device group.

**On `Failure`**: `error` is <code>[CreateDeviceGroupErrorBody](verizon/errors/create_device_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_device_group(aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectivityManagementSuccessResult, DeleteDeviceGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a device group from the account. Devices in the group are moved to the default device group and are not deleted from the account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_groups.with_raw_response.delete_device_group(aname, gname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteDeviceGroupErrorBody
```

**Async**

```python
result = await async_client.device_groups.with_raw_response.delete_device_group(aname, gname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteDeviceGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>gname</code> | <code>str</code> | Group name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py), [DeleteDeviceGroupErrorBody](verizon/errors/delete_device_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[DeleteDeviceGroupErrorBody](verizon/errors/delete_device_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device_group_information(aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceGroupDevicesData, GetDeviceGroupInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

When HTTP status is 202, a URL will be returned in the Location header of the form /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_groups.with_raw_response.get_device_group_information(aname, gname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceGroupDevicesData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceGroupInformationErrorBody
```

**Async**

```python
result = await async_client.device_groups.with_raw_response.get_device_group_information(aname, gname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceGroupDevicesData
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceGroupInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>gname</code> | <code>str</code> | Group name. |
| <code>next</code> | <code>int \| None</code> | Continue the previous query from the pageUrl pagetoken.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceGroupDevicesData](verizon/models/device_group_devices_data.py), [GetDeviceGroupInformationErrorBody](verizon/errors/get_device_group_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceGroupDevicesData](verizon/models/device_group_devices_data.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[GetDeviceGroupInformationErrorBody](verizon/errors/get_device_group_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_device_groups(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceGroup], ListDeviceGroupsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all device groups in a specified account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_groups.with_raw_response.list_device_groups(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceGroup]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDeviceGroupsErrorBody
```

**Async**

```python
result = await async_client.device_groups.with_raw_response.list_device_groups(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceGroup]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDeviceGroupsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceGroup](verizon/models/device_group.py)&#93;, [ListDeviceGroupsErrorBody](verizon/errors/list_device_groups_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceGroup](verizon/models/device_group.py)&#93;</code> -- The list of device groups in the account.

**On `Failure`**: `error` is <code>[ListDeviceGroupsErrorBody](verizon/errors/list_device_groups_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_device_group(aname: str, gname: str, body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectivityManagementSuccessResult, UpdateDeviceGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Make changes to a device group, including changing the name and description, and adding or removing devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_groups.with_raw_response.update_device_group(aname, gname, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDeviceGroupErrorBody
```

**Async**

```python
result = await async_client.device_groups.with_raw_response.update_device_group(aname, gname, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDeviceGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>gname</code> | <code>str</code> | Group name. |
| <code>body</code> | <code>[DeviceGroupUpdateRequest](verizon/models/device_group_update_request.py) \| [DeviceGroupUpdateRequestDict](verizon/models/device_group_update_request.py)</code> | Request to update device group. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py), [UpdateDeviceGroupErrorBody](verizon/errors/update_device_group_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UpdateDeviceGroupErrorBody](verizon/errors/update_device_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceLocationCallbacks

> Source: [DeviceLocationCallbacks](verizon/apis/device_location_callbacks.py)

<details>
<summary><code>def cancel_async_report(txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionId, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel an asynchronous report request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_location_callbacks.with_raw_response.cancel_async_report(txid, account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_location_callbacks.with_raw_response.cancel_async_report(txid, account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>txid</code> | <code>str</code> | The `transactionId` value. |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TransactionId](verizon/models/transaction_id.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionId](verizon/models/transaction_id.py)</code> -- Request canceled.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deregister_callback2(account_name: str, service: CallbackServiceNameOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceLocationSuccessResult, DeregisterCallback2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deregister a URL to stop receiving callback messages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_location_callbacks.with_raw_response.deregister_callback2(account_name, service)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback2ErrorBody
```

**Async**

```python
result = await async_client.device_location_callbacks.with_raw_response.deregister_callback2(account_name, service)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account number. |
| <code>service</code> | <code>[CallbackServiceNameOrStr](verizon/models/enums/callback_service_name.py)</code> | Callback service name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py), [DeregisterCallback2ErrorBody](verizon/errors/deregister_callback2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Deregistration successful.

**On `Failure`**: `error` is <code>[DeregisterCallback2ErrorBody](verizon/errors/deregister_callback2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_registered_callbacks2(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceLocationCallback], ListRegisteredCallbacks2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all registered callback URLs for the account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_location_callbacks.with_raw_response.list_registered_callbacks2(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLocationCallback]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks2ErrorBody
```

**Async**

```python
result = await async_client.device_location_callbacks.with_raw_response.list_registered_callbacks2(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceLocationCallback]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceLocationCallback](verizon/models/device_location_callback.py)&#93;, [ListRegisteredCallbacks2ErrorBody](verizon/errors/list_registered_callbacks2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceLocationCallback](verizon/models/device_location_callback.py)&#93;</code> -- List of all registered callback URLs.

**On `Failure`**: `error` is <code>[ListRegisteredCallbacks2ErrorBody](verizon/errors/list_registered_callbacks2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_callback2(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CallbackRegistrationResult, RegisterCallback2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provide a URL to receive messages from a ThingSpace callback service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_location_callbacks.with_raw_response.register_callback2(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback2ErrorBody
```

**Async**

```python
result = await async_client.device_location_callbacks.with_raw_response.register_callback2(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account number. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CallbackRegistrationResult](verizon/models/callback_registration_result.py), [RegisterCallback2ErrorBody](verizon/errors/register_callback2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CallbackRegistrationResult](verizon/models/callback_registration_result.py)</code> -- Callback registration response.

**On `Failure`**: `error` is <code>[RegisterCallback2ErrorBody](verizon/errors/register_callback2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceManagement

> Source: [DeviceManagement](verizon/apis/device_management.py)

<details>
<summary><code>def activate_service_for_devices(body: CarrierActivateRequest | CarrierActivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, ActivateServiceForDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

If the devices do not already exist in the account, this API resource adds them before activation.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.activate_service_for_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivateServiceForDevicesErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.activate_service_for_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivateServiceForDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CarrierActivateRequest](verizon/models/carrier_activate_request.py) \| [CarrierActivateRequestDict](verizon/models/carrier_activate_request.py)</code> | Request for activating a service on devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [ActivateServiceForDevicesErrorBody](verizon/errors/activate_service_for_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[ActivateServiceForDevicesErrorBody](verizon/errors/activate_service_for_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def add_devices(body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[AddDevicesResult], AddDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API if you want to manage some device settings before you are ready to activate service for the devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.add_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[AddDevicesResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddDevicesErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.add_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[AddDevicesResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AddDevicesRequest](verizon/models/add_devices_request.py) \| [AddDevicesRequestDict](verizon/models/add_devices_request.py)</code> | Devices to add. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[AddDevicesResult](verizon/models/add_devices_result.py)&#93;, [AddDevicesErrorBody](verizon/errors/add_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[AddDevicesResult](verizon/models/add_devices_result.py)&#93;</code> -- For each device in the request, contains device identifiers and a success or failure response.

**On `Failure`**: `error` is <code>[AddDevicesErrorBody](verizon/errors/add_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def billed_usage_info(body: BilledusageListRequest | BilledusageListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, BilledUsageInfoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets billed usage for for either multiple devices or an entire billing account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.billed_usage_info(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BilledUsageInfoErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.billed_usage_info(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type BilledUsageInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BilledusageListRequest](verizon/models/billedusage_list_request.py) \| [BilledusageListRequestDict](verizon/models/billedusage_list_request.py)</code> | Request to list devices with mismatched IMEIs and ICCIDs. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [BilledUsageInfoErrorBody](verizon/errors/billed_usage_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[BilledUsageInfoErrorBody](verizon/errors/billed_usage_info_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_devices_service_plan(body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, ChangeDevicesServicePlanErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes the service plan for one or more devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.change_devices_service_plan(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ChangeDevicesServicePlanErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.change_devices_service_plan(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ChangeDevicesServicePlanErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ServicePlanUpdateRequest](verizon/models/service_plan_update_request.py) \| [ServicePlanUpdateRequestDict](verizon/models/service_plan_update_request.py)</code> | Request to change device service plan. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [ChangeDevicesServicePlanErrorBody](verizon/errors/change_devices_service_plan_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[ChangeDevicesServicePlanErrorBody](verizon/errors/change_devices_service_plan_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def check_devices_availability_for_activation(body: DeviceActivationRequest | DeviceActivationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, CheckDevicesAvailabilityForActivationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Checks whether specified devices are registered by the manufacturer with the Verizon network and are available to be activated.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.check_devices_availability_for_activation(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CheckDevicesAvailabilityForActivationErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.check_devices_availability_for_activation(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CheckDevicesAvailabilityForActivationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceActivationRequest](verizon/models/device_activation_request.py) \| [DeviceActivationRequestDict](verizon/models/device_activation_request.py)</code> | Request to check if devices can be activated or not. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [CheckDevicesAvailabilityForActivationErrorBody](verizon/errors/check_devices_availability_for_activation_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[CheckDevicesAvailabilityForActivationErrorBody](verizon/errors/check_devices_availability_for_activation_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_service_for_devices(body: CarrierDeactivateRequest | CarrierDeactivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, DeactivateServiceForDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deactivating service for a device may result in an early termination fee (ETF) being charged to the account, depending on the terms of the contract with Verizon. If your contract allows ETF waivers and if you want to use one for a particular deactivation, set the etfWaiver value to True.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.deactivate_service_for_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeactivateServiceForDevicesErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.deactivate_service_for_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeactivateServiceForDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CarrierDeactivateRequest](verizon/models/carrier_deactivate_request.py) \| [CarrierDeactivateRequestDict](verizon/models/carrier_deactivate_request.py)</code> | Request to deactivate service for one or more devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [DeactivateServiceForDevicesErrorBody](verizon/errors/deactivate_service_for_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[DeactivateServiceForDevicesErrorBody](verizon/errors/deactivate_service_for_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_deactivated_devices(body: DeleteDevicesRequest | DeleteDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeleteDevicesResult], DeleteDeactivatedDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API to remove unneeded devices from an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.delete_deactivated_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeleteDevicesResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteDeactivatedDevicesErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.delete_deactivated_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeleteDevicesResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteDeactivatedDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeleteDevicesRequest](verizon/models/delete_devices_request.py) \| [DeleteDevicesRequestDict](verizon/models/delete_devices_request.py)</code> | Devices to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeleteDevicesResult](verizon/models/delete_devices_result.py)&#93;, [DeleteDeactivatedDevicesErrorBody](verizon/errors/delete_deactivated_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeleteDevicesResult](verizon/models/delete_devices_result.py)&#93;</code> -- For each device in the request, contains device identifiers and a success or failure response.

**On `Failure`**: `error` is <code>[DeleteDeactivatedDevicesErrorBody](verizon/errors/delete_deactivated_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def device_upload(body: DeviceUploadRequest | DeviceUploadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, DeviceUploadErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Upload a device record

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.device_upload(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceUploadErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.device_upload(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceUploadErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceUploadRequest](verizon/models/device_upload_request.py) \| [DeviceUploadRequestDict](verizon/models/device_upload_request.py)</code> | Device Upload Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [DeviceUploadErrorBody](verizon/errors/device_upload_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[DeviceUploadErrorBody](verizon/errors/device_upload_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def device_upload_status(body: CheckOrderStatusRequest | CheckOrderStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, DeviceUploadStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Checks the status of an activation order and lists where the order is in the provisioning process.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.device_upload_status(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceUploadStatusErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.device_upload_status(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceUploadStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CheckOrderStatusRequest](verizon/models/check_order_status_request.py) \| [CheckOrderStatusRequestDict](verizon/models/check_order_status_request.py)</code> | The request body identifies the device and reporting period that you want included in the report. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [DeviceUploadStatusErrorBody](verizon/errors/device_upload_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[DeviceUploadStatusErrorBody](verizon/errors/device_upload_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device_extended_diagnostic_information(body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceExtendedDiagnosticsResult, GetDeviceExtendedDiagnosticInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns extended diagnostic information about a specified device, including connectivity, provisioning, billing and location status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.get_device_extended_diagnostic_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceExtendedDiagnosticsResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceExtendedDiagnosticInformationErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.get_device_extended_diagnostic_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceExtendedDiagnosticsResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceExtendedDiagnosticInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceExtendedDiagnosticsRequest](verizon/models/device_extended_diagnostics_request.py) \| [DeviceExtendedDiagnosticsRequestDict](verizon/models/device_extended_diagnostics_request.py)</code> | Request to query extended diagnostics information for a device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceExtendedDiagnosticsResult](verizon/models/device_extended_diagnostics_result.py), [GetDeviceExtendedDiagnosticInformationErrorBody](verizon/errors/get_device_extended_diagnostic_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceExtendedDiagnosticsResult](verizon/models/device_extended_diagnostics_result.py)</code> -- Device diagnostic information.

**On `Failure`**: `error` is <code>[GetDeviceExtendedDiagnosticInformationErrorBody](verizon/errors/get_device_extended_diagnostic_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device_service_suspension_status(body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, GetDeviceServiceSuspensionStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns DeviceSuspensionStatus callback messages containing the current device state and information on how many days a device has been suspended and can continue to be suspended.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.get_device_service_suspension_status(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceServiceSuspensionStatusErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.get_device_service_suspension_status(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceServiceSuspensionStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceSuspensionStatusRequest](verizon/models/device_suspension_status_request.py) \| [DeviceSuspensionStatusRequestDict](verizon/models/device_suspension_status_request.py)</code> | Request to obtain service suspenstion status for a device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [GetDeviceServiceSuspensionStatusErrorBody](verizon/errors/get_device_service_suspension_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[GetDeviceServiceSuspensionStatusErrorBody](verizon/errors/get_device_service_suspension_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_current_devices_prl_version(body: DevicePrlListRequest | DevicePrlListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, ListCurrentDevicesPrlversionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

4G and GSM devices do not have a PRL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.list_current_devices_prl_version(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListCurrentDevicesPrlversionErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.list_current_devices_prl_version(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListCurrentDevicesPrlversionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DevicePrlListRequest](verizon/models/device_prl_list_request.py) \| [DevicePrlListRequestDict](verizon/models/device_prl_list_request.py)</code> | Request to query device PRL. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [ListCurrentDevicesPrlversionErrorBody](verizon/errors/list_current_devices_prlversion_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[ListCurrentDevicesPrlversionErrorBody](verizon/errors/list_current_devices_prlversion_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_information(body: AccountDeviceListRequest | AccountDeviceListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountDeviceListResult, ListDevicesInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about a single device or information about all devices that match the given parameters. Returned information includes device provisioning state, service plan, MDN, MIN, and IP address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.list_devices_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountDeviceListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesInformationErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.list_devices_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountDeviceListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountDeviceListRequest](verizon/models/account_device_list_request.py) \| [AccountDeviceListRequestDict](verizon/models/account_device_list_request.py)</code> | Device information query. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AccountDeviceListResult](verizon/models/account_device_list_result.py), [ListDevicesInformationErrorBody](verizon/errors/list_devices_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountDeviceListResult](verizon/models/account_device_list_result.py)</code> -- List of devices that match the request parameters, ordered by device creation date, oldest first.

**On `Failure`**: `error` is <code>[ListDevicesInformationErrorBody](verizon/errors/list_devices_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_provisioning_history(body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceProvisioningHistoryListResult], ListDevicesProvisioningHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the provisioning history of a specified device during a specified time period.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.list_devices_provisioning_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceProvisioningHistoryListResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesProvisioningHistoryErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.list_devices_provisioning_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceProvisioningHistoryListResult]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesProvisioningHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceProvisioningHistoryListRequest](verizon/models/device_provisioning_history_list_request.py) \| [DeviceProvisioningHistoryListRequestDict](verizon/models/device_provisioning_history_list_request.py)</code> | Query to obtain device provisioning history. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceProvisioningHistoryListResult](verizon/models/device_provisioning_history_list_result.py)&#93;, [ListDevicesProvisioningHistoryErrorBody](verizon/errors/list_devices_provisioning_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceProvisioningHistoryListResult](verizon/models/device_provisioning_history_list_result.py)&#93;</code> -- List of Device Provision History events, sorted by the timestamp, oldest first.

**On `Failure`**: `error` is <code>[ListDevicesProvisioningHistoryErrorBody](verizon/errors/list_devices_provisioning_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_usage_history(body: DeviceUsageListRequest | DeviceUsageListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceUsageListResult, ListDevicesUsageHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the network data usage history of a device during a specified time period.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.list_devices_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceUsageListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesUsageHistoryErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.list_devices_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceUsageListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesUsageHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceUsageListRequest](verizon/models/device_usage_list_request.py) \| [DeviceUsageListRequestDict](verizon/models/device_usage_list_request.py)</code> | Request to obtain usage history for a specific device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceUsageListResult](verizon/models/device_usage_list_result.py), [ListDevicesUsageHistoryErrorBody](verizon/errors/list_devices_usage_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceUsageListResult](verizon/models/device_usage_list_result.py)</code> -- List of device usage events, sorted by the timestamp, oldest first.

**On `Failure`**: `error` is <code>[ListDevicesUsageHistoryErrorBody](verizon/errors/list_devices_usage_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_with_imei_iccid_mismatch(body: DeviceMismatchListRequest | DeviceMismatchListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceMismatchListResult, ListDevicesWithImeiIccidMismatchErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time frame.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.list_devices_with_imei_iccid_mismatch(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceMismatchListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesWithImeiIccidMismatchErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.list_devices_with_imei_iccid_mismatch(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceMismatchListResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesWithImeiIccidMismatchErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceMismatchListRequest](verizon/models/device_mismatch_list_request.py) \| [DeviceMismatchListRequestDict](verizon/models/device_mismatch_list_request.py)</code> | Request to list devices with mismatched IMEIs and ICCIDs. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceMismatchListResult](verizon/models/device_mismatch_list_result.py), [ListDevicesWithImeiIccidMismatchErrorBody](verizon/errors/list_devices_with_imei_iccid_mismatch_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceMismatchListResult](verizon/models/device_mismatch_list_result.py)</code> -- List of devices that have mismatched IMEIs and ICCIDs.

**On `Failure`**: `error` is <code>[ListDevicesWithImeiIccidMismatchErrorBody](verizon/errors/list_devices_with_imei_iccid_mismatch_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def move_devices_within_accounts_of_profile(body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, MoveDevicesWithinAccountsOfProfileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Move active devices from one billing account to another within a customer profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.move_devices_within_accounts_of_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MoveDevicesWithinAccountsOfProfileErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.move_devices_within_accounts_of_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type MoveDevicesWithinAccountsOfProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[MoveDeviceRequest](verizon/models/move_device_request.py) \| [MoveDeviceRequestDict](verizon/models/move_device_request.py)</code> | Request to move devices between accounts. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [MoveDevicesWithinAccountsOfProfileErrorBody](verizon/errors/move_devices_within_accounts_of_profile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[MoveDevicesWithinAccountsOfProfileErrorBody](verizon/errors/move_devices_within_accounts_of_profile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def restore_service_for_suspended_devices(body: CarrierActionsRequest | CarrierActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, RestoreServiceForSuspendedDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Restores service to one or more suspended devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.restore_service_for_suspended_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RestoreServiceForSuspendedDevicesErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.restore_service_for_suspended_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RestoreServiceForSuspendedDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CarrierActionsRequest](verizon/models/carrier_actions_request.py) \| [CarrierActionsRequestDict](verizon/models/carrier_actions_request.py)</code> | Request to restore services of one or more suspended devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [RestoreServiceForSuspendedDevicesErrorBody](verizon/errors/restore_service_for_suspended_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[RestoreServiceForSuspendedDevicesErrorBody](verizon/errors/restore_service_for_suspended_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_aggregate_device_usage_history(body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, RetrieveAggregateDeviceUsageHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The information is returned in a callback response, so you must register a URL for DeviceUsage callback messages using the POST /callbacks API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.retrieve_aggregate_device_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveAggregateDeviceUsageHistoryErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.retrieve_aggregate_device_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveAggregateDeviceUsageHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceAggregateUsageListRequest](verizon/models/device_aggregate_usage_list_request.py) \| [DeviceAggregateUsageListRequestDict](verizon/models/device_aggregate_usage_list_request.py)</code> | A request to retrieve aggregated device usage history information. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [RetrieveAggregateDeviceUsageHistoryErrorBody](verizon/errors/retrieve_aggregate_device_usage_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- A unique string that associates the request with the results that are sent via a callback service.

**On `Failure`**: `error` is <code>[RetrieveAggregateDeviceUsageHistoryErrorBody](verizon/errors/retrieve_aggregate_device_usage_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_device_connection_history(body: DeviceConnectionListRequest | DeviceConnectionListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectionHistoryResult, RetrieveDeviceConnectionHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Each response includes a maximum of 500 records. To obtain more records, you can call the API multiple times, adjusting the earliest value each time to start where the previous request finished.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.retrieve_device_connection_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectionHistoryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveDeviceConnectionHistoryErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.retrieve_device_connection_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectionHistoryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveDeviceConnectionHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceConnectionListRequest](verizon/models/device_connection_list_request.py) \| [DeviceConnectionListRequestDict](verizon/models/device_connection_list_request.py)</code> | Query to retrieve device connection history. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectionHistoryResult](verizon/models/connection_history_result.py), [RetrieveDeviceConnectionHistoryErrorBody](verizon/errors/retrieve_device_connection_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectionHistoryResult](verizon/models/connection_history_result.py)</code> -- List of device connection events, sorted by the occurredAt timestamp, oldest first.

**On `Failure`**: `error` is <code>[RetrieveDeviceConnectionHistoryErrorBody](verizon/errors/retrieve_device_connection_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def suspend_service_for_devices(body: CarrierActionsRequest | CarrierActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, SuspendServiceForDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Suspends service for one or more devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.suspend_service_for_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SuspendServiceForDevicesErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.suspend_service_for_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SuspendServiceForDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CarrierActionsRequest](verizon/models/carrier_actions_request.py) \| [CarrierActionsRequestDict](verizon/models/carrier_actions_request.py)</code> | Request to suspend service for one or more devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [SuspendServiceForDevicesErrorBody](verizon/errors/suspend_service_for_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[SuspendServiceForDevicesErrorBody](verizon/errors/suspend_service_for_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_device_id(service_type: str, body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UpdateDeviceIdErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes the identifier of a 3G or 4G device to match hardware changes made for a line of service. Use this request to transfer the line of service and the MDN to new hardware, or to change the MDN.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.update_device_id(service_type, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDeviceIdErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.update_device_id(service_type, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDeviceIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>service_type</code> | <code>str</code> | Identifier type. |
| <code>body</code> | <code>[ChangeDeviceIdRequest](verizon/models/change_device_id_request.py) \| [ChangeDeviceIdRequestDict](verizon/models/change_device_id_request.py)</code> | Request to update device id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UpdateDeviceIdErrorBody](verizon/errors/update_device_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- A unique string that associates the request with the results that are sent via a callback service.

**On `Failure`**: `error` is <code>[UpdateDeviceIdErrorBody](verizon/errors/update_device_id_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_devices_contact_information(body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UpdateDevicesContactInformationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a CarrierService callback message for each device in the request when the contact information has been changed, or if there was a problem and the change could not be completed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.update_devices_contact_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesContactInformationErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.update_devices_contact_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesContactInformationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ContactInfoUpdateRequest](verizon/models/contact_info_update_request.py) \| [ContactInfoUpdateRequestDict](verizon/models/contact_info_update_request.py)</code> | Request to update contact information for devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UpdateDevicesContactInformationErrorBody](verizon/errors/update_devices_contact_information_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID returned in a success response.

**On `Failure`**: `error` is <code>[UpdateDevicesContactInformationErrorBody](verizon/errors/update_devices_contact_information_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_devices_cost_center_code(body: DeviceCostCenterRequest | DeviceCostCenterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UpdateDevicesCostCenterCodeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes or removes the CostCenterCode value or customer name and address (Primary Place of Use) for one or more devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.update_devices_cost_center_code(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesCostCenterCodeErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.update_devices_cost_center_code(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesCostCenterCodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceCostCenterRequest](verizon/models/device_cost_center_request.py) \| [DeviceCostCenterRequestDict](verizon/models/device_cost_center_request.py)</code> | Request to update cost center code value for one or more devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UpdateDevicesCostCenterCodeErrorBody](verizon/errors/update_devices_cost_center_code_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[UpdateDevicesCostCenterCodeErrorBody](verizon/errors/update_devices_cost_center_code_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_devices_custom_fields(body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UpdateDevicesCustomFieldsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends a CarrierService callback message for each device in the request when the custom fields have been changed, or if there was a problem and the change could not be completed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.update_devices_custom_fields(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesCustomFieldsErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.update_devices_custom_fields(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesCustomFieldsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CustomFieldsUpdateRequest](verizon/models/custom_fields_update_request.py) \| [CustomFieldsUpdateRequestDict](verizon/models/custom_fields_update_request.py)</code> | Request to update custom field of devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UpdateDevicesCustomFieldsErrorBody](verizon/errors/update_devices_custom_fields_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[UpdateDevicesCustomFieldsErrorBody](verizon/errors/update_devices_custom_fields_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_devices_state(body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UpdateDevicesStateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes the provisioning state of one or more devices to a specified customer-defined service and state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.update_devices_state(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesStateErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.update_devices_state(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDevicesStateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GoToStateRequest](verizon/models/go_to_state_request.py) \| [GoToStateRequestDict](verizon/models/go_to_state_request.py)</code> | Request to change device state to one defined by the user. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UpdateDevicesStateErrorBody](verizon/errors/update_devices_state_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[UpdateDevicesStateErrorBody](verizon/errors/update_devices_state_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upload_activate_device(body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UploadActivateDeviceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads and activates device identifiers and SKUs for new devices from OEMs to Verizon.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.upload_activate_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadActivateDeviceErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.upload_activate_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UploadActivateDeviceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UploadsActivatesDeviceRequest](verizon/models/uploads_activates_device_request.py) \| [UploadsActivatesDeviceRequestDict](verizon/models/uploads_activates_device_request.py)</code> | Request to Upload and Activate device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UploadActivateDeviceErrorBody](verizon/errors/upload_activate_device_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[UploadActivateDeviceErrorBody](verizon/errors/upload_activate_device_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usage_segmentation_label_association(body: AssociateLabelRequest | AssociateLabelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UsageSegmentationLabelAssociationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows you to associate your own usage segmentation label with a device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.usage_segmentation_label_association(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UsageSegmentationLabelAssociationErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.usage_segmentation_label_association(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UsageSegmentationLabelAssociationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssociateLabelRequest](verizon/models/associate_label_request.py) \| [AssociateLabelRequestDict](verizon/models/associate_label_request.py)</code> | Request to associate a label to a device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UsageSegmentationLabelAssociationErrorBody](verizon/errors/usage_segmentation_label_association_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[UsageSegmentationLabelAssociationErrorBody](verizon/errors/usage_segmentation_label_association_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def usage_segmentation_label_deletion(account_name: str, label_list: LabelsList | LabelsListDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, UsageSegmentationLabelDeletionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allow customers to remove the associated label from a device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_management.with_raw_response.usage_segmentation_label_deletion(account_name, label_list)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UsageSegmentationLabelDeletionErrorBody
```

**Async**

```python
result = await async_client.device_management.with_raw_response.usage_segmentation_label_deletion(
    account_name, label_list
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UsageSegmentationLabelDeletionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The numeric name of the account. |
| <code>label_list</code> | <code>[LabelsList](verizon/models/labels_list.py) \| [LabelsListDict](verizon/models/labels_list.py)</code> | A list of the Label IDs to remove from the exclusion list. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [UsageSegmentationLabelDeletionErrorBody](verizon/errors/usage_segmentation_label_deletion_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[UsageSegmentationLabelDeletionErrorBody](verizon/errors/usage_segmentation_label_deletion_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceMonitoring

> Source: [DeviceMonitoring](verizon/apis/device_monitoring.py)

<details>
<summary><code>def device_reachability(body: NotificationReportRequest | NotificationReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, DeviceReachabilityErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_monitoring.with_raw_response.device_reachability(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceReachabilityErrorBody
```

**Async**

```python
result = await async_client.device_monitoring.with_raw_response.device_reachability(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceReachabilityErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[NotificationReportRequest](verizon/models/notification_report_request.py) \| [NotificationReportRequestDict](verizon/models/notification_report_request.py)</code> | Create Reachability Report Request |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [DeviceReachabilityErrorBody](verizon/errors/device_reachability_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[DeviceReachabilityErrorBody](verizon/errors/device_reachability_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_device_reachability(stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, StopDeviceReachabilityErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_monitoring.with_raw_response.stop_device_reachability(stopreachabilitypayload)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StopDeviceReachabilityErrorBody
```

**Async**

```python
result = await async_client.device_monitoring.with_raw_response.stop_device_reachability(stopreachabilitypayload)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StopDeviceReachabilityErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>stopreachabilitypayload</code> | <code>[StopMonitorRequest](verizon/models/stop_monitor_request.py) \| [StopMonitorRequestDict](verizon/models/stop_monitor_request.py)</code> | Payload for the Stop Device Reachability monitors request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [StopDeviceReachabilityErrorBody](verizon/errors/stop_device_reachability_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[StopDeviceReachabilityErrorBody](verizon/errors/stop_device_reachability_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceProfileManagement

> Source: [DeviceProfileManagement](verizon/apis/device_profile_management.py)

<details>
<summary><code>def activate_device_through_profile(body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, ActivateDeviceThroughProfileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the profile to bring the device under management.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_profile_management.with_raw_response.activate_device_through_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivateDeviceThroughProfileErrorBody
```

**Async**

```python
result = await async_client.device_profile_management.with_raw_response.activate_device_through_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ActivateDeviceThroughProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ActivateDeviceProfileRequest](verizon/models/activate_device_profile_request.py) \| [ActivateDeviceProfileRequestDict](verizon/models/activate_device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [ActivateDeviceThroughProfileErrorBody](verizon/errors/activate_device_through_profile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[ActivateDeviceThroughProfileErrorBody](verizon/errors/activate_device_through_profile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_to_activate_device(body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, ProfileToActivateDeviceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the profile to activate the device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_profile_management.with_raw_response.profile_to_activate_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ProfileToActivateDeviceErrorBody
```

**Async**

```python
result = await async_client.device_profile_management.with_raw_response.profile_to_activate_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ProfileToActivateDeviceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileRequest](verizon/models/profile_request.py) \| [ProfileRequestDict](verizon/models/profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [ProfileToActivateDeviceErrorBody](verizon/errors/profile_to_activate_device_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[ProfileToActivateDeviceErrorBody](verizon/errors/profile_to_activate_device_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_to_deactivate_device(body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, ProfileToDeactivateDeviceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the profile to deactivate the device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_profile_management.with_raw_response.profile_to_deactivate_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ProfileToDeactivateDeviceErrorBody
```

**Async**

```python
result = await async_client.device_profile_management.with_raw_response.profile_to_deactivate_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ProfileToDeactivateDeviceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeactivateDeviceProfileRequest](verizon/models/deactivate_device_profile_request.py) \| [DeactivateDeviceProfileRequestDict](verizon/models/deactivate_device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [ProfileToDeactivateDeviceErrorBody](verizon/errors/profile_to_deactivate_device_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[ProfileToDeactivateDeviceErrorBody](verizon/errors/profile_to_deactivate_device_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_to_set_fallback_attribute(body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, ProfileToSetFallbackAttributeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Allows the profile to set the fallback attribute to the device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_profile_management.with_raw_response.profile_to_set_fallback_attribute(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ProfileToSetFallbackAttributeErrorBody
```

**Async**

```python
result = await async_client.device_profile_management.with_raw_response.profile_to_set_fallback_attribute(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ProfileToSetFallbackAttributeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SetFallbackAttributeRequest](verizon/models/set_fallback_attribute_request.py) \| [SetFallbackAttributeRequestDict](verizon/models/set_fallback_attribute_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [ProfileToSetFallbackAttributeErrorBody](verizon/errors/profile_to_set_fallback_attribute_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[ProfileToSetFallbackAttributeErrorBody](verizon/errors/profile_to_set_fallback_attribute_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceReports

> Source: [DeviceReports](verizon/apis/device_reports.py)

<details>
<summary><code>def calculate_aggregated_report_asynchronous(body: AggregateSessionReportRequest | AggregateSessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AggregatedReportCallbackResult, CalculateAggregatedReportAsynchronousErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Calculate aggregated report per day with number of sessions and usage information. User will receive an asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_reports.with_raw_response.calculate_aggregated_report_asynchronous(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AggregatedReportCallbackResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CalculateAggregatedReportAsynchronousErrorBody
```

**Async**

```python
result = await async_client.device_reports.with_raw_response.calculate_aggregated_report_asynchronous(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AggregatedReportCallbackResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CalculateAggregatedReportAsynchronousErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AggregateSessionReportRequest](verizon/models/aggregate_session_report_request.py) \| [AggregateSessionReportRequestDict](verizon/models/aggregate_session_report_request.py)</code> | Aggregated session report request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AggregatedReportCallbackResult](verizon/models/aggregated_report_callback_result.py), [CalculateAggregatedReportAsynchronousErrorBody](verizon/errors/calculate_aggregated_report_asynchronous_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AggregatedReportCallbackResult](verizon/models/aggregated_report_callback_result.py)</code> -- A successful response shows the request is queued with a unique `txid` to identify the report data with.

**On `Failure`**: `error` is <code>[CalculateAggregatedReportAsynchronousErrorBody](verizon/errors/calculate_aggregated_report_asynchronous_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calculate_aggregated_report_synchronous(body: AggregateSessionReportRequest | AggregateSessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AggregateSessionReport, CalculateAggregatedReportSynchronousErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Calculate aggregated report per day with number of sessions and usage information. User will receive synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_reports.with_raw_response.calculate_aggregated_report_synchronous(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AggregateSessionReport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CalculateAggregatedReportSynchronousErrorBody
```

**Async**

```python
result = await async_client.device_reports.with_raw_response.calculate_aggregated_report_synchronous(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AggregateSessionReport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CalculateAggregatedReportSynchronousErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AggregateSessionReportRequest](verizon/models/aggregate_session_report_request.py) \| [AggregateSessionReportRequestDict](verizon/models/aggregate_session_report_request.py)</code> | Aggregated report request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AggregateSessionReport](verizon/models/aggregate_session_report.py), [CalculateAggregatedReportSynchronousErrorBody](verizon/errors/calculate_aggregated_report_synchronous_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AggregateSessionReport](verizon/models/aggregate_session_report.py)</code> -- A successful response shows session and usage details for up to 10 devices.

**On `Failure`**: `error` is <code>[CalculateAggregatedReportSynchronousErrorBody](verizon/errors/calculate_aggregated_report_synchronous_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_sessions_report(body: SessionReportRequest | SessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SessionReport, GetSessionsReportErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Detailed report of session duration and number of bytes transferred per day.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_reports.with_raw_response.get_sessions_report(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SessionReport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSessionsReportErrorBody
```

**Async**

```python
result = await async_client.device_reports.with_raw_response.get_sessions_report(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SessionReport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetSessionsReportErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SessionReportRequest](verizon/models/session_report_request.py) \| [SessionReportRequestDict](verizon/models/session_report_request.py)</code> | Request for sessions report. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SessionReport](verizon/models/session_report.py), [GetSessionsReportErrorBody](verizon/errors/get_sessions_report_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SessionReport](verizon/models/session_report.py)</code> -- A successful response includes the session information for an individual device.

**On `Failure`**: `error` is <code>[GetSessionsReportErrorBody](verizon/errors/get_sessions_report_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceSmsMessaging

> Source: [DeviceSmsMessaging](verizon/apis/device_sms_messaging.py)

<details>
<summary><code>def get_sms_messages(account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SmsMessagesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_sms_messaging.with_raw_response.get_sms_messages(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SmsMessagesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_sms_messaging.with_raw_response.get_sms_messages(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SmsMessagesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Numeric account name |
| <code>next</code> | <code>str \| None</code> | Continue the previous query from the pageUrl in Location Header<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SmsMessagesResponse](verizon/models/sms_messages_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SmsMessagesResponse](verizon/models/sms_messages_response.py)</code> -- Successful response

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_sms_message_history(body: SmseventHistoryRequest | SmseventHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of sms history for a given device during a specified time frame.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_sms_messaging.with_raw_response.list_sms_message_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_sms_messaging.with_raw_response.list_sms_message_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SmseventHistoryRequest](verizon/models/smsevent_history_request.py) \| [SmseventHistoryRequestDict](verizon/models/smsevent_history_request.py)</code> | Device Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_an_sms_message(body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible, but they may be delayed due to traffic and routing considerations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_sms_messaging.with_raw_response.send_an_sms_message(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_sms_messaging.with_raw_response.send_an_sms_message(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GiosmssendRequest](verizon/models/giosmssend_request.py) \| [GiosmssendRequestDict](verizon/models/giosmssend_request.py)</code> | SMS message to an indiividual device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_sms_message_delivery(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SuccessResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Starts delivery of SMS messages for the specified account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_sms_messaging.with_raw_response.start_sms_message_delivery(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SuccessResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.device_sms_messaging.with_raw_response.start_sms_message_delivery(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SuccessResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Numeric account name |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SuccessResponse](verizon/models/success_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SuccessResponse](verizon/models/success_response.py)</code> -- Request Success Message

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceServiceManagement

> Source: [DeviceServiceManagement](verizon/apis/device_service_management.py)

<details>
<summary><code>def get_device_hyper_precise_status(imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BullseyeServiceResult, GetDeviceHyperPreciseStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Gets the list of a status for hyper-precise location devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_service_management.with_raw_response.get_device_hyper_precise_status(imei, account_number)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BullseyeServiceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceHyperPreciseStatusErrorBody
```

**Async**

```python
result = await async_client.device_service_management.with_raw_response.get_device_hyper_precise_status(
    imei, account_number
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BullseyeServiceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceHyperPreciseStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>imei</code> | <code>str</code> | The International Mobile Equipment Identifier of the device. |
| <code>account_number</code> | <code>str</code> | The numeric name of the account and must include leading zeroes. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[BullseyeServiceResult](verizon/models/bullseye_service_result.py), [GetDeviceHyperPreciseStatusErrorBody](verizon/errors/get_device_hyper_precise_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BullseyeServiceResult](verizon/models/bullseye_service_result.py)</code> -- Returns the status of Hyper Precise Location on the device.

**On `Failure`**: `error` is <code>[GetDeviceHyperPreciseStatusErrorBody](verizon/errors/get_device_hyper_precise_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_device_hyper_precise_status(body: BullseyeServiceRequest | BullseyeServiceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BullseyeServiceResult, UpdateDeviceHyperPreciseStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable/disable hyper-precise service for a device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_service_management.with_raw_response.update_device_hyper_precise_status(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BullseyeServiceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDeviceHyperPreciseStatusErrorBody
```

**Async**

```python
result = await async_client.device_service_management.with_raw_response.update_device_hyper_precise_status(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BullseyeServiceResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateDeviceHyperPreciseStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BullseyeServiceRequest](verizon/models/bullseye_service_request.py) \| [BullseyeServiceRequestDict](verizon/models/bullseye_service_request.py)</code> | List of devices and hyper-precise required statuses. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[BullseyeServiceResult](verizon/models/bullseye_service_result.py), [UpdateDeviceHyperPreciseStatusErrorBody](verizon/errors/update_device_hyper_precise_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[BullseyeServiceResult](verizon/models/bullseye_service_result.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[UpdateDeviceHyperPreciseStatusErrorBody](verizon/errors/update_device_hyper_precise_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DevicesLocationSubscriptions

> Source: [DevicesLocationSubscriptions](verizon/apis/devices_location_subscriptions.py)

<details>
<summary><code>def get_location_service_subscription_status(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceLocationSubscription, GetLocationServiceSubscriptionStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This subscriptions endpoint retrieves an account's current location subscription status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_location_subscriptions.with_raw_response.get_location_service_subscription_status(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSubscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLocationServiceSubscriptionStatusErrorBody
```

**Async**

```python
result = await async_client.devices_location_subscriptions.with_raw_response.get_location_service_subscription_status(
    account_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSubscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLocationServiceSubscriptionStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceLocationSubscription](verizon/models/device_location_subscription.py), [GetLocationServiceSubscriptionStatusErrorBody](verizon/errors/get_location_service_subscription_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceLocationSubscription](verizon/models/device_location_subscription.py)</code> -- Device location subscription information.

**On `Failure`**: `error` is <code>[GetLocationServiceSubscriptionStatusErrorBody](verizon/errors/get_location_service_subscription_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_location_service_usage(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Any, GetLocationServiceUsageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to search for billable usage for accounts based on the provided date range.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_location_subscriptions.with_raw_response.get_location_service_usage()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLocationServiceUsageErrorBody
```

**Async**

```python
result = await async_client.devices_location_subscriptions.with_raw_response.get_location_service_usage()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Any
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetLocationServiceUsageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;Any, [GetLocationServiceUsageErrorBody](verizon/errors/get_location_service_usage_error.py)&#93;</code>

**On `Success`**: `payload` is <code>Any</code> -- Billable usage report.

**On `Failure`**: `error` is <code>[GetLocationServiceUsageErrorBody](verizon/errors/get_location_service_usage_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DevicesLocations

> Source: [DevicesLocations](verizon/apis/devices_locations.py)

<details>
<summary><code>def cancel_queued_location_report_generation(account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TransactionId, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel a queued device location report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_locations.with_raw_response.cancel_queued_location_report_generation(account_name, txid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices_locations.with_raw_response.cancel_queued_location_report_generation(
    account_name, txid
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>txid</code> | <code>str</code> | Transaction ID of the report to cancel. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TransactionId](verizon/models/transaction_id.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TransactionId](verizon/models/transaction_id.py)</code> -- Report generation cancelled.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_location_report(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AsynchronousLocationRequestResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Request an asynchronous device location report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_locations.with_raw_response.create_location_report()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsynchronousLocationRequestResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices_locations.with_raw_response.create_location_report()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsynchronousLocationRequestResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AsynchronousLocationRequestResult](verizon/models/asynchronous_location_request_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AsynchronousLocationRequestResult](verizon/models/asynchronous_location_request_result.py)</code> -- Request accepted; location report in progress.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_location_report_status(account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LocationReportStatus, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the current status of a requested device location report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_locations.with_raw_response.get_location_report_status(account_name, txid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LocationReportStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices_locations.with_raw_response.get_location_report_status(account_name, txid)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LocationReportStatus
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>txid</code> | <code>str</code> | Transaction ID of the report. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[LocationReportStatus](verizon/models/location_report_status.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LocationReportStatus](verizon/models/location_report_status.py)</code> -- Location report status.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_locations_asynchronous(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SynchronousLocationRequestResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Requests the current or cached location of up to 10,000 IoT or consumer devices (phones, tablets. etc.). This request returns a synchronous transaction ID, and the location information for each device is returned asynchronously as a DeviceLocation callback message.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_locations.with_raw_response.list_devices_locations_asynchronous()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SynchronousLocationRequestResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices_locations.with_raw_response.list_devices_locations_asynchronous()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SynchronousLocationRequestResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SynchronousLocationRequestResult](verizon/models/synchronous_location_request_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SynchronousLocationRequestResult](verizon/models/synchronous_location_request_result.py)</code> -- Request accepted; location report in progress

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_locations_synchronous(body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Location], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This locations endpoint retrieves the locations for a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_locations.with_raw_response.list_devices_locations_synchronous(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Location]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices_locations.with_raw_response.list_devices_locations_synchronous(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Location]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LocationRequest](verizon/models/location_request.py) \| [LocationRequestDict](verizon/models/location_request.py)</code> | Request to obtain location of devices. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[Location](verizon/models/location.py)&#93;, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Location](verizon/models/location.py)&#93;</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location_report(account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LocationReport, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Download a completed asynchronous device location report.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices_locations.with_raw_response.retrieve_location_report(account_name, txid, startindex)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LocationReport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices_locations.with_raw_response.retrieve_location_report(account_name, txid, startindex)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LocationReport
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>txid</code> | <code>str</code> | Transaction ID from POST /locationreports response. |
| <code>startindex</code> | <code>int</code> | Zero-based number of the first record to return. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[LocationReport](verizon/models/location_report.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LocationReport](verizon/models/location_report.py)</code> -- Location information for up to 1,000 devices.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsCallbacks

> Source: [DiagnosticsCallbacks](verizon/apis/diagnostics_callbacks.py)

<details>
<summary><code>def get_diagnostics_subscription_callback_info(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceDiagnosticsCallback], GetDiagnosticsSubscriptionCallbackInfoErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to get the registered callback information of an existing diagnostics subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_callbacks.with_raw_response.get_diagnostics_subscription_callback_info(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceDiagnosticsCallback]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDiagnosticsSubscriptionCallbackInfoErrorBody
```

**Async**

```python
result = await async_client.diagnostics_callbacks.with_raw_response.get_diagnostics_subscription_callback_info(
    account_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceDiagnosticsCallback]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDiagnosticsSubscriptionCallbackInfoErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)&#93;, [GetDiagnosticsSubscriptionCallbackInfoErrorBody](verizon/errors/get_diagnostics_subscription_callback_info_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)&#93;</code> -- Returns callback registration.

**On `Failure`**: `error` is <code>[GetDiagnosticsSubscriptionCallbackInfoErrorBody](verizon/errors/get_diagnostics_subscription_callback_info_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceDiagnosticsResult](verizon/models/device_diagnostics_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_diagnostics_callback_url(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceDiagnosticsCallback, RegisterDiagnosticsCallbackUrlErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user update the callback HTTPS address of an existing diagnostics subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_callbacks.with_raw_response.register_diagnostics_callback_url()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceDiagnosticsCallback
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterDiagnosticsCallbackUrlErrorBody
```

**Async**

```python
result = await async_client.diagnostics_callbacks.with_raw_response.register_diagnostics_callback_url()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceDiagnosticsCallback
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterDiagnosticsCallbackUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py), [RegisterDiagnosticsCallbackUrlErrorBody](verizon/errors/register_diagnostics_callback_url_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)</code> -- Returns callback registration.

**On `Failure`**: `error` is <code>[RegisterDiagnosticsCallbackUrlErrorBody](verizon/errors/register_diagnostics_callback_url_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceDiagnosticsResult](verizon/models/device_diagnostics_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unregister_diagnostics_callback(account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceDiagnosticsCallback, UnregisterDiagnosticsCallbackErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to delete a registered callback URL and credential.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_callbacks.with_raw_response.unregister_diagnostics_callback(account_name, service_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceDiagnosticsCallback
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnregisterDiagnosticsCallbackErrorBody
```

**Async**

```python
result = await async_client.diagnostics_callbacks.with_raw_response.unregister_diagnostics_callback(
    account_name, service_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceDiagnosticsCallback
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnregisterDiagnosticsCallbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>service_name</code> | <code>str</code> | Service name for callback notification. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py), [UnregisterDiagnosticsCallbackErrorBody](verizon/errors/unregister_diagnostics_callback_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)</code> -- Device diagnostics callback registration.

**On `Failure`**: `error` is <code>[UnregisterDiagnosticsCallbackErrorBody](verizon/errors/unregister_diagnostics_callback_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceDiagnosticsResult](verizon/models/device_diagnostics_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsFactoryReset

> Source: [DiagnosticsFactoryReset](verizon/apis/diagnostics_factory_reset.py)

<details>
<summary><code>def decives_restart(body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DiagnosticsObservationResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Performs a device reboot or a factory reset on the modem portion of the device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_factory_reset.with_raw_response.decives_restart(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsObservationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.diagnostics_factory_reset.with_raw_response.decives_restart(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsObservationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceResetRequest](verizon/models/device_reset_request.py) \| [DeviceResetRequestDict](verizon/models/device_reset_request.py)</code> | A request to perform a device reboot. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py)</code> -- Diagnostics observation result.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsHistory

> Source: [DiagnosticsHistory](verizon/apis/diagnostics_history.py)

<details>
<summary><code>def get_diagnostics_history(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[History], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to get the history data.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_history.with_raw_response.get_diagnostics_history()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[History]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.diagnostics_history.with_raw_response.get_diagnostics_history()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[History]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[History](verizon/models/history.py)&#93;, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[History](verizon/models/history.py)&#93;</code> -- History search response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsObservations

> Source: [DiagnosticsObservations](verizon/apis/diagnostics_observations.py)

<details>
<summary><code>def start_diagnostics_observation(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DiagnosticsObservationResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to start or change observe diagnostics.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_observations.with_raw_response.start_diagnostics_observation()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsObservationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.diagnostics_observations.with_raw_response.start_diagnostics_observation()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsObservationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py)</code> -- Diagnostics observation result.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_diagnostics_observation(transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DiagnosticsObservationResult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to stop or reset observe diagnostics.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_observations.with_raw_response.stop_diagnostics_observation(transaction_id, account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsObservationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.diagnostics_observations.with_raw_response.stop_diagnostics_observation(
    transaction_id, account_name
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsObservationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transaction_id</code> | <code>str</code> | The ID value associated with the transaction. |
| <code>account_name</code> | <code>str</code> | The numeric account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py)</code> -- Diagnostics observation result.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsSettings

> Source: [DiagnosticsSettings](verizon/apis/diagnostics_settings.py)

<details>
<summary><code>def list_diagnostics_settings(account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DiagnosticObservationSetting], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint retrieves diagnostics settings synchronously.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_settings.with_raw_response.list_diagnostics_settings(account_name, devices)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DiagnosticObservationSetting]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.diagnostics_settings.with_raw_response.list_diagnostics_settings(account_name, devices)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DiagnosticObservationSetting]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>devices</code> | <code>str</code> | Devices list formatted as "id, kind" |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DiagnosticObservationSetting](verizon/models/diagnostic_observation_setting.py)&#93;, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DiagnosticObservationSetting](verizon/models/diagnostic_observation_setting.py)&#93;</code> -- Diagnostic settings.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsSubscriptions

> Source: [DiagnosticsSubscriptions](verizon/apis/diagnostics_subscriptions.py)

<details>
<summary><code>def get_diagnostics_subscription(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DiagnosticsSubscription, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint retrieves a diagnostics subscription by account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.diagnostics_subscriptions.with_raw_response.get_diagnostics_subscription(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsSubscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.diagnostics_subscriptions.with_raw_response.get_diagnostics_subscription(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DiagnosticsSubscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DiagnosticsSubscription](verizon/models/diagnostics_subscription.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DiagnosticsSubscription](verizon/models/diagnostics_subscription.py)</code> -- Diagnostics subscription response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## EtxappConfiguration

> Source: [EtxappConfiguration](verizon/apis/etxapp_configuration.py)

<details>
<summary><code>def create_configuration(vendor_id: str, body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GeoFenceConfigurationResponse, CreateConfigurationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint creates a new configuration in the system. The data for the new configuration should be provided as JSON in the body of the POST request. The system will return with a unique ID for the configuration, which is needed for any further manipulation (update or delete) of the configuration.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxapp_configuration.with_raw_response.create_configuration(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeoFenceConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfigurationErrorBody
```

**Async**

```python
result = await async_client.etxapp_configuration.with_raw_response.create_configuration(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeoFenceConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The vendor's identifier |
| <code>body</code> | <code>[GeoFenceConfigurationRequest](verizon/models/geo_fence_configuration_request.py) \| [GeoFenceConfigurationRequestDict](verizon/models/geo_fence_configuration_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GeoFenceConfigurationResponse](verizon/models/geo_fence_configuration_response.py), [CreateConfigurationErrorBody](verizon/errors/create_configuration_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GeoFenceConfigurationResponse](verizon/models/geo_fence_configuration_response.py)</code> -- Configuration created

**On `Failure`**: `error` is <code>[CreateConfigurationErrorBody](verizon/errors/create_configuration_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 429 | <code>[ResponseError](verizon/models/response_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_configuration(id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteConfigurationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint deletes a specific configuration from the system. It requires the configuration ID parameter, which was provided by the POST (create) operation.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxapp_configuration.with_raw_response.delete_configuration(id, vendor_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteConfigurationErrorBody
```

**Async**

```python
result = await async_client.etxapp_configuration.with_raw_response.delete_configuration(id, vendor_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The configuration identifier |
| <code>vendor_id</code> | <code>str</code> | The vendor's identifier |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DeleteConfigurationErrorBody](verizon/errors/delete_configuration_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteConfigurationErrorBody](verizon/errors/delete_configuration_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 429 | <code>[ResponseError](verizon/models/response_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_configuration(id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GeoFenceConfigurationResponse, GetConfigurationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint fetches and returns a specific configuration's details. The configuration ID parameter, which was provided when the configuration was created through the POST request, is need to retrieve the configuration details.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxapp_configuration.with_raw_response.get_configuration(id, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeoFenceConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetConfigurationErrorBody
```

**Async**

```python
result = await async_client.etxapp_configuration.with_raw_response.get_configuration(id, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GeoFenceConfigurationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The configuration identifier |
| <code>vendor_id</code> | <code>str</code> | The vendor's identifier |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GeoFenceConfigurationResponse](verizon/models/geo_fence_configuration_response.py), [GetConfigurationErrorBody](verizon/errors/get_configuration_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GeoFenceConfigurationResponse](verizon/models/geo_fence_configuration_response.py)</code> -- Configuration found

**On `Failure`**: `error` is <code>[GetConfigurationErrorBody](verizon/errors/get_configuration_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 404, 429 | <code>[ResponseError](verizon/models/response_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_configuration_list(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ConfigurationListItem], GetConfigurationListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint fetches and returns the list of configurations defined by the Vendor. The list contains the configurations' identifier, name, description, and active flag. The vendor ID is provided when the configuration is created through the POST request.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxapp_configuration.with_raw_response.get_configuration_list(vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ConfigurationListItem]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetConfigurationListErrorBody
```

**Async**

```python
result = await async_client.etxapp_configuration.with_raw_response.get_configuration_list(vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ConfigurationListItem]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetConfigurationListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The vendor's identifier |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ConfigurationListItem](verizon/models/configuration_list_item.py)&#93;, [GetConfigurationListErrorBody](verizon/errors/get_configuration_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ConfigurationListItem](verizon/models/configuration_list_item.py)&#93;</code> -- Configuration list was queried successfully

**On `Failure`**: `error` is <code>[GetConfigurationListErrorBody](verizon/errors/get_configuration_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 403, 404, 429 | <code>[ResponseError](verizon/models/response_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_configuration(id: str, vendor_id: str, body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, UpdateConfigurationErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint updates an existing configuration. Similar to POST, the updated data for the configuration should be provided as JSON in the body of the PUT request. The configuration ID parameter, which was provided by the POST (create) operation, is required to do any updates on the configuration.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxapp_configuration.with_raw_response.update_configuration(id, vendor_id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateConfigurationErrorBody
```

**Async**

```python
result = await async_client.etxapp_configuration.with_raw_response.update_configuration(id, vendor_id, body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateConfigurationErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The configuration identifier |
| <code>vendor_id</code> | <code>str</code> | The vendor's identifier |
| <code>body</code> | <code>[GeoFenceConfigurationUpdateRequest](verizon/models/geo_fence_configuration_update_request.py) \| [GeoFenceConfigurationUpdateRequestDict](verizon/models/geo_fence_configuration_update_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [UpdateConfigurationErrorBody](verizon/errors/update_configuration_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[UpdateConfigurationErrorBody](verizon/errors/update_configuration_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 429 | <code>[ResponseError](verizon/models/response_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Etxregistration

> Source: [Etxregistration](verizon/apis/etxregistration.py)

<details>
<summary><code>def get_etx_client_certificate(id: EtxclientIdlookup | EtxclientIdlookupDict, vendor_id: str, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ClientPersistenceResponse, GetEtxclientCertificateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

With this API call the user can check the certificate of the device. At least one of the DeviceID, IMEI, ICCID or IMSI is required to make the call.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.get_etx_client_certificate(id, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ClientPersistenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEtxclientCertificateErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.get_etx_client_certificate(id, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ClientPersistenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEtxclientCertificateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>[EtxclientIdlookup](verizon/models/etxclient_idlookup.py) \| [EtxclientIdlookupDict](verizon/models/etxclient_idlookup.py)</code> | One of the following IDs is required- DeviceID, IMEI, ICCID, IMSI. If more than one ID is provided, the API will return the certificate for the first ID found. The IDs are evaluated in the following order: DeviceID, IMEI, ICCID, IMSI. If the first provided ID is not found, the API will return an error. |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ClientPersistenceResponse](verizon/models/client_persistence_response.py), [GetEtxclientCertificateErrorBody](verizon/errors/get_etxclient_certificate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ClientPersistenceResponse](verizon/models/client_persistence_response.py)</code> -- Successful retrieval

**On `Failure`**: `error` is <code>[GetEtxclientCertificateErrorBody](verizon/errors/get_etxclient_certificate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 429, 500 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_etx_connection_url(vendor_id: str, body: ConnectionRequest | ConnectionRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectionResponse, GetEtxconnectionUrlErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

With this API call the device or software service requests the MQTT URL for the location that it needs to connect. To determine the proper URL the device or software service needs to provide its ID (the one that was provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular network or not.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.get_etx_connection_url(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEtxconnectionUrlErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.get_etx_connection_url(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEtxconnectionUrlErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>body</code> | <code>[ConnectionRequest](verizon/models/connection_request.py) \| [ConnectionRequestDict](verizon/models/connection_request.py)</code> | The request body. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectionResponse](verizon/models/connection_response.py), [GetEtxconnectionUrlErrorBody](verizon/errors/get_etxconnection_url_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectionResponse](verizon/models/connection_response.py)</code> -- Successful retrieval

**On `Failure`**: `error` is <code>[GetEtxconnectionUrlErrorBody](verizon/errors/get_etxconnection_url_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 503 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_etx_connection_url_multi_mec(vendor_id: str, body: ConnectionRequest | ConnectionRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectionResponseV3, GetEtxconnectionUrlMultiMecErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

With this API call the device or software service requests the MQTT URL for the location that it needs to connect. To determine the proper URL the device or software service needs to provide its ID (the one that was provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular network or not.

If there are multiple MECs that serve the location of the client all options are provided in the response, and the client is free to choose which MEC they want to connect.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.get_etx_connection_url_multi_mec(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectionResponseV3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEtxconnectionUrlMultiMecErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.get_etx_connection_url_multi_mec(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectionResponseV3
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetEtxconnectionUrlMultiMecErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>body</code> | <code>[ConnectionRequest](verizon/models/connection_request.py) \| [ConnectionRequestDict](verizon/models/connection_request.py)</code> | The request body. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectionResponseV3](verizon/models/connection_response_v3.py), [GetEtxconnectionUrlMultiMecErrorBody](verizon/errors/get_etxconnection_url_multi_mec_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectionResponseV3](verizon/models/connection_response_v3.py)</code> -- Successful retrieval

**On `Failure`**: `error` is <code>[GetEtxconnectionUrlMultiMecErrorBody](verizon/errors/get_etxconnection_url_multi_mec_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 503 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_etx_devices(body: DevicesRequest | DevicesRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DevicesResponse], QueryEtxdevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows retrieving devices by vendor ID and optional filters. The request should include the VendorID and any filters to apply.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.query_etx_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DevicesResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryEtxdevicesErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.query_etx_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DevicesResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryEtxdevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DevicesRequest](verizon/models/devices_request.py) \| [DevicesRequestDict](verizon/models/devices_request.py)</code> | The request body. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DevicesResponse](verizon/models/devices_response.py)&#93;, [QueryEtxdevicesErrorBody](verizon/errors/query_etxdevices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DevicesResponse](verizon/models/devices_response.py)&#93;</code> -- Successful retrieval of devices

**On `Failure`**: `error` is <code>[QueryEtxdevicesErrorBody](verizon/errors/query_etxdevices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 500 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_etx_client(body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ClientRegistrationResponse, RegisterEtxclientErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

With this API call the user (client) registers its device or software service to the ETX system. Therefore, when a connection is initiated from the device or software service to the ETX system along with the credential provided by this registration call, then the connection will be authorized.

- The user can register multiple devices or software services, which can all be used at the same time.
- There rules set in the system that limit the type and subtype of the clients that are allowed to be registered under the VendorID. The rules are created based ont he agreement between the Vendor and Verizon.
- The user will only be able to register a limited number of devices or software services under the same VendorID. This registration limit is specified by the agreement between the Vendor and Verizon.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.register_etx_client(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ClientRegistrationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterEtxclientErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.register_etx_client(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ClientRegistrationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterEtxclientErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ClientRegistrationRequestV2](verizon/models/client_registration_request_v2.py) \| [ClientRegistrationRequestV2Dict](verizon/models/client_registration_request_v2.py)</code> | The request body. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ClientRegistrationResponse](verizon/models/client_registration_response.py), [RegisterEtxclientErrorBody](verizon/errors/register_etxclient_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ClientRegistrationResponse](verizon/models/client_registration_response.py)</code> -- Successful Registration

**On `Failure`**: `error` is <code>[RegisterEtxclientErrorBody](verizon/errors/register_etxclient_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 503 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def renew_etx_client_certificate(device_id: UUID, vendor_id: str, *, x_transaction_id: UUID | None = None, body: Any | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ClientRegistrationResponse, RenewEtxclientCertificateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

With this API call the user (client) can:
- renew the certificate of a device or software service in the ETX system if the original certificate has expired. If the client's certificate expired or going to expire within 30 days and new certificate will be issued. If the certificate expires more than 30 days, the current certificate will be returned to the client.
- complete its device or software service registration to the ETX system if the original registration request was not successful because of a pending certificate generation. Whenever the user receives a "client registration is pending" response (HTTP 202) from POST /clients/registration call. The client should initiate this PUT API call to finish the registration process and get the required certificate.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.renew_etx_client_certificate(device_id, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ClientRegistrationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenewEtxclientCertificateErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.renew_etx_client_certificate(device_id, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ClientRegistrationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RenewEtxclientCertificateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_id</code> | <code>UUID</code> | Value sent with the request. |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>body</code> | <code>Any \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ClientRegistrationResponse](verizon/models/client_registration_response.py), [RenewEtxclientCertificateErrorBody](verizon/errors/renew_etxclient_certificate_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ClientRegistrationResponse](verizon/models/client_registration_response.py)</code> -- Successful Registration

**On `Failure`**: `error` is <code>[RenewEtxclientCertificateErrorBody](verizon/errors/renew_etxclient_certificate_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 503 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unregister_etx_clients(device_ids: list[UUID], vendor_id: str, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, UnregisterEtxclientsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

With this API call the user (client) can unregister its devices and software services from the ETX system. The unregistered devices and services will no longer be able to use the ETX Message Exchange.

Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.etxregistration.with_raw_response.unregister_etx_clients(device_ids, vendor_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnregisterEtxclientsErrorBody
```

**Async**

```python
result = await async_client.etxregistration.with_raw_response.unregister_etx_clients(device_ids, vendor_id)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnregisterEtxclientsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_ids</code> | <code>list&#91;UUID&#93;</code> | The list of device IDs and software service IDs to be unregistered |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>x_transaction_id</code> | <code>UUID \| None</code> | Optional transaction identifier for tracing requests. If not provided, the application will generate one.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [UnregisterEtxclientsErrorBody](verizon/errors/unregister_etxclients_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[UnregisterEtxclientsErrorBody](verizon/errors/unregister_etxclients_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 429, 503 | <code>[EtxrespondingError](verizon/models/etxresponding_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Exclusions

> Source: [Exclusions](verizon/apis/exclusions.py)

<details>
<summary><code>def devices_location_get_consent_async(account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetAccountDeviceConsent, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get the consent settings for the entire account or device list in an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.exclusions.with_raw_response.devices_location_get_consent_async(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAccountDeviceConsent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.exclusions.with_raw_response.devices_location_get_consent_async(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetAccountDeviceConsent
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The numeric name of the account. |
| <code>device_id</code> | <code>str \| None</code> | The IMEI of the device being queried<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GetAccountDeviceConsent](verizon/models/get_account_device_consent.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetAccountDeviceConsent](verizon/models/get_account_device_consent.py)</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def devices_location_give_consent_async(*, body: AccountConsentCreate | AccountConsentCreateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConsentTransactionId, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a consent record to use location services as an asynchronous request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.exclusions.with_raw_response.devices_location_give_consent_async()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConsentTransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.exclusions.with_raw_response.devices_location_give_consent_async()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConsentTransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountConsentCreate](verizon/models/account_consent_create.py) \| [AccountConsentCreateDict](verizon/models/account_consent_create.py) \| None</code> | Account details to create a consent record.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConsentTransactionId](verizon/models/consent_transaction_id.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConsentTransactionId](verizon/models/consent_transaction_id.py)</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def devices_location_update_consent(*, body: AccountConsentUpdate | AccountConsentUpdateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConsentTransactionId, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update the location services consent record for an entire account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.exclusions.with_raw_response.devices_location_update_consent()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConsentTransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.exclusions.with_raw_response.devices_location_update_consent()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConsentTransactionId
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AccountConsentUpdate](verizon/models/account_consent_update.py) \| [AccountConsentUpdateDict](verizon/models/account_consent_update.py) \| None</code> | Account details to update a consent record.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConsentTransactionId](verizon/models/consent_transaction_id.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConsentTransactionId](verizon/models/consent_transaction_id.py)</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exclude_devices(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceLocationSuccessResult, ExcludeDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This consents endpoint sets a new exclusion list.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.exclusions.with_raw_response.exclude_devices()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ExcludeDevicesErrorBody
```

**Async**

```python
result = await async_client.exclusions.with_raw_response.exclude_devices()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ExcludeDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py), [ExcludeDevicesErrorBody](verizon/errors/exclude_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Success response.

**On `Failure`**: `error` is <code>[ExcludeDevicesErrorBody](verizon/errors/exclude_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_excluded_devices(account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DevicesConsentResult, ListExcludedDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This consents endpoint retrieves a list of excluded devices in an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.exclusions.with_raw_response.list_excluded_devices(account_name, start_index)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DevicesConsentResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListExcludedDevicesErrorBody
```

**Async**

```python
result = await async_client.exclusions.with_raw_response.list_excluded_devices(account_name, start_index)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DevicesConsentResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListExcludedDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>start_index</code> | <code>str</code> | Zero-based number of the first record to return. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DevicesConsentResult](verizon/models/devices_consent_result.py), [ListExcludedDevicesErrorBody](verizon/errors/list_excluded_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DevicesConsentResult](verizon/models/devices_consent_result.py)</code> -- Excluded devices result.

**On `Failure`**: `error` is <code>[ListExcludedDevicesErrorBody](verizon/errors/list_excluded_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_devices_from_exclusion_list(account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceLocationSuccessResult, RemoveDevicesFromExclusionListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes devices from the exclusion list so that they can be located with Device Location Services requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.exclusions.with_raw_response.remove_devices_from_exclusion_list(account_name, device_list)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveDevicesFromExclusionListErrorBody
```

**Async**

```python
result = await async_client.exclusions.with_raw_response.remove_devices_from_exclusion_list(account_name, device_list)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveDevicesFromExclusionListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The numeric name of the account. |
| <code>device_list</code> | <code>str</code> | A list of the device IDs to remove from the exclusion list. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py), [RemoveDevicesFromExclusionListErrorBody](verizon/errors/remove_devices_from_exclusion_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Devices successfully removed from list.

**On `Failure`**: `error` is <code>[RemoveDevicesFromExclusionListErrorBody](verizon/errors/remove_devices_from_exclusion_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FirmwareV1

> Source: [FirmwareV1](verizon/apis/firmware_v1.py)

<details>
<summary><code>def cancel_scheduled_firmware_upgrade(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV1SuccessResult, CancelScheduledFirmwareUpgradeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancel a scheduled firmware upgrade.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v1.with_raw_response.cancel_scheduled_firmware_upgrade(account_name, upgrade_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV1SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelScheduledFirmwareUpgradeErrorBody
```

**Async**

```python
result = await async_client.firmware_v1.with_raw_response.cancel_scheduled_firmware_upgrade(account_name, upgrade_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV1SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CancelScheduledFirmwareUpgradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>upgrade_id</code> | <code>str</code> | The UUID of the scheduled upgrade that you want to cancel. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV1SuccessResult](verizon/models/fota_v1_success_result.py), [CancelScheduledFirmwareUpgradeErrorBody](verizon/errors/cancel_scheduled_firmware_upgrade_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV1SuccessResult](verizon/models/fota_v1_success_result.py)</code> -- Upgrade canceled.

**On `Failure`**: `error` is <code>[CancelScheduledFirmwareUpgradeErrorBody](verizon/errors/cancel_scheduled_firmware_upgrade_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_available_firmware(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Firmware], ListAvailableFirmwareErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all device firmware images available for an account, based on the devices registered to that account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v1.with_raw_response.list_available_firmware(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Firmware]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAvailableFirmwareErrorBody
```

**Async**

```python
result = await async_client.firmware_v1.with_raw_response.list_available_firmware(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Firmware]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAvailableFirmwareErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[Firmware](verizon/models/firmware.py)&#93;, [ListAvailableFirmwareErrorBody](verizon/errors/list_available_firmware_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Firmware](verizon/models/firmware.py)&#93;</code> -- List of available firmware.

**On `Failure`**: `error` is <code>[ListAvailableFirmwareErrorBody](verizon/errors/list_available_firmware_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_firmware_upgrade_details(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FirmwareUpgrade, ListFirmwareUpgradeDetailsErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about a specified upgrade, include the target date of the upgrade, the list of devices in the upgrade, and the status of the upgrade for each device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v1.with_raw_response.list_firmware_upgrade_details(account_name, upgrade_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareUpgrade
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFirmwareUpgradeDetailsErrorBody
```

**Async**

```python
result = await async_client.firmware_v1.with_raw_response.list_firmware_upgrade_details(account_name, upgrade_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareUpgrade
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListFirmwareUpgradeDetailsErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>upgrade_id</code> | <code>str</code> | The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FirmwareUpgrade](verizon/models/firmware_upgrade.py), [ListFirmwareUpgradeDetailsErrorBody](verizon/errors/list_firmware_upgrade_details_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FirmwareUpgrade](verizon/models/firmware_upgrade.py)</code> -- Firmware upgrade information.

**On `Failure`**: `error` is <code>[ListFirmwareUpgradeDetailsErrorBody](verizon/errors/list_firmware_upgrade_details_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def schedule_firmware_upgrade(body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FirmwareUpgrade, ScheduleFirmwareUpgradeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a firmware upgrade for devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v1.with_raw_response.schedule_firmware_upgrade(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareUpgrade
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleFirmwareUpgradeErrorBody
```

**Async**

```python
result = await async_client.firmware_v1.with_raw_response.schedule_firmware_upgrade(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareUpgrade
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ScheduleFirmwareUpgradeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FirmwareUpgradeRequest](verizon/models/firmware_upgrade_request.py) \| [FirmwareUpgradeRequestDict](verizon/models/firmware_upgrade_request.py)</code> | Details of the firmware upgrade request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FirmwareUpgrade](verizon/models/firmware_upgrade.py), [ScheduleFirmwareUpgradeErrorBody](verizon/errors/schedule_firmware_upgrade_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FirmwareUpgrade](verizon/models/firmware_upgrade.py)</code> -- Confirmation of successful firmware upgrade.

**On `Failure`**: `error` is <code>[ScheduleFirmwareUpgradeErrorBody](verizon/errors/schedule_firmware_upgrade_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_firmware_upgrade_devices(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FirmwareUpgradeChangeResult, UpdateFirmwareUpgradeDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Add or remove devices from a scheduled upgrade.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v1.with_raw_response.update_firmware_upgrade_devices(account_name, upgrade_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareUpgradeChangeResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateFirmwareUpgradeDevicesErrorBody
```

**Async**

```python
result = await async_client.firmware_v1.with_raw_response.update_firmware_upgrade_devices(account_name, upgrade_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FirmwareUpgradeChangeResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateFirmwareUpgradeDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>upgrade_id</code> | <code>str</code> | The UUID of the upgrade, returned by POST /upgrades when the upgrade was scheduled. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FirmwareUpgradeChangeResult](verizon/models/firmware_upgrade_change_result.py), [UpdateFirmwareUpgradeDevicesErrorBody](verizon/errors/update_firmware_upgrade_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FirmwareUpgradeChangeResult](verizon/models/firmware_upgrade_change_result.py)</code> -- Upgrade information.

**On `Failure`**: `error` is <code>[UpdateFirmwareUpgradeDevicesErrorBody](verizon/errors/update_firmware_upgrade_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## FirmwareV3

> Source: [FirmwareV3](verizon/apis/firmware_v3.py)

<details>
<summary><code>def list_available_firmware2(acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[FirmwarePackage], ListAvailableFirmware2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to list the firmware of an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v3.with_raw_response.list_available_firmware2(acc, protocol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[FirmwarePackage]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAvailableFirmware2ErrorBody
```

**Async**

```python
result = await async_client.firmware_v3.with_raw_response.list_available_firmware2(acc, protocol)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[FirmwarePackage]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAvailableFirmware2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>protocol</code> | <code>[FirmwareProtocolOrStr](verizon/models/enums/firmware_protocol.py)</code> | Filter to retrieve a specific protocol type used. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[FirmwarePackage](verizon/models/firmware_package.py)&#93;, [ListAvailableFirmware2ErrorBody](verizon/errors/list_available_firmware2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[FirmwarePackage](verizon/models/firmware_package.py)&#93;</code> -- Returns an array of firmware objects.

**On `Failure`**: `error` is <code>[ListAvailableFirmware2ErrorBody](verizon/errors/list_available_firmware2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def report_device_firmware(acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceFirmwareVersionUpdateResult, ReportDeviceFirmwareErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Ask a device to report its firmware version asynchronously.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v3.with_raw_response.report_device_firmware(acc, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceFirmwareVersionUpdateResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReportDeviceFirmwareErrorBody
```

**Async**

```python
result = await async_client.firmware_v3.with_raw_response.report_device_firmware(acc, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceFirmwareVersionUpdateResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ReportDeviceFirmwareErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceFirmwareVersionUpdateResult](verizon/models/device_firmware_version_update_result.py), [ReportDeviceFirmwareErrorBody](verizon/errors/report_device_firmware_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceFirmwareVersionUpdateResult](verizon/models/device_firmware_version_update_result.py)</code> -- Device firmware version update request.

**On `Failure`**: `error` is <code>[ReportDeviceFirmwareErrorBody](verizon/errors/report_device_firmware_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def synchronize_device_firmware(acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceFirmwareList, SynchronizeDeviceFirmwareErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Synchronize ThingSpace with the FOTA server for up to 100 devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.firmware_v3.with_raw_response.synchronize_device_firmware(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceFirmwareList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SynchronizeDeviceFirmwareErrorBody
```

**Async**

```python
result = await async_client.firmware_v3.with_raw_response.synchronize_device_firmware(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceFirmwareList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SynchronizeDeviceFirmwareErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[FirmwareImei](verizon/models/firmware_imei.py) \| [FirmwareImeiDict](verizon/models/firmware_imei.py)</code> | DeviceIds to get firmware info synchronously. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceFirmwareList](verizon/models/device_firmware_list.py), [SynchronizeDeviceFirmwareErrorBody](verizon/errors/synchronize_device_firmware_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceFirmwareList](verizon/models/device_firmware_list.py)</code> -- Returns device firmware information.

**On `Failure`**: `error` is <code>[SynchronizeDeviceFirmwareErrorBody](verizon/errors/synchronize_device_firmware_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## GlobalReporting

> Source: [GlobalReporting](verizon/apis/global_reporting.py)

<details>
<summary><code>def retrieve_global_list(body: ESimglobalDeviceList | ESimglobalDeviceListDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ESimrequestResponse, RetrieveGlobalListErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a list of all devices associated with an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.global_reporting.with_raw_response.retrieve_global_list(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveGlobalListErrorBody
```

**Async**

```python
result = await async_client.global_reporting.with_raw_response.retrieve_global_list(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RetrieveGlobalListErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ESimglobalDeviceList](verizon/models/e_simglobal_device_list.py) \| [ESimglobalDeviceListDict](verizon/models/e_simglobal_device_list.py)</code> | Device List |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ESimrequestResponse](verizon/models/e_simrequest_response.py), [RetrieveGlobalListErrorBody](verizon/errors/retrieve_global_list_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RetrieveGlobalListErrorBody](verizon/errors/retrieve_global_list_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[ESimrestErrorResponse](verizon/models/e_simrest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deviceprovhistory_using_post(body: ESimprovhistoryRequest | ESimprovhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ESimrequestResponse, DeviceprovhistoryUsingPostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the provisioning history of a specific device or devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.global_reporting.with_raw_response.deviceprovhistory_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceprovhistoryUsingPostErrorBody
```

**Async**

```python
result = await async_client.global_reporting.with_raw_response.deviceprovhistory_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeviceprovhistoryUsingPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ESimprovhistoryRequest](verizon/models/e_simprovhistory_request.py) \| [ESimprovhistoryRequestDict](verizon/models/e_simprovhistory_request.py)</code> | Device Provisioning History |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ESimrequestResponse](verizon/models/e_simrequest_response.py), [DeviceprovhistoryUsingPostErrorBody](verizon/errors/deviceprovhistory_using_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[DeviceprovhistoryUsingPostErrorBody](verizon/errors/deviceprovhistory_using_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[ESimrestErrorResponse](verizon/models/e_simrest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## HplDeviceManagement

> Source: [HplDeviceManagement](verizon/apis/hpl_device_management.py)

<details>
<summary><code>def add_devices_hyper_precise(body: HplAddDevicesRequest | HplAddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[HplAddDevicesRequest], AddDevicesHyperPreciseErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Use this API if you want to manage some device settings before you are ready to activate service for the devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.hpl_device_management.with_raw_response.add_devices_hyper_precise(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[HplAddDevicesRequest]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddDevicesHyperPreciseErrorBody
```

**Async**

```python
result = await async_client.hpl_device_management.with_raw_response.add_devices_hyper_precise(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[HplAddDevicesRequest]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AddDevicesHyperPreciseErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[HplAddDevicesRequest](verizon/models/hpl_add_devices_request.py) \| [HplAddDevicesRequestDict](verizon/models/hpl_add_devices_request.py)</code> | Devices to add to the account. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[HplAddDevicesRequest](verizon/models/hpl_add_devices_request.py)&#93;, [AddDevicesHyperPreciseErrorBody](verizon/errors/add_devices_hyper_precise_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[HplAddDevicesRequest](verizon/models/hpl_add_devices_request.py)&#93;</code> -- For each device in the request, contains device identifiers and a success or failure response.

**On `Failure`**: `error` is <code>[AddDevicesHyperPreciseErrorBody](verizon/errors/add_devices_hyper_precise_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 405, 406, 429, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## HyperPreciseLocationCallbacks

> Source: [HyperPreciseLocationCallbacks](verizon/apis/hyper_precise_location_callbacks.py)

<details>
<summary><code>def deregister_callback6(account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeregisterCallback6ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Stops ThingSpace from sending callback messages for the specified account and listener name.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.hyper_precise_location_callbacks.with_raw_response.deregister_callback6(account_number, service)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback6ErrorBody
```

**Async**

```python
result = await async_client.hyper_precise_location_callbacks.with_raw_response.deregister_callback6(
    account_number, service
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback6ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_number</code> | <code>str</code> | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |
| <code>service</code> | <code>str</code> | The name of the callback service that will be deleted. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DeregisterCallback6ErrorBody](verizon/errors/deregister_callback6_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeregisterCallback6ErrorBody](verizon/errors/deregister_callback6_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_registered_callbacks6(account_number: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CallbackCreated], ListRegisteredCallbacks6ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Find registered callback listener for account by account number.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.hyper_precise_location_callbacks.with_raw_response.list_registered_callbacks6(account_number)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CallbackCreated]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks6ErrorBody
```

**Async**

```python
result = await async_client.hyper_precise_location_callbacks.with_raw_response.list_registered_callbacks6(
    account_number
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CallbackCreated]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks6ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_number</code> | <code>str</code> | The numeric ID of the account and must include leading zeroes. This value is indentical to `accountName`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[CallbackCreated](verizon/models/callback_created.py)&#93;, [ListRegisteredCallbacks6ErrorBody](verizon/errors/list_registered_callbacks6_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CallbackCreated](verizon/models/callback_created.py)&#93;</code> -- A successful response will display the billing account number (`accountName`), the name of the callback service (`name`) and the address of the callback listening service (`url`).

**On `Failure`**: `error` is <code>[ListRegisteredCallbacks6ErrorBody](verizon/errors/list_registered_callbacks6_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_callback6(account_number: str, body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CallbackRegistered, RegisterCallback6ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers a URL at which an account receives asynchronous responses and other messages from a ThingSpace Platform callback service. The messages are REST messages. You are responsible for creating and running a listening process on your server at that URL to receive and parse the messages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.hyper_precise_location_callbacks.with_raw_response.register_callback6(account_number, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackRegistered
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback6ErrorBody
```

**Async**

```python
result = await async_client.hyper_precise_location_callbacks.with_raw_response.register_callback6(account_number, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackRegistered
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback6ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_number</code> | <code>str</code> | A unique identifier for an account. |
| <code>body</code> | <code>[HyperPreciseLocationCallback](verizon/models/hyper_precise_location_callback.py) \| [HyperPreciseLocationCallbackDict](verizon/models/hyper_precise_location_callback.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CallbackRegistered](verizon/models/callback_registered.py), [RegisterCallback6ErrorBody](verizon/errors/register_callback6_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CallbackRegistered](verizon/models/callback_registered.py)</code> -- A successful response will display the billing account number (`accountName`), the name of the callback service (`name`) and the address of the callback listening service (`url`).

**On `Failure`**: `error` is <code>[RegisterCallback6ErrorBody](verizon/errors/register_callback6_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 409, 500 | <code>[HyperPreciseLocationResult](verizon/models/hyper_precise_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## IntelligenceServiceController

> Source: [IntelligenceServiceController](verizon/apis/intelligence_service_controller.py)

<details>
<summary><code>def set_connection_planner(*, body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AsynchronousRequestResultforplanner, SetConnectionPlannerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves available device windows for Connection Planner.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.intelligence_service_controller.with_raw_response.set_connection_planner()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsynchronousRequestResultforplanner
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetConnectionPlannerErrorBody
```

**Async**

```python
result = await async_client.intelligence_service_controller.with_raw_response.set_connection_planner()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AsynchronousRequestResultforplanner
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetConnectionPlannerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetDevicesWindowsRequestforplanner](verizon/models/get_devices_windows_requestforplanner.py) \| [GetDevicesWindowsRequestforplannerDict](verizon/models/get_devices_windows_requestforplanner.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AsynchronousRequestResultforplanner](verizon/models/asynchronous_request_resultforplanner.py), [SetConnectionPlannerErrorBody](verizon/errors/set_connection_planner_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AsynchronousRequestResultforplanner](verizon/models/asynchronous_request_resultforplanner.py)</code> -- The asynchronous request status.

**On `Failure`**: `error` is <code>[SetConnectionPlannerErrorBody](verizon/errors/set_connection_planner_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 406, 429 | <code>[RestErrorResponseforplanner](verizon/models/rest_error_responseforplanner.py)</code> |
| 401 | <code>[AuthRestErrorResponseforplanner](verizon/models/auth_rest_error_responseforplanner.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def status_connection_planner(*, body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetDeviceStatusesResponseforplanner, StatusConnectionPlannerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the device status for the Connection Planner service.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.intelligence_service_controller.with_raw_response.status_connection_planner()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeviceStatusesResponseforplanner
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StatusConnectionPlannerErrorBody
```

**Async**

```python
result = await async_client.intelligence_service_controller.with_raw_response.status_connection_planner()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeviceStatusesResponseforplanner
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StatusConnectionPlannerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetDeviceStatusesRequestforplanner](verizon/models/get_device_statuses_requestforplanner.py) \| [GetDeviceStatusesRequestforplannerDict](verizon/models/get_device_statuses_requestforplanner.py) \| None</code> | The request body.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GetDeviceStatusesResponseforplanner](verizon/models/get_device_statuses_responseforplanner.py), [StatusConnectionPlannerErrorBody](verizon/errors/status_connection_planner_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetDeviceStatusesResponseforplanner](verizon/models/get_device_statuses_responseforplanner.py)</code> -- Success

**On `Failure`**: `error` is <code>[StatusConnectionPlannerErrorBody](verizon/errors/status_connection_planner_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 403, 404, 406, 429 | <code>[RestErrorResponseforplanner](verizon/models/rest_error_responseforplanner.py)</code> |
| 401 | <code>[AuthRestErrorResponseforplanner](verizon/models/auth_rest_error_responseforplanner.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ManagingESimProfiles

> Source: [ManagingESimProfiles](verizon/apis/managing_e_sim_profiles.py)

<details>
<summary><code>def activate_a_device_profile(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activate a device with either a lead or local profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.activate_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.activate_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GioprofileRequest](verizon/models/gioprofile_request.py) \| [GioprofileRequestDict](verizon/models/gioprofile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_a_device_profile(body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deactivate the lead or local profile. **Note:** to reactivate the profile, use the **Activate** endpoint above.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.deactivate_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.deactivate_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GiodeactivateDeviceProfileRequest](verizon/models/giodeactivate_device_profile_request.py) \| [GiodeactivateDeviceProfileRequestDict](verizon/models/giodeactivate_device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a device profile for Global IoT Orchestration. **Note:** the profile must be deactivated first!

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.delete_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.delete_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceProfileRequest](verizon/models/device_profile_request.py) \| [DeviceProfileRequestDict](verizon/models/device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def device_suspend(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Suspend all service to an eUICC device, including the lead and local profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.device_suspend(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.device_suspend(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GioprofileRequest](verizon/models/gioprofile_request.py) \| [GioprofileRequestDict](verizon/models/gioprofile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Download a Global IoT Orchestration device profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.download_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.download_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceProfileRequest](verizon/models/device_profile_request.py) \| [DeviceProfileRequestDict](verizon/models/device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable a device lead or local profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.enable_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.enable_a_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceProfileRequest](verizon/models/device_profile_request.py) \| [DeviceProfileRequestDict](verizon/models/device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_a_device_profile_for_download(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable the Global IoT Orchestration device profile for download.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.enable_a_device_profile_for_download(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.enable_a_device_profile_for_download(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeviceProfileRequest](verizon/models/device_profile_request.py) \| [DeviceProfileRequestDict](verizon/models/device_profile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_suspend(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Suspend a device's Global profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.profile_suspend(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.profile_suspend(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GioprofileRequest](verizon/models/gioprofile_request.py) \| [GioprofileRequestDict](verizon/models/gioprofile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def resume_profile(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Resume service to a device with either a lead or local profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.resume_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.resume_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GioprofileRequest](verizon/models/gioprofile_request.py) \| [GioprofileRequestDict](verizon/models/gioprofile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_fallback(body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GiorequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable a fallback profile to be set.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.managing_e_sim_profiles.with_raw_response.set_fallback(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.managing_e_sim_profiles.with_raw_response.set_fallback(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GiorequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[FallBack](verizon/models/fall_back.py) \| [FallBackDict](verizon/models/fall_back.py)</code> | Set the fallback attributes to allow a fallback profile to be activated. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GiorequestResponse](verizon/models/giorequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Pwn

> Source: [Pwn](verizon/apis/pwn.py)

<details>
<summary><code>def change_pwn_device_i_paddress(body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChangePwndeviceIpaddressResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PUT` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.change_pwn_device_i_paddress(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceIpaddressResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.change_pwn_device_i_paddress(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceIpaddressResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ChangePwndeviceIpaddressRequest](verizon/models/change_pwndevice_ipaddress_request.py) \| [ChangePwndeviceIpaddressRequestDict](verizon/models/change_pwndevice_ipaddress_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ChangePwndeviceIpaddressResponse](verizon/models/change_pwndevice_ipaddress_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChangePwndeviceIpaddressResponse](verizon/models/change_pwndevice_ipaddress_response.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_pwn_device_profile(body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChangePwndeviceProfileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.change_pwn_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.change_pwn_device_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ChangePwndeviceProfileRequest](verizon/models/change_pwndevice_profile_request.py) \| [ChangePwndeviceProfileRequestDict](verizon/models/change_pwndevice_profile_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ChangePwndeviceProfileResponse](verizon/models/change_pwndevice_profile_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChangePwndeviceProfileResponse](verizon/models/change_pwndevice_profile_response.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_pwn_device_state_activate(body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChangePwndeviceStateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.change_pwn_device_state_activate(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.change_pwn_device_state_activate(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ChangePwndeviceStateActivateRequest](verizon/models/change_pwndevice_state_activate_request.py) \| [ChangePwndeviceStateActivateRequestDict](verizon/models/change_pwndevice_state_activate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ChangePwndeviceStateResponse](verizon/models/change_pwndevice_state_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChangePwndeviceStateResponse](verizon/models/change_pwndevice_state_response.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_pwn_device_state_deactivate(body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChangePwndeviceStateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.change_pwn_device_state_deactivate(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.change_pwn_device_state_deactivate(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangePwndeviceStateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ChangePwndeviceStateDeactivateRequest](verizon/models/change_pwndevice_state_deactivate_request.py) \| [ChangePwndeviceStateDeactivateRequestDict](verizon/models/change_pwndevice_state_deactivate_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ChangePwndeviceStateResponse](verizon/models/change_pwndevice_state_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChangePwndeviceStateResponse](verizon/models/change_pwndevice_state_response.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_pwn_performance_consent(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPwnperformanceConsentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.get_pwn_performance_consent(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPwnperformanceConsentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.get_pwn_performance_consent(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPwnperformanceConsentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GetPwnperformanceConsentResponse](verizon/models/get_pwnperformance_consent_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPwnperformanceConsentResponse](verizon/models/get_pwnperformance_consent_response.py)</code> -- consent received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_profile_list(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PwnprofileList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.get_profile_list(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PwnprofileList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.get_profile_list(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PwnprofileList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[PwnprofileList](verizon/models/pwnprofile_list.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PwnprofileList](verizon/models/pwnprofile_list.py)</code> -- PWN profiles list received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def kpi_list(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[KpiinfoList, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.pwn.with_raw_response.kpi_list(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type KpiinfoList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.pwn.with_raw_response.kpi_list(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type KpiinfoList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[KpiinfoList](verizon/models/kpiinfo_list.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[KpiinfoList](verizon/models/kpiinfo_list.py)</code> -- Kpi list received on a successful response.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## PromotionPeriodInformation

> Source: [PromotionPeriodInformation](verizon/apis/promotion_period_information.py)

<details>
<summary><code>def get_promo_device_aggregate_usage_history(body: RequestBodyForUsage | RequestBodyForUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsageRequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the aggregate usage for an account using pseudo-MDN during the promotional period using a callback.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.promotion_period_information.with_raw_response.get_promo_device_aggregate_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageRequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.promotion_period_information.with_raw_response.get_promo_device_aggregate_usage_history(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageRequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RequestBodyForUsage](verizon/models/request_body_for_usage.py) \| [RequestBodyForUsageDict](verizon/models/request_body_for_usage.py)</code> | Retrieve Aggregate Usage |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UsageRequestResponse](verizon/models/usage_request_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsageRequestResponse](verizon/models/usage_request_response.py)</code> -- Request response

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_promo_device_usage_history(body: ARequestBodyForUsage | ARequestBodyForUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ResponseToUsageQuery, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the usage history of a device during the promotion period.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.promotion_period_information.with_raw_response.get_promo_device_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResponseToUsageQuery
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.promotion_period_information.with_raw_response.get_promo_device_usage_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResponseToUsageQuery
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ARequestBodyForUsage](verizon/models/a_request_body_for_usage.py) \| [ARequestBodyForUsageDict](verizon/models/a_request_body_for_usage.py)</code> | Retrieve Aggregate Usage |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ResponseToUsageQuery](verizon/models/response_to_usage_query.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ResponseToUsageQuery](verizon/models/response_to_usage_query.py)</code> -- Usage History

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## RetrieveRatePlanList

> Source: [RetrieveRatePlanList](verizon/apis/retrieve_rate_plan_list.py)

<details>
<summary><code>def get_rate_plan_list(ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Rateplan, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the rate plans and rate plan details for a profile ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.retrieve_rate_plan_list.with_raw_response.get_rate_plan_list(ecpd_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Rateplan
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.retrieve_rate_plan_list.with_raw_response.get_rate_plan_list(ecpd_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Rateplan
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>ecpd_id</code> | <code>str</code> | The Enterprise Customer Profile Database ID. This is the same as the accountName value |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Rateplan](verizon/models/rateplan.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Rateplan](verizon/models/rateplan.py)</code> -- This is a syncronous response showing the rate plans associated.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## RetrieveTheTriggers

> Source: [RetrieveTheTriggers](verizon/apis/retrieve_the_triggers.py)

<details>
<summary><code>def get_all_available_triggers(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TriggerValueResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves all of the available triggers for pseudo-MDN.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.retrieve_the_triggers.with_raw_response.get_all_available_triggers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.retrieve_the_triggers.with_raw_response.get_all_available_triggers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TriggerValueResponse](verizon/models/trigger_value_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TriggerValueResponse](verizon/models/trigger_value_response.py)</code> -- Status of Request

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_triggers_by_account_name(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TriggerValueResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve the triggers associated with an account name.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.retrieve_the_triggers.with_raw_response.get_all_triggers_by_account_name(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.retrieve_the_triggers.with_raw_response.get_all_triggers_by_account_name(account_name)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | The account name |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TriggerValueResponse](verizon/models/trigger_value_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TriggerValueResponse](verizon/models/trigger_value_response.py)</code> -- Status of Request

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_triggers_by_trigger_category(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TriggerValueResponse2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves all of the triggers for the specified account associated with the PromoAlert category

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.retrieve_the_triggers.with_raw_response.get_all_triggers_by_trigger_category()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.retrieve_the_triggers.with_raw_response.get_all_triggers_by_trigger_category()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TriggerValueResponse2](verizon/models/trigger_value_response2.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TriggerValueResponse2](verizon/models/trigger_value_response2.py)</code> -- Request response

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_triggers_by_id(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TriggerValueResponse2, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrives a specific trigger by its ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.retrieve_the_triggers.with_raw_response.get_triggers_by_id(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.retrieve_the_triggers.with_raw_response.get_triggers_by_id(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerValueResponse2
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | The ID of a specific trigger |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TriggerValueResponse2](verizon/models/trigger_value_response2.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TriggerValueResponse2](verizon/models/trigger_value_response2.py)</code> -- Request response

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## SimActions

> Source: [SimActions](verizon/apis/sim_actions.py)

<details>
<summary><code>def newactivatecode(body: ESimprofileRequest2 | ESimprofileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ESimrequestResponse, NewactivatecodeErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

System assign a new activation code to reactivate a deactivated device. **Note:** the previously assigned ICCID must be used to request a new activation code.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sim_actions.with_raw_response.newactivatecode(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type NewactivatecodeErrorBody
```

**Async**

```python
result = await async_client.sim_actions.with_raw_response.newactivatecode(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type NewactivatecodeErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ESimprofileRequest2](verizon/models/e_simprofile_request2.py) \| [ESimprofileRequest2Dict](verizon/models/e_simprofile_request2.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ESimrequestResponse](verizon/models/e_simrequest_response.py), [NewactivatecodeErrorBody](verizon/errors/newactivatecode_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[NewactivatecodeErrorBody](verizon/errors/newactivatecode_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[ESimrestErrorResponse](verizon/models/e_simrest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def setactivate_using_post(body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ESimrequestResponse, SetactivateUsingPostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the profile to activate the SIM.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sim_actions.with_raw_response.setactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetactivateUsingPostErrorBody
```

**Async**

```python
result = await async_client.sim_actions.with_raw_response.setactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetactivateUsingPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ESimprofileRequest](verizon/models/e_simprofile_request.py) \| [ESimprofileRequestDict](verizon/models/e_simprofile_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ESimrequestResponse](verizon/models/e_simrequest_response.py), [SetactivateUsingPostErrorBody](verizon/errors/setactivate_using_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[SetactivateUsingPostErrorBody](verizon/errors/setactivate_using_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[ESimrestErrorResponse](verizon/models/e_simrest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def setdeactivate_using_post(body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ESimrequestResponse, SetdeactivateUsingPostErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uses the profile to deactivate the SIM.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sim_actions.with_raw_response.setdeactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetdeactivateUsingPostErrorBody
```

**Async**

```python
result = await async_client.sim_actions.with_raw_response.setdeactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ESimrequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SetdeactivateUsingPostErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileRequest2](verizon/models/profile_request2.py) \| [ProfileRequest2Dict](verizon/models/profile_request2.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ESimrequestResponse](verizon/models/e_simrequest_response.py), [SetdeactivateUsingPostErrorBody](verizon/errors/setdeactivate_using_post_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[SetdeactivateUsingPostErrorBody](verizon/errors/setdeactivate_using_post_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[ESimrestErrorResponse](verizon/models/e_simrest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SimSecureForIoTLicenses

> Source: [SimSecureForIoTLicenses](verizon/apis/sim_secure_for_io_t_licenses.py)

<details>
<summary><code>def assign_license_to_devices(body: AssignLicenseRequest | AssignLicenseRequestDict, *, x_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SecuritySuccessResult, AssignLicenseToDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Assigns SIM-Secure for IoT licenses to SIMs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sim_secure_for_io_t_licenses.with_raw_response.assign_license_to_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecuritySuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicenseToDevicesErrorBody
```

**Async**

```python
result = await async_client.sim_secure_for_io_t_licenses.with_raw_response.assign_license_to_devices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecuritySuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicenseToDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[AssignLicenseRequest](verizon/models/assign_license_request.py) \| [AssignLicenseRequestDict](verizon/models/assign_license_request.py)</code> | Request to assign license to devices. |
| <code>x_request_id</code> | <code>str \| None</code> | Transaction Id.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SecuritySuccessResult](verizon/models/security_success_result.py), [AssignLicenseToDevicesErrorBody](verizon/errors/assign_license_to_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SecuritySuccessResult](verizon/models/security_success_result.py)</code> -- Success response.

**On `Failure`**: `error` is <code>[AssignLicenseToDevicesErrorBody](verizon/errors/assign_license_to_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[SecurityResult](verizon/models/security_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unassign_license_to_devices(x_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SecuritySuccessResult, UnassignLicenseToDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from SIMs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sim_secure_for_io_t_licenses.with_raw_response.unassign_license_to_devices(x_request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecuritySuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnassignLicenseToDevicesErrorBody
```

**Async**

```python
result = await async_client.sim_secure_for_io_t_licenses.with_raw_response.unassign_license_to_devices(x_request_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SecuritySuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UnassignLicenseToDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>x_request_id</code> | <code>str</code> | Transaction Id. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SecuritySuccessResult](verizon/models/security_success_result.py), [UnassignLicenseToDevicesErrorBody](verizon/errors/unassign_license_to_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SecuritySuccessResult](verizon/models/security_success_result.py)</code> -- Success response.

**On `Failure`**: `error` is <code>[UnassignLicenseToDevicesErrorBody](verizon/errors/unassign_license_to_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 429 | <code>[SecurityResult](verizon/models/security_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Sms

> Source: [Sms](verizon/apis/sms.py)

<details>
<summary><code>def list_devices_sms_messages(aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SmsmessagesQueryResult, ListDevicesSmsmessagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

When HTTP status is 202, a URL will be returned in the Location header of the form /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sms.with_raw_response.list_devices_sms_messages(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SmsmessagesQueryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesSmsmessagesErrorBody
```

**Async**

```python
result = await async_client.sms.with_raw_response.list_devices_sms_messages(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SmsmessagesQueryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListDevicesSmsmessagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>next</code> | <code>int \| None</code> | Continue the previous query from the URL in Location Header.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SmsmessagesQueryResult](verizon/models/smsmessages_query_result.py), [ListDevicesSmsmessagesErrorBody](verizon/errors/list_devices_smsmessages_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SmsmessagesQueryResult](verizon/models/smsmessages_query_result.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[ListDevicesSmsmessagesErrorBody](verizon/errors/list_devices_smsmessages_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_sms_to_device(body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, SendSmstoDeviceErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due to traffic and routing considerations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sms.with_raw_response.send_sms_to_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SendSmstoDeviceErrorBody
```

**Async**

```python
result = await async_client.sms.with_raw_response.send_sms_to_device(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SendSmstoDeviceErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SmssendRequest](verizon/models/smssend_request.py) \| [SmssendRequestDict](verizon/models/smssend_request.py)</code> | Request to send SMS. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [SendSmstoDeviceErrorBody](verizon/errors/send_smsto_device_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[SendSmstoDeviceErrorBody](verizon/errors/send_smsto_device_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_queued_sms_delivery(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ConnectivityManagementSuccessResult, StartQueuedSmsdeliveryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by your application, either by callback or synchronously with GET /sms/{accountName}/history.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sms.with_raw_response.start_queued_sms_delivery(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StartQueuedSmsdeliveryErrorBody
```

**Async**

```python
result = await async_client.sms.with_raw_response.start_queued_sms_delivery(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ConnectivityManagementSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StartQueuedSmsdeliveryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py), [StartQueuedSmsdeliveryErrorBody](verizon/errors/start_queued_smsdelivery_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response.

**On `Failure`**: `error` is <code>[StartQueuedSmsdeliveryErrorBody](verizon/errors/start_queued_smsdelivery_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsDeviceProfile

> Source: [SensorInsightsDeviceProfile](verizon/apis/sensor_insights_device_profile.py)

<details>
<summary><code>def create_a_profile(body: DtoConfigurationProfile | DtoConfigurationProfileDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DtoProfileResponse], CreateAprofileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a device profile

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_device_profile.with_raw_response.create_a_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAprofileErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_device_profile.with_raw_response.create_a_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateAprofileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoConfigurationProfile](verizon/models/dto_configuration_profile.py) \| [DtoConfigurationProfileDict](verizon/models/dto_configuration_profile.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;, [CreateAprofileErrorBody](verizon/errors/create_aprofile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[CreateAprofileErrorBody](verizon/errors/create_aprofile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_a_profile(deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DtoProfileResponse], DeleteAprofileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a device profile

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_device_profile.with_raw_response.delete_a_profile(deleterequest)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteAprofileErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_device_profile.with_raw_response.delete_a_profile(deleterequest)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteAprofileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>deleterequest</code> | <code>[DtoConfigurationProfileDelete](verizon/models/dto_configuration_profile_delete.py) \| [DtoConfigurationProfileDeleteDict](verizon/models/dto_configuration_profile_delete.py)</code> | payload for the delete request |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;, [DeleteAprofileErrorBody](verizon/errors/delete_aprofile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[DeleteAprofileErrorBody](verizon/errors/delete_aprofile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_a_profile(body: ResourceResourceQuery | ResourceResourceQueryDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DtoProfileResponse], QueryAprofileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Query a device profile for an individual device

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_device_profile.with_raw_response.query_a_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryAprofileErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_device_profile.with_raw_response.query_a_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryAprofileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ResourceResourceQuery](verizon/models/resource_resource_query.py) \| [ResourceResourceQueryDict](verizon/models/resource_resource_query.py)</code> | body |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;, [QueryAprofileErrorBody](verizon/errors/query_aprofile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[QueryAprofileErrorBody](verizon/errors/query_aprofile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_a_profile(body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DtoProfileResponse], UpdateAprofileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Partially update a device profile

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_device_profile.with_raw_response.update_a_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateAprofileErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_device_profile.with_raw_response.update_a_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoProfileResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateAprofileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoConfigurationProfilePath](verizon/models/dto_configuration_profile_path.py) \| [DtoConfigurationProfilePathDict](verizon/models/dto_configuration_profile_path.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;, [UpdateAprofileErrorBody](verizon/errors/update_aprofile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[UpdateAprofileErrorBody](verizon/errors/update_aprofile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsDevices

> Source: [SensorInsightsDevices](verizon/apis/sensor_insights_devices.py)

<details>
<summary><code>def sensor_insights_device_action_set_request(body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoDeviceActionSetResponse, SensorInsightsDeviceActionSetRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_devices.with_raw_response.sensor_insights_device_action_set_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoDeviceActionSetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsDeviceActionSetRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_devices.with_raw_response.sensor_insights_device_action_set_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoDeviceActionSetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsDeviceActionSetRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DmV1DevicesActionsSetRequest](verizon/models/unions/dm_v1_devices_actions_set_request.py) \| [DmV1DevicesActionsSetRequestDict](verizon/models/unions/dm_v1_devices_actions_set_request.py)</code> | Set device configuration |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoDeviceActionSetResponse](verizon/models/dto_device_action_set_response.py), [SensorInsightsDeviceActionSetRequestErrorBody](verizon/errors/sensor_insights_device_action_set_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoDeviceActionSetResponse](verizon/models/dto_device_action_set_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsDeviceActionSetRequestErrorBody](verizon/errors/sensor_insights_device_action_set_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_last_reported_time_request(body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoLastReportedTimeResponse, SensorInsightsLastReportedTimeRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_devices.with_raw_response.sensor_insights_last_reported_time_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoLastReportedTimeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsLastReportedTimeRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_devices.with_raw_response.sensor_insights_last_reported_time_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoLastReportedTimeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsLastReportedTimeRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoLastReportedTimeRequest](verizon/models/dto_last_reported_time_request.py) \| [DtoLastReportedTimeRequestDict](verizon/models/dto_last_reported_time_request.py)</code> | Get the last reported information for a device |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoLastReportedTimeResponse](verizon/models/dto_last_reported_time_response.py), [SensorInsightsLastReportedTimeRequestErrorBody](verizon/errors/sensor_insights_last_reported_time_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoLastReportedTimeResponse](verizon/models/dto_last_reported_time_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsLastReportedTimeRequestErrorBody](verizon/errors/sensor_insights_last_reported_time_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_list_device_experience_history_request(body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[UserDeviceExperienceHistory], SensorInsightsListDeviceExperienceHistoryRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_devices.with_raw_response.sensor_insights_list_device_experience_history_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UserDeviceExperienceHistory]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListDeviceExperienceHistoryRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_devices.with_raw_response.sensor_insights_list_device_experience_history_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UserDeviceExperienceHistory]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListDeviceExperienceHistoryRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListDeviceExperienceHistoryRequest](verizon/models/dto_list_device_experience_history_request.py) \| [DtoListDeviceExperienceHistoryRequestDict](verizon/models/dto_list_device_experience_history_request.py)</code> | List the device experience |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[UserDeviceExperienceHistory](verizon/models/user_device_experience_history.py)&#93;, [SensorInsightsListDeviceExperienceHistoryRequestErrorBody](verizon/errors/sensor_insights_list_device_experience_history_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[UserDeviceExperienceHistory](verizon/models/user_device_experience_history.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListDeviceExperienceHistoryRequestErrorBody](verizon/errors/sensor_insights_list_device_experience_history_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_list_devices_request(body: DtoListDevicesRequest | DtoListDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DtoExpandedDeviceResponse], SensorInsightsListDevicesRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_devices.with_raw_response.sensor_insights_list_devices_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoExpandedDeviceResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListDevicesRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_devices.with_raw_response.sensor_insights_list_devices_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoExpandedDeviceResponse]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListDevicesRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListDevicesRequest](verizon/models/dto_list_devices_request.py) \| [DtoListDevicesRequestDict](verizon/models/dto_list_devices_request.py)</code> | List all device details on an account |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DtoExpandedDeviceResponse](verizon/models/dto_expanded_device_response.py)&#93;, [SensorInsightsListDevicesRequestErrorBody](verizon/errors/sensor_insights_list_devices_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DtoExpandedDeviceResponse](verizon/models/dto_expanded_device_response.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListDevicesRequestErrorBody](verizon/errors/sensor_insights_list_devices_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 406, 415, 429, 500 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_list_network_experience_history_request(body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[UserNetworkExperienceHistory], SensorInsightsListNetworkExperienceHistoryRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_devices.with_raw_response.sensor_insights_list_network_experience_history_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UserNetworkExperienceHistory]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListNetworkExperienceHistoryRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_devices.with_raw_response.sensor_insights_list_network_experience_history_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UserNetworkExperienceHistory]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListNetworkExperienceHistoryRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListNetworkExperienceHistoryRequest](verizon/models/dto_list_network_experience_history_request.py) \| [DtoListNetworkExperienceHistoryRequestDict](verizon/models/dto_list_network_experience_history_request.py)</code> | List the network experience |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[UserNetworkExperienceHistory](verizon/models/user_network_experience_history.py)&#93;, [SensorInsightsListNetworkExperienceHistoryRequestErrorBody](verizon/errors/sensor_insights_list_network_experience_history_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[UserNetworkExperienceHistory](verizon/models/user_network_experience_history.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListNetworkExperienceHistoryRequestErrorBody](verizon/errors/sensor_insights_list_network_experience_history_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_patch_device_request(body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ResourceDevice, SensorInsightsPatchDeviceRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_devices.with_raw_response.sensor_insights_patch_device_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceDevice
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsPatchDeviceRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_devices.with_raw_response.sensor_insights_patch_device_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceDevice
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsPatchDeviceRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoPatchDeviceRequest](verizon/models/dto_patch_device_request.py) \| [DtoPatchDeviceRequestDict](verizon/models/dto_patch_device_request.py)</code> | Partially update a device's details |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ResourceDevice](verizon/models/resource_device.py), [SensorInsightsPatchDeviceRequestErrorBody](verizon/errors/sensor_insights_patch_device_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ResourceDevice](verizon/models/resource_device.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsPatchDeviceRequestErrorBody](verizon/errors/sensor_insights_patch_device_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsGateways

> Source: [SensorInsightsGateways](verizon/apis/sensor_insights_gateways.py)

<details>
<summary><code>def sensor_insights_list_gateway_devices_request(body: DtoListDevicesRequest | DtoListDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ResourceDevice], SensorInsightsListGatewayDevicesRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_gateways.with_raw_response.sensor_insights_list_gateway_devices_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceDevice]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListGatewayDevicesRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_gateways.with_raw_response.sensor_insights_list_gateway_devices_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceDevice]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListGatewayDevicesRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListDevicesRequest](verizon/models/dto_list_devices_request.py) \| [DtoListDevicesRequestDict](verizon/models/dto_list_devices_request.py)</code> | Get gateway information |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ResourceDevice](verizon/models/resource_device.py)&#93;, [SensorInsightsListGatewayDevicesRequestErrorBody](verizon/errors/sensor_insights_list_gateway_devices_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ResourceDevice](verizon/models/resource_device.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListGatewayDevicesRequestErrorBody](verizon/errors/sensor_insights_list_gateway_devices_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsHealthScore

> Source: [SensorInsightsHealthScore](verizon/apis/sensor_insights_health_score.py)

<details>
<summary><code>def sensor_insights_get_network_health_score_response(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoGetNetworkHealthScoreResponse, SensorInsightsGetNetworkHealthScoreResponseErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_health_score.with_raw_response.sensor_insights_get_network_health_score_response()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoGetNetworkHealthScoreResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsGetNetworkHealthScoreResponseErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_health_score.with_raw_response.sensor_insights_get_network_health_score_response()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoGetNetworkHealthScoreResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsGetNetworkHealthScoreResponseErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoGetNetworkHealthScoreResponse](verizon/models/dto_get_network_health_score_response.py), [SensorInsightsGetNetworkHealthScoreResponseErrorBody](verizon/errors/sensor_insights_get_network_health_score_response_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoGetNetworkHealthScoreResponse](verizon/models/dto_get_network_health_score_response.py)</code> -- Get a network health score

**On `Failure`**: `error` is <code>[SensorInsightsGetNetworkHealthScoreResponseErrorBody](verizon/errors/sensor_insights_get_network_health_score_response_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_health_score_summary(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoHealthScoreSummary, SensorInsightsHealthScoreSummaryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_health_score.with_raw_response.sensor_insights_health_score_summary()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoHealthScoreSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsHealthScoreSummaryErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_health_score.with_raw_response.sensor_insights_health_score_summary()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoHealthScoreSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsHealthScoreSummaryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoHealthScoreSummary](verizon/models/dto_health_score_summary.py), [SensorInsightsHealthScoreSummaryErrorBody](verizon/errors/sensor_insights_health_score_summary_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoHealthScoreSummary](verizon/models/dto_health_score_summary.py)</code> -- Get health score summary

**On `Failure`**: `error` is <code>[SensorInsightsHealthScoreSummaryErrorBody](verizon/errors/sensor_insights_health_score_summary_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsNotificationGroups

> Source: [SensorInsightsNotificationGroups](verizon/apis/sensor_insights_notification_groups.py)

<details>
<summary><code>def sensor_insights_add_users_to_notification_group_request(body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SensorInsightsAddUsersToNotificationGroupRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_notification_groups.with_raw_response.sensor_insights_add_users_to_notification_group_request(
    body
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsAddUsersToNotificationGroupRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_notification_groups.with_raw_response.sensor_insights_add_users_to_notification_group_request(
    body
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsAddUsersToNotificationGroupRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoAddUsersToNotificationGroupRequest](verizon/models/dto_add_users_to_notification_group_request.py) \| [DtoAddUsersToNotificationGroupRequestDict](verizon/models/dto_add_users_to_notification_group_request.py)</code> | Add users to a notification group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [SensorInsightsAddUsersToNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_add_users_to_notification_group_request_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SensorInsightsAddUsersToNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_add_users_to_notification_group_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_create_notification_group_request(body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsCreateNotificationGroupRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_notification_groups.with_raw_response.sensor_insights_create_notification_group_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoNotificationGroupResponseEntity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsCreateNotificationGroupRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_notification_groups.with_raw_response.sensor_insights_create_notification_group_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoNotificationGroupResponseEntity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsCreateNotificationGroupRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoCreateNotificationGroupRequest](verizon/models/dto_create_notification_group_request.py) \| [DtoCreateNotificationGroupRequestDict](verizon/models/dto_create_notification_group_request.py)</code> | Create a notification group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py), [SensorInsightsCreateNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_create_notification_group_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsCreateNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_create_notification_group_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_delete_notification_group(payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SensorInsightsDeleteNotificationGroupErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_notification_groups.with_raw_response.sensor_insights_delete_notification_group(payload)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsDeleteNotificationGroupErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_notification_groups.with_raw_response.sensor_insights_delete_notification_group(
    payload
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsDeleteNotificationGroupErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payload</code> | <code>[DtoDeleteNotificationGroupRequest](verizon/models/dto_delete_notification_group_request.py) \| [DtoDeleteNotificationGroupRequestDict](verizon/models/dto_delete_notification_group_request.py)</code> | Payload for the delete request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [SensorInsightsDeleteNotificationGroupErrorBody](verizon/errors/sensor_insights_delete_notification_group_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SensorInsightsDeleteNotificationGroupErrorBody](verizon/errors/sensor_insights_delete_notification_group_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_list_notification_group_request(body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DtoNotificationGroupResponseEntity], SensorInsightsListNotificationGroupRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_notification_groups.with_raw_response.sensor_insights_list_notification_group_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoNotificationGroupResponseEntity]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListNotificationGroupRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_notification_groups.with_raw_response.sensor_insights_list_notification_group_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DtoNotificationGroupResponseEntity]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListNotificationGroupRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListNotificationGroupRequest](verizon/models/dto_list_notification_group_request.py) \| [DtoListNotificationGroupRequestDict](verizon/models/dto_list_notification_group_request.py)</code> | Retrieve a notification group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)&#93;, [SensorInsightsListNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_list_notification_group_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_list_notification_group_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_remove_users_from_notification_group_request(body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_notification_groups.with_raw_response.sensor_insights_remove_users_from_notification_group_request(
    body
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_notification_groups.with_raw_response.sensor_insights_remove_users_from_notification_group_request(
    body
)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoRemoveUsersFromNotificationGroupRequest](verizon/models/dto_remove_users_from_notification_group_request.py) \| [DtoRemoveUsersFromNotificationGroupRequestDict](verizon/models/dto_remove_users_from_notification_group_request.py)</code> | Remove users from a notification group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_remove_users_from_notification_group_request_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_remove_users_from_notification_group_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_update_notification_group_request(body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoNotificationGroupResponseEntity, SensorInsightsUpdateNotificationGroupRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_notification_groups.with_raw_response.sensor_insights_update_notification_group_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoNotificationGroupResponseEntity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsUpdateNotificationGroupRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_notification_groups.with_raw_response.sensor_insights_update_notification_group_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoNotificationGroupResponseEntity
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsUpdateNotificationGroupRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoUpdateNotificationGroupRequest](verizon/models/dto_update_notification_group_request.py) \| [DtoUpdateNotificationGroupRequestDict](verizon/models/dto_update_notification_group_request.py)</code> | Partially update a notification group |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py), [SensorInsightsUpdateNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_update_notification_group_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsUpdateNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_update_notification_group_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsRules

> Source: [SensorInsightsRules](verizon/apis/sensor_insights_rules.py)

<details>
<summary><code>def sensor_insights_list_rules_request(body: DtoListRulesRequest | DtoListRulesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ResourceRule], SensorInsightsListRulesRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_rules.with_raw_response.sensor_insights_list_rules_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceRule]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListRulesRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_rules.with_raw_response.sensor_insights_list_rules_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceRule]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListRulesRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListRulesRequest](verizon/models/dto_list_rules_request.py) \| [DtoListRulesRequestDict](verizon/models/dto_list_rules_request.py)</code> | Retrieve a rule |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ResourceRule](verizon/models/resource_rule.py)&#93;, [SensorInsightsListRulesRequestErrorBody](verizon/errors/sensor_insights_list_rules_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ResourceRule](verizon/models/resource_rule.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListRulesRequestErrorBody](verizon/errors/sensor_insights_list_rules_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_overwrite_rule_request(body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ResourceRule, SensorInsightsOverwriteRuleRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_rules.with_raw_response.sensor_insights_overwrite_rule_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceRule
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsOverwriteRuleRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_rules.with_raw_response.sensor_insights_overwrite_rule_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceRule
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsOverwriteRuleRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoOverwriteRuleRequest](verizon/models/dto_overwrite_rule_request.py) \| [DtoOverwriteRuleRequestDict](verizon/models/dto_overwrite_rule_request.py)</code> | Overwrite a rule |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ResourceRule](verizon/models/resource_rule.py), [SensorInsightsOverwriteRuleRequestErrorBody](verizon/errors/sensor_insights_overwrite_rule_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ResourceRule](verizon/models/resource_rule.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsOverwriteRuleRequestErrorBody](verizon/errors/sensor_insights_overwrite_rule_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsSensors

> Source: [SensorInsightsSensors](verizon/apis/sensor_insights_sensors.py)

<details>
<summary><code>def sensor_insights_list_sensor_devices_request(body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ResourceDevice], SensorInsightsListSensorDevicesRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_sensors.with_raw_response.sensor_insights_list_sensor_devices_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceDevice]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListSensorDevicesRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_sensors.with_raw_response.sensor_insights_list_sensor_devices_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceDevice]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListSensorDevicesRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListSensorDevicesRequest](verizon/models/dto_list_sensor_devices_request.py) \| [DtoListSensorDevicesRequestDict](verizon/models/dto_list_sensor_devices_request.py)</code> | List details of the sensors |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ResourceDevice](verizon/models/resource_device.py)&#93;, [SensorInsightsListSensorDevicesRequestErrorBody](verizon/errors/sensor_insights_list_sensor_devices_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ResourceDevice](verizon/models/resource_device.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListSensorDevicesRequestErrorBody](verizon/errors/sensor_insights_list_sensor_devices_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_off_board_sensor_request(body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SensorInsightsOffBoardSensorRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_sensors.with_raw_response.sensor_insights_off_board_sensor_request(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsOffBoardSensorRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_sensors.with_raw_response.sensor_insights_off_board_sensor_request(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsOffBoardSensorRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoOffBoardSensorRequest](verizon/models/dto_off_board_sensor_request.py) \| [DtoOffBoardSensorRequestDict](verizon/models/dto_off_board_sensor_request.py)</code> | Offboard a sensor |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [SensorInsightsOffBoardSensorRequestErrorBody](verizon/errors/sensor_insights_off_board_sensor_request_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SensorInsightsOffBoardSensorRequestErrorBody](verizon/errors/sensor_insights_off_board_sensor_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_on_board_sensor_request(body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SensorInsightsOnBoardSensorRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_sensors.with_raw_response.sensor_insights_on_board_sensor_request(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsOnBoardSensorRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_sensors.with_raw_response.sensor_insights_on_board_sensor_request(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsOnBoardSensorRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoOnBoardSensorRequest](verizon/models/dto_on_board_sensor_request.py) \| [DtoOnBoardSensorRequestDict](verizon/models/dto_on_board_sensor_request.py)</code> | Onboarding a sensor |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [SensorInsightsOnBoardSensorRequestErrorBody](verizon/errors/sensor_insights_on_board_sensor_request_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SensorInsightsOnBoardSensorRequestErrorBody](verizon/errors/sensor_insights_on_board_sensor_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_sensor_off_boarding_status_request(body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoSensorOffBoardingStatusResponse, SensorInsightsSensorOffBoardingStatusRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_sensors.with_raw_response.sensor_insights_sensor_off_boarding_status_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoSensorOffBoardingStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsSensorOffBoardingStatusRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_sensors.with_raw_response.sensor_insights_sensor_off_boarding_status_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoSensorOffBoardingStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsSensorOffBoardingStatusRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoSensorOffBoardStatusRequest](verizon/models/dto_sensor_off_board_status_request.py) \| [DtoSensorOffBoardStatusRequestDict](verizon/models/dto_sensor_off_board_status_request.py)</code> | Get a sensor's offboarding status |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoSensorOffBoardingStatusResponse](verizon/models/dto_sensor_off_boarding_status_response.py), [SensorInsightsSensorOffBoardingStatusRequestErrorBody](verizon/errors/sensor_insights_sensor_off_boarding_status_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoSensorOffBoardingStatusResponse](verizon/models/dto_sensor_off_boarding_status_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsSensorOffBoardingStatusRequestErrorBody](verizon/errors/sensor_insights_sensor_off_boarding_status_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_sensor_on_board_status_request(body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoSensorOnBoardingStatusResponse, SensorInsightsSensorOnBoardStatusRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_sensors.with_raw_response.sensor_insights_sensor_on_board_status_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoSensorOnBoardingStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsSensorOnBoardStatusRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_sensors.with_raw_response.sensor_insights_sensor_on_board_status_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoSensorOnBoardingStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsSensorOnBoardStatusRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoSensorOnBoardStatusRequest](verizon/models/dto_sensor_on_board_status_request.py) \| [DtoSensorOnBoardStatusRequestDict](verizon/models/dto_sensor_on_board_status_request.py)</code> | Get the sensor's onboarding status |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoSensorOnBoardingStatusResponse](verizon/models/dto_sensor_on_boarding_status_response.py), [SensorInsightsSensorOnBoardStatusRequestErrorBody](verizon/errors/sensor_insights_sensor_on_board_status_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoSensorOnBoardingStatusResponse](verizon/models/dto_sensor_on_boarding_status_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsSensorOnBoardStatusRequestErrorBody](verizon/errors/sensor_insights_sensor_on_board_status_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsSmartAlertMetrics

> Source: [SensorInsightsSmartAlertMetrics](verizon/apis/sensor_insights_smart_alert_metrics.py)

<details>
<summary><code>def sensorinsightsmetricsquery(body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DtoQueryMetricsResponse, SensorinsightsmetricsqueryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get Device Alerts for the most recent daily period, up to 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_smart_alert_metrics.with_raw_response.sensorinsightsmetricsquery(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoQueryMetricsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorinsightsmetricsqueryErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_smart_alert_metrics.with_raw_response.sensorinsightsmetricsquery(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DtoQueryMetricsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorinsightsmetricsqueryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoQueryMetrics](verizon/models/dto_query_metrics.py) \| [DtoQueryMetricsDict](verizon/models/dto_query_metrics.py)</code> | Daily period requested, up to 30 days. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DtoQueryMetricsResponse](verizon/models/dto_query_metrics_response.py), [SensorinsightsmetricsqueryErrorBody](verizon/errors/sensorinsightsmetricsquery_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DtoQueryMetricsResponse](verizon/models/dto_query_metrics_response.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorinsightsmetricsqueryErrorBody](verizon/errors/sensorinsightsmetricsquery_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsSmartAlerts

> Source: [SensorInsightsSmartAlerts](verizon/apis/sensor_insights_smart_alerts.py)

<details>
<summary><code>def sensor_insights_bulk_update(body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserSmartAlert, SensorInsightsBulkUpdateErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_smart_alerts.with_raw_response.sensor_insights_bulk_update(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserSmartAlert
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsBulkUpdateErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_smart_alerts.with_raw_response.sensor_insights_bulk_update(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserSmartAlert
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsBulkUpdateErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoBulkUpdate](verizon/models/dto_bulk_update.py) \| [DtoBulkUpdateDict](verizon/models/dto_bulk_update.py)</code> | Bulk update smart alerts |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UserSmartAlert](verizon/models/user_smart_alert.py), [SensorInsightsBulkUpdateErrorBody](verizon/errors/sensor_insights_bulk_update_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserSmartAlert](verizon/models/user_smart_alert.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsBulkUpdateErrorBody](verizon/errors/sensor_insights_bulk_update_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_list_smart_alerts_request(body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[UserSmartAlert], SensorInsightsListSmartAlertsRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_smart_alerts.with_raw_response.sensor_insights_list_smart_alerts_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UserSmartAlert]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListSmartAlertsRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_smart_alerts.with_raw_response.sensor_insights_list_smart_alerts_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[UserSmartAlert]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListSmartAlertsRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListSmartAlertsRequest](verizon/models/dto_list_smart_alerts_request.py) \| [DtoListSmartAlertsRequestDict](verizon/models/dto_list_smart_alerts_request.py)</code> | Retrieve a smart alert |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[UserSmartAlert](verizon/models/user_smart_alert.py)&#93;, [SensorInsightsListSmartAlertsRequestErrorBody](verizon/errors/sensor_insights_list_smart_alerts_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[UserSmartAlert](verizon/models/user_smart_alert.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListSmartAlertsRequestErrorBody](verizon/errors/sensor_insights_list_smart_alerts_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_patch_smart_alert_request(body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UserSmartAlert, SensorInsightsPatchSmartAlertRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_smart_alerts.with_raw_response.sensor_insights_patch_smart_alert_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserSmartAlert
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsPatchSmartAlertRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_smart_alerts.with_raw_response.sensor_insights_patch_smart_alert_request(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UserSmartAlert
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsPatchSmartAlertRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoPatchSmartAlertRequest](verizon/models/dto_patch_smart_alert_request.py) \| [DtoPatchSmartAlertRequestDict](verizon/models/dto_patch_smart_alert_request.py)</code> | Partially update a smart alert |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UserSmartAlert](verizon/models/user_smart_alert.py), [SensorInsightsPatchSmartAlertRequestErrorBody](verizon/errors/sensor_insights_patch_smart_alert_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UserSmartAlert](verizon/models/user_smart_alert.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsPatchSmartAlertRequestErrorBody](verizon/errors/sensor_insights_patch_smart_alert_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SensorInsightsUsers

> Source: [SensorInsightsUsers](verizon/apis/sensor_insights_users.py)

<details>
<summary><code>def sensor_insights_create_user_request(body: DtoCreateUserRequest | DtoCreateUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ResourceUser, SensorInsightsCreateUserRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_users.with_raw_response.sensor_insights_create_user_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceUser
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsCreateUserRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_users.with_raw_response.sensor_insights_create_user_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceUser
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsCreateUserRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoCreateUserRequest](verizon/models/dto_create_user_request.py) \| [DtoCreateUserRequestDict](verizon/models/dto_create_user_request.py)</code> | Create a user profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ResourceUser](verizon/models/resource_user.py), [SensorInsightsCreateUserRequestErrorBody](verizon/errors/sensor_insights_create_user_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ResourceUser](verizon/models/resource_user.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsCreateUserRequestErrorBody](verizon/errors/sensor_insights_create_user_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_delete_user(deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, SensorInsightsDeleteUserErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `DELETE` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_users.with_raw_response.sensor_insights_delete_user(deleterequestpayload)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsDeleteUserErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_users.with_raw_response.sensor_insights_delete_user(deleterequestpayload)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsDeleteUserErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>deleterequestpayload</code> | <code>[DtoDeleteUserRequest](verizon/models/dto_delete_user_request.py) \| [DtoDeleteUserRequestDict](verizon/models/dto_delete_user_request.py)</code> | Payload for the delete user request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [SensorInsightsDeleteUserErrorBody](verizon/errors/sensor_insights_delete_user_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[SensorInsightsDeleteUserErrorBody](verizon/errors/sensor_insights_delete_user_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_list_user_request(body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ResourceUser], SensorInsightsListUserRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_users.with_raw_response.sensor_insights_list_user_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceUser]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListUserRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_users.with_raw_response.sensor_insights_list_user_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ResourceUser]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsListUserRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoListUserRequest](verizon/models/dto_list_user_request.py) \| [DtoListUserRequestDict](verizon/models/dto_list_user_request.py)</code> | A summary of user profile records on an account |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ResourceUser](verizon/models/resource_user.py)&#93;, [SensorInsightsListUserRequestErrorBody](verizon/errors/sensor_insights_list_user_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ResourceUser](verizon/models/resource_user.py)&#93;</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsListUserRequestErrorBody](verizon/errors/sensor_insights_list_user_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def sensor_insights_update_user_request(body: DtoUpdateUserRequest | DtoUpdateUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ResourceUser, SensorInsightsUpdateUserRequestErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `PATCH` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sensor_insights_users.with_raw_response.sensor_insights_update_user_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceUser
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsUpdateUserRequestErrorBody
```

**Async**

```python
result = await async_client.sensor_insights_users.with_raw_response.sensor_insights_update_user_request(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResourceUser
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type SensorInsightsUpdateUserRequestErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DtoUpdateUserRequest](verizon/models/dto_update_user_request.py) \| [DtoUpdateUserRequestDict](verizon/models/dto_update_user_request.py)</code> | Partially update a user profile |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[ResourceUser](verizon/models/resource_user.py), [SensorInsightsUpdateUserRequestErrorBody](verizon/errors/sensor_insights_update_user_request_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[ResourceUser](verizon/models/resource_user.py)</code> -- OK

**On `Failure`**: `error` is <code>[SensorInsightsUpdateUserRequestErrorBody](verizon/errors/sensor_insights_update_user_request_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ManagementError400](verizon/models/management_error400.py)</code> |
| 401, 406, 415, 429 | <code>[ManagementError](verizon/models/management_error.py)</code> |
| 403 | <code>[ManagementError403](verizon/models/management_error403.py)</code> |
| 404 | <code>[ManagementError404](verizon/models/management_error404.py)</code> |
| 500 | <code>[ManagementError500](verizon/models/management_error500.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ServerLogging

> Source: [ServerLogging](verizon/apis/server_logging.py)

<details>
<summary><code>def get_device_check_in_history(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[CheckInHistoryItem], GetDeviceCheckInHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Check-in history can be retrieved for any device belonging to the account, not necessarily with logging enabled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.server_logging.with_raw_response.get_device_check_in_history(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CheckInHistoryItem]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceCheckInHistoryErrorBody
```

**Async**

```python
result = await async_client.server_logging.with_raw_response.get_device_check_in_history(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[CheckInHistoryItem]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceCheckInHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device IMEI identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[CheckInHistoryItem](verizon/models/check_in_history_item.py)&#93;, [GetDeviceCheckInHistoryErrorBody](verizon/errors/get_device_check_in_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[CheckInHistoryItem](verizon/models/check_in_history_item.py)&#93;</code> -- List of check-in history entries.

**On `Failure`**: `error` is <code>[GetDeviceCheckInHistoryErrorBody](verizon/errors/get_device_check_in_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## ServicePlans

> Source: [ServicePlans](verizon/apis/service_plans.py)

<details>
<summary><code>def list_account_service_plans(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[ServicePlan], ListAccountServicePlansErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all data service plans that are associated with a specified billing account. When you send a request to /devices/actions/activate to activate a line of service you must specify the code for one of the service plans associated with your account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.service_plans.with_raw_response.list_account_service_plans(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ServicePlan]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountServicePlansErrorBody
```

**Async**

```python
result = await async_client.service_plans.with_raw_response.list_account_service_plans(aname)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[ServicePlan]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountServicePlansErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>aname</code> | <code>str</code> | Account name. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[ServicePlan](verizon/models/service_plan.py)&#93;, [ListAccountServicePlansErrorBody](verizon/errors/list_account_service_plans_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[ServicePlan](verizon/models/service_plan.py)&#93;</code> -- The list of service plans associated with the account.

**On `Failure`**: `error` is <code>[ListAccountServicePlansErrorBody](verizon/errors/list_account_service_plans_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SessionManagement

> Source: [SessionManagement](verizon/apis/session_management.py)

<details>
<summary><code>def end_connectivity_management_session(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LogOutRequest, EndConnectivityManagementSessionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Ends a Connectivity Management session.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.session_management.with_raw_response.end_connectivity_management_session()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LogOutRequest
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EndConnectivityManagementSessionErrorBody
```

**Async**

```python
result = await async_client.session_management.with_raw_response.end_connectivity_management_session()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LogOutRequest
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EndConnectivityManagementSessionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[LogOutRequest](verizon/models/log_out_request.py), [EndConnectivityManagementSessionErrorBody](verizon/errors/end_connectivity_management_session_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LogOutRequest](verizon/models/log_out_request.py)</code> -- VZ-M2M session token.

**On `Failure`**: `error` is <code>[EndConnectivityManagementSessionErrorBody](verizon/errors/end_connectivity_management_session_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reset_connectivity_management_password(body: SessionResetPasswordRequest | SessionResetPasswordRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SessionResetPasswordResult, ResetConnectivityManagementPasswordErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The new password is effective immediately. Passwords do not expire, but Verizon recommends changing your password every 90 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.session_management.with_raw_response.reset_connectivity_management_password(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SessionResetPasswordResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ResetConnectivityManagementPasswordErrorBody
```

**Async**

```python
result = await async_client.session_management.with_raw_response.reset_connectivity_management_password(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SessionResetPasswordResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ResetConnectivityManagementPasswordErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SessionResetPasswordRequest](verizon/models/session_reset_password_request.py) \| [SessionResetPasswordRequestDict](verizon/models/session_reset_password_request.py)</code> | Request with current password that needs to be reset. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SessionResetPasswordResult](verizon/models/session_reset_password_result.py), [ResetConnectivityManagementPasswordErrorBody](verizon/errors/reset_connectivity_management_password_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[SessionResetPasswordResult](verizon/models/session_reset_password_result.py)</code> -- Returns a new, randomly generated password for the current username.

**On `Failure`**: `error` is <code>[ResetConnectivityManagementPasswordErrorBody](verizon/errors/reset_connectivity_management_password_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_connectivity_management_session(*, body: LogInRequest | LogInRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LogInResult, StartConnectivityManagementSessionErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Initiates a Connectivity Management session and returns a VZ-M2M session token that is required in subsequent API requests.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.session_management.with_raw_response.start_connectivity_management_session()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LogInResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StartConnectivityManagementSessionErrorBody
```

**Async**

```python
result = await async_client.session_management.with_raw_response.start_connectivity_management_session()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LogInResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type StartConnectivityManagementSessionErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[LogInRequest](verizon/models/log_in_request.py) \| [LogInRequestDict](verizon/models/log_in_request.py) \| None</code> | Request to initiate a session.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[LogInResult](verizon/models/log_in_result.py), [StartConnectivityManagementSessionErrorBody](verizon/errors/start_connectivity_management_session_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[LogInResult](verizon/models/log_in_result.py)</code> -- VZ-M2M session token.

**On `Failure`**: `error` is <code>[StartConnectivityManagementSessionErrorBody](verizon/errors/start_connectivity_management_session_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementCallbacksV1

> Source: [SoftwareManagementCallbacksV1](verizon/apis/software_management_callbacks_v1.py)

<details>
<summary><code>def deregister_callback3(account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeregisterCallback3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deregisters the callback endpoint and stops ThingSpace from sending FOTA callback messages for the specified account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v1.with_raw_response.deregister_callback3(account, service)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback3ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v1.with_raw_response.deregister_callback3(account, service)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>service</code> | <code>[CallbackServiceOrStr](verizon/models/enums/callback_service.py)</code> | Callback type. Must be 'Fota' for Software Management Services API. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DeregisterCallback3ErrorBody](verizon/errors/deregister_callback3_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeregisterCallback3ErrorBody](verizon/errors/deregister_callback3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](verizon/core/results.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_registered_callbacks3(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[RegisteredCallbacks], ListRegisteredCallbacks3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the name and endpoint URL of the callback listening services registered for a given account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v1.with_raw_response.list_registered_callbacks3(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[RegisteredCallbacks]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks3ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v1.with_raw_response.list_registered_callbacks3(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[RegisteredCallbacks]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[RegisteredCallbacks](verizon/models/registered_callbacks.py)&#93;, [ListRegisteredCallbacks3ErrorBody](verizon/errors/list_registered_callbacks3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[RegisteredCallbacks](verizon/models/registered_callbacks.py)&#93;</code> -- List of callbacks.

**On `Failure`**: `error` is <code>[ListRegisteredCallbacks3ErrorBody](verizon/errors/list_registered_callbacks3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_callback3(account: str, body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV1CallbackRegistrationResult, RegisterCallback3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Registers a URL to receive RESTful messages from a callback service when new firmware versions are available and when upgrades start and finish.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v1.with_raw_response.register_callback3(account, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV1CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback3ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v1.with_raw_response.register_callback3(account, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV1CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>body</code> | <code>[FotaV1CallbackRegistrationRequest](verizon/models/fota_v1_callback_registration_request.py) \| [FotaV1CallbackRegistrationRequestDict](verizon/models/fota_v1_callback_registration_request.py)</code> | Callback details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV1CallbackRegistrationResult](verizon/models/fota_v1_callback_registration_result.py), [RegisterCallback3ErrorBody](verizon/errors/register_callback3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV1CallbackRegistrationResult](verizon/models/fota_v1_callback_registration_result.py)</code> -- Result of registering a callback.

**On `Failure`**: `error` is <code>[RegisterCallback3ErrorBody](verizon/errors/register_callback3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementCallbacksV2

> Source: [SoftwareManagementCallbacksV2](verizon/apis/software_management_callbacks_v2.py)

<details>
<summary><code>def deregister_callback4(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV2SuccessResult, DeregisterCallback4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to delete a previously registered callback URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v2.with_raw_response.deregister_callback4(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback4ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v2.with_raw_response.deregister_callback4(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py), [DeregisterCallback4ErrorBody](verizon/errors/deregister_callback4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py)</code> -- Result of deregistering a callback.

**On `Failure`**: `error` is <code>[DeregisterCallback4ErrorBody](verizon/errors/deregister_callback4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_registered_callbacks4(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CallbackSummary, ListRegisteredCallbacks4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to get the registered callback information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v2.with_raw_response.list_registered_callbacks4(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks4ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v2.with_raw_response.list_registered_callbacks4(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CallbackSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CallbackSummary](verizon/models/callback_summary.py), [ListRegisteredCallbacks4ErrorBody](verizon/errors/list_registered_callbacks4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[CallbackSummary](verizon/models/callback_summary.py)</code> -- Return callback registration.

**On `Failure`**: `error` is <code>[ListRegisteredCallbacks4ErrorBody](verizon/errors/list_registered_callbacks4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_callback4(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV2CallbackRegistrationResult, RegisterCallback4ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to create the HTTPS callback address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v2.with_raw_response.register_callback4(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback4ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v2.with_raw_response.register_callback4(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback4ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV2CallbackRegistrationResult](verizon/models/fota_v2_callback_registration_result.py), [RegisterCallback4ErrorBody](verizon/errors/register_callback4_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV2CallbackRegistrationResult](verizon/models/fota_v2_callback_registration_result.py)</code> -- Return callback registration.

**On `Failure`**: `error` is <code>[RegisterCallback4ErrorBody](verizon/errors/register_callback4_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_callback(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV2CallbackRegistrationResult, UpdateCallbackErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to update the HTTPS callback address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v2.with_raw_response.update_callback(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCallbackErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v2.with_raw_response.update_callback(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCallbackErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV2CallbackRegistrationResult](verizon/models/fota_v2_callback_registration_result.py), [UpdateCallbackErrorBody](verizon/errors/update_callback_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV2CallbackRegistrationResult](verizon/models/fota_v2_callback_registration_result.py)</code> -- Return callback registration.

**On `Failure`**: `error` is <code>[UpdateCallbackErrorBody](verizon/errors/update_callback_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementCallbacksV3

> Source: [SoftwareManagementCallbacksV3](verizon/apis/software_management_callbacks_v3.py)

<details>
<summary><code>def deregister_callback5(acc: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV3SuccessResult, DeregisterCallback5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to delete a previously registered callback URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v3.with_raw_response.deregister_callback5(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback5ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v3.with_raw_response.deregister_callback5(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeregisterCallback5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV3SuccessResult](verizon/models/fota_v3_success_result.py), [DeregisterCallback5ErrorBody](verizon/errors/deregister_callback5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV3SuccessResult](verizon/models/fota_v3_success_result.py)</code> -- Delete request result.

**On `Failure`**: `error` is <code>[DeregisterCallback5ErrorBody](verizon/errors/deregister_callback5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_registered_callbacks5(acc: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV3CallbackSummary, ListRegisteredCallbacks5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to get the registered callback information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v3.with_raw_response.list_registered_callbacks5(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3CallbackSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks5ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v3.with_raw_response.list_registered_callbacks5(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3CallbackSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListRegisteredCallbacks5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV3CallbackSummary](verizon/models/fota_v3_callback_summary.py), [ListRegisteredCallbacks5ErrorBody](verizon/errors/list_registered_callbacks5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV3CallbackSummary](verizon/models/fota_v3_callback_summary.py)</code> -- Return callback registration.

**On `Failure`**: `error` is <code>[ListRegisteredCallbacks5ErrorBody](verizon/errors/list_registered_callbacks5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def register_callback5(acc: str, body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV3CallbackRegistrationResult, RegisterCallback5ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to create the HTTPS callback address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v3.with_raw_response.register_callback5(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback5ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v3.with_raw_response.register_callback5(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RegisterCallback5ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[FotaV3CallbackRegistrationRequest](verizon/models/fota_v3_callback_registration_request.py) \| [FotaV3CallbackRegistrationRequestDict](verizon/models/fota_v3_callback_registration_request.py)</code> | Callback URL registration. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV3CallbackRegistrationResult](verizon/models/fota_v3_callback_registration_result.py), [RegisterCallback5ErrorBody](verizon/errors/register_callback5_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV3CallbackRegistrationResult](verizon/models/fota_v3_callback_registration_result.py)</code> -- Return callback registration.

**On `Failure`**: `error` is <code>[RegisterCallback5ErrorBody](verizon/errors/register_callback5_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_callback2(acc: str, body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV3CallbackRegistrationResult, UpdateCallback2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to update the HTTPS callback address.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_callbacks_v3.with_raw_response.update_callback2(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCallback2ErrorBody
```

**Async**

```python
result = await async_client.software_management_callbacks_v3.with_raw_response.update_callback2(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3CallbackRegistrationResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateCallback2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[FotaV3CallbackRegistrationRequest](verizon/models/fota_v3_callback_registration_request.py) \| [FotaV3CallbackRegistrationRequestDict](verizon/models/fota_v3_callback_registration_request.py)</code> | Callback URL registration. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV3CallbackRegistrationResult](verizon/models/fota_v3_callback_registration_result.py), [UpdateCallback2ErrorBody](verizon/errors/update_callback2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV3CallbackRegistrationResult](verizon/models/fota_v3_callback_registration_result.py)</code> -- Return callback registration.

**On `Failure`**: `error` is <code>[UpdateCallback2ErrorBody](verizon/errors/update_callback2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementLicensesV1

> Source: [SoftwareManagementLicensesV1](verizon/apis/software_management_licenses_v1.py)

<details>
<summary><code>def assign_licenses_to_devices(account: str, body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1LicensesAssignedRemovedResult, AssignLicensesToDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v1.with_raw_response.assign_licenses_to_devices(account, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicensesToDevicesErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v1.with_raw_response.assign_licenses_to_devices(account, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicensesToDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>body</code> | <code>[V1LicensesAssignedRemovedRequest](verizon/models/v1_licenses_assigned_removed_request.py) \| [V1LicensesAssignedRemovedRequestDict](verizon/models/v1_licenses_assigned_removed_request.py)</code> | IMEIs of the devices to assign licenses to. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V1LicensesAssignedRemovedResult](verizon/models/v1_licenses_assigned_removed_result.py), [AssignLicensesToDevicesErrorBody](verizon/errors/assign_licenses_to_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1LicensesAssignedRemovedResult](verizon/models/v1_licenses_assigned_removed_result.py)</code> -- List of licenses assigned.

**On `Failure`**: `error` is <code>[AssignLicensesToDevicesErrorBody](verizon/errors/assign_licenses_to_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_list_of_licenses_to_remove(account: str, body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1ListOfLicensesToRemoveResult, CreateListOfLicensesToRemoveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than the number of assigned licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v1.with_raw_response.create_list_of_licenses_to_remove(account, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1ListOfLicensesToRemoveResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateListOfLicensesToRemoveErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v1.with_raw_response.create_list_of_licenses_to_remove(
    account, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1ListOfLicensesToRemoveResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateListOfLicensesToRemoveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>body</code> | <code>[V1ListOfLicensesToRemoveRequest](verizon/models/v1_list_of_licenses_to_remove_request.py) \| [V1ListOfLicensesToRemoveRequestDict](verizon/models/v1_list_of_licenses_to_remove_request.py)</code> | Cancellation candidate device list. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V1ListOfLicensesToRemoveResult](verizon/models/v1_list_of_licenses_to_remove_result.py), [CreateListOfLicensesToRemoveErrorBody](verizon/errors/create_list_of_licenses_to_remove_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1ListOfLicensesToRemoveResult](verizon/models/v1_list_of_licenses_to_remove_result.py)</code> -- List of licenses assigned.

**On `Failure`**: `error` is <code>[CreateListOfLicensesToRemoveErrorBody](verizon/errors/create_list_of_licenses_to_remove_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_list_of_licenses_to_remove(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteListOfLicensesToRemoveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the entire list of cancellation candidate devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v1.with_raw_response.delete_list_of_licenses_to_remove(account)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteListOfLicensesToRemoveErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v1.with_raw_response.delete_list_of_licenses_to_remove(account)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteListOfLicensesToRemoveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DeleteListOfLicensesToRemoveErrorBody](verizon/errors/delete_list_of_licenses_to_remove_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteListOfLicensesToRemoveErrorBody](verizon/errors/delete_list_of_licenses_to_remove_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RawError](verizon/core/results.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_licenses_to_remove(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1ListOfLicensesToRemove, ListLicensesToRemoveErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than the number of assigned licenses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v1.with_raw_response.list_licenses_to_remove(account, start_index)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1ListOfLicensesToRemove
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListLicensesToRemoveErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v1.with_raw_response.list_licenses_to_remove(
    account, start_index
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1ListOfLicensesToRemove
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListLicensesToRemoveErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>start_index</code> | <code>str</code> | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for the third request, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V1ListOfLicensesToRemove](verizon/models/v1_list_of_licenses_to_remove.py), [ListLicensesToRemoveErrorBody](verizon/errors/list_licenses_to_remove_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1ListOfLicensesToRemove](verizon/models/v1_list_of_licenses_to_remove.py)</code> -- List of cancellation candidate devices.

**On `Failure`**: `error` is <code>[ListLicensesToRemoveErrorBody](verizon/errors/list_licenses_to_remove_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_licenses_from_devices(account: str, body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1LicensesAssignedRemovedResult, RemoveLicensesFromDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove unused licenses from device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v1.with_raw_response.remove_licenses_from_devices(account, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveLicensesFromDevicesErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v1.with_raw_response.remove_licenses_from_devices(
    account, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveLicensesFromDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>body</code> | <code>[V1LicensesAssignedRemovedRequest](verizon/models/v1_licenses_assigned_removed_request.py) \| [V1LicensesAssignedRemovedRequestDict](verizon/models/v1_licenses_assigned_removed_request.py)</code> | IMEIs of the devices to remove licenses from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V1LicensesAssignedRemovedResult](verizon/models/v1_licenses_assigned_removed_result.py), [RemoveLicensesFromDevicesErrorBody](verizon/errors/remove_licenses_from_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1LicensesAssignedRemovedResult](verizon/models/v1_licenses_assigned_removed_result.py)</code> -- List of devices with license removal status.

**On `Failure`**: `error` is <code>[RemoveLicensesFromDevicesErrorBody](verizon/errors/remove_licenses_from_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementLicensesV2

> Source: [SoftwareManagementLicensesV2](verizon/apis/software_management_licenses_v2.py)

<details>
<summary><code>def assign_licenses_to_devices2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2LicensesAssignedRemovedResult, AssignLicensesToDevices2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to assign licenses to a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v2.with_raw_response.assign_licenses_to_devices2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicensesToDevices2ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v2.with_raw_response.assign_licenses_to_devices2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicensesToDevices2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2LicensesAssignedRemovedResult](verizon/models/v2_licenses_assigned_removed_result.py), [AssignLicensesToDevices2ErrorBody](verizon/errors/assign_licenses_to_devices2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2LicensesAssignedRemovedResult](verizon/models/v2_licenses_assigned_removed_result.py)</code> -- License assignment result.

**On `Failure`**: `error` is <code>[AssignLicensesToDevices2ErrorBody](verizon/errors/assign_licenses_to_devices2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_list_of_licenses_to_remove2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2ListOfLicensesToRemoveResult, CreateListOfLicensesToRemove2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The license cancel endpoint allows user to create a list of license cancellation candidate devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v2.with_raw_response.create_list_of_licenses_to_remove2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2ListOfLicensesToRemoveResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateListOfLicensesToRemove2ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v2.with_raw_response.create_list_of_licenses_to_remove2(
    account
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2ListOfLicensesToRemoveResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateListOfLicensesToRemove2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2ListOfLicensesToRemoveResult](verizon/models/v2_list_of_licenses_to_remove_result.py), [CreateListOfLicensesToRemove2ErrorBody](verizon/errors/create_list_of_licenses_to_remove2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2ListOfLicensesToRemoveResult](verizon/models/v2_list_of_licenses_to_remove_result.py)</code> -- Return a created license cancellation device list.

**On `Failure`**: `error` is <code>[CreateListOfLicensesToRemove2ErrorBody](verizon/errors/create_list_of_licenses_to_remove2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_list_of_licenses_to_remove2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV2SuccessResult, DeleteListOfLicensesToRemove2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to delete a created cancel candidate device list.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v2.with_raw_response.delete_list_of_licenses_to_remove2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteListOfLicensesToRemove2ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v2.with_raw_response.delete_list_of_licenses_to_remove2(
    account
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2SuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteListOfLicensesToRemove2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py), [DeleteListOfLicensesToRemove2ErrorBody](verizon/errors/delete_list_of_licenses_to_remove2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py)</code> -- Result of deletion of candidate list of devices to remove.

**On `Failure`**: `error` is <code>[DeleteListOfLicensesToRemove2ErrorBody](verizon/errors/delete_list_of_licenses_to_remove2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_account_license_status2(account: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2LicenseSummary, GetAccountLicenseStatus2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The endpoint allows user to list license usage.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v2.with_raw_response.get_account_license_status2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2LicenseSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountLicenseStatus2ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v2.with_raw_response.get_account_license_status2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2LicenseSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountLicenseStatus2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>last_seen_device_id</code> | <code>str \| None</code> | Last seen device identifier.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2LicenseSummary](verizon/models/v2_license_summary.py), [GetAccountLicenseStatus2ErrorBody](verizon/errors/get_account_license_status2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2LicenseSummary](verizon/models/v2_license_summary.py)</code> -- Summary of license assignment.

**On `Failure`**: `error` is <code>[GetAccountLicenseStatus2ErrorBody](verizon/errors/get_account_license_status2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_licenses_to_remove2(account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2ListOfLicensesToRemove, ListLicensesToRemove2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The license cancel endpoint allows user to list registered license cancellation candidate devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v2.with_raw_response.list_licenses_to_remove2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2ListOfLicensesToRemove
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListLicensesToRemove2ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v2.with_raw_response.list_licenses_to_remove2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2ListOfLicensesToRemove
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListLicensesToRemove2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>start_index</code> | <code>str \| None</code> | Start index to retrieve.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2ListOfLicensesToRemove](verizon/models/v2_list_of_licenses_to_remove.py), [ListLicensesToRemove2ErrorBody](verizon/errors/list_licenses_to_remove2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2ListOfLicensesToRemove](verizon/models/v2_list_of_licenses_to_remove.py)</code> -- A list of license cancellation candidate devices.

**On `Failure`**: `error` is <code>[ListLicensesToRemove2ErrorBody](verizon/errors/list_licenses_to_remove2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_licenses_from_devices2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2LicensesAssignedRemovedResult, RemoveLicensesFromDevices2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to remove licenses from a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v2.with_raw_response.remove_licenses_from_devices2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveLicensesFromDevices2ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v2.with_raw_response.remove_licenses_from_devices2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2LicensesAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveLicensesFromDevices2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2LicensesAssignedRemovedResult](verizon/models/v2_licenses_assigned_removed_result.py), [RemoveLicensesFromDevices2ErrorBody](verizon/errors/remove_licenses_from_devices2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2LicensesAssignedRemovedResult](verizon/models/v2_licenses_assigned_removed_result.py)</code> -- License removal result.

**On `Failure`**: `error` is <code>[RemoveLicensesFromDevices2ErrorBody](verizon/errors/remove_licenses_from_devices2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementLicensesV3

> Source: [SoftwareManagementLicensesV3](verizon/apis/software_management_licenses_v3.py)

<details>
<summary><code>def assign_licenses_to_devices3(acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3LicenseAssignedRemovedResult, AssignLicensesToDevices3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to assign licenses to a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v3.with_raw_response.assign_licenses_to_devices3(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3LicenseAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicensesToDevices3ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v3.with_raw_response.assign_licenses_to_devices3(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3LicenseAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type AssignLicensesToDevices3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[V3LicenseImei](verizon/models/v3_license_imei.py) \| [V3LicenseImeiDict](verizon/models/v3_license_imei.py)</code> | License assignment. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3LicenseAssignedRemovedResult](verizon/models/v3_license_assigned_removed_result.py), [AssignLicensesToDevices3ErrorBody](verizon/errors/assign_licenses_to_devices3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3LicenseAssignedRemovedResult](verizon/models/v3_license_assigned_removed_result.py)</code> -- License assignment result.

**On `Failure`**: `error` is <code>[AssignLicensesToDevices3ErrorBody](verizon/errors/assign_licenses_to_devices3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_account_licenses_status(acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3LicenseSummary, GetAccountLicensesStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The endpoint allows user to list license usage.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v3.with_raw_response.get_account_licenses_status(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3LicenseSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountLicensesStatusErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v3.with_raw_response.get_account_licenses_status(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3LicenseSummary
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountLicensesStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>last_seen_device_id</code> | <code>str \| None</code> | Last seen device identifier.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3LicenseSummary](verizon/models/v3_license_summary.py), [GetAccountLicensesStatusErrorBody](verizon/errors/get_account_licenses_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3LicenseSummary](verizon/models/v3_license_summary.py)</code> -- Summary of license assignment.

**On `Failure`**: `error` is <code>[GetAccountLicensesStatusErrorBody](verizon/errors/get_account_licenses_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_licenses_from_devices3(acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3LicenseAssignedRemovedResult, RemoveLicensesFromDevices3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to remove licenses from a list of devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_licenses_v3.with_raw_response.remove_licenses_from_devices3(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3LicenseAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveLicensesFromDevices3ErrorBody
```

**Async**

```python
result = await async_client.software_management_licenses_v3.with_raw_response.remove_licenses_from_devices3(acc, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3LicenseAssignedRemovedResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RemoveLicensesFromDevices3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>body</code> | <code>[V3LicenseImei](verizon/models/v3_license_imei.py) \| [V3LicenseImeiDict](verizon/models/v3_license_imei.py)</code> | License removal. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3LicenseAssignedRemovedResult](verizon/models/v3_license_assigned_removed_result.py), [RemoveLicensesFromDevices3ErrorBody](verizon/errors/remove_licenses_from_devices3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3LicenseAssignedRemovedResult](verizon/models/v3_license_assigned_removed_result.py)</code> -- License removal result.

**On `Failure`**: `error` is <code>[RemoveLicensesFromDevices3ErrorBody](verizon/errors/remove_licenses_from_devices3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementReportsV1

> Source: [SoftwareManagementReportsV1](verizon/apis/software_management_reports_v1.py)

<details>
<summary><code>def get_device_firmware_upgrade_history(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceUpgradeHistory], GetDeviceFirmwareUpgradeHistoryErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the upgrade history of the specified device from the previous six months.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v1.with_raw_response.get_device_firmware_upgrade_history(account, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceUpgradeHistory]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceFirmwareUpgradeHistoryErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v1.with_raw_response.get_device_firmware_upgrade_history(
    account, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceUpgradeHistory]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceFirmwareUpgradeHistoryErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>device_id</code> | <code>str</code> | The IMEI of the device. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceUpgradeHistory](verizon/models/device_upgrade_history.py)&#93;, [GetDeviceFirmwareUpgradeHistoryErrorBody](verizon/errors/get_device_firmware_upgrade_history_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceUpgradeHistory](verizon/models/device_upgrade_history.py)&#93;</code> -- Device upgrade history.

**On `Failure`**: `error` is <code>[GetDeviceFirmwareUpgradeHistoryErrorBody](verizon/errors/get_device_firmware_upgrade_history_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_account_devices(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceListQueryResult, ListAccountDevicesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an array of all devices in the specified account. Each device object includes information needed for managing firmware, including the device make and model, MDN and IMEI, and current firmware version.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v1.with_raw_response.list_account_devices(account, start_index)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceListQueryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountDevicesErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v1.with_raw_response.list_account_devices(account, start_index)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceListQueryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountDevicesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>start_index</code> | <code>str</code> | Only return devices with IMEIs larger than this value. Use 0 for the first request. If `hasMoreData`=true in the response, use the `lastSeenDeviceId` value from the response as the startIndex in the next request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceListQueryResult](verizon/models/device_list_query_result.py), [ListAccountDevicesErrorBody](verizon/errors/list_account_devices_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceListQueryResult](verizon/models/device_list_query_result.py)</code> -- List of all devices in the specified account.

**On `Failure`**: `error` is <code>[ListAccountDevicesErrorBody](verizon/errors/list_account_devices_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_upgrades_for_specified_status(account: str, upgrade_status: UpgradeStatusOrStr, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpgradeListQueryResult, ListUpgradesForSpecifiedStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all upgrades with a specified status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v1.with_raw_response.list_upgrades_for_specified_status(
    account, upgrade_status, start_index
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpgradeListQueryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListUpgradesForSpecifiedStatusErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v1.with_raw_response.list_upgrades_for_specified_status(
    account, upgrade_status, start_index
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpgradeListQueryResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListUpgradesForSpecifiedStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>upgrade_status</code> | <code>[UpgradeStatusOrStr](verizon/models/enums/upgrade_status.py)</code> | The status of the upgrades that you want to retrieve. |
| <code>start_index</code> | <code>str</code> | The zero-based number of the first record to return. Set startIndex=0 for the first request. If `hasMoreFlag`=true in the response, use the `lastSeenUpgradeId` value from the response as the startIndex in the next request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UpgradeListQueryResult](verizon/models/upgrade_list_query_result.py), [ListUpgradesForSpecifiedStatusErrorBody](verizon/errors/list_upgrades_for_specified_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpgradeListQueryResult](verizon/models/upgrade_list_query_result.py)</code> -- A list of all upgrades with a specified status.

**On `Failure`**: `error` is <code>[ListUpgradesForSpecifiedStatusErrorBody](verizon/errors/list_upgrades_for_specified_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementReportsV2

> Source: [SoftwareManagementReportsV2](verizon/apis/software_management_reports_v2.py)

<details>
<summary><code>def get_campaign_device_status(account: str, campaign_id: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2CampaignDevice, GetCampaignDeviceStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The report endpoint allows user to get the full list of device of a campaign.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v2.with_raw_response.get_campaign_device_status(account, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2CampaignDevice
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignDeviceStatusErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v2.with_raw_response.get_campaign_device_status(
    account, campaign_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2CampaignDevice
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignDeviceStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Campaign identifier. |
| <code>last_seen_device_id</code> | <code>str \| None</code> | Last seen device identifier.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2CampaignDevice](verizon/models/v2_campaign_device.py), [GetCampaignDeviceStatusErrorBody](verizon/errors/get_campaign_device_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2CampaignDevice](verizon/models/v2_campaign_device.py)</code> -- Return list of campaign history.

**On `Failure`**: `error` is <code>[GetCampaignDeviceStatusErrorBody](verizon/errors/get_campaign_device_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_campaign_history_by_status(account: str, campaign_status: str, *, last_seen_campaign_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2CampaignHistory, GetCampaignHistoryByStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The report endpoint allows user to get campaign history of an account for specified status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v2.with_raw_response.get_campaign_history_by_status(
    account, campaign_status
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2CampaignHistory
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignHistoryByStatusErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v2.with_raw_response.get_campaign_history_by_status(
    account, campaign_status
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2CampaignHistory
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignHistoryByStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>campaign_status</code> | <code>str</code> | Status of the campaign. |
| <code>last_seen_campaign_id</code> | <code>str \| None</code> | Last seen campaign Id.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2CampaignHistory](verizon/models/v2_campaign_history.py), [GetCampaignHistoryByStatusErrorBody](verizon/errors/get_campaign_history_by_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2CampaignHistory](verizon/models/v2_campaign_history.py)</code> -- Return list of campaign history.

**On `Failure`**: `error` is <code>[GetCampaignHistoryByStatusErrorBody](verizon/errors/get_campaign_history_by_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device_firmware_upgrade_history2(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceSoftwareUpgrade], GetDeviceFirmwareUpgradeHistory2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The endpoint allows user to get software upgrade history of a device based on device IMEI.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v2.with_raw_response.get_device_firmware_upgrade_history2(
    account, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceSoftwareUpgrade]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceFirmwareUpgradeHistory2ErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v2.with_raw_response.get_device_firmware_upgrade_history2(
    account, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceSoftwareUpgrade]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceFirmwareUpgradeHistory2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device IMEI identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceSoftwareUpgrade](verizon/models/device_software_upgrade.py)&#93;, [GetDeviceFirmwareUpgradeHistory2ErrorBody](verizon/errors/get_device_firmware_upgrade_history2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceSoftwareUpgrade](verizon/models/device_software_upgrade.py)&#93;</code> -- Return array of upgrades.

**On `Failure`**: `error` is <code>[GetDeviceFirmwareUpgradeHistory2ErrorBody](verizon/errors/get_device_firmware_upgrade_history2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_account_devices2(account: str, *, last_seen_device_id: str | None = None, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V2AccountDeviceList, ListAccountDevices2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

The device endpoint gets devices information of an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v2.with_raw_response.list_account_devices2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2AccountDeviceList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountDevices2ErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v2.with_raw_response.list_account_devices2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V2AccountDeviceList
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAccountDevices2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>last_seen_device_id</code> | <code>str \| None</code> | Last seen device identifier.<br>**Default**: <code>None</code> |
| <code>distribution_type</code> | <code>str \| None</code> | Filter distributionType to get specific type of devices. Values is LWM2M, OMD-DM or HTTP.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V2AccountDeviceList](verizon/models/v2_account_device_list.py), [ListAccountDevices2ErrorBody](verizon/errors/list_account_devices2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V2AccountDeviceList](verizon/models/v2_account_device_list.py)</code> -- Return array of devices.

**On `Failure`**: `error` is <code>[ListAccountDevices2ErrorBody](verizon/errors/list_account_devices2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_available_software(account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[SoftwarePackage], ListAvailableSoftwareErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows user to list a certain type of software of an account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v2.with_raw_response.list_available_software(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[SoftwarePackage]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAvailableSoftwareErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v2.with_raw_response.list_available_software(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[SoftwarePackage]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type ListAvailableSoftwareErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>distribution_type</code> | <code>str \| None</code> | Filter distributionType to get specific type of software. Value is LWM2M, OMD-DM or HTTP.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[SoftwarePackage](verizon/models/software_package.py)&#93;, [ListAvailableSoftwareErrorBody](verizon/errors/list_available_software_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[SoftwarePackage](verizon/models/software_package.py)&#93;</code> -- Return array of software.

**On `Failure`**: `error` is <code>[ListAvailableSoftwareErrorBody](verizon/errors/list_available_software_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementReportsV3

> Source: [SoftwareManagementReportsV3](verizon/apis/software_management_reports_v3.py)

<details>
<summary><code>def get_campaign_device_status2(acc: str, campaign_id: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3CampaignDevice, GetCampaignDeviceStatus2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a list of all devices in a campaign and the status of each device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v3.with_raw_response.get_campaign_device_status2(acc, campaign_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3CampaignDevice
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignDeviceStatus2ErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v3.with_raw_response.get_campaign_device_status2(
    acc, campaign_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3CampaignDevice
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignDeviceStatus2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>campaign_id</code> | <code>str</code> | Campaign identifier. |
| <code>last_seen_device_id</code> | <code>str \| None</code> | Last seen device identifier.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3CampaignDevice](verizon/models/v3_campaign_device.py), [GetCampaignDeviceStatus2ErrorBody](verizon/errors/get_campaign_device_status2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3CampaignDevice](verizon/models/v3_campaign_device.py)</code> -- Returns an array of campaign history.

**On `Failure`**: `error` is <code>[GetCampaignDeviceStatus2ErrorBody](verizon/errors/get_campaign_device_status2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_campaign_history_by_status2(acc: str, campaign_status: CampaignStatusOrStr, *, last_seen_campaign_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V3CampaignHistory, GetCampaignHistoryByStatus2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a list of campaigns for an account that have a specified campaign status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v3.with_raw_response.get_campaign_history_by_status2(acc, campaign_status)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3CampaignHistory
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignHistoryByStatus2ErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v3.with_raw_response.get_campaign_history_by_status2(
    acc, campaign_status
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V3CampaignHistory
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetCampaignHistoryByStatus2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>campaign_status</code> | <code>[CampaignStatusOrStr](verizon/models/enums/campaign_status.py)</code> | Campaign status. |
| <code>last_seen_campaign_id</code> | <code>str \| None</code> | Last seen campaign Id.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V3CampaignHistory](verizon/models/v3_campaign_history.py), [GetCampaignHistoryByStatus2ErrorBody](verizon/errors/get_campaign_history_by_status2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V3CampaignHistory](verizon/models/v3_campaign_history.py)</code> -- Return array of campaign history.

**On `Failure`**: `error` is <code>[GetCampaignHistoryByStatus2ErrorBody](verizon/errors/get_campaign_history_by_status2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device_firmware_upgrade_history3(acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceFirmwareUpgrade], GetDeviceFirmwareUpgradeHistory3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve campaign history for a specific device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_reports_v3.with_raw_response.get_device_firmware_upgrade_history3(acc, device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceFirmwareUpgrade]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceFirmwareUpgradeHistory3ErrorBody
```

**Async**

```python
result = await async_client.software_management_reports_v3.with_raw_response.get_device_firmware_upgrade_history3(
    acc, device_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceFirmwareUpgrade]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetDeviceFirmwareUpgradeHistory3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>device_id</code> | <code>str</code> | Device IMEI identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceFirmwareUpgrade](verizon/models/device_firmware_upgrade.py)&#93;, [GetDeviceFirmwareUpgradeHistory3ErrorBody](verizon/errors/get_device_firmware_upgrade_history3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceFirmwareUpgrade](verizon/models/device_firmware_upgrade.py)&#93;</code> -- Returns a list of firmware upgrades.

**On `Failure`**: `error` is <code>[GetDeviceFirmwareUpgradeHistory3ErrorBody](verizon/errors/get_device_firmware_upgrade_history3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementSubscriptionsV1

> Source: [SoftwareManagementSubscriptionsV1](verizon/apis/software_management_subscriptions_v1.py)

<details>
<summary><code>def get_account_license_status(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccountLicenseInfo, GetAccountLicenseStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about an account's Software Management Services licenses and a list of licensed devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_subscriptions_v1.with_raw_response.get_account_license_status(account, start_index)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountLicenseInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountLicenseStatusErrorBody
```

**Async**

```python
result = await async_client.software_management_subscriptions_v1.with_raw_response.get_account_license_status(
    account, start_index
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccountLicenseInfo
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountLicenseStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>start_index</code> | <code>str</code> | The zero-based number of the first record to return. Set startIndex=0 for the first request. If there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for the third request, etc. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[AccountLicenseInfo](verizon/models/account_license_info.py), [GetAccountLicenseStatusErrorBody](verizon/errors/get_account_license_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccountLicenseInfo](verizon/models/account_license_info.py)</code> -- Account license information.

**On `Failure`**: `error` is <code>[GetAccountLicenseStatusErrorBody](verizon/errors/get_account_license_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_account_subscription_status(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1AccountSubscription, GetAccountSubscriptionStatusErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_subscriptions_v1.with_raw_response.get_account_subscription_status(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1AccountSubscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountSubscriptionStatusErrorBody
```

**Async**

```python
result = await async_client.software_management_subscriptions_v1.with_raw_response.get_account_subscription_status(
    account
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1AccountSubscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountSubscriptionStatusErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier in "##########-#####". |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[V1AccountSubscription](verizon/models/v1_account_subscription.py), [GetAccountSubscriptionStatusErrorBody](verizon/errors/get_account_subscription_status_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1AccountSubscription](verizon/models/v1_account_subscription.py)</code> -- Account subscription information.

**On `Failure`**: `error` is <code>[GetAccountSubscriptionStatusErrorBody](verizon/errors/get_account_subscription_status_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV1Result](verizon/models/fota_v1_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementSubscriptionsV2

> Source: [SoftwareManagementSubscriptionsV2](verizon/apis/software_management_subscriptions_v2.py)

<details>
<summary><code>def get_account_subscription_status2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV2Subscription, GetAccountSubscriptionStatus2ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint retrieves a FOTA subscription by account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_subscriptions_v2.with_raw_response.get_account_subscription_status2(account)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2Subscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountSubscriptionStatus2ErrorBody
```

**Async**

```python
result = await async_client.software_management_subscriptions_v2.with_raw_response.get_account_subscription_status2(
    account
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV2Subscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountSubscriptionStatus2ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV2Subscription](verizon/models/fota_v2_subscription.py), [GetAccountSubscriptionStatus2ErrorBody](verizon/errors/get_account_subscription_status2_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV2Subscription](verizon/models/fota_v2_subscription.py)</code> -- FOTA Subscription.

**On `Failure`**: `error` is <code>[GetAccountSubscriptionStatus2ErrorBody](verizon/errors/get_account_subscription_status2_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV2Result](verizon/models/fota_v2_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## SoftwareManagementSubscriptionsV3

> Source: [SoftwareManagementSubscriptionsV3](verizon/apis/software_management_subscriptions_v3.py)

<details>
<summary><code>def get_account_subscription_status3(acc: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[FotaV3Subscription, GetAccountSubscriptionStatus3ErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint retrieves a FOTA subscription by account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.software_management_subscriptions_v3.with_raw_response.get_account_subscription_status3(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3Subscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountSubscriptionStatus3ErrorBody
```

**Async**

```python
result = await async_client.software_management_subscriptions_v3.with_raw_response.get_account_subscription_status3(acc)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type FotaV3Subscription
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAccountSubscriptionStatus3ErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>acc</code> | <code>str</code> | Account identifier. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[FotaV3Subscription](verizon/models/fota_v3_subscription.py), [GetAccountSubscriptionStatus3ErrorBody](verizon/errors/get_account_subscription_status3_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[FotaV3Subscription](verizon/models/fota_v3_subscription.py)</code> -- FOTA Subscription.

**On `Failure`**: `error` is <code>[GetAccountSubscriptionStatus3ErrorBody](verizon/errors/get_account_subscription_status3_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[FotaV3Result](verizon/models/fota_v3_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## Targets

> Source: [Targets](verizon/apis/targets.py)

<details>
<summary><code>def create_azure_central_io_t_application(billingaccount_id: str, body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateIoTapplicationResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deploy a new Azure IoT Central application based on the Verizon ARM template within the specified Azure Active Directory account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.targets.with_raw_response.create_azure_central_io_t_application(billingaccount_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateIoTapplicationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.targets.with_raw_response.create_azure_central_io_t_application(billingaccount_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateIoTapplicationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>billingaccount_id</code> | <code>str</code> | TThe ThingSpace ID of the authenticating billing account. |
| <code>body</code> | <code>[CreateIoTapplicationRequest](verizon/models/create_io_tapplication_request.py) \| [CreateIoTapplicationRequestDict](verizon/models/create_io_tapplication_request.py)</code> | The request body must include the UUID of the subscription that you want to update plus any properties that you want to change. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[CreateIoTapplicationResponse](verizon/models/create_io_tapplication_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateIoTapplicationResponse](verizon/models/create_io_tapplication_response.py)</code> -- A success response includes the full subscription resource definition.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_target(body: CreateTargetRequest | CreateTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Target, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Define a target to receive data streams, alerts, or callbacks. After creating the target resource, use its ID in a subscription to set up a data stream.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.targets.with_raw_response.create_target(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Target
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.targets.with_raw_response.create_target(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Target
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTargetRequest](verizon/models/create_target_request.py) \| [CreateTargetRequestDict](verizon/models/create_target_request.py)</code> | The request body provides the details of the target that you want to create. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Target](verizon/models/target.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Target](verizon/models/target.py)</code> -- A success response includes the full target resource definition.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_target(body: DeleteTargetRequest | DeleteTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Remove a target from a ThingSpace account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.targets.with_raw_response.delete_target(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.targets.with_raw_response.delete_target(body)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeleteTargetRequest](verizon/models/delete_target_request.py) \| [DeleteTargetRequestDict](verizon/models/delete_target_request.py)</code> | The request body identifies the target to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_target_external_id(body: GenerateExternalIdrequest | GenerateExternalIdrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GenerateExternalIdresult, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a unique string that ThingSpace will pass to AWS for increased security.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.targets.with_raw_response.generate_target_external_id(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateExternalIdresult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.targets.with_raw_response.generate_target_external_id(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GenerateExternalIdresult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GenerateExternalIdrequest](verizon/models/generate_external_idrequest.py) \| [GenerateExternalIdrequestDict](verizon/models/generate_external_idrequest.py)</code> | The request body only contains the authenticating account. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[GenerateExternalIdresult](verizon/models/generate_external_idresult.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GenerateExternalIdresult](verizon/models/generate_external_idresult.py)</code> -- Returns a new external ID.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_target(body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Target], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for targets by property values. Returns an array of all matching target resources.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.targets.with_raw_response.query_target(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Target]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.targets.with_raw_response.query_target(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Target]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[QueryTargetRequest](verizon/models/query_target_request.py) \| [QueryTargetRequestDict](verizon/models/query_target_request.py)</code> | Search for targets by property values. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[Target](verizon/models/target.py)&#93;, [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[Target](verizon/models/target.py)&#93;</code> -- A success response includes an array of all matching targets. Each target includes the full target resource definition.

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ThingSpaceQualityOfServiceApiActions

> Source: [ThingSpaceQualityOfServiceApiActions](verizon/apis/thing_space_quality_of_service_api_actions.py)

<details>
<summary><code>def create_a_thing_space_quality_of_service_api_subscription(body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Success201, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a QoS elevation subscription ID and activates the subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.thing_space_quality_of_service_api_actions.with_raw_response.create_a_thing_space_quality_of_service_api_subscription(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Success201
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.thing_space_quality_of_service_api_actions.with_raw_response.create_a_thing_space_quality_of_service_api_subscription(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Success201
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SubscribeRequest](verizon/models/subscribe_request.py) \| [SubscribeRequestDict](verizon/models/subscribe_request.py)</code> | The request details to create a ThingSpace Quality of Service API subscription. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Success201](verizon/models/success201.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Success201](verizon/models/success201.py)</code> -- Success Response

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_a_thing_space_quality_of_service_api_subscription(account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[Success201, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Stops an active ThingSpace Quality of Service API subscription using the account name and the subscription ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.thing_space_quality_of_service_api_actions.with_raw_response.stop_a_thing_space_quality_of_service_api_subscription(
    account_name, qos_subscription_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Success201
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.thing_space_quality_of_service_api_actions.with_raw_response.stop_a_thing_space_quality_of_service_api_subscription(
    account_name, qos_subscription_id
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type Success201
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Value sent with the request. |
| <code>qos_subscription_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[Success201](verizon/models/success201.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[Success201](verizon/models/success201.py)</code> -- Success Response

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UpdatePricePlanTriggers

> Source: [UpdatePricePlanTriggers](verizon/apis/update_price_plan_triggers.py)

<details>
<summary><code>def update_trigger_rules(body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TriggerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a usage trigger at the account level, device level or a price plan trigger for all devices on the account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.update_price_plan_triggers.with_raw_response.update_trigger_rules(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.update_price_plan_triggers.with_raw_response.update_trigger_rules(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[V2TriggersRequest1](verizon/models/unions/v2_triggers_request1.py) \| [V2TriggersRequest1Dict](verizon/models/unions/v2_triggers_request1.py)</code> | Update a trigger |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[TriggerResponse](verizon/models/trigger_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TriggerResponse](verizon/models/trigger_response.py)</code> -- Successful request

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UpdateTriggers

> Source: [UpdateTriggers](verizon/apis/update_triggers.py)

<details>
<summary><code>def update_all_available_triggers(*, body: RequestTrigger | RequestTriggerDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SuccessModel, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the promotional triggers for pseudo-MDN.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.update_triggers.with_raw_response.update_all_available_triggers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SuccessModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.update_triggers.with_raw_response.update_all_available_triggers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SuccessModel
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RequestTrigger](verizon/models/request_trigger.py) \| [RequestTriggerDict](verizon/models/request_trigger.py) \| None</code> | Update the triggers<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[SuccessModel](verizon/models/success_model.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SuccessModel](verizon/models/success_model.py)</code> -- Status of Request

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UsageTriggerManagement

> Source: [UsageTriggerManagement](verizon/apis/usage_trigger_management.py)

<details>
<summary><code>def create_new_trigger(*, body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsageTriggerResponse, CreateNewTriggerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Create a new usage trigger, which will send an alert when the number of device location service transactions reaches a specified percentage of the monthly subscription amount.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.usage_trigger_management.with_raw_response.create_new_trigger()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageTriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateNewTriggerErrorBody
```

**Async**

```python
result = await async_client.usage_trigger_management.with_raw_response.create_new_trigger()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageTriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type CreateNewTriggerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UsageTriggerAddRequest](verizon/models/usage_trigger_add_request.py) \| [UsageTriggerAddRequestDict](verizon/models/usage_trigger_add_request.py) \| None</code> | License assignment.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UsageTriggerResponse](verizon/models/usage_trigger_response.py), [CreateNewTriggerErrorBody](verizon/errors/create_new_trigger_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsageTriggerResponse](verizon/models/usage_trigger_response.py)</code> -- Usage trigger Add result

**On `Failure`**: `error` is <code>[CreateNewTriggerErrorBody](verizon/errors/create_new_trigger_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_trigger(account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceLocationSuccessResult, DeleteTriggerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

eletes the specified usage trigger from the given account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.usage_trigger_management.with_raw_response.delete_trigger(account_name, trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteTriggerErrorBody
```

**Async**

```python
result = await async_client.usage_trigger_management.with_raw_response.delete_trigger(account_name, trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceLocationSuccessResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteTriggerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_name</code> | <code>str</code> | Account name |
| <code>trigger_id</code> | <code>str</code> | Usage trigger ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py), [DeleteTriggerErrorBody](verizon/errors/delete_trigger_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Delete result

**On `Failure`**: `error` is <code>[DeleteTriggerErrorBody](verizon/errors/delete_trigger_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_trigger(trigger_id: str, *, body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UsageTriggerResponse, UpdateTriggerErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Update an existing usage trigger

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.usage_trigger_management.with_raw_response.update_trigger(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageTriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateTriggerErrorBody
```

**Async**

```python
result = await async_client.usage_trigger_management.with_raw_response.update_trigger(trigger_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UsageTriggerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type UpdateTriggerErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>trigger_id</code> | <code>str</code> | Usage trigger ID |
| <code>body</code> | <code>[UsageTriggerUpdateRequest](verizon/models/usage_trigger_update_request.py) \| [UsageTriggerUpdateRequestDict](verizon/models/usage_trigger_update_request.py) \| None</code> | New trigger values<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[UsageTriggerResponse](verizon/models/usage_trigger_response.py), [UpdateTriggerErrorBody](verizon/errors/update_trigger_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[UsageTriggerResponse](verizon/models/usage_trigger_response.py)</code> -- Usage trigger Modify result

**On `Failure`**: `error` is <code>[UpdateTriggerErrorBody](verizon/errors/update_trigger_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[DeviceLocationResult](verizon/models/device_location_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## WirelessNetworkPerformance

> Source: [WirelessNetworkPerformance](verizon/apis/wireless_network_performance.py)

<details>
<summary><code>def device_experience30days_history(body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WnprequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

A report of a specific device's service scores over a 30 day period.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wireless_network_performance.with_raw_response.device_experience30days_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.wireless_network_performance.with_raw_response.device_experience30days_history(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetDeviceExperienceScoreHistoryRequest](verizon/models/get_device_experience_score_history_request.py) \| [GetDeviceExperienceScoreHistoryRequestDict](verizon/models/get_device_experience_score_history_request.py)</code> | Request for a device's 30 day experience. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[WnprequestResponse](verizon/models/wnprequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def device_experience_bulk_latest(body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WnprequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Run a report to view the latest device experience score for specific devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wireless_network_performance.with_raw_response.device_experience_bulk_latest(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.wireless_network_performance.with_raw_response.device_experience_bulk_latest(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetDeviceExperienceScoreBulkRequest](verizon/models/get_device_experience_score_bulk_request.py) \| [GetDeviceExperienceScoreBulkRequestDict](verizon/models/get_device_experience_score_bulk_request.py)</code> | Request for bulk latest history details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[WnprequestResponse](verizon/models/wnprequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def domestic4_g_and5_g_nationwide_network_coverage(body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WnprequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Run a report for FWA Address qualification or to determine network types available and available coverage. Network types covered include: CAT-M, NB-IOT, LTE, LTE-AWS, 5GNW, MMWAVE and C-BAND.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wireless_network_performance.with_raw_response.domestic4_g_and5_g_nationwide_network_coverage(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.wireless_network_performance.with_raw_response.domestic4_g_and5_g_nationwide_network_coverage(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[M2MV1IntelligenceWirelessCoverageRequest](verizon/models/unions/m2_mv1_intelligence_wireless_coverage_request.py) \| [M2MV1IntelligenceWirelessCoverageRequestDict](verizon/models/unions/m2_mv1_intelligence_wireless_coverage_request.py)</code> | Request for network coverage details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[WnprequestResponse](verizon/models/wnprequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def near_real_time_network_conditions(body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WnprequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

WNP Query for current network condition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wireless_network_performance.with_raw_response.near_real_time_network_conditions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.wireless_network_performance.with_raw_response.near_real_time_network_conditions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetNetworkConditionsRequest](verizon/models/get_network_conditions_request.py) \| [GetNetworkConditionsRequestDict](verizon/models/get_network_conditions_request.py)</code> | Request for current network health. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[WnprequestResponse](verizon/models/wnprequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def site_proximity(body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[WnprequestResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Identify the direction and general distance of nearby cell sites and the technology supported by the equipment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.wireless_network_performance.with_raw_response.site_proximity(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.wireless_network_performance.with_raw_response.site_proximity(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type WnprequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[GetNetworkConditionsRequest](verizon/models/get_network_conditions_request.py) \| [GetNetworkConditionsRequestDict](verizon/models/get_network_conditions_request.py)</code> | Request for cell site proximity. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[WnprequestResponse](verizon/models/wnprequest_response.py), [RawError](verizon/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[RawError](verizon/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceRoleController

> Source: [DeviceRoleController](verizon/apis/device_role_controller.py)

<details>
<summary><code>def get_acl_rules_by_vendor_id(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[DeviceRole], GetAclrulesByVendorIdErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This API allows the user to get the access control rules defined for them.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.device_role_controller.with_raw_response.get_acl_rules_by_vendor_id(vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceRole]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAclrulesByVendorIdErrorBody
```

**Async**

```python
result = await async_client.device_role_controller.with_raw_response.get_acl_rules_by_vendor_id(vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[DeviceRole]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type GetAclrulesByVendorIdErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The user's Vendor ID |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;[DeviceRole](verizon/models/device_role.py)&#93;, [GetAclrulesByVendorIdErrorBody](verizon/errors/get_aclrules_by_vendor_id_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[DeviceRole](verizon/models/device_role.py)&#93;</code> -- List of Access Rules

**On `Failure`**: `error` is <code>[GetAclrulesByVendorIdErrorBody](verizon/errors/get_aclrules_by_vendor_id_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 406, 429 | <code>str</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## EUiccDeviceProfileManagement

> Source: [EUiccDeviceProfileManagement](verizon/apis/e_uicc_device_profile_management.py)

<details>
<summary><code>def delete_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, DeleteLocalProfileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Delete a local profile from eUICC devices. If the local profile is enabled, it will first be disabled and the boot or default profile will be enabled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.e_uicc_device_profile_management.with_raw_response.delete_local_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteLocalProfileErrorBody
```

**Async**

```python
result = await async_client.e_uicc_device_profile_management.with_raw_response.delete_local_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteLocalProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileChangeStateRequest](verizon/models/profile_change_state_request.py) \| [ProfileChangeStateRequestDict](verizon/models/profile_change_state_request.py)</code> | Update state |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [DeleteLocalProfileErrorBody](verizon/errors/delete_local_profile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[DeleteLocalProfileErrorBody](verizon/errors/delete_local_profile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, DisableLocalProfileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disable a local profile on eUICC devices. The default or boot profile will become the enabled profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.e_uicc_device_profile_management.with_raw_response.disable_local_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DisableLocalProfileErrorBody
```

**Async**

```python
result = await async_client.e_uicc_device_profile_management.with_raw_response.disable_local_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DisableLocalProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileChangeStateRequest](verizon/models/profile_change_state_request.py) \| [ProfileChangeStateRequestDict](verizon/models/profile_change_state_request.py)</code> | Update state |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [DisableLocalProfileErrorBody](verizon/errors/disable_local_profile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[DisableLocalProfileErrorBody](verizon/errors/disable_local_profile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_local_profile_to_disable(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, DownloadLocalProfileToDisableErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads an eUICC local profile to devices and leaves the profile disabled.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.e_uicc_device_profile_management.with_raw_response.download_local_profile_to_disable(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadLocalProfileToDisableErrorBody
```

**Async**

```python
result = await async_client.e_uicc_device_profile_management.with_raw_response.download_local_profile_to_disable(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadLocalProfileToDisableErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileChangeStateRequest](verizon/models/profile_change_state_request.py) \| [ProfileChangeStateRequestDict](verizon/models/profile_change_state_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [DownloadLocalProfileToDisableErrorBody](verizon/errors/download_local_profile_to_disable_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[DownloadLocalProfileToDisableErrorBody](verizon/errors/download_local_profile_to_disable_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_local_profile_to_enable(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeviceManagementResult, DownloadLocalProfileToEnableErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Downloads an eUICC local profile to devices and enables the profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.e_uicc_device_profile_management.with_raw_response.download_local_profile_to_enable(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadLocalProfileToEnableErrorBody
```

**Async**

```python
result = await async_client.e_uicc_device_profile_management.with_raw_response.download_local_profile_to_enable(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeviceManagementResult
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadLocalProfileToEnableErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileChangeStateRequest](verizon/models/profile_change_state_request.py) \| [ProfileChangeStateRequestDict](verizon/models/profile_change_state_request.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[DeviceManagementResult](verizon/models/device_management_result.py), [DownloadLocalProfileToEnableErrorBody](verizon/errors/download_local_profile_to_enable_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**On `Failure`**: `error` is <code>[DownloadLocalProfileToEnableErrorBody](verizon/errors/download_local_profile_to_enable_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[ConnectivityManagementResult](verizon/models/connectivity_management_result.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RequestResponse, EnableLocalProfileErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enable a local profile that has been downloaded to eUICC devices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.e_uicc_device_profile_management.with_raw_response.enable_local_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EnableLocalProfileErrorBody
```

**Async**

```python
result = await async_client.e_uicc_device_profile_management.with_raw_response.enable_local_profile(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RequestResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type EnableLocalProfileErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ProfileChangeStateRequest](verizon/models/profile_change_state_request.py) \| [ProfileChangeStateRequestDict](verizon/models/profile_change_state_request.py)</code> | Update state |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;[RequestResponse](verizon/models/request_response.py), [EnableLocalProfileErrorBody](verizon/errors/enable_local_profile_error.py)&#93;</code>

**On `Success`**: `payload` is <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**On `Failure`**: `error` is <code>[EnableLocalProfileErrorBody](verizon/errors/enable_local_profile_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400 | <code>[RestErrorResponse](verizon/models/rest_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

## MapMessageController

> Source: [MapMessageController](verizon/apis/map_message_controller.py)

<details>
<summary><code>def delete_map_message(region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[None, DeleteMapMessageErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a map message for the specified region and intersection ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.map_message_controller.with_raw_response.delete_map_message(region_id, i10nid)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteMapMessageErrorBody
```

**Async**

```python
result = await async_client.map_message_controller.with_raw_response.delete_map_message(region_id, i10nid)
match result:
    case Success():
        ...  # 2xx, no content
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DeleteMapMessageErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>region_id</code> | <code>str</code> | Region ID to filter the map messages. |
| <code>i10nid</code> | <code>str</code> | Intersection ID to filter the map messages. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;None, [DeleteMapMessageErrorBody](verizon/errors/delete_map_message_error.py)&#93;</code>

**On `Success`**: the 2xx carries no content; `payload` is <code>None</code>

**On `Failure`**: `error` is <code>[DeleteMapMessageErrorBody](verizon/errors/delete_map_message_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 429, 503 | <code>[MdmErrorResponse](verizon/models/mdm_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_map_messages(geofence: GeofencePolygon | GeofencePolygonDict, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, DownloadMapmessagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint is deprecated. (Use /api/v2/mapdata/query for new integrations).

This endpoint allows user to download SAE J2735 or ETSI MAP messages in ASN.1 UPER base64 encoded format. The area for the MAP messages is needed to be defined in the query.


**Required request header:** `Accept` — specifies the response format. Omitting this header will result in a `400 Bad Request`. Supported values:
- `text/plain` — ASN.1 UPER base64-encoded MAP messages (one per line)
- `application/json` — JSON-encoded MAP messages

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.map_message_controller.with_raw_response.download_map_messages(geofence, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadMapmessagesErrorBody
```

**Async**

```python
result = await async_client.map_message_controller.with_raw_response.download_map_messages(geofence, vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type DownloadMapmessagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>geofence</code> | <code>[GeofencePolygon](verizon/models/geofence_polygon.py) \| [GeofencePolygonDict](verizon/models/geofence_polygon.py)</code> | GeoJSON Polygon defining the area to retrieve MAP messages for. |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;str, [DownloadMapmessagesErrorBody](verizon/errors/download_mapmessages_error.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- Line separated ASN.1 UPER J2735/ETSI base64 encoded MapData messages

**On `Failure`**: `error` is <code>[DownloadMapmessagesErrorBody](verizon/errors/download_mapmessages_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 404, 429, 503 | <code>[MdmErrorResponse](verizon/models/mdm_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def ingest_map_messages(vendor_id: str, map_data_message_standard: EtxmessageStandardEnumOrStr, body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[str, IngestMapmessagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows the user to upload map messages in ASN.1 UPER base64 encoded format or JER (JSON) formats. The MAP data message can have more than one intersections in it.
Both SAE and ETSI defined MAP messages are supported. The SAE type MAP messages have to be wrapped in a MessageFrame, as defined in the SAE J2735 standard.
The ETSI type MAP messages are expected as MAPEM structures that include the ETSI header, as defined in the ETSI TS 103 301 standard.
Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M tokens in order to call this API.

**Required request header:** `Content-Type` — specifies the format of the request body. Omitting or sending an unsupported value will result in a `415 Unsupported Media Type`. Supported values:
- `text/plain` — ASN.1 UPER base64-encoded MAP message
- `application/json` — JSON representation of the MAP message

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.map_message_controller.with_raw_response.ingest_map_messages(vendor_id, map_data_message_standard, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type IngestMapmessagesErrorBody
```

**Async**

```python
result = await async_client.map_message_controller.with_raw_response.ingest_map_messages(
    vendor_id, map_data_message_standard, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type str
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type IngestMapmessagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>map_data_message_standard</code> | <code>[EtxmessageStandardEnumOrStr](verizon/models/enums/etxmessage_standard_enum.py)</code> | Select which V2X messaging standard will be used for the message generation. The following options are supported:<br>- "etsi": The message will be generated using the ETSI (European) standard (e.g. MAPEM).<br>- "sae": The message will be generated using the SAE J2735 (North American) standard (e.g. MAP).<br>- if not sent while POST, defaults to "sae" |
| <code>body</code> | <code>[EtxMapDataIngestRequest](verizon/models/etx_map_data_ingest_request.py) \| [EtxMapDataIngestRequestDict](verizon/models/etx_map_data_ingest_request.py)</code> | UPER/ASN.1 J2735/ETSI base64 encoded MapData message or JSON representation of the MapData message. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;str, [IngestMapmessagesErrorBody](verizon/errors/ingest_mapmessages_error.py)&#93;</code>

**On `Success`**: `payload` is <code>str</code> -- Map message/s successfully uploaded

**On `Failure`**: `error` is <code>[IngestMapmessagesErrorBody](verizon/errors/ingest_mapmessages_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 405, 429, 503 | <code>[MdmErrorResponse](verizon/models/mdm_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_map_messages(vendor_id: str, body: MapDataQueryRequest | MapDataQueryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[Any], QueryMapMessagesErrorBody]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

This endpoint allows users to download SAE J2735 or ETSI MAP messages as a JSON list. 
Depending on the expectedType parameter, the response contains either ASN.1 UPER base64-encoded messages with their respective region and intersection IDs, or fully decoded JSON messages. 
The area for MAP message retrieval must be defined in the request body using one of two methods: 
An array of region and intersection ID pairs, or a GeoJSON geofence specification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.map_message_controller.with_raw_response.query_map_messages(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Any]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryMapMessagesErrorBody
```

**Async**

```python
result = await async_client.map_message_controller.with_raw_response.query_map_messages(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[Any]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type QueryMapMessagesErrorBody
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | The VendorID set during the Vendor registration call. |
| <code>body</code> | <code>[MapDataQueryRequest](verizon/models/unions/map_data_query_request.py) \| [MapDataQueryRequestDict](verizon/models/unions/map_data_query_request.py)</code> | The request body. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](verizon/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](verizon/core/results.py)&#91;list&#91;Any&#93;, [QueryMapMessagesErrorBody](verizon/errors/query_map_messages_error.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;Any&#93;</code> -- Successfully retrieved MAP messages. Returns a JSON array where each element contains either a base64 string or parsed message object.

**On `Failure`**: `error` is <code>[QueryMapMessagesErrorBody](verizon/errors/query_map_messages_error.py)</code>

Mapped in first-match order -- an earlier row wins over a later range that also covers the status:

| Status | `error` is |
| --- | --- |
| 400, 401, 403, 405, 429, 503 | <code>[MdmErrorResponse](verizon/models/mdm_error_response.py)</code> |
| anything unmapped | <code>[RawError](verizon/core/results.py)</code> |

</dd>
</dl>

</dd>
</dl>

</details>

