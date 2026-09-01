# Reference

**Parsed** endpoints return the typed payload and raise `ApiError` on a documented non-2xx. For the raw endpoints, see [Raw API Reference](raw-api-reference.md).

> Source: [VerizonClient](verizon/client.py)

## GbiDeviceActions5

> Source: [GbiDeviceActions5](verizon/apis/gbi_device_actions5.py)

<details>
<summary><code>def business_internet_serviceplanchange(body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None) -> GbiRequestResponse5</code></summary>

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
try:
    response = client.gbi_device_actions5.business_internet_serviceplanchange(body)
    # TODO: Handle 'response' of type GbiRequestResponse5
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.gbi_device_actions5.business_internet_serviceplanchange(body)
    # TODO: Handle 'response' of type GbiRequestResponse5
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GbiRequestResponse5](verizon/models/gbi_request_response5.py)</code> -- A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_internetactivate_using_post(body: GbiactivateRequest5 | GbiactivateRequest5Dict, *, request_options: RequestOptionsOrDict | None = None) -> GbiRequestResponse5</code></summary>

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
try:
    response = client.gbi_device_actions5.business_internetactivate_using_post(body)
    # TODO: Handle 'response' of type GbiRequestResponse5
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.gbi_device_actions5.business_internetactivate_using_post(body)
    # TODO: Handle 'response' of type GbiRequestResponse5
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GbiRequestResponse5](verizon/models/gbi_request_response5.py)</code> -- A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def business_internetlist_device_information(body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None) -> GbideviceDetailsresponse5</code></summary>

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
try:
    response = client.gbi_device_actions5.business_internetlist_device_information(body)
    # TODO: Handle 'response' of type GbideviceDetailsresponse5
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.gbi_device_actions5.business_internetlist_device_information(body)
    # TODO: Handle 'response' of type GbideviceDetailsresponse5
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GbideviceDetailsresponse5](verizon/models/gbidevice_detailsresponse5.py)</code> -- The device's details will be returned from a successful request.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AccountDevices

> Source: [AccountDevices](verizon/apis/account_devices.py)

<details>
<summary><code>def get_account_device_information(acc: str, *, last_seen_device_id: str | None = None, protocol: DevicesProtocolOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> V3AccountDeviceList</code></summary>

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
try:
    response = client.account_devices.get_account_device_information(acc)
    # TODO: Handle 'response' of type V3AccountDeviceList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountDeviceInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.account_devices.get_account_device_information(acc)
    # TODO: Handle 'response' of type V3AccountDeviceList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountDeviceInformationErrorBody
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

**OnSuccess**: <code>[V3AccountDeviceList](verizon/models/v3_account_device_list.py)</code> -- Returns an array of devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountDeviceInformationErrorBody](verizon/errors/get_account_device_information_error.py)&#93;</code>

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
<summary><code>def list_account_devices_information(acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceListResult</code></summary>

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
try:
    response = client.account_devices.list_account_devices_information(acc, body)
    # TODO: Handle 'response' of type DeviceListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountDevicesInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.account_devices.list_account_devices_information(acc, body)
    # TODO: Handle 'response' of type DeviceListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountDevicesInformationErrorBody
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

**OnSuccess**: <code>[DeviceListResult](verizon/models/device_list_result.py)</code> -- Get device list information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountDevicesInformationErrorBody](verizon/errors/list_account_devices_information_error.py)&#93;</code>

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
<summary><code>def get_current_asynchronous_request_status(aname: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AsynchronousRequestResult</code></summary>

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
try:
    response = client.account_requests.get_current_asynchronous_request_status(aname, request_id)
    # TODO: Handle 'response' of type AsynchronousRequestResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrentAsynchronousRequestStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.account_requests.get_current_asynchronous_request_status(aname, request_id)
    # TODO: Handle 'response' of type AsynchronousRequestResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCurrentAsynchronousRequestStatusErrorBody
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

**OnSuccess**: <code>[AsynchronousRequestResult](verizon/models/asynchronous_request_result.py)</code> -- The asynchronous request status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCurrentAsynchronousRequestStatusErrorBody](verizon/errors/get_current_asynchronous_request_status_error.py)&#93;</code>

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
<summary><code>def get_account_information_using_get(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> GetAccountInformationResponseforplanner</code></summary>

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
try:
    response = client.account_service_controller.get_account_information_using_get(account_name)
    # TODO: Handle 'response' of type GetAccountInformationResponseforplanner
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountInformationUsingGetErrorBody
```

**Async**

```python
try:
    response = await async_client.account_service_controller.get_account_information_using_get(account_name)
    # TODO: Handle 'response' of type GetAccountInformationResponseforplanner
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountInformationUsingGetErrorBody
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

**OnSuccess**: <code>[GetAccountInformationResponseforplanner](verizon/models/get_account_information_responseforplanner.py)</code> -- The account information related to an account.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountInformationUsingGetErrorBody](verizon/errors/get_account_information_using_get_error.py)&#93;</code>

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
<summary><code>def list_account_subscriptions(body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict, *, x_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SecuritySubscriptionResult</code></summary>

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
try:
    response = client.account_subscriptions.list_account_subscriptions(body)
    # TODO: Handle 'response' of type SecuritySubscriptionResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountSubscriptionsErrorBody
```

**Async**

```python
try:
    response = await async_client.account_subscriptions.list_account_subscriptions(body)
    # TODO: Handle 'response' of type SecuritySubscriptionResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountSubscriptionsErrorBody
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

**OnSuccess**: <code>[SecuritySubscriptionResult](verizon/models/security_subscription_result.py)</code> -- Security subscription result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountSubscriptionsErrorBody](verizon/errors/list_account_subscriptions_error.py)&#93;</code>

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
<summary><code>def get_account_information(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> Account</code></summary>

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
try:
    response = client.accounts.get_account_information(aname)
    # TODO: Handle 'response' of type Account
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.accounts.get_account_information(aname)
    # TODO: Handle 'response' of type Account
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountInformationErrorBody
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

**OnSuccess**: <code>[Account](verizon/models/account.py)</code> -- The account information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountInformationErrorBody](verizon/errors/get_account_information_error.py)&#93;</code>

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
<summary><code>def list_account_leads(aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None) -> AccountLeadsResult</code></summary>

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
try:
    response = client.accounts.list_account_leads(aname)
    # TODO: Handle 'response' of type AccountLeadsResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountLeadsErrorBody
```

**Async**

```python
try:
    response = await async_client.accounts.list_account_leads(aname)
    # TODO: Handle 'response' of type AccountLeadsResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountLeadsErrorBody
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

**OnSuccess**: <code>[AccountLeadsResult](verizon/models/account_leads_result.py)</code> -- The list of leads associated with the account.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountLeadsErrorBody](verizon/errors/list_account_leads_error.py)&#93;</code>

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
<summary><code>def list_account_states_and_services(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> AccountStatesAndServices</code></summary>

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
try:
    response = client.accounts.list_account_states_and_services(aname)
    # TODO: Handle 'response' of type AccountStatesAndServices
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountStatesAndServicesErrorBody
```

**Async**

```python
try:
    response = await async_client.accounts.list_account_states_and_services(aname)
    # TODO: Handle 'response' of type AccountStatesAndServices
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountStatesAndServicesErrorBody
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

**OnSuccess**: <code>[AccountStatesAndServices](verizon/models/account_states_and_services.py)</code> -- The account's engagements, services, and states.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountStatesAndServicesErrorBody](verizon/errors/list_account_states_and_services_error.py)&#93;</code>

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
<summary><code>def activate_anomaly_detection(body: AnomalyDetectionRequest | AnomalyDetectionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> IntelligenceSuccessResult</code></summary>

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
try:
    response = client.anomaly_settings.activate_anomaly_detection(body)
    # TODO: Handle 'response' of type IntelligenceSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_settings.activate_anomaly_detection(body)
    # TODO: Handle 'response' of type IntelligenceSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py)</code> -- Success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_settings(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> AnomalyDetectionSettings</code></summary>

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
try:
    response = client.anomaly_settings.list_anomaly_detection_settings(account_name)
    # TODO: Handle 'response' of type AnomalyDetectionSettings
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_settings.list_anomaly_detection_settings(account_name)
    # TODO: Handle 'response' of type AnomalyDetectionSettings
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AnomalyDetectionSettings](verizon/models/anomaly_detection_settings.py)</code> -- Retrieve the settings for anomaly detection.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def reset_anomaly_detection_parameters(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> IntelligenceSuccessResult</code></summary>

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
try:
    response = client.anomaly_settings.reset_anomaly_detection_parameters(account_name)
    # TODO: Handle 'response' of type IntelligenceSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_settings.reset_anomaly_detection_parameters(account_name)
    # TODO: Handle 'response' of type IntelligenceSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py)</code> -- Success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## AnomalyTriggers

> Source: [AnomalyTriggers](verizon/apis/anomaly_triggers.py)

<details>
<summary><code>def create_anomaly_detection_trigger(body: CreateTriggerRequest | CreateTriggerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AnomalyDetectionTrigger</code></summary>

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
try:
    response = client.anomaly_triggers.create_anomaly_detection_trigger(body)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAnomalyDetectionTriggerErrorBody
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers.create_anomaly_detection_trigger(body)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAnomalyDetectionTriggerErrorBody
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

**OnSuccess**: <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- Trigger ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateAnomalyDetectionTriggerErrorBody](verizon/errors/create_anomaly_detection_trigger_error.py)&#93;</code>

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
<summary><code>def delete_anomaly_detection_trigger(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AnomalyDetectionTrigger</code></summary>

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
try:
    response = client.anomaly_triggers.delete_anomaly_detection_trigger(trigger_id)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers.delete_anomaly_detection_trigger(trigger_id)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- The ID of the deleted trigger is returned

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_trigger_settings(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[GetTriggerResponseList]</code></summary>

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
try:
    response = client.anomaly_triggers.list_anomaly_detection_trigger_settings(trigger_id)
    # TODO: Handle 'response' of type list[GetTriggerResponseList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAnomalyDetectionTriggerSettingsErrorBody
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers.list_anomaly_detection_trigger_settings(trigger_id)
    # TODO: Handle 'response' of type list[GetTriggerResponseList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAnomalyDetectionTriggerSettingsErrorBody
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

**OnSuccess**: <code>list&#91;[GetTriggerResponseList](verizon/models/get_trigger_response_list.py)&#93;</code> -- Trigger information associated to a Trigger Id

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAnomalyDetectionTriggerSettingsErrorBody](verizon/errors/list_anomaly_detection_trigger_settings_error.py)&#93;</code>

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
<summary><code>def list_anomaly_detection_triggers(*, request_options: RequestOptionsOrDict | None = None) -> list[GetTriggerResponseList]</code></summary>

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
try:
    response = client.anomaly_triggers.list_anomaly_detection_triggers()
    # TODO: Handle 'response' of type list[GetTriggerResponseList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAnomalyDetectionTriggersErrorBody
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers.list_anomaly_detection_triggers()
    # TODO: Handle 'response' of type list[GetTriggerResponseList]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAnomalyDetectionTriggersErrorBody
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

**OnSuccess**: <code>list&#91;[GetTriggerResponseList](verizon/models/get_trigger_response_list.py)&#93;</code> -- List of triggers associated to a Contact

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAnomalyDetectionTriggersErrorBody](verizon/errors/list_anomaly_detection_triggers_error.py)&#93;</code>

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
<summary><code>def update_anomaly_detection_trigger(body: UpdateTriggerRequest | UpdateTriggerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AnomalyDetectionTrigger</code></summary>

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
try:
    response = client.anomaly_triggers.update_anomaly_detection_trigger(body)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateAnomalyDetectionTriggerErrorBody
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers.update_anomaly_detection_trigger(body)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateAnomalyDetectionTriggerErrorBody
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

**OnSuccess**: <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- Trigger ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateAnomalyDetectionTriggerErrorBody](verizon/errors/update_anomaly_detection_trigger_error.py)&#93;</code>

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
<summary><code>def create_anomaly_detection_trigger_v2(body: list[CreateTriggerRequestOptions | CreateTriggerRequestOptionsDict], *, request_options: RequestOptionsOrDict | None = None) -> AnomalyDetectionTrigger</code></summary>

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
try:
    response = client.anomaly_triggers_v2.create_anomaly_detection_trigger_v2(body)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers_v2.create_anomaly_detection_trigger_v2(body)
    # TODO: Handle 'response' of type AnomalyDetectionTrigger
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AnomalyDetectionTrigger](verizon/models/anomaly_detection_trigger.py)</code> -- Result of request to create a trigger for anomaly detection.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_anomaly_detection_trigger_settings_v2(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> AnomalyTriggerResult</code></summary>

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
try:
    response = client.anomaly_triggers_v2.list_anomaly_detection_trigger_settings_v2(trigger_id)
    # TODO: Handle 'response' of type AnomalyTriggerResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers_v2.list_anomaly_detection_trigger_settings_v2(trigger_id)
    # TODO: Handle 'response' of type AnomalyTriggerResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AnomalyTriggerResult](verizon/models/anomaly_trigger_result.py)</code> -- Anomaly detection trigger details.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_anomaly_detection_trigger_v2(body: list[UpdateTriggerRequestOptions | UpdateTriggerRequestOptionsDict], *, request_options: RequestOptionsOrDict | None = None) -> IntelligenceSuccessResult</code></summary>

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
try:
    response = client.anomaly_triggers_v2.update_anomaly_detection_trigger_v2(body)
    # TODO: Handle 'response' of type IntelligenceSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.anomaly_triggers_v2.update_anomaly_detection_trigger_v2(body)
    # TODO: Handle 'response' of type IntelligenceSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[IntelligenceSuccessResult](verizon/models/intelligence_success_result.py)</code> -- Success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Billing

> Source: [Billing](verizon/apis/billing.py)

<details>
<summary><code>def add_account(body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ManagedAccountsAddResponse</code></summary>

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
try:
    response = client.billing.add_account(body)
    # TODO: Handle 'response' of type ManagedAccountsAddResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.add_account(body)
    # TODO: Handle 'response' of type ManagedAccountsAddResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddAccountErrorBody
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

**OnSuccess**: <code>[ManagedAccountsAddResponse](verizon/models/managed_accounts_add_response.py)</code> -- Add managed accounts response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AddAccountErrorBody](verizon/errors/add_account_error.py)&#93;</code>

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
<summary><code>def cancel_managed_account_action(body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ManagedAccountCancelResponse</code></summary>

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
try:
    response = client.billing.cancel_managed_account_action(body)
    # TODO: Handle 'response' of type ManagedAccountCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelManagedAccountActionErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.cancel_managed_account_action(body)
    # TODO: Handle 'response' of type ManagedAccountCancelResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelManagedAccountActionErrorBody
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

**OnSuccess**: <code>[ManagedAccountCancelResponse](verizon/models/managed_account_cancel_response.py)</code> -- Managed account cancel response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CancelManagedAccountActionErrorBody](verizon/errors/cancel_managed_account_action_error.py)&#93;</code>

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
<summary><code>def list_managed_account(account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None) -> ManagedAccountsGetAllResponse</code></summary>

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
try:
    response = client.billing.list_managed_account(account_name, service_name)
    # TODO: Handle 'response' of type ManagedAccountsGetAllResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListManagedAccountErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.list_managed_account(account_name, service_name)
    # TODO: Handle 'response' of type ManagedAccountsGetAllResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListManagedAccountErrorBody
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

**OnSuccess**: <code>[ManagedAccountsGetAllResponse](verizon/models/managed_accounts_get_all_response.py)</code> -- List of managed accounts

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListManagedAccountErrorBody](verizon/errors/list_managed_account_error.py)&#93;</code>

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
<summary><code>def managed_account_action(body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ManagedAccountsProvisionResponse</code></summary>

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
try:
    response = client.billing.managed_account_action(body)
    # TODO: Handle 'response' of type ManagedAccountsProvisionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ManagedAccountActionErrorBody
```

**Async**

```python
try:
    response = await async_client.billing.managed_account_action(body)
    # TODO: Handle 'response' of type ManagedAccountsProvisionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ManagedAccountActionErrorBody
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

**OnSuccess**: <code>[ManagedAccountsProvisionResponse](verizon/models/managed_accounts_provision_response.py)</code> -- Managed account provision response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ManagedAccountActionErrorBody](verizon/errors/managed_account_action_error.py)&#93;</code>

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
<summary><code>def cancel_campaign(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV2SuccessResult</code></summary>

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
try:
    response = client.campaigns_v2.cancel_campaign(account, campaign_id)
    # TODO: Handle 'response' of type FotaV2SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelCampaignErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.cancel_campaign(account, campaign_id)
    # TODO: Handle 'response' of type FotaV2SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelCampaignErrorBody
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

**OnSuccess**: <code>[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py)</code> -- Return cancellation status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CancelCampaignErrorBody](verizon/errors/cancel_campaign_error.py)&#93;</code>

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
<summary><code>def get_campaign_information(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CampaignSoftware</code></summary>

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
try:
    response = client.campaigns_v2.get_campaign_information(account, campaign_id)
    # TODO: Handle 'response' of type CampaignSoftware
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.get_campaign_information(account, campaign_id)
    # TODO: Handle 'response' of type CampaignSoftware
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignInformationErrorBody
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

**OnSuccess**: <code>[CampaignSoftware](verizon/models/campaign_software.py)</code> -- Return software upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCampaignInformationErrorBody](verizon/errors/get_campaign_information_error.py)&#93;</code>

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
<summary><code>def schedule_campaign_firmware_upgrade(account: str, *, request_options: RequestOptionsOrDict | None = None) -> CampaignSoftware</code></summary>

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
try:
    response = client.campaigns_v2.schedule_campaign_firmware_upgrade(account)
    # TODO: Handle 'response' of type CampaignSoftware
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleCampaignFirmwareUpgradeErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.schedule_campaign_firmware_upgrade(account)
    # TODO: Handle 'response' of type CampaignSoftware
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleCampaignFirmwareUpgradeErrorBody
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

**OnSuccess**: <code>[CampaignSoftware](verizon/models/campaign_software.py)</code> -- Return software upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ScheduleCampaignFirmwareUpgradeErrorBody](verizon/errors/schedule_campaign_firmware_upgrade_error.py)&#93;</code>

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
<summary><code>def schedule_file_upgrade(acc: str, body: UploadAndScheduleFileRequest | UploadAndScheduleFileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UploadAndScheduleFileResponse</code></summary>

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
try:
    response = client.campaigns_v2.schedule_file_upgrade(acc, body)
    # TODO: Handle 'response' of type UploadAndScheduleFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleFileUpgradeErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.schedule_file_upgrade(acc, body)
    # TODO: Handle 'response' of type UploadAndScheduleFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleFileUpgradeErrorBody
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

**OnSuccess**: <code>[UploadAndScheduleFileResponse](verizon/models/upload_and_schedule_file_response.py)</code> -- Successful responses.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ScheduleFileUpgradeErrorBody](verizon/errors/schedule_file_upgrade_error.py)&#93;</code>

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
<summary><code>def schedule_sw_upgrade_http_devices(acc: str, body: SchedulesSoftwareUpgradeRequest | SchedulesSoftwareUpgradeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UploadAndScheduleFileResponse</code></summary>

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
try:
    response = client.campaigns_v2.schedule_sw_upgrade_http_devices(acc, body)
    # TODO: Handle 'response' of type UploadAndScheduleFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleSwupgradeHttpDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.schedule_sw_upgrade_http_devices(acc, body)
    # TODO: Handle 'response' of type UploadAndScheduleFileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleSwupgradeHttpDevicesErrorBody
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

**OnSuccess**: <code>[UploadAndScheduleFileResponse](verizon/models/upload_and_schedule_file_response.py)</code> -- Successful responses.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ScheduleSwupgradeHttpDevicesErrorBody](verizon/errors/schedule_swupgrade_http_devices_error.py)&#93;</code>

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
<summary><code>def update_campaign_dates(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> CampaignSoftware</code></summary>

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
try:
    response = client.campaigns_v2.update_campaign_dates(account, campaign_id)
    # TODO: Handle 'response' of type CampaignSoftware
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignDatesErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.update_campaign_dates(account, campaign_id)
    # TODO: Handle 'response' of type CampaignSoftware
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignDatesErrorBody
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

**OnSuccess**: <code>[CampaignSoftware](verizon/models/campaign_software.py)</code> -- Updated campaign information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateCampaignDatesErrorBody](verizon/errors/update_campaign_dates_error.py)&#93;</code>

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
<summary><code>def update_campaign_firmware_devices(account: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> V2AddOrRemoveDeviceResult</code></summary>

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
try:
    response = client.campaigns_v2.update_campaign_firmware_devices(account, campaign_id)
    # TODO: Handle 'response' of type V2AddOrRemoveDeviceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignFirmwareDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v2.update_campaign_firmware_devices(account, campaign_id)
    # TODO: Handle 'response' of type V2AddOrRemoveDeviceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignFirmwareDevicesErrorBody
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

**OnSuccess**: <code>[V2AddOrRemoveDeviceResult](verizon/models/v2_add_or_remove_device_result.py)</code> -- Result of adding or removing devices to existing software upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateCampaignFirmwareDevicesErrorBody](verizon/errors/update_campaign_firmware_devices_error.py)&#93;</code>

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
<summary><code>def cancel_campaign2(account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV3SuccessResult</code></summary>

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
try:
    response = client.campaigns_v3.cancel_campaign2(account_name, campaign_id)
    # TODO: Handle 'response' of type FotaV3SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelCampaign2ErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v3.cancel_campaign2(account_name, campaign_id)
    # TODO: Handle 'response' of type FotaV3SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelCampaign2ErrorBody
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

**OnSuccess**: <code>[FotaV3SuccessResult](verizon/models/fota_v3_success_result.py)</code> -- Returns cancellation status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CancelCampaign2ErrorBody](verizon/errors/cancel_campaign2_error.py)&#93;</code>

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
<summary><code>def get_campaign_information2(account_name: str, campaign_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Campaign</code></summary>

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
try:
    response = client.campaigns_v3.get_campaign_information2(account_name, campaign_id)
    # TODO: Handle 'response' of type Campaign
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignInformation2ErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v3.get_campaign_information2(account_name, campaign_id)
    # TODO: Handle 'response' of type Campaign
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignInformation2ErrorBody
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

**OnSuccess**: <code>[Campaign](verizon/models/campaign.py)</code> -- Returns firmware upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCampaignInformation2ErrorBody](verizon/errors/get_campaign_information2_error.py)&#93;</code>

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
<summary><code>def schedule_campaign_firmware_upgrade2(account_name: str, body: CampaignFirmwareUpgrade | CampaignFirmwareUpgradeDict, *, request_options: RequestOptionsOrDict | None = None) -> FirmwareCampaign</code></summary>

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
try:
    response = client.campaigns_v3.schedule_campaign_firmware_upgrade2(account_name, body)
    # TODO: Handle 'response' of type FirmwareCampaign
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleCampaignFirmwareUpgrade2ErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v3.schedule_campaign_firmware_upgrade2(account_name, body)
    # TODO: Handle 'response' of type FirmwareCampaign
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleCampaignFirmwareUpgrade2ErrorBody
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

**OnSuccess**: <code>[FirmwareCampaign](verizon/models/firmware_campaign.py)</code> -- Return upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ScheduleCampaignFirmwareUpgrade2ErrorBody](verizon/errors/schedule_campaign_firmware_upgrade2_error.py)&#93;</code>

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
<summary><code>def update_campaign_dates2(acc: str, campaign_id: str, body: V3ChangeCampaignDatesRequest | V3ChangeCampaignDatesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FirmwareCampaign</code></summary>

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
try:
    response = client.campaigns_v3.update_campaign_dates2(acc, campaign_id, body)
    # TODO: Handle 'response' of type FirmwareCampaign
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignDates2ErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v3.update_campaign_dates2(acc, campaign_id, body)
    # TODO: Handle 'response' of type FirmwareCampaign
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignDates2ErrorBody
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

**OnSuccess**: <code>[FirmwareCampaign](verizon/models/firmware_campaign.py)</code> -- Updated campaign information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateCampaignDates2ErrorBody](verizon/errors/update_campaign_dates2_error.py)&#93;</code>

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
<summary><code>def update_campaign_firmware_devices2(acc: str, campaign_id: str, body: V3AddOrRemoveDeviceRequest | V3AddOrRemoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> V3AddOrRemoveDeviceResult</code></summary>

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
try:
    response = client.campaigns_v3.update_campaign_firmware_devices2(acc, campaign_id, body)
    # TODO: Handle 'response' of type V3AddOrRemoveDeviceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignFirmwareDevices2ErrorBody
```

**Async**

```python
try:
    response = await async_client.campaigns_v3.update_campaign_firmware_devices2(acc, campaign_id, body)
    # TODO: Handle 'response' of type V3AddOrRemoveDeviceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCampaignFirmwareDevices2ErrorBody
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

**OnSuccess**: <code>[V3AddOrRemoveDeviceResult](verizon/models/v3_add_or_remove_device_result.py)</code> -- Returns add or remove devices to existing upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateCampaignFirmwareDevices2ErrorBody](verizon/errors/update_campaign_firmware_devices2_error.py)&#93;</code>

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
<summary><code>def disable_device_logging(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.client_logging.disable_device_logging(account, device_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableDeviceLoggingErrorBody
```

**Async**

```python
try:
    await async_client.client_logging.disable_device_logging(account, device_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableDeviceLoggingErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DisableDeviceLoggingErrorBody](verizon/errors/disable_device_logging_error.py)&#93;</code>

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
<summary><code>def disable_logging_for_devices(account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.client_logging.disable_logging_for_devices(account, device_ids)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableLoggingForDevicesErrorBody
```

**Async**

```python
try:
    await async_client.client_logging.disable_logging_for_devices(account, device_ids)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableLoggingForDevicesErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DisableLoggingForDevicesErrorBody](verizon/errors/disable_logging_for_devices_error.py)&#93;</code>

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
<summary><code>def enable_device_logging(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceLoggingStatus</code></summary>

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
try:
    response = client.client_logging.enable_device_logging(account, device_id)
    # TODO: Handle 'response' of type DeviceLoggingStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableDeviceLoggingErrorBody
```

**Async**

```python
try:
    response = await async_client.client_logging.enable_device_logging(account, device_id)
    # TODO: Handle 'response' of type DeviceLoggingStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableDeviceLoggingErrorBody
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

**OnSuccess**: <code>[DeviceLoggingStatus](verizon/models/device_logging_status.py)</code> -- Device logging status information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[EnableDeviceLoggingErrorBody](verizon/errors/enable_device_logging_error.py)&#93;</code>

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
<summary><code>def enable_logging_for_devices(account: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceLoggingStatus]</code></summary>

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
try:
    response = client.client_logging.enable_logging_for_devices(account)
    # TODO: Handle 'response' of type list[DeviceLoggingStatus]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableLoggingForDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.client_logging.enable_logging_for_devices(account)
    # TODO: Handle 'response' of type list[DeviceLoggingStatus]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableLoggingForDevicesErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py)&#93;</code> -- List containing device logging status information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[EnableLoggingForDevicesErrorBody](verizon/errors/enable_logging_for_devices_error.py)&#93;</code>

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
<summary><code>def list_device_logs(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceLog]</code></summary>

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
try:
    response = client.client_logging.list_device_logs(account, device_id)
    # TODO: Handle 'response' of type list[DeviceLog]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDeviceLogsErrorBody
```

**Async**

```python
try:
    response = await async_client.client_logging.list_device_logs(account, device_id)
    # TODO: Handle 'response' of type list[DeviceLog]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDeviceLogsErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceLog](verizon/models/device_log.py)&#93;</code> -- List of device logs.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDeviceLogsErrorBody](verizon/errors/list_device_logs_error.py)&#93;</code>

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
<summary><code>def list_devices_with_logging_enabled(account: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceLoggingStatus]</code></summary>

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
try:
    response = client.client_logging.list_devices_with_logging_enabled(account)
    # TODO: Handle 'response' of type list[DeviceLoggingStatus]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesWithLoggingEnabledErrorBody
```

**Async**

```python
try:
    response = await async_client.client_logging.list_devices_with_logging_enabled(account)
    # TODO: Handle 'response' of type list[DeviceLoggingStatus]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesWithLoggingEnabledErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceLoggingStatus](verizon/models/device_logging_status.py)&#93;</code> -- List containing device logging status information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDevicesWithLoggingEnabledErrorBody](verizon/errors/list_devices_with_logging_enabled_error.py)&#93;</code>

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
<summary><code>def delete_device_from_account(body: RemoveDeviceRequest | RemoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.cloud_connector_devices.delete_device_from_account(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.cloud_connector_devices.delete_device_from_account(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def find_device_by_property_values(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FindDeviceByPropertyResponseList</code></summary>

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
try:
    response = client.cloud_connector_devices.find_device_by_property_values(body)
    # TODO: Handle 'response' of type FindDeviceByPropertyResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_devices.find_device_by_property_values(body)
    # TODO: Handle 'response' of type FindDeviceByPropertyResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[FindDeviceByPropertyResponseList](verizon/models/find_device_by_property_response_list.py)</code> -- A success response includes an array of all matching devices. Each device includes the full device resource definition.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_device_event_history(body: SearchDeviceEventHistoryRequest | SearchDeviceEventHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SearchDeviceEventHistoryResponseList</code></summary>

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
try:
    response = client.cloud_connector_devices.search_device_event_history(body)
    # TODO: Handle 'response' of type SearchDeviceEventHistoryResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_devices.search_device_event_history(body)
    # TODO: Handle 'response' of type SearchDeviceEventHistoryResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SearchDeviceEventHistoryResponseList](verizon/models/search_device_event_history_response_list.py)</code> -- A success response includes an array of all matching devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_devices_resources_by_property_values(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SearchDeviceByPropertyResponseList</code></summary>

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
try:
    response = client.cloud_connector_devices.search_devices_resources_by_property_values(body)
    # TODO: Handle 'response' of type SearchDeviceByPropertyResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_devices.search_devices_resources_by_property_values(body)
    # TODO: Handle 'response' of type SearchDeviceByPropertyResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SearchDeviceByPropertyResponseList](verizon/models/search_device_by_property_response_list.py)</code> -- A success response includes an array of all matching devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_sensor_readings(fieldname: str, body: SearchSensorHistoryRequest | SearchSensorHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SearchSensorHistoryResponseList</code></summary>

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
try:
    response = client.cloud_connector_devices.search_sensor_readings(fieldname, body)
    # TODO: Handle 'response' of type SearchSensorHistoryResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_devices.search_sensor_readings(fieldname, body)
    # TODO: Handle 'response' of type SearchSensorHistoryResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SearchSensorHistoryResponseList](verizon/models/search_sensor_history_response_list.py)</code> -- A success response includes an array of all matching devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_devices_configuration_value(body: ChangeConfigurationRequest | ChangeConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ChangeConfigurationResponse</code></summary>

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
try:
    response = client.cloud_connector_devices.update_devices_configuration_value(body)
    # TODO: Handle 'response' of type ChangeConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_devices.update_devices_configuration_value(body)
    # TODO: Handle 'response' of type ChangeConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ChangeConfigurationResponse](verizon/models/change_configuration_response.py)</code> -- A success response contains the ts.event.configuration event that was created to record the change.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CloudConnectorSubscriptions

> Source: [CloudConnectorSubscriptions](verizon/apis/cloud_connector_subscriptions.py)

<details>
<summary><code>def create_subscription(body: CreateSubscriptionRequest | CreateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Subscription</code></summary>

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
try:
    response = client.cloud_connector_subscriptions.create_subscription(body)
    # TODO: Handle 'response' of type Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_subscriptions.create_subscription(body)
    # TODO: Handle 'response' of type Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[Subscription](verizon/models/subscription.py)</code> -- Returns full subscription resource definition.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription(body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.cloud_connector_subscriptions.delete_subscription(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.cloud_connector_subscriptions.delete_subscription(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_subscription(body: QuerySubscriptionRequest | QuerySubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[Subscription]</code></summary>

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
try:
    response = client.cloud_connector_subscriptions.query_subscription(body)
    # TODO: Handle 'response' of type list[Subscription]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.cloud_connector_subscriptions.query_subscription(body)
    # TODO: Handle 'response' of type list[Subscription]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>list&#91;[Subscription](verizon/models/subscription.py)&#93;</code> -- Returns an array of all matching subscriptions. Each subscription includes the full subscription resource definition.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ConfigurationFiles

> Source: [ConfigurationFiles](verizon/apis/configuration_files.py)

<details>
<summary><code>def get_list_of_files(acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None) -> RetrievesAvailableFilesResponseList</code></summary>

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
try:
    response = client.configuration_files.get_list_of_files(acc, distribution_type)
    # TODO: Handle 'response' of type RetrievesAvailableFilesResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListOfFilesErrorBody
```

**Async**

```python
try:
    response = await async_client.configuration_files.get_list_of_files(acc, distribution_type)
    # TODO: Handle 'response' of type RetrievesAvailableFilesResponseList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetListOfFilesErrorBody
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

**OnSuccess**: <code>[RetrievesAvailableFilesResponseList](verizon/models/retrieves_available_files_response_list.py)</code> -- Successful responses.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetListOfFilesErrorBody](verizon/errors/get_list_of_files_error.py)&#93;</code>

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
<summary><code>def upload_config_file(acc: str, *, file_version: str | None = None, make: str | None = None, model: str | None = None, local_target_path: str | None = None, fileupload: bytes | None = None, request_options: RequestOptionsOrDict | None = None) -> UploadConfigurationFilesResponse</code></summary>

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
try:
    response = client.configuration_files.upload_config_file(acc)
    # TODO: Handle 'response' of type UploadConfigurationFilesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadConfigFileErrorBody
```

**Async**

```python
try:
    response = await async_client.configuration_files.upload_config_file(acc)
    # TODO: Handle 'response' of type UploadConfigurationFilesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadConfigFileErrorBody
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

**OnSuccess**: <code>[UploadConfigurationFilesResponse](verizon/models/upload_configuration_files_response.py)</code> -- Successful responses.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UploadConfigFileErrorBody](verizon/errors/upload_config_file_error.py)&#93;</code>

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
<summary><code>def deregister_callback(aname: str, sname: str, *, request_options: RequestOptionsOrDict | None = None) -> CallbackActionResult</code></summary>

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
try:
    response = client.connectivity_callbacks.deregister_callback(aname, sname)
    # TODO: Handle 'response' of type CallbackActionResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallbackErrorBody
```

**Async**

```python
try:
    response = await async_client.connectivity_callbacks.deregister_callback(aname, sname)
    # TODO: Handle 'response' of type CallbackActionResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallbackErrorBody
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

**OnSuccess**: <code>[CallbackActionResult](verizon/models/callback_action_result.py)</code> -- Response for a request to deregister a callback.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeregisterCallbackErrorBody](verizon/errors/deregister_callback_error.py)&#93;</code>

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
<summary><code>def list_registered_callbacks(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> list[ConnectivityManagementCallback]</code></summary>

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
try:
    response = client.connectivity_callbacks.list_registered_callbacks(aname)
    # TODO: Handle 'response' of type list[ConnectivityManagementCallback]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacksErrorBody
```

**Async**

```python
try:
    response = await async_client.connectivity_callbacks.list_registered_callbacks(aname)
    # TODO: Handle 'response' of type list[ConnectivityManagementCallback]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacksErrorBody
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

**OnSuccess**: <code>list&#91;[ConnectivityManagementCallback](verizon/models/connectivity_management_callback.py)&#93;</code> -- A list of callback listeners.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListRegisteredCallbacksErrorBody](verizon/errors/list_registered_callbacks_error.py)&#93;</code>

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
<summary><code>def register_callback(aname: str, body: RegisterCallbackRequest | RegisterCallbackRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CallbackActionResult</code></summary>

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
try:
    response = client.connectivity_callbacks.register_callback(aname, body)
    # TODO: Handle 'response' of type CallbackActionResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallbackErrorBody
```

**Async**

```python
try:
    response = await async_client.connectivity_callbacks.register_callback(aname, body)
    # TODO: Handle 'response' of type CallbackActionResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallbackErrorBody
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

**OnSuccess**: <code>[CallbackActionResult](verizon/models/callback_action_result.py)</code> -- A success response for registering a callback.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterCallbackErrorBody](verizon/errors/register_callback_error.py)&#93;</code>

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
<summary><code>def create_trigger_rules(body: V2TriggersRequest | V2TriggersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> TriggerResponse</code></summary>

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
try:
    response = client.create_price_plan_triggers.create_trigger_rules(body)
    # TODO: Handle 'response' of type TriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.create_price_plan_triggers.create_trigger_rules(body)
    # TODO: Handle 'response' of type TriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TriggerResponse](verizon/models/trigger_response.py)</code> -- Successful request

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceActions

> Source: [DeviceActions](verizon/apis/device_actions.py)

<details>
<summary><code>def account_information(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> AccountDetails</code></summary>

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
try:
    response = client.device_actions.account_information(account_name)
    # TODO: Handle 'response' of type AccountDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.account_information(account_name)
    # TODO: Handle 'response' of type AccountDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AccountDetails](verizon/models/account_details.py)</code> -- Account details **Note:** The response will have placeholders. You can identify the placeholders by `"sizeKb":0` and that the record will only have `name` and `sizeKb` values.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def aggregate_usage(body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.device_actions.aggregate_usage(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.aggregate_usage(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def daily_usage(body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> DailyUsageResponse</code></summary>

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
try:
    response = client.device_actions.daily_usage(body)
    # TODO: Handle 'response' of type DailyUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.daily_usage(body)
    # TODO: Handle 'response' of type DailyUsageResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DailyUsageResponse](verizon/models/daily_usage_response.py)</code> -- Syncronous response of device usage

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_asynchronous_request_status(account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> StatusResponse</code></summary>

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
try:
    response = client.device_actions.get_asynchronous_request_status(account_name, request_id)
    # TODO: Handle 'response' of type StatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.get_asynchronous_request_status(account_name, request_id)
    # TODO: Handle 'response' of type StatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[StatusResponse](verizon/models/status_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_device_provisioning_history(body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.device_actions.retrieve_device_provisioning_history(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.retrieve_device_provisioning_history(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_the_global_device_list(body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.device_actions.retrieve_the_global_device_list(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.retrieve_the_global_device_list(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def service_plan_list(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> AccountDetails</code></summary>

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
try:
    response = client.device_actions.service_plan_list(account_name)
    # TODO: Handle 'response' of type AccountDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_actions.service_plan_list(account_name)
    # TODO: Handle 'response' of type AccountDetails
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AccountDetails](verizon/models/account_details.py)</code> -- Account details **Note:** The response will have placeholders. You can identify the placeholders by `"sizeKb":0` and that the record will only have `name` and `sizeKb` values.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceCredentialManagement

> Source: [DeviceCredentialManagement](verizon/apis/device_credential_management.py)

<details>
<summary><code>def drop_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DropResponse</code></summary>

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
try:
    response = client.device_credential_management.drop_credentials(body)
    # TODO: Handle 'response' of type DropResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DropCredentialsErrorBody
```

**Async**

```python
try:
    response = await async_client.device_credential_management.drop_credentials(body)
    # TODO: Handle 'response' of type DropResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DropCredentialsErrorBody
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

**OnSuccess**: <code>[DropResponse](verizon/models/drop_response.py)</code> -- Credentials dropped successfully

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DropCredentialsErrorBody](verizon/errors/drop_credentials_error.py)&#93;</code>

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
<summary><code>def generate_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenerateResponse</code></summary>

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
try:
    response = client.device_credential_management.generate_credentials(body)
    # TODO: Handle 'response' of type GenerateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateCredentialsErrorBody
```

**Async**

```python
try:
    response = await async_client.device_credential_management.generate_credentials(body)
    # TODO: Handle 'response' of type GenerateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GenerateCredentialsErrorBody
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

**OnSuccess**: <code>[GenerateResponse](verizon/models/generate_response.py)</code> -- Credentials generated successfully

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GenerateCredentialsErrorBody](verizon/errors/generate_credentials_error.py)&#93;</code>

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
<summary><code>def reset_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenerateResponse</code></summary>

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
try:
    response = client.device_credential_management.reset_credentials(body)
    # TODO: Handle 'response' of type GenerateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResetCredentialsErrorBody
```

**Async**

```python
try:
    response = await async_client.device_credential_management.reset_credentials(body)
    # TODO: Handle 'response' of type GenerateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResetCredentialsErrorBody
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

**OnSuccess**: <code>[GenerateResponse](verizon/models/generate_response.py)</code> -- Credentials reset successfully

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ResetCredentialsErrorBody](verizon/errors/reset_credentials_error.py)&#93;</code>

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
<summary><code>def retrieve_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RetrieveResponse</code></summary>

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
try:
    response = client.device_credential_management.retrieve_credentials(body)
    # TODO: Handle 'response' of type RetrieveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveCredentialsErrorBody
```

**Async**

```python
try:
    response = await async_client.device_credential_management.retrieve_credentials(body)
    # TODO: Handle 'response' of type RetrieveResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveCredentialsErrorBody
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

**OnSuccess**: <code>[RetrieveResponse](verizon/models/retrieve_response.py)</code> -- Successful retrieval

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RetrieveCredentialsErrorBody](verizon/errors/retrieve_credentials_error.py)&#93;</code>

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
<summary><code>def device_reachability_status_using_post(body: NotificationReportStatusRequest | NotificationReportStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_diagnostics.device_reachability_status_using_post(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceReachabilityStatusUsingPostErrorBody
```

**Async**

```python
try:
    response = await async_client.device_diagnostics.device_reachability_status_using_post(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceReachabilityStatusUsingPostErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeviceReachabilityStatusUsingPostErrorBody](verizon/errors/device_reachability_status_using_post_error.py)&#93;</code>

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
<summary><code>def retrieve_active_monitors_using_post(body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_diagnostics.retrieve_active_monitors_using_post(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveActiveMonitorsUsingPostErrorBody
```

**Async**

```python
try:
    response = await async_client.device_diagnostics.retrieve_active_monitors_using_post(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveActiveMonitorsUsingPostErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RetrieveActiveMonitorsUsingPostErrorBody](verizon/errors/retrieve_active_monitors_using_post_error.py)&#93;</code>

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
<summary><code>def create_device_group(body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ConnectivityManagementSuccessResult</code></summary>

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
try:
    response = client.device_groups.create_device_group(body)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateDeviceGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.device_groups.create_device_group(body)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateDeviceGroupErrorBody
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

**OnSuccess**: <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response, Creates a new device group.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateDeviceGroupErrorBody](verizon/errors/create_device_group_error.py)&#93;</code>

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
<summary><code>def delete_device_group(aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None) -> ConnectivityManagementSuccessResult</code></summary>

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
try:
    response = client.device_groups.delete_device_group(aname, gname)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteDeviceGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.device_groups.delete_device_group(aname, gname)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteDeviceGroupErrorBody
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

**OnSuccess**: <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteDeviceGroupErrorBody](verizon/errors/delete_device_group_error.py)&#93;</code>

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
<summary><code>def get_device_group_information(aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None) -> DeviceGroupDevicesData</code></summary>

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
try:
    response = client.device_groups.get_device_group_information(aname, gname)
    # TODO: Handle 'response' of type DeviceGroupDevicesData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceGroupInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.device_groups.get_device_group_information(aname, gname)
    # TODO: Handle 'response' of type DeviceGroupDevicesData
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceGroupInformationErrorBody
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

**OnSuccess**: <code>[DeviceGroupDevicesData](verizon/models/device_group_devices_data.py)</code> -- Successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceGroupInformationErrorBody](verizon/errors/get_device_group_information_error.py)&#93;</code>

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
<summary><code>def list_device_groups(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceGroup]</code></summary>

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
try:
    response = client.device_groups.list_device_groups(aname)
    # TODO: Handle 'response' of type list[DeviceGroup]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDeviceGroupsErrorBody
```

**Async**

```python
try:
    response = await async_client.device_groups.list_device_groups(aname)
    # TODO: Handle 'response' of type list[DeviceGroup]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDeviceGroupsErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceGroup](verizon/models/device_group.py)&#93;</code> -- The list of device groups in the account.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDeviceGroupsErrorBody](verizon/errors/list_device_groups_error.py)&#93;</code>

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
<summary><code>def update_device_group(aname: str, gname: str, body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ConnectivityManagementSuccessResult</code></summary>

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
try:
    response = client.device_groups.update_device_group(aname, gname, body)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDeviceGroupErrorBody
```

**Async**

```python
try:
    response = await async_client.device_groups.update_device_group(aname, gname, body)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDeviceGroupErrorBody
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

**OnSuccess**: <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDeviceGroupErrorBody](verizon/errors/update_device_group_error.py)&#93;</code>

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
<summary><code>def cancel_async_report(txid: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> TransactionId</code></summary>

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
try:
    response = client.device_location_callbacks.cancel_async_report(txid, account_name)
    # TODO: Handle 'response' of type TransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_location_callbacks.cancel_async_report(txid, account_name)
    # TODO: Handle 'response' of type TransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionId](verizon/models/transaction_id.py)</code> -- Request canceled.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deregister_callback2(account_name: str, service: CallbackServiceNameOrStr, *, request_options: RequestOptionsOrDict | None = None) -> DeviceLocationSuccessResult</code></summary>

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
try:
    response = client.device_location_callbacks.deregister_callback2(account_name, service)
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback2ErrorBody
```

**Async**

```python
try:
    response = await async_client.device_location_callbacks.deregister_callback2(account_name, service)
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback2ErrorBody
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

**OnSuccess**: <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Deregistration successful.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeregisterCallback2ErrorBody](verizon/errors/deregister_callback2_error.py)&#93;</code>

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
<summary><code>def list_registered_callbacks2(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceLocationCallback]</code></summary>

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
try:
    response = client.device_location_callbacks.list_registered_callbacks2(account_name)
    # TODO: Handle 'response' of type list[DeviceLocationCallback]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks2ErrorBody
```

**Async**

```python
try:
    response = await async_client.device_location_callbacks.list_registered_callbacks2(account_name)
    # TODO: Handle 'response' of type list[DeviceLocationCallback]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks2ErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceLocationCallback](verizon/models/device_location_callback.py)&#93;</code> -- List of all registered callback URLs.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListRegisteredCallbacks2ErrorBody](verizon/errors/list_registered_callbacks2_error.py)&#93;</code>

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
<summary><code>def register_callback2(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> CallbackRegistrationResult</code></summary>

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
try:
    response = client.device_location_callbacks.register_callback2(account_name)
    # TODO: Handle 'response' of type CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback2ErrorBody
```

**Async**

```python
try:
    response = await async_client.device_location_callbacks.register_callback2(account_name)
    # TODO: Handle 'response' of type CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback2ErrorBody
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

**OnSuccess**: <code>[CallbackRegistrationResult](verizon/models/callback_registration_result.py)</code> -- Callback registration response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterCallback2ErrorBody](verizon/errors/register_callback2_error.py)&#93;</code>

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
<summary><code>def activate_service_for_devices(body: CarrierActivateRequest | CarrierActivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.activate_service_for_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateServiceForDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.activate_service_for_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateServiceForDevicesErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ActivateServiceForDevicesErrorBody](verizon/errors/activate_service_for_devices_error.py)&#93;</code>

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
<summary><code>def add_devices(body: AddDevicesRequest | AddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[AddDevicesResult]</code></summary>

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
try:
    response = client.device_management.add_devices(body)
    # TODO: Handle 'response' of type list[AddDevicesResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.add_devices(body)
    # TODO: Handle 'response' of type list[AddDevicesResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddDevicesErrorBody
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

**OnSuccess**: <code>list&#91;[AddDevicesResult](verizon/models/add_devices_result.py)&#93;</code> -- For each device in the request, contains device identifiers and a success or failure response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AddDevicesErrorBody](verizon/errors/add_devices_error.py)&#93;</code>

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
<summary><code>def billed_usage_info(body: BilledusageListRequest | BilledusageListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.billed_usage_info(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BilledUsageInfoErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.billed_usage_info(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type BilledUsageInfoErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[BilledUsageInfoErrorBody](verizon/errors/billed_usage_info_error.py)&#93;</code>

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
<summary><code>def change_devices_service_plan(body: ServicePlanUpdateRequest | ServicePlanUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.change_devices_service_plan(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeDevicesServicePlanErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.change_devices_service_plan(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ChangeDevicesServicePlanErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ChangeDevicesServicePlanErrorBody](verizon/errors/change_devices_service_plan_error.py)&#93;</code>

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
<summary><code>def check_devices_availability_for_activation(body: DeviceActivationRequest | DeviceActivationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.check_devices_availability_for_activation(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDevicesAvailabilityForActivationErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.check_devices_availability_for_activation(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CheckDevicesAvailabilityForActivationErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CheckDevicesAvailabilityForActivationErrorBody](verizon/errors/check_devices_availability_for_activation_error.py)&#93;</code>

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
<summary><code>def deactivate_service_for_devices(body: CarrierDeactivateRequest | CarrierDeactivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.deactivate_service_for_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeactivateServiceForDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.deactivate_service_for_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeactivateServiceForDevicesErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeactivateServiceForDevicesErrorBody](verizon/errors/deactivate_service_for_devices_error.py)&#93;</code>

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
<summary><code>def delete_deactivated_devices(body: DeleteDevicesRequest | DeleteDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DeleteDevicesResult]</code></summary>

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
try:
    response = client.device_management.delete_deactivated_devices(body)
    # TODO: Handle 'response' of type list[DeleteDevicesResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteDeactivatedDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.delete_deactivated_devices(body)
    # TODO: Handle 'response' of type list[DeleteDevicesResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteDeactivatedDevicesErrorBody
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

**OnSuccess**: <code>list&#91;[DeleteDevicesResult](verizon/models/delete_devices_result.py)&#93;</code> -- For each device in the request, contains device identifiers and a success or failure response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteDeactivatedDevicesErrorBody](verizon/errors/delete_deactivated_devices_error.py)&#93;</code>

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
<summary><code>def device_upload(body: DeviceUploadRequest | DeviceUploadRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_management.device_upload(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceUploadErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.device_upload(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceUploadErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeviceUploadErrorBody](verizon/errors/device_upload_error.py)&#93;</code>

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
<summary><code>def device_upload_status(body: CheckOrderStatusRequest | CheckOrderStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.device_upload_status(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceUploadStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.device_upload_status(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceUploadStatusErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeviceUploadStatusErrorBody](verizon/errors/device_upload_status_error.py)&#93;</code>

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
<summary><code>def get_device_extended_diagnostic_information(body: DeviceExtendedDiagnosticsRequest | DeviceExtendedDiagnosticsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceExtendedDiagnosticsResult</code></summary>

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
try:
    response = client.device_management.get_device_extended_diagnostic_information(body)
    # TODO: Handle 'response' of type DeviceExtendedDiagnosticsResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceExtendedDiagnosticInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.get_device_extended_diagnostic_information(body)
    # TODO: Handle 'response' of type DeviceExtendedDiagnosticsResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceExtendedDiagnosticInformationErrorBody
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

**OnSuccess**: <code>[DeviceExtendedDiagnosticsResult](verizon/models/device_extended_diagnostics_result.py)</code> -- Device diagnostic information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceExtendedDiagnosticInformationErrorBody](verizon/errors/get_device_extended_diagnostic_information_error.py)&#93;</code>

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
<summary><code>def get_device_service_suspension_status(body: DeviceSuspensionStatusRequest | DeviceSuspensionStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.get_device_service_suspension_status(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceServiceSuspensionStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.get_device_service_suspension_status(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceServiceSuspensionStatusErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceServiceSuspensionStatusErrorBody](verizon/errors/get_device_service_suspension_status_error.py)&#93;</code>

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
<summary><code>def list_current_devices_prl_version(body: DevicePrlListRequest | DevicePrlListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.list_current_devices_prl_version(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListCurrentDevicesPrlversionErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.list_current_devices_prl_version(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListCurrentDevicesPrlversionErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListCurrentDevicesPrlversionErrorBody](verizon/errors/list_current_devices_prlversion_error.py)&#93;</code>

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
<summary><code>def list_devices_information(body: AccountDeviceListRequest | AccountDeviceListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AccountDeviceListResult</code></summary>

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
try:
    response = client.device_management.list_devices_information(body)
    # TODO: Handle 'response' of type AccountDeviceListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.list_devices_information(body)
    # TODO: Handle 'response' of type AccountDeviceListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesInformationErrorBody
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

**OnSuccess**: <code>[AccountDeviceListResult](verizon/models/account_device_list_result.py)</code> -- List of devices that match the request parameters, ordered by device creation date, oldest first.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDevicesInformationErrorBody](verizon/errors/list_devices_information_error.py)&#93;</code>

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
<summary><code>def list_devices_provisioning_history(body: DeviceProvisioningHistoryListRequest | DeviceProvisioningHistoryListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceProvisioningHistoryListResult]</code></summary>

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
try:
    response = client.device_management.list_devices_provisioning_history(body)
    # TODO: Handle 'response' of type list[DeviceProvisioningHistoryListResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesProvisioningHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.list_devices_provisioning_history(body)
    # TODO: Handle 'response' of type list[DeviceProvisioningHistoryListResult]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesProvisioningHistoryErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceProvisioningHistoryListResult](verizon/models/device_provisioning_history_list_result.py)&#93;</code> -- List of Device Provision History events, sorted by the timestamp, oldest first.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDevicesProvisioningHistoryErrorBody](verizon/errors/list_devices_provisioning_history_error.py)&#93;</code>

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
<summary><code>def list_devices_usage_history(body: DeviceUsageListRequest | DeviceUsageListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceUsageListResult</code></summary>

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
try:
    response = client.device_management.list_devices_usage_history(body)
    # TODO: Handle 'response' of type DeviceUsageListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesUsageHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.list_devices_usage_history(body)
    # TODO: Handle 'response' of type DeviceUsageListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesUsageHistoryErrorBody
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

**OnSuccess**: <code>[DeviceUsageListResult](verizon/models/device_usage_list_result.py)</code> -- List of device usage events, sorted by the timestamp, oldest first.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDevicesUsageHistoryErrorBody](verizon/errors/list_devices_usage_history_error.py)&#93;</code>

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
<summary><code>def list_devices_with_imei_iccid_mismatch(body: DeviceMismatchListRequest | DeviceMismatchListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceMismatchListResult</code></summary>

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
try:
    response = client.device_management.list_devices_with_imei_iccid_mismatch(body)
    # TODO: Handle 'response' of type DeviceMismatchListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesWithImeiIccidMismatchErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.list_devices_with_imei_iccid_mismatch(body)
    # TODO: Handle 'response' of type DeviceMismatchListResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesWithImeiIccidMismatchErrorBody
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

**OnSuccess**: <code>[DeviceMismatchListResult](verizon/models/device_mismatch_list_result.py)</code> -- List of devices that have mismatched IMEIs and ICCIDs.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDevicesWithImeiIccidMismatchErrorBody](verizon/errors/list_devices_with_imei_iccid_mismatch_error.py)&#93;</code>

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
<summary><code>def move_devices_within_accounts_of_profile(body: MoveDeviceRequest | MoveDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.move_devices_within_accounts_of_profile(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MoveDevicesWithinAccountsOfProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.move_devices_within_accounts_of_profile(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type MoveDevicesWithinAccountsOfProfileErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[MoveDevicesWithinAccountsOfProfileErrorBody](verizon/errors/move_devices_within_accounts_of_profile_error.py)&#93;</code>

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
<summary><code>def restore_service_for_suspended_devices(body: CarrierActionsRequest | CarrierActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.restore_service_for_suspended_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreServiceForSuspendedDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.restore_service_for_suspended_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RestoreServiceForSuspendedDevicesErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RestoreServiceForSuspendedDevicesErrorBody](verizon/errors/restore_service_for_suspended_devices_error.py)&#93;</code>

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
<summary><code>def retrieve_aggregate_device_usage_history(body: DeviceAggregateUsageListRequest | DeviceAggregateUsageListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.retrieve_aggregate_device_usage_history(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveAggregateDeviceUsageHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.retrieve_aggregate_device_usage_history(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveAggregateDeviceUsageHistoryErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- A unique string that associates the request with the results that are sent via a callback service.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RetrieveAggregateDeviceUsageHistoryErrorBody](verizon/errors/retrieve_aggregate_device_usage_history_error.py)&#93;</code>

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
<summary><code>def retrieve_device_connection_history(body: DeviceConnectionListRequest | DeviceConnectionListRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ConnectionHistoryResult</code></summary>

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
try:
    response = client.device_management.retrieve_device_connection_history(body)
    # TODO: Handle 'response' of type ConnectionHistoryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveDeviceConnectionHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.retrieve_device_connection_history(body)
    # TODO: Handle 'response' of type ConnectionHistoryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveDeviceConnectionHistoryErrorBody
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

**OnSuccess**: <code>[ConnectionHistoryResult](verizon/models/connection_history_result.py)</code> -- List of device connection events, sorted by the occurredAt timestamp, oldest first.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RetrieveDeviceConnectionHistoryErrorBody](verizon/errors/retrieve_device_connection_history_error.py)&#93;</code>

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
<summary><code>def suspend_service_for_devices(body: CarrierActionsRequest | CarrierActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.suspend_service_for_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SuspendServiceForDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.suspend_service_for_devices(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SuspendServiceForDevicesErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SuspendServiceForDevicesErrorBody](verizon/errors/suspend_service_for_devices_error.py)&#93;</code>

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
<summary><code>def update_device_id(service_type: str, body: ChangeDeviceIdRequest | ChangeDeviceIdRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.update_device_id(service_type, body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDeviceIdErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.update_device_id(service_type, body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDeviceIdErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- A unique string that associates the request with the results that are sent via a callback service.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDeviceIdErrorBody](verizon/errors/update_device_id_error.py)&#93;</code>

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
<summary><code>def update_devices_contact_information(body: ContactInfoUpdateRequest | ContactInfoUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.update_devices_contact_information(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesContactInformationErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.update_devices_contact_information(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesContactInformationErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID returned in a success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDevicesContactInformationErrorBody](verizon/errors/update_devices_contact_information_error.py)&#93;</code>

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
<summary><code>def update_devices_cost_center_code(body: DeviceCostCenterRequest | DeviceCostCenterRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.update_devices_cost_center_code(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesCostCenterCodeErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.update_devices_cost_center_code(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesCostCenterCodeErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDevicesCostCenterCodeErrorBody](verizon/errors/update_devices_cost_center_code_error.py)&#93;</code>

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
<summary><code>def update_devices_custom_fields(body: CustomFieldsUpdateRequest | CustomFieldsUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.update_devices_custom_fields(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesCustomFieldsErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.update_devices_custom_fields(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesCustomFieldsErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDevicesCustomFieldsErrorBody](verizon/errors/update_devices_custom_fields_error.py)&#93;</code>

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
<summary><code>def update_devices_state(body: GoToStateRequest | GoToStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.update_devices_state(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesStateErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.update_devices_state(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDevicesStateErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDevicesStateErrorBody](verizon/errors/update_devices_state_error.py)&#93;</code>

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
<summary><code>def upload_activate_device(body: UploadsActivatesDeviceRequest | UploadsActivatesDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.upload_activate_device(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadActivateDeviceErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.upload_activate_device(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UploadActivateDeviceErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UploadActivateDeviceErrorBody](verizon/errors/upload_activate_device_error.py)&#93;</code>

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
<summary><code>def usage_segmentation_label_association(body: AssociateLabelRequest | AssociateLabelRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.usage_segmentation_label_association(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UsageSegmentationLabelAssociationErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.usage_segmentation_label_association(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UsageSegmentationLabelAssociationErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UsageSegmentationLabelAssociationErrorBody](verizon/errors/usage_segmentation_label_association_error.py)&#93;</code>

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
<summary><code>def usage_segmentation_label_deletion(account_name: str, label_list: LabelsList | LabelsListDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.device_management.usage_segmentation_label_deletion(account_name, label_list)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UsageSegmentationLabelDeletionErrorBody
```

**Async**

```python
try:
    response = await async_client.device_management.usage_segmentation_label_deletion(account_name, label_list)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UsageSegmentationLabelDeletionErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UsageSegmentationLabelDeletionErrorBody](verizon/errors/usage_segmentation_label_deletion_error.py)&#93;</code>

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
<summary><code>def device_reachability(body: NotificationReportRequest | NotificationReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_monitoring.device_reachability(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceReachabilityErrorBody
```

**Async**

```python
try:
    response = await async_client.device_monitoring.device_reachability(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceReachabilityErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeviceReachabilityErrorBody](verizon/errors/device_reachability_error.py)&#93;</code>

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
<summary><code>def stop_device_reachability(stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_monitoring.stop_device_reachability(stopreachabilitypayload)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StopDeviceReachabilityErrorBody
```

**Async**

```python
try:
    response = await async_client.device_monitoring.stop_device_reachability(stopreachabilitypayload)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StopDeviceReachabilityErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[StopDeviceReachabilityErrorBody](verizon/errors/stop_device_reachability_error.py)&#93;</code>

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
<summary><code>def activate_device_through_profile(body: ActivateDeviceProfileRequest | ActivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_profile_management.activate_device_through_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateDeviceThroughProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.device_profile_management.activate_device_through_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ActivateDeviceThroughProfileErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ActivateDeviceThroughProfileErrorBody](verizon/errors/activate_device_through_profile_error.py)&#93;</code>

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
<summary><code>def profile_to_activate_device(body: ProfileRequest | ProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_profile_management.profile_to_activate_device(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ProfileToActivateDeviceErrorBody
```

**Async**

```python
try:
    response = await async_client.device_profile_management.profile_to_activate_device(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ProfileToActivateDeviceErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ProfileToActivateDeviceErrorBody](verizon/errors/profile_to_activate_device_error.py)&#93;</code>

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
<summary><code>def profile_to_deactivate_device(body: DeactivateDeviceProfileRequest | DeactivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_profile_management.profile_to_deactivate_device(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ProfileToDeactivateDeviceErrorBody
```

**Async**

```python
try:
    response = await async_client.device_profile_management.profile_to_deactivate_device(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ProfileToDeactivateDeviceErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ProfileToDeactivateDeviceErrorBody](verizon/errors/profile_to_deactivate_device_error.py)&#93;</code>

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
<summary><code>def profile_to_set_fallback_attribute(body: SetFallbackAttributeRequest | SetFallbackAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.device_profile_management.profile_to_set_fallback_attribute(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ProfileToSetFallbackAttributeErrorBody
```

**Async**

```python
try:
    response = await async_client.device_profile_management.profile_to_set_fallback_attribute(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ProfileToSetFallbackAttributeErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ProfileToSetFallbackAttributeErrorBody](verizon/errors/profile_to_set_fallback_attribute_error.py)&#93;</code>

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
<summary><code>def calculate_aggregated_report_asynchronous(body: AggregateSessionReportRequest | AggregateSessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AggregatedReportCallbackResult</code></summary>

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
try:
    response = client.device_reports.calculate_aggregated_report_asynchronous(body)
    # TODO: Handle 'response' of type AggregatedReportCallbackResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CalculateAggregatedReportAsynchronousErrorBody
```

**Async**

```python
try:
    response = await async_client.device_reports.calculate_aggregated_report_asynchronous(body)
    # TODO: Handle 'response' of type AggregatedReportCallbackResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CalculateAggregatedReportAsynchronousErrorBody
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

**OnSuccess**: <code>[AggregatedReportCallbackResult](verizon/models/aggregated_report_callback_result.py)</code> -- A successful response shows the request is queued with a unique `txid` to identify the report data with.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CalculateAggregatedReportAsynchronousErrorBody](verizon/errors/calculate_aggregated_report_asynchronous_error.py)&#93;</code>

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
<summary><code>def calculate_aggregated_report_synchronous(body: AggregateSessionReportRequest | AggregateSessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> AggregateSessionReport</code></summary>

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
try:
    response = client.device_reports.calculate_aggregated_report_synchronous(body)
    # TODO: Handle 'response' of type AggregateSessionReport
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CalculateAggregatedReportSynchronousErrorBody
```

**Async**

```python
try:
    response = await async_client.device_reports.calculate_aggregated_report_synchronous(body)
    # TODO: Handle 'response' of type AggregateSessionReport
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CalculateAggregatedReportSynchronousErrorBody
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

**OnSuccess**: <code>[AggregateSessionReport](verizon/models/aggregate_session_report.py)</code> -- A successful response shows session and usage details for up to 10 devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CalculateAggregatedReportSynchronousErrorBody](verizon/errors/calculate_aggregated_report_synchronous_error.py)&#93;</code>

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
<summary><code>def get_sessions_report(body: SessionReportRequest | SessionReportRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SessionReport</code></summary>

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
try:
    response = client.device_reports.get_sessions_report(body)
    # TODO: Handle 'response' of type SessionReport
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSessionsReportErrorBody
```

**Async**

```python
try:
    response = await async_client.device_reports.get_sessions_report(body)
    # TODO: Handle 'response' of type SessionReport
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetSessionsReportErrorBody
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

**OnSuccess**: <code>[SessionReport](verizon/models/session_report.py)</code> -- A successful response includes the session information for an individual device.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetSessionsReportErrorBody](verizon/errors/get_sessions_report_error.py)&#93;</code>

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
<summary><code>def get_sms_messages(account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SmsMessagesResponse</code></summary>

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
try:
    response = client.device_sms_messaging.get_sms_messages(account_name)
    # TODO: Handle 'response' of type SmsMessagesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_sms_messaging.get_sms_messages(account_name)
    # TODO: Handle 'response' of type SmsMessagesResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SmsMessagesResponse](verizon/models/sms_messages_response.py)</code> -- Successful response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_sms_message_history(body: SmseventHistoryRequest | SmseventHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.device_sms_messaging.list_sms_message_history(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_sms_messaging.list_sms_message_history(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def send_an_sms_message(body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.device_sms_messaging.send_an_sms_message(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_sms_messaging.send_an_sms_message(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_sms_message_delivery(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> SuccessResponse</code></summary>

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
try:
    response = client.device_sms_messaging.start_sms_message_delivery(account_name)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.device_sms_messaging.start_sms_message_delivery(account_name)
    # TODO: Handle 'response' of type SuccessResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SuccessResponse](verizon/models/success_response.py)</code> -- Request Success Message

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceServiceManagement

> Source: [DeviceServiceManagement](verizon/apis/device_service_management.py)

<details>
<summary><code>def get_device_hyper_precise_status(imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None) -> BullseyeServiceResult</code></summary>

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
try:
    response = client.device_service_management.get_device_hyper_precise_status(imei, account_number)
    # TODO: Handle 'response' of type BullseyeServiceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceHyperPreciseStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.device_service_management.get_device_hyper_precise_status(imei, account_number)
    # TODO: Handle 'response' of type BullseyeServiceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceHyperPreciseStatusErrorBody
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

**OnSuccess**: <code>[BullseyeServiceResult](verizon/models/bullseye_service_result.py)</code> -- Returns the status of Hyper Precise Location on the device.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceHyperPreciseStatusErrorBody](verizon/errors/get_device_hyper_precise_status_error.py)&#93;</code>

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
<summary><code>def update_device_hyper_precise_status(body: BullseyeServiceRequest | BullseyeServiceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> BullseyeServiceResult</code></summary>

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
try:
    response = client.device_service_management.update_device_hyper_precise_status(body)
    # TODO: Handle 'response' of type BullseyeServiceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDeviceHyperPreciseStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.device_service_management.update_device_hyper_precise_status(body)
    # TODO: Handle 'response' of type BullseyeServiceResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateDeviceHyperPreciseStatusErrorBody
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

**OnSuccess**: <code>[BullseyeServiceResult](verizon/models/bullseye_service_result.py)</code> -- Successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateDeviceHyperPreciseStatusErrorBody](verizon/errors/update_device_hyper_precise_status_error.py)&#93;</code>

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
<summary><code>def get_location_service_subscription_status(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceLocationSubscription</code></summary>

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
try:
    response = client.devices_location_subscriptions.get_location_service_subscription_status(account_name)
    # TODO: Handle 'response' of type DeviceLocationSubscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLocationServiceSubscriptionStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.devices_location_subscriptions.get_location_service_subscription_status(account_name)
    # TODO: Handle 'response' of type DeviceLocationSubscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLocationServiceSubscriptionStatusErrorBody
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

**OnSuccess**: <code>[DeviceLocationSubscription](verizon/models/device_location_subscription.py)</code> -- Device location subscription information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetLocationServiceSubscriptionStatusErrorBody](verizon/errors/get_location_service_subscription_status_error.py)&#93;</code>

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
<summary><code>def get_location_service_usage(*, request_options: RequestOptionsOrDict | None = None) -> Any</code></summary>

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
try:
    response = client.devices_location_subscriptions.get_location_service_usage()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLocationServiceUsageErrorBody
```

**Async**

```python
try:
    response = await async_client.devices_location_subscriptions.get_location_service_usage()
    # TODO: Handle 'response' of type Any
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetLocationServiceUsageErrorBody
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

**OnSuccess**: <code>Any</code> -- Billable usage report.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetLocationServiceUsageErrorBody](verizon/errors/get_location_service_usage_error.py)&#93;</code>

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
<summary><code>def cancel_queued_location_report_generation(account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None) -> TransactionId</code></summary>

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
try:
    response = client.devices_locations.cancel_queued_location_report_generation(account_name, txid)
    # TODO: Handle 'response' of type TransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.devices_locations.cancel_queued_location_report_generation(account_name, txid)
    # TODO: Handle 'response' of type TransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TransactionId](verizon/models/transaction_id.py)</code> -- Report generation cancelled.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_location_report(*, request_options: RequestOptionsOrDict | None = None) -> AsynchronousLocationRequestResult</code></summary>

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
try:
    response = client.devices_locations.create_location_report()
    # TODO: Handle 'response' of type AsynchronousLocationRequestResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.devices_locations.create_location_report()
    # TODO: Handle 'response' of type AsynchronousLocationRequestResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[AsynchronousLocationRequestResult](verizon/models/asynchronous_location_request_result.py)</code> -- Request accepted; location report in progress.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_location_report_status(account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None) -> LocationReportStatus</code></summary>

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
try:
    response = client.devices_locations.get_location_report_status(account_name, txid)
    # TODO: Handle 'response' of type LocationReportStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.devices_locations.get_location_report_status(account_name, txid)
    # TODO: Handle 'response' of type LocationReportStatus
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LocationReportStatus](verizon/models/location_report_status.py)</code> -- Location report status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_locations_asynchronous(*, request_options: RequestOptionsOrDict | None = None) -> SynchronousLocationRequestResult</code></summary>

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
try:
    response = client.devices_locations.list_devices_locations_asynchronous()
    # TODO: Handle 'response' of type SynchronousLocationRequestResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.devices_locations.list_devices_locations_asynchronous()
    # TODO: Handle 'response' of type SynchronousLocationRequestResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SynchronousLocationRequestResult](verizon/models/synchronous_location_request_result.py)</code> -- Request accepted; location report in progress

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices_locations_synchronous(body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[Location]</code></summary>

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
try:
    response = client.devices_locations.list_devices_locations_synchronous(body)
    # TODO: Handle 'response' of type list[Location]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.devices_locations.list_devices_locations_synchronous(body)
    # TODO: Handle 'response' of type list[Location]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>list&#91;[Location](verizon/models/location.py)&#93;</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location_report(account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None) -> LocationReport</code></summary>

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
try:
    response = client.devices_locations.retrieve_location_report(account_name, txid, startindex)
    # TODO: Handle 'response' of type LocationReport
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.devices_locations.retrieve_location_report(account_name, txid, startindex)
    # TODO: Handle 'response' of type LocationReport
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[LocationReport](verizon/models/location_report.py)</code> -- Location information for up to 1,000 devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsCallbacks

> Source: [DiagnosticsCallbacks](verizon/apis/diagnostics_callbacks.py)

<details>
<summary><code>def get_diagnostics_subscription_callback_info(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceDiagnosticsCallback]</code></summary>

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
try:
    response = client.diagnostics_callbacks.get_diagnostics_subscription_callback_info(account_name)
    # TODO: Handle 'response' of type list[DeviceDiagnosticsCallback]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDiagnosticsSubscriptionCallbackInfoErrorBody
```

**Async**

```python
try:
    response = await async_client.diagnostics_callbacks.get_diagnostics_subscription_callback_info(account_name)
    # TODO: Handle 'response' of type list[DeviceDiagnosticsCallback]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDiagnosticsSubscriptionCallbackInfoErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)&#93;</code> -- Returns callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDiagnosticsSubscriptionCallbackInfoErrorBody](verizon/errors/get_diagnostics_subscription_callback_info_error.py)&#93;</code>

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
<summary><code>def register_diagnostics_callback_url(*, request_options: RequestOptionsOrDict | None = None) -> DeviceDiagnosticsCallback</code></summary>

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
try:
    response = client.diagnostics_callbacks.register_diagnostics_callback_url()
    # TODO: Handle 'response' of type DeviceDiagnosticsCallback
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterDiagnosticsCallbackUrlErrorBody
```

**Async**

```python
try:
    response = await async_client.diagnostics_callbacks.register_diagnostics_callback_url()
    # TODO: Handle 'response' of type DeviceDiagnosticsCallback
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterDiagnosticsCallbackUrlErrorBody
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

**OnSuccess**: <code>[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)</code> -- Returns callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterDiagnosticsCallbackUrlErrorBody](verizon/errors/register_diagnostics_callback_url_error.py)&#93;</code>

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
<summary><code>def unregister_diagnostics_callback(account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceDiagnosticsCallback</code></summary>

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
try:
    response = client.diagnostics_callbacks.unregister_diagnostics_callback(account_name, service_name)
    # TODO: Handle 'response' of type DeviceDiagnosticsCallback
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnregisterDiagnosticsCallbackErrorBody
```

**Async**

```python
try:
    response = await async_client.diagnostics_callbacks.unregister_diagnostics_callback(account_name, service_name)
    # TODO: Handle 'response' of type DeviceDiagnosticsCallback
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnregisterDiagnosticsCallbackErrorBody
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

**OnSuccess**: <code>[DeviceDiagnosticsCallback](verizon/models/device_diagnostics_callback.py)</code> -- Device diagnostics callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UnregisterDiagnosticsCallbackErrorBody](verizon/errors/unregister_diagnostics_callback_error.py)&#93;</code>

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
<summary><code>def decives_restart(body: DeviceResetRequest | DeviceResetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DiagnosticsObservationResult</code></summary>

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
try:
    response = client.diagnostics_factory_reset.decives_restart(body)
    # TODO: Handle 'response' of type DiagnosticsObservationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.diagnostics_factory_reset.decives_restart(body)
    # TODO: Handle 'response' of type DiagnosticsObservationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py)</code> -- Diagnostics observation result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsHistory

> Source: [DiagnosticsHistory](verizon/apis/diagnostics_history.py)

<details>
<summary><code>def get_diagnostics_history(*, request_options: RequestOptionsOrDict | None = None) -> list[History]</code></summary>

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
try:
    response = client.diagnostics_history.get_diagnostics_history()
    # TODO: Handle 'response' of type list[History]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.diagnostics_history.get_diagnostics_history()
    # TODO: Handle 'response' of type list[History]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>list&#91;[History](verizon/models/history.py)&#93;</code> -- History search response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsObservations

> Source: [DiagnosticsObservations](verizon/apis/diagnostics_observations.py)

<details>
<summary><code>def start_diagnostics_observation(*, request_options: RequestOptionsOrDict | None = None) -> DiagnosticsObservationResult</code></summary>

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
try:
    response = client.diagnostics_observations.start_diagnostics_observation()
    # TODO: Handle 'response' of type DiagnosticsObservationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.diagnostics_observations.start_diagnostics_observation()
    # TODO: Handle 'response' of type DiagnosticsObservationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py)</code> -- Diagnostics observation result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_diagnostics_observation(transaction_id: str, account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> DiagnosticsObservationResult</code></summary>

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
try:
    response = client.diagnostics_observations.stop_diagnostics_observation(transaction_id, account_name)
    # TODO: Handle 'response' of type DiagnosticsObservationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.diagnostics_observations.stop_diagnostics_observation(transaction_id, account_name)
    # TODO: Handle 'response' of type DiagnosticsObservationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DiagnosticsObservationResult](verizon/models/diagnostics_observation_result.py)</code> -- Diagnostics observation result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsSettings

> Source: [DiagnosticsSettings](verizon/apis/diagnostics_settings.py)

<details>
<summary><code>def list_diagnostics_settings(account_name: str, devices: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DiagnosticObservationSetting]</code></summary>

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
try:
    response = client.diagnostics_settings.list_diagnostics_settings(account_name, devices)
    # TODO: Handle 'response' of type list[DiagnosticObservationSetting]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.diagnostics_settings.list_diagnostics_settings(account_name, devices)
    # TODO: Handle 'response' of type list[DiagnosticObservationSetting]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>list&#91;[DiagnosticObservationSetting](verizon/models/diagnostic_observation_setting.py)&#93;</code> -- Diagnostic settings.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DiagnosticsSubscriptions

> Source: [DiagnosticsSubscriptions](verizon/apis/diagnostics_subscriptions.py)

<details>
<summary><code>def get_diagnostics_subscription(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> DiagnosticsSubscription</code></summary>

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
try:
    response = client.diagnostics_subscriptions.get_diagnostics_subscription(account_name)
    # TODO: Handle 'response' of type DiagnosticsSubscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.diagnostics_subscriptions.get_diagnostics_subscription(account_name)
    # TODO: Handle 'response' of type DiagnosticsSubscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[DiagnosticsSubscription](verizon/models/diagnostics_subscription.py)</code> -- Diagnostics subscription response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## EtxappConfiguration

> Source: [EtxappConfiguration](verizon/apis/etxapp_configuration.py)

<details>
<summary><code>def create_configuration(vendor_id: str, body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GeoFenceConfigurationResponse</code></summary>

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
try:
    response = client.etxapp_configuration.create_configuration(vendor_id, body)
    # TODO: Handle 'response' of type GeoFenceConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.etxapp_configuration.create_configuration(vendor_id, body)
    # TODO: Handle 'response' of type GeoFenceConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateConfigurationErrorBody
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

**OnSuccess**: <code>[GeoFenceConfigurationResponse](verizon/models/geo_fence_configuration_response.py)</code> -- Configuration created

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateConfigurationErrorBody](verizon/errors/create_configuration_error.py)&#93;</code>

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
<summary><code>def delete_configuration(id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.etxapp_configuration.delete_configuration(id, vendor_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteConfigurationErrorBody
```

**Async**

```python
try:
    await async_client.etxapp_configuration.delete_configuration(id, vendor_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteConfigurationErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteConfigurationErrorBody](verizon/errors/delete_configuration_error.py)&#93;</code>

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
<summary><code>def get_configuration(id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GeoFenceConfigurationResponse</code></summary>

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
try:
    response = client.etxapp_configuration.get_configuration(id, vendor_id)
    # TODO: Handle 'response' of type GeoFenceConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetConfigurationErrorBody
```

**Async**

```python
try:
    response = await async_client.etxapp_configuration.get_configuration(id, vendor_id)
    # TODO: Handle 'response' of type GeoFenceConfigurationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetConfigurationErrorBody
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

**OnSuccess**: <code>[GeoFenceConfigurationResponse](verizon/models/geo_fence_configuration_response.py)</code> -- Configuration found

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetConfigurationErrorBody](verizon/errors/get_configuration_error.py)&#93;</code>

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
<summary><code>def get_configuration_list(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[ConfigurationListItem]</code></summary>

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
try:
    response = client.etxapp_configuration.get_configuration_list(vendor_id)
    # TODO: Handle 'response' of type list[ConfigurationListItem]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetConfigurationListErrorBody
```

**Async**

```python
try:
    response = await async_client.etxapp_configuration.get_configuration_list(vendor_id)
    # TODO: Handle 'response' of type list[ConfigurationListItem]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetConfigurationListErrorBody
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

**OnSuccess**: <code>list&#91;[ConfigurationListItem](verizon/models/configuration_list_item.py)&#93;</code> -- Configuration list was queried successfully

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetConfigurationListErrorBody](verizon/errors/get_configuration_list_error.py)&#93;</code>

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
<summary><code>def update_configuration(id: str, vendor_id: str, body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.etxapp_configuration.update_configuration(id, vendor_id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateConfigurationErrorBody
```

**Async**

```python
try:
    await async_client.etxapp_configuration.update_configuration(id, vendor_id, body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateConfigurationErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateConfigurationErrorBody](verizon/errors/update_configuration_error.py)&#93;</code>

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
<summary><code>def get_etx_client_certificate(id: EtxclientIdlookup | EtxclientIdlookupDict, vendor_id: str, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ClientPersistenceResponse</code></summary>

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
try:
    response = client.etxregistration.get_etx_client_certificate(id, vendor_id)
    # TODO: Handle 'response' of type ClientPersistenceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEtxclientCertificateErrorBody
```

**Async**

```python
try:
    response = await async_client.etxregistration.get_etx_client_certificate(id, vendor_id)
    # TODO: Handle 'response' of type ClientPersistenceResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEtxclientCertificateErrorBody
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

**OnSuccess**: <code>[ClientPersistenceResponse](verizon/models/client_persistence_response.py)</code> -- Successful retrieval

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetEtxclientCertificateErrorBody](verizon/errors/get_etxclient_certificate_error.py)&#93;</code>

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
<summary><code>def get_etx_connection_url(vendor_id: str, body: ConnectionRequest | ConnectionRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ConnectionResponse</code></summary>

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
try:
    response = client.etxregistration.get_etx_connection_url(vendor_id, body)
    # TODO: Handle 'response' of type ConnectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEtxconnectionUrlErrorBody
```

**Async**

```python
try:
    response = await async_client.etxregistration.get_etx_connection_url(vendor_id, body)
    # TODO: Handle 'response' of type ConnectionResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEtxconnectionUrlErrorBody
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

**OnSuccess**: <code>[ConnectionResponse](verizon/models/connection_response.py)</code> -- Successful retrieval

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetEtxconnectionUrlErrorBody](verizon/errors/get_etxconnection_url_error.py)&#93;</code>

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
<summary><code>def get_etx_connection_url_multi_mec(vendor_id: str, body: ConnectionRequest | ConnectionRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ConnectionResponseV3</code></summary>

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
try:
    response = client.etxregistration.get_etx_connection_url_multi_mec(vendor_id, body)
    # TODO: Handle 'response' of type ConnectionResponseV3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEtxconnectionUrlMultiMecErrorBody
```

**Async**

```python
try:
    response = await async_client.etxregistration.get_etx_connection_url_multi_mec(vendor_id, body)
    # TODO: Handle 'response' of type ConnectionResponseV3
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetEtxconnectionUrlMultiMecErrorBody
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

**OnSuccess**: <code>[ConnectionResponseV3](verizon/models/connection_response_v3.py)</code> -- Successful retrieval

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetEtxconnectionUrlMultiMecErrorBody](verizon/errors/get_etxconnection_url_multi_mec_error.py)&#93;</code>

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
<summary><code>def query_etx_devices(body: DevicesRequest | DevicesRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> list[DevicesResponse]</code></summary>

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
try:
    response = client.etxregistration.query_etx_devices(body)
    # TODO: Handle 'response' of type list[DevicesResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryEtxdevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.etxregistration.query_etx_devices(body)
    # TODO: Handle 'response' of type list[DevicesResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryEtxdevicesErrorBody
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

**OnSuccess**: <code>list&#91;[DevicesResponse](verizon/models/devices_response.py)&#93;</code> -- Successful retrieval of devices

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[QueryEtxdevicesErrorBody](verizon/errors/query_etxdevices_error.py)&#93;</code>

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
<summary><code>def register_etx_client(body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> ClientRegistrationResponse</code></summary>

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
try:
    response = client.etxregistration.register_etx_client(body)
    # TODO: Handle 'response' of type ClientRegistrationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterEtxclientErrorBody
```

**Async**

```python
try:
    response = await async_client.etxregistration.register_etx_client(body)
    # TODO: Handle 'response' of type ClientRegistrationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterEtxclientErrorBody
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

**OnSuccess**: <code>[ClientRegistrationResponse](verizon/models/client_registration_response.py)</code> -- Successful Registration

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterEtxclientErrorBody](verizon/errors/register_etxclient_error.py)&#93;</code>

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
<summary><code>def renew_etx_client_certificate(device_id: UUID, vendor_id: str, *, x_transaction_id: UUID | None = None, body: Any | None = None, request_options: RequestOptionsOrDict | None = None) -> ClientRegistrationResponse</code></summary>

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
try:
    response = client.etxregistration.renew_etx_client_certificate(device_id, vendor_id)
    # TODO: Handle 'response' of type ClientRegistrationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenewEtxclientCertificateErrorBody
```

**Async**

```python
try:
    response = await async_client.etxregistration.renew_etx_client_certificate(device_id, vendor_id)
    # TODO: Handle 'response' of type ClientRegistrationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RenewEtxclientCertificateErrorBody
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

**OnSuccess**: <code>[ClientRegistrationResponse](verizon/models/client_registration_response.py)</code> -- Successful Registration

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RenewEtxclientCertificateErrorBody](verizon/errors/renew_etxclient_certificate_error.py)&#93;</code>

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
<summary><code>def unregister_etx_clients(device_ids: list[UUID], vendor_id: str, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.etxregistration.unregister_etx_clients(device_ids, vendor_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnregisterEtxclientsErrorBody
```

**Async**

```python
try:
    await async_client.etxregistration.unregister_etx_clients(device_ids, vendor_id)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnregisterEtxclientsErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UnregisterEtxclientsErrorBody](verizon/errors/unregister_etxclients_error.py)&#93;</code>

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
<summary><code>def devices_location_get_consent_async(account_name: str, *, device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> GetAccountDeviceConsent</code></summary>

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
try:
    response = client.exclusions.devices_location_get_consent_async(account_name)
    # TODO: Handle 'response' of type GetAccountDeviceConsent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exclusions.devices_location_get_consent_async(account_name)
    # TODO: Handle 'response' of type GetAccountDeviceConsent
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GetAccountDeviceConsent](verizon/models/get_account_device_consent.py)</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def devices_location_give_consent_async(*, body: AccountConsentCreate | AccountConsentCreateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ConsentTransactionId</code></summary>

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
try:
    response = client.exclusions.devices_location_give_consent_async()
    # TODO: Handle 'response' of type ConsentTransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exclusions.devices_location_give_consent_async()
    # TODO: Handle 'response' of type ConsentTransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ConsentTransactionId](verizon/models/consent_transaction_id.py)</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def devices_location_update_consent(*, body: AccountConsentUpdate | AccountConsentUpdateDict | None = None, request_options: RequestOptionsOrDict | None = None) -> ConsentTransactionId</code></summary>

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
try:
    response = client.exclusions.devices_location_update_consent()
    # TODO: Handle 'response' of type ConsentTransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.exclusions.devices_location_update_consent()
    # TODO: Handle 'response' of type ConsentTransactionId
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ConsentTransactionId](verizon/models/consent_transaction_id.py)</code> -- List of JSON objects, each containing the position data or an error for a device in the request.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def exclude_devices(*, request_options: RequestOptionsOrDict | None = None) -> DeviceLocationSuccessResult</code></summary>

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
try:
    response = client.exclusions.exclude_devices()
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExcludeDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.exclusions.exclude_devices()
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ExcludeDevicesErrorBody
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

**OnSuccess**: <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ExcludeDevicesErrorBody](verizon/errors/exclude_devices_error.py)&#93;</code>

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
<summary><code>def list_excluded_devices(account_name: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> DevicesConsentResult</code></summary>

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
try:
    response = client.exclusions.list_excluded_devices(account_name, start_index)
    # TODO: Handle 'response' of type DevicesConsentResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExcludedDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.exclusions.list_excluded_devices(account_name, start_index)
    # TODO: Handle 'response' of type DevicesConsentResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListExcludedDevicesErrorBody
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

**OnSuccess**: <code>[DevicesConsentResult](verizon/models/devices_consent_result.py)</code> -- Excluded devices result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListExcludedDevicesErrorBody](verizon/errors/list_excluded_devices_error.py)&#93;</code>

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
<summary><code>def remove_devices_from_exclusion_list(account_name: str, device_list: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceLocationSuccessResult</code></summary>

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
try:
    response = client.exclusions.remove_devices_from_exclusion_list(account_name, device_list)
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveDevicesFromExclusionListErrorBody
```

**Async**

```python
try:
    response = await async_client.exclusions.remove_devices_from_exclusion_list(account_name, device_list)
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveDevicesFromExclusionListErrorBody
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

**OnSuccess**: <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Devices successfully removed from list.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RemoveDevicesFromExclusionListErrorBody](verizon/errors/remove_devices_from_exclusion_list_error.py)&#93;</code>

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
<summary><code>def cancel_scheduled_firmware_upgrade(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV1SuccessResult</code></summary>

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
try:
    response = client.firmware_v1.cancel_scheduled_firmware_upgrade(account_name, upgrade_id)
    # TODO: Handle 'response' of type FotaV1SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelScheduledFirmwareUpgradeErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v1.cancel_scheduled_firmware_upgrade(account_name, upgrade_id)
    # TODO: Handle 'response' of type FotaV1SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CancelScheduledFirmwareUpgradeErrorBody
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

**OnSuccess**: <code>[FotaV1SuccessResult](verizon/models/fota_v1_success_result.py)</code> -- Upgrade canceled.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CancelScheduledFirmwareUpgradeErrorBody](verizon/errors/cancel_scheduled_firmware_upgrade_error.py)&#93;</code>

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
<summary><code>def list_available_firmware(account: str, *, request_options: RequestOptionsOrDict | None = None) -> list[Firmware]</code></summary>

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
try:
    response = client.firmware_v1.list_available_firmware(account)
    # TODO: Handle 'response' of type list[Firmware]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAvailableFirmwareErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v1.list_available_firmware(account)
    # TODO: Handle 'response' of type list[Firmware]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAvailableFirmwareErrorBody
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

**OnSuccess**: <code>list&#91;[Firmware](verizon/models/firmware.py)&#93;</code> -- List of available firmware.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAvailableFirmwareErrorBody](verizon/errors/list_available_firmware_error.py)&#93;</code>

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
<summary><code>def list_firmware_upgrade_details(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FirmwareUpgrade</code></summary>

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
try:
    response = client.firmware_v1.list_firmware_upgrade_details(account_name, upgrade_id)
    # TODO: Handle 'response' of type FirmwareUpgrade
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFirmwareUpgradeDetailsErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v1.list_firmware_upgrade_details(account_name, upgrade_id)
    # TODO: Handle 'response' of type FirmwareUpgrade
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListFirmwareUpgradeDetailsErrorBody
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

**OnSuccess**: <code>[FirmwareUpgrade](verizon/models/firmware_upgrade.py)</code> -- Firmware upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListFirmwareUpgradeDetailsErrorBody](verizon/errors/list_firmware_upgrade_details_error.py)&#93;</code>

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
<summary><code>def schedule_firmware_upgrade(body: FirmwareUpgradeRequest | FirmwareUpgradeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FirmwareUpgrade</code></summary>

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
try:
    response = client.firmware_v1.schedule_firmware_upgrade(body)
    # TODO: Handle 'response' of type FirmwareUpgrade
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleFirmwareUpgradeErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v1.schedule_firmware_upgrade(body)
    # TODO: Handle 'response' of type FirmwareUpgrade
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ScheduleFirmwareUpgradeErrorBody
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

**OnSuccess**: <code>[FirmwareUpgrade](verizon/models/firmware_upgrade.py)</code> -- Confirmation of successful firmware upgrade.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ScheduleFirmwareUpgradeErrorBody](verizon/errors/schedule_firmware_upgrade_error.py)&#93;</code>

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
<summary><code>def update_firmware_upgrade_devices(account_name: str, upgrade_id: str, *, request_options: RequestOptionsOrDict | None = None) -> FirmwareUpgradeChangeResult</code></summary>

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
try:
    response = client.firmware_v1.update_firmware_upgrade_devices(account_name, upgrade_id)
    # TODO: Handle 'response' of type FirmwareUpgradeChangeResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFirmwareUpgradeDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v1.update_firmware_upgrade_devices(account_name, upgrade_id)
    # TODO: Handle 'response' of type FirmwareUpgradeChangeResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateFirmwareUpgradeDevicesErrorBody
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

**OnSuccess**: <code>[FirmwareUpgradeChangeResult](verizon/models/firmware_upgrade_change_result.py)</code> -- Upgrade information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateFirmwareUpgradeDevicesErrorBody](verizon/errors/update_firmware_upgrade_devices_error.py)&#93;</code>

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
<summary><code>def list_available_firmware2(acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None) -> list[FirmwarePackage]</code></summary>

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
try:
    response = client.firmware_v3.list_available_firmware2(acc, protocol)
    # TODO: Handle 'response' of type list[FirmwarePackage]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAvailableFirmware2ErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v3.list_available_firmware2(acc, protocol)
    # TODO: Handle 'response' of type list[FirmwarePackage]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAvailableFirmware2ErrorBody
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

**OnSuccess**: <code>list&#91;[FirmwarePackage](verizon/models/firmware_package.py)&#93;</code> -- Returns an array of firmware objects.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAvailableFirmware2ErrorBody](verizon/errors/list_available_firmware2_error.py)&#93;</code>

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
<summary><code>def report_device_firmware(acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceFirmwareVersionUpdateResult</code></summary>

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
try:
    response = client.firmware_v3.report_device_firmware(acc, device_id)
    # TODO: Handle 'response' of type DeviceFirmwareVersionUpdateResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReportDeviceFirmwareErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v3.report_device_firmware(acc, device_id)
    # TODO: Handle 'response' of type DeviceFirmwareVersionUpdateResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ReportDeviceFirmwareErrorBody
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

**OnSuccess**: <code>[DeviceFirmwareVersionUpdateResult](verizon/models/device_firmware_version_update_result.py)</code> -- Device firmware version update request.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ReportDeviceFirmwareErrorBody](verizon/errors/report_device_firmware_error.py)&#93;</code>

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
<summary><code>def synchronize_device_firmware(acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceFirmwareList</code></summary>

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
try:
    response = client.firmware_v3.synchronize_device_firmware(acc, body)
    # TODO: Handle 'response' of type DeviceFirmwareList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SynchronizeDeviceFirmwareErrorBody
```

**Async**

```python
try:
    response = await async_client.firmware_v3.synchronize_device_firmware(acc, body)
    # TODO: Handle 'response' of type DeviceFirmwareList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SynchronizeDeviceFirmwareErrorBody
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

**OnSuccess**: <code>[DeviceFirmwareList](verizon/models/device_firmware_list.py)</code> -- Returns device firmware information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SynchronizeDeviceFirmwareErrorBody](verizon/errors/synchronize_device_firmware_error.py)&#93;</code>

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
<summary><code>def retrieve_global_list(body: ESimglobalDeviceList | ESimglobalDeviceListDict, *, request_options: RequestOptionsOrDict | None = None) -> ESimrequestResponse</code></summary>

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
try:
    response = client.global_reporting.retrieve_global_list(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveGlobalListErrorBody
```

**Async**

```python
try:
    response = await async_client.global_reporting.retrieve_global_list(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RetrieveGlobalListErrorBody
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

**OnSuccess**: <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RetrieveGlobalListErrorBody](verizon/errors/retrieve_global_list_error.py)&#93;</code>

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
<summary><code>def deviceprovhistory_using_post(body: ESimprovhistoryRequest | ESimprovhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ESimrequestResponse</code></summary>

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
try:
    response = client.global_reporting.deviceprovhistory_using_post(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceprovhistoryUsingPostErrorBody
```

**Async**

```python
try:
    response = await async_client.global_reporting.deviceprovhistory_using_post(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeviceprovhistoryUsingPostErrorBody
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

**OnSuccess**: <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeviceprovhistoryUsingPostErrorBody](verizon/errors/deviceprovhistory_using_post_error.py)&#93;</code>

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
<summary><code>def add_devices_hyper_precise(body: HplAddDevicesRequest | HplAddDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[HplAddDevicesRequest]</code></summary>

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
try:
    response = client.hpl_device_management.add_devices_hyper_precise(body)
    # TODO: Handle 'response' of type list[HplAddDevicesRequest]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddDevicesHyperPreciseErrorBody
```

**Async**

```python
try:
    response = await async_client.hpl_device_management.add_devices_hyper_precise(body)
    # TODO: Handle 'response' of type list[HplAddDevicesRequest]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AddDevicesHyperPreciseErrorBody
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

**OnSuccess**: <code>list&#91;[HplAddDevicesRequest](verizon/models/hpl_add_devices_request.py)&#93;</code> -- For each device in the request, contains device identifiers and a success or failure response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AddDevicesHyperPreciseErrorBody](verizon/errors/add_devices_hyper_precise_error.py)&#93;</code>

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
<summary><code>def deregister_callback6(account_number: str, service: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.hyper_precise_location_callbacks.deregister_callback6(account_number, service)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback6ErrorBody
```

**Async**

```python
try:
    await async_client.hyper_precise_location_callbacks.deregister_callback6(account_number, service)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback6ErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeregisterCallback6ErrorBody](verizon/errors/deregister_callback6_error.py)&#93;</code>

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
<summary><code>def list_registered_callbacks6(account_number: str, *, request_options: RequestOptionsOrDict | None = None) -> list[CallbackCreated]</code></summary>

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
try:
    response = client.hyper_precise_location_callbacks.list_registered_callbacks6(account_number)
    # TODO: Handle 'response' of type list[CallbackCreated]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks6ErrorBody
```

**Async**

```python
try:
    response = await async_client.hyper_precise_location_callbacks.list_registered_callbacks6(account_number)
    # TODO: Handle 'response' of type list[CallbackCreated]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks6ErrorBody
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

**OnSuccess**: <code>list&#91;[CallbackCreated](verizon/models/callback_created.py)&#93;</code> -- A successful response will display the billing account number (`accountName`), the name of the callback service (`name`) and the address of the callback listening service (`url`).

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListRegisteredCallbacks6ErrorBody](verizon/errors/list_registered_callbacks6_error.py)&#93;</code>

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
<summary><code>def register_callback6(account_number: str, body: HyperPreciseLocationCallback | HyperPreciseLocationCallbackDict, *, request_options: RequestOptionsOrDict | None = None) -> CallbackRegistered</code></summary>

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
try:
    response = client.hyper_precise_location_callbacks.register_callback6(account_number, body)
    # TODO: Handle 'response' of type CallbackRegistered
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback6ErrorBody
```

**Async**

```python
try:
    response = await async_client.hyper_precise_location_callbacks.register_callback6(account_number, body)
    # TODO: Handle 'response' of type CallbackRegistered
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback6ErrorBody
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

**OnSuccess**: <code>[CallbackRegistered](verizon/models/callback_registered.py)</code> -- A successful response will display the billing account number (`accountName`), the name of the callback service (`name`) and the address of the callback listening service (`url`).

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterCallback6ErrorBody](verizon/errors/register_callback6_error.py)&#93;</code>

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
<summary><code>def set_connection_planner(*, body: GetDevicesWindowsRequestforplanner | GetDevicesWindowsRequestforplannerDict | None = None, request_options: RequestOptionsOrDict | None = None) -> AsynchronousRequestResultforplanner</code></summary>

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
try:
    response = client.intelligence_service_controller.set_connection_planner()
    # TODO: Handle 'response' of type AsynchronousRequestResultforplanner
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetConnectionPlannerErrorBody
```

**Async**

```python
try:
    response = await async_client.intelligence_service_controller.set_connection_planner()
    # TODO: Handle 'response' of type AsynchronousRequestResultforplanner
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetConnectionPlannerErrorBody
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

**OnSuccess**: <code>[AsynchronousRequestResultforplanner](verizon/models/asynchronous_request_resultforplanner.py)</code> -- The asynchronous request status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SetConnectionPlannerErrorBody](verizon/errors/set_connection_planner_error.py)&#93;</code>

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
<summary><code>def status_connection_planner(*, body: GetDeviceStatusesRequestforplanner | GetDeviceStatusesRequestforplannerDict | None = None, request_options: RequestOptionsOrDict | None = None) -> GetDeviceStatusesResponseforplanner</code></summary>

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
try:
    response = client.intelligence_service_controller.status_connection_planner()
    # TODO: Handle 'response' of type GetDeviceStatusesResponseforplanner
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StatusConnectionPlannerErrorBody
```

**Async**

```python
try:
    response = await async_client.intelligence_service_controller.status_connection_planner()
    # TODO: Handle 'response' of type GetDeviceStatusesResponseforplanner
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StatusConnectionPlannerErrorBody
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

**OnSuccess**: <code>[GetDeviceStatusesResponseforplanner](verizon/models/get_device_statuses_responseforplanner.py)</code> -- Success

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[StatusConnectionPlannerErrorBody](verizon/errors/status_connection_planner_error.py)&#93;</code>

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
<summary><code>def activate_a_device_profile(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.activate_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.activate_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deactivate_a_device_profile(body: GiodeactivateDeviceProfileRequest | GiodeactivateDeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.deactivate_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.deactivate_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.delete_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.delete_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def device_suspend(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.device_suspend(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.device_suspend(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def download_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.download_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.download_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_a_device_profile(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.enable_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.enable_a_device_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_a_device_profile_for_download(body: DeviceProfileRequest | DeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.enable_a_device_profile_for_download(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.enable_a_device_profile_for_download(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def profile_suspend(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.profile_suspend(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.profile_suspend(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def resume_profile(body: GioprofileRequest | GioprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.resume_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.resume_profile(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def set_fallback(body: FallBack | FallBackDict, *, request_options: RequestOptionsOrDict | None = None) -> GiorequestResponse</code></summary>

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
try:
    response = client.managing_e_sim_profiles.set_fallback(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.managing_e_sim_profiles.set_fallback(body)
    # TODO: Handle 'response' of type GiorequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GiorequestResponse](verizon/models/giorequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Pwn

> Source: [Pwn](verizon/apis/pwn.py)

<details>
<summary><code>def change_pwn_device_i_paddress(body: ChangePwndeviceIpaddressRequest | ChangePwndeviceIpaddressRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ChangePwndeviceIpaddressResponse</code></summary>

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
try:
    response = client.pwn.change_pwn_device_i_paddress(body)
    # TODO: Handle 'response' of type ChangePwndeviceIpaddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.change_pwn_device_i_paddress(body)
    # TODO: Handle 'response' of type ChangePwndeviceIpaddressResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ChangePwndeviceIpaddressResponse](verizon/models/change_pwndevice_ipaddress_response.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_pwn_device_profile(body: ChangePwndeviceProfileRequest | ChangePwndeviceProfileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ChangePwndeviceProfileResponse</code></summary>

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
try:
    response = client.pwn.change_pwn_device_profile(body)
    # TODO: Handle 'response' of type ChangePwndeviceProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.change_pwn_device_profile(body)
    # TODO: Handle 'response' of type ChangePwndeviceProfileResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ChangePwndeviceProfileResponse](verizon/models/change_pwndevice_profile_response.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_pwn_device_state_activate(body: ChangePwndeviceStateActivateRequest | ChangePwndeviceStateActivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ChangePwndeviceStateResponse</code></summary>

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
try:
    response = client.pwn.change_pwn_device_state_activate(body)
    # TODO: Handle 'response' of type ChangePwndeviceStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.change_pwn_device_state_activate(body)
    # TODO: Handle 'response' of type ChangePwndeviceStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ChangePwndeviceStateResponse](verizon/models/change_pwndevice_state_response.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_pwn_device_state_deactivate(body: ChangePwndeviceStateDeactivateRequest | ChangePwndeviceStateDeactivateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ChangePwndeviceStateResponse</code></summary>

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
try:
    response = client.pwn.change_pwn_device_state_deactivate(body)
    # TODO: Handle 'response' of type ChangePwndeviceStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.change_pwn_device_state_deactivate(body)
    # TODO: Handle 'response' of type ChangePwndeviceStateResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ChangePwndeviceStateResponse](verizon/models/change_pwndevice_state_response.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_pwn_performance_consent(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> GetPwnperformanceConsentResponse</code></summary>

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
try:
    response = client.pwn.get_pwn_performance_consent(aname)
    # TODO: Handle 'response' of type GetPwnperformanceConsentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.get_pwn_performance_consent(aname)
    # TODO: Handle 'response' of type GetPwnperformanceConsentResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GetPwnperformanceConsentResponse](verizon/models/get_pwnperformance_consent_response.py)</code> -- consent received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_profile_list(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> PwnprofileList</code></summary>

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
try:
    response = client.pwn.get_profile_list(aname)
    # TODO: Handle 'response' of type PwnprofileList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.get_profile_list(aname)
    # TODO: Handle 'response' of type PwnprofileList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[PwnprofileList](verizon/models/pwnprofile_list.py)</code> -- PWN profiles list received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def kpi_list(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> KpiinfoList</code></summary>

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
try:
    response = client.pwn.kpi_list(aname)
    # TODO: Handle 'response' of type KpiinfoList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.pwn.kpi_list(aname)
    # TODO: Handle 'response' of type KpiinfoList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[KpiinfoList](verizon/models/kpiinfo_list.py)</code> -- Kpi list received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## PromotionPeriodInformation

> Source: [PromotionPeriodInformation](verizon/apis/promotion_period_information.py)

<details>
<summary><code>def get_promo_device_aggregate_usage_history(body: RequestBodyForUsage | RequestBodyForUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> UsageRequestResponse</code></summary>

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
try:
    response = client.promotion_period_information.get_promo_device_aggregate_usage_history(body)
    # TODO: Handle 'response' of type UsageRequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.promotion_period_information.get_promo_device_aggregate_usage_history(body)
    # TODO: Handle 'response' of type UsageRequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[UsageRequestResponse](verizon/models/usage_request_response.py)</code> -- Request response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_promo_device_usage_history(body: ARequestBodyForUsage | ARequestBodyForUsageDict, *, request_options: RequestOptionsOrDict | None = None) -> ResponseToUsageQuery</code></summary>

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
try:
    response = client.promotion_period_information.get_promo_device_usage_history(body)
    # TODO: Handle 'response' of type ResponseToUsageQuery
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.promotion_period_information.get_promo_device_usage_history(body)
    # TODO: Handle 'response' of type ResponseToUsageQuery
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[ResponseToUsageQuery](verizon/models/response_to_usage_query.py)</code> -- Usage History

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## RetrieveRatePlanList

> Source: [RetrieveRatePlanList](verizon/apis/retrieve_rate_plan_list.py)

<details>
<summary><code>def get_rate_plan_list(ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Rateplan</code></summary>

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
try:
    response = client.retrieve_rate_plan_list.get_rate_plan_list(ecpd_id)
    # TODO: Handle 'response' of type Rateplan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.retrieve_rate_plan_list.get_rate_plan_list(ecpd_id)
    # TODO: Handle 'response' of type Rateplan
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[Rateplan](verizon/models/rateplan.py)</code> -- This is a syncronous response showing the rate plans associated.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## RetrieveTheTriggers

> Source: [RetrieveTheTriggers](verizon/apis/retrieve_the_triggers.py)

<details>
<summary><code>def get_all_available_triggers(*, request_options: RequestOptionsOrDict | None = None) -> TriggerValueResponse</code></summary>

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
try:
    response = client.retrieve_the_triggers.get_all_available_triggers()
    # TODO: Handle 'response' of type TriggerValueResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.retrieve_the_triggers.get_all_available_triggers()
    # TODO: Handle 'response' of type TriggerValueResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TriggerValueResponse](verizon/models/trigger_value_response.py)</code> -- Status of Request

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_triggers_by_account_name(account_name: str, *, request_options: RequestOptionsOrDict | None = None) -> TriggerValueResponse</code></summary>

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
try:
    response = client.retrieve_the_triggers.get_all_triggers_by_account_name(account_name)
    # TODO: Handle 'response' of type TriggerValueResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.retrieve_the_triggers.get_all_triggers_by_account_name(account_name)
    # TODO: Handle 'response' of type TriggerValueResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TriggerValueResponse](verizon/models/trigger_value_response.py)</code> -- Status of Request

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_all_triggers_by_trigger_category(*, request_options: RequestOptionsOrDict | None = None) -> TriggerValueResponse2</code></summary>

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
try:
    response = client.retrieve_the_triggers.get_all_triggers_by_trigger_category()
    # TODO: Handle 'response' of type TriggerValueResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.retrieve_the_triggers.get_all_triggers_by_trigger_category()
    # TODO: Handle 'response' of type TriggerValueResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TriggerValueResponse2](verizon/models/trigger_value_response2.py)</code> -- Request response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_triggers_by_id(trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> TriggerValueResponse2</code></summary>

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
try:
    response = client.retrieve_the_triggers.get_triggers_by_id(trigger_id)
    # TODO: Handle 'response' of type TriggerValueResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.retrieve_the_triggers.get_triggers_by_id(trigger_id)
    # TODO: Handle 'response' of type TriggerValueResponse2
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TriggerValueResponse2](verizon/models/trigger_value_response2.py)</code> -- Request response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## SimActions

> Source: [SimActions](verizon/apis/sim_actions.py)

<details>
<summary><code>def newactivatecode(body: ESimprofileRequest2 | ESimprofileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None) -> ESimrequestResponse</code></summary>

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
try:
    response = client.sim_actions.newactivatecode(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewactivatecodeErrorBody
```

**Async**

```python
try:
    response = await async_client.sim_actions.newactivatecode(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type NewactivatecodeErrorBody
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

**OnSuccess**: <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[NewactivatecodeErrorBody](verizon/errors/newactivatecode_error.py)&#93;</code>

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
<summary><code>def setactivate_using_post(body: ESimprofileRequest | ESimprofileRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ESimrequestResponse</code></summary>

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
try:
    response = client.sim_actions.setactivate_using_post(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetactivateUsingPostErrorBody
```

**Async**

```python
try:
    response = await async_client.sim_actions.setactivate_using_post(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetactivateUsingPostErrorBody
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

**OnSuccess**: <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SetactivateUsingPostErrorBody](verizon/errors/setactivate_using_post_error.py)&#93;</code>

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
<summary><code>def setdeactivate_using_post(body: ProfileRequest2 | ProfileRequest2Dict, *, request_options: RequestOptionsOrDict | None = None) -> ESimrequestResponse</code></summary>

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
try:
    response = client.sim_actions.setdeactivate_using_post(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetdeactivateUsingPostErrorBody
```

**Async**

```python
try:
    response = await async_client.sim_actions.setdeactivate_using_post(body)
    # TODO: Handle 'response' of type ESimrequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SetdeactivateUsingPostErrorBody
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

**OnSuccess**: <code>[ESimrequestResponse](verizon/models/e_simrequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SetdeactivateUsingPostErrorBody](verizon/errors/setdeactivate_using_post_error.py)&#93;</code>

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
<summary><code>def assign_license_to_devices(body: AssignLicenseRequest | AssignLicenseRequestDict, *, x_request_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> SecuritySuccessResult</code></summary>

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
try:
    response = client.sim_secure_for_io_t_licenses.assign_license_to_devices(body)
    # TODO: Handle 'response' of type SecuritySuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicenseToDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.sim_secure_for_io_t_licenses.assign_license_to_devices(body)
    # TODO: Handle 'response' of type SecuritySuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicenseToDevicesErrorBody
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

**OnSuccess**: <code>[SecuritySuccessResult](verizon/models/security_success_result.py)</code> -- Success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AssignLicenseToDevicesErrorBody](verizon/errors/assign_license_to_devices_error.py)&#93;</code>

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
<summary><code>def unassign_license_to_devices(x_request_id: str, *, request_options: RequestOptionsOrDict | None = None) -> SecuritySuccessResult</code></summary>

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
try:
    response = client.sim_secure_for_io_t_licenses.unassign_license_to_devices(x_request_id)
    # TODO: Handle 'response' of type SecuritySuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnassignLicenseToDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.sim_secure_for_io_t_licenses.unassign_license_to_devices(x_request_id)
    # TODO: Handle 'response' of type SecuritySuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UnassignLicenseToDevicesErrorBody
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

**OnSuccess**: <code>[SecuritySuccessResult](verizon/models/security_success_result.py)</code> -- Success response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UnassignLicenseToDevicesErrorBody](verizon/errors/unassign_license_to_devices_error.py)&#93;</code>

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
<summary><code>def list_devices_sms_messages(aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None) -> SmsmessagesQueryResult</code></summary>

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
try:
    response = client.sms.list_devices_sms_messages(aname)
    # TODO: Handle 'response' of type SmsmessagesQueryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesSmsmessagesErrorBody
```

**Async**

```python
try:
    response = await async_client.sms.list_devices_sms_messages(aname)
    # TODO: Handle 'response' of type SmsmessagesQueryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListDevicesSmsmessagesErrorBody
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

**OnSuccess**: <code>[SmsmessagesQueryResult](verizon/models/smsmessages_query_result.py)</code> -- Successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListDevicesSmsmessagesErrorBody](verizon/errors/list_devices_smsmessages_error.py)&#93;</code>

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
<summary><code>def send_sms_to_device(body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.sms.send_sms_to_device(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendSmstoDeviceErrorBody
```

**Async**

```python
try:
    response = await async_client.sms.send_sms_to_device(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SendSmstoDeviceErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SendSmstoDeviceErrorBody](verizon/errors/send_smsto_device_error.py)&#93;</code>

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
<summary><code>def start_queued_sms_delivery(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> ConnectivityManagementSuccessResult</code></summary>

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
try:
    response = client.sms.start_queued_sms_delivery(aname)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartQueuedSmsdeliveryErrorBody
```

**Async**

```python
try:
    response = await async_client.sms.start_queued_sms_delivery(aname)
    # TODO: Handle 'response' of type ConnectivityManagementSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartQueuedSmsdeliveryErrorBody
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

**OnSuccess**: <code>[ConnectivityManagementSuccessResult](verizon/models/connectivity_management_success_result.py)</code> -- Successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[StartQueuedSmsdeliveryErrorBody](verizon/errors/start_queued_smsdelivery_error.py)&#93;</code>

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
<summary><code>def create_a_profile(body: DtoConfigurationProfile | DtoConfigurationProfileDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DtoProfileResponse]</code></summary>

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
try:
    response = client.sensor_insights_device_profile.create_a_profile(body)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAprofileErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_device_profile.create_a_profile(body)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateAprofileErrorBody
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

**OnSuccess**: <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateAprofileErrorBody](verizon/errors/create_aprofile_error.py)&#93;</code>

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
<summary><code>def delete_a_profile(deleterequest: DtoConfigurationProfileDelete | DtoConfigurationProfileDeleteDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DtoProfileResponse]</code></summary>

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
try:
    response = client.sensor_insights_device_profile.delete_a_profile(deleterequest)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteAprofileErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_device_profile.delete_a_profile(deleterequest)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteAprofileErrorBody
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

**OnSuccess**: <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteAprofileErrorBody](verizon/errors/delete_aprofile_error.py)&#93;</code>

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
<summary><code>def query_a_profile(body: ResourceResourceQuery | ResourceResourceQueryDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DtoProfileResponse]</code></summary>

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
try:
    response = client.sensor_insights_device_profile.query_a_profile(body)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAprofileErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_device_profile.query_a_profile(body)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryAprofileErrorBody
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

**OnSuccess**: <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[QueryAprofileErrorBody](verizon/errors/query_aprofile_error.py)&#93;</code>

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
<summary><code>def update_a_profile(body: DtoConfigurationProfilePath | DtoConfigurationProfilePathDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DtoProfileResponse]</code></summary>

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
try:
    response = client.sensor_insights_device_profile.update_a_profile(body)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateAprofileErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_device_profile.update_a_profile(body)
    # TODO: Handle 'response' of type list[DtoProfileResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateAprofileErrorBody
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

**OnSuccess**: <code>list&#91;[DtoProfileResponse](verizon/models/dto_profile_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateAprofileErrorBody](verizon/errors/update_aprofile_error.py)&#93;</code>

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
<summary><code>def sensor_insights_device_action_set_request(body: DmV1DevicesActionsSetRequest | DmV1DevicesActionsSetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoDeviceActionSetResponse</code></summary>

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
try:
    response = client.sensor_insights_devices.sensor_insights_device_action_set_request(body)
    # TODO: Handle 'response' of type DtoDeviceActionSetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsDeviceActionSetRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_devices.sensor_insights_device_action_set_request(body)
    # TODO: Handle 'response' of type DtoDeviceActionSetResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsDeviceActionSetRequestErrorBody
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

**OnSuccess**: <code>[DtoDeviceActionSetResponse](verizon/models/dto_device_action_set_response.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsDeviceActionSetRequestErrorBody](verizon/errors/sensor_insights_device_action_set_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_last_reported_time_request(body: DtoLastReportedTimeRequest | DtoLastReportedTimeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoLastReportedTimeResponse</code></summary>

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
try:
    response = client.sensor_insights_devices.sensor_insights_last_reported_time_request(body)
    # TODO: Handle 'response' of type DtoLastReportedTimeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsLastReportedTimeRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_devices.sensor_insights_last_reported_time_request(body)
    # TODO: Handle 'response' of type DtoLastReportedTimeResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsLastReportedTimeRequestErrorBody
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

**OnSuccess**: <code>[DtoLastReportedTimeResponse](verizon/models/dto_last_reported_time_response.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsLastReportedTimeRequestErrorBody](verizon/errors/sensor_insights_last_reported_time_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_device_experience_history_request(body: DtoListDeviceExperienceHistoryRequest | DtoListDeviceExperienceHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[UserDeviceExperienceHistory]</code></summary>

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
try:
    response = client.sensor_insights_devices.sensor_insights_list_device_experience_history_request(body)
    # TODO: Handle 'response' of type list[UserDeviceExperienceHistory]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListDeviceExperienceHistoryRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_devices.sensor_insights_list_device_experience_history_request(body)
    # TODO: Handle 'response' of type list[UserDeviceExperienceHistory]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListDeviceExperienceHistoryRequestErrorBody
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

**OnSuccess**: <code>list&#91;[UserDeviceExperienceHistory](verizon/models/user_device_experience_history.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListDeviceExperienceHistoryRequestErrorBody](verizon/errors/sensor_insights_list_device_experience_history_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_devices_request(body: DtoListDevicesRequest | DtoListDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DtoExpandedDeviceResponse]</code></summary>

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
try:
    response = client.sensor_insights_devices.sensor_insights_list_devices_request(body)
    # TODO: Handle 'response' of type list[DtoExpandedDeviceResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListDevicesRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_devices.sensor_insights_list_devices_request(body)
    # TODO: Handle 'response' of type list[DtoExpandedDeviceResponse]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListDevicesRequestErrorBody
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

**OnSuccess**: <code>list&#91;[DtoExpandedDeviceResponse](verizon/models/dto_expanded_device_response.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListDevicesRequestErrorBody](verizon/errors/sensor_insights_list_devices_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_network_experience_history_request(body: DtoListNetworkExperienceHistoryRequest | DtoListNetworkExperienceHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[UserNetworkExperienceHistory]</code></summary>

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
try:
    response = client.sensor_insights_devices.sensor_insights_list_network_experience_history_request(body)
    # TODO: Handle 'response' of type list[UserNetworkExperienceHistory]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListNetworkExperienceHistoryRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_devices.sensor_insights_list_network_experience_history_request(body)
    # TODO: Handle 'response' of type list[UserNetworkExperienceHistory]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListNetworkExperienceHistoryRequestErrorBody
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

**OnSuccess**: <code>list&#91;[UserNetworkExperienceHistory](verizon/models/user_network_experience_history.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListNetworkExperienceHistoryRequestErrorBody](verizon/errors/sensor_insights_list_network_experience_history_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_patch_device_request(body: DtoPatchDeviceRequest | DtoPatchDeviceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ResourceDevice</code></summary>

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
try:
    response = client.sensor_insights_devices.sensor_insights_patch_device_request(body)
    # TODO: Handle 'response' of type ResourceDevice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsPatchDeviceRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_devices.sensor_insights_patch_device_request(body)
    # TODO: Handle 'response' of type ResourceDevice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsPatchDeviceRequestErrorBody
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

**OnSuccess**: <code>[ResourceDevice](verizon/models/resource_device.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsPatchDeviceRequestErrorBody](verizon/errors/sensor_insights_patch_device_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_gateway_devices_request(body: DtoListDevicesRequest | DtoListDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[ResourceDevice]</code></summary>

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
try:
    response = client.sensor_insights_gateways.sensor_insights_list_gateway_devices_request(body)
    # TODO: Handle 'response' of type list[ResourceDevice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListGatewayDevicesRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_gateways.sensor_insights_list_gateway_devices_request(body)
    # TODO: Handle 'response' of type list[ResourceDevice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListGatewayDevicesRequestErrorBody
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

**OnSuccess**: <code>list&#91;[ResourceDevice](verizon/models/resource_device.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListGatewayDevicesRequestErrorBody](verizon/errors/sensor_insights_list_gateway_devices_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_get_network_health_score_response(*, request_options: RequestOptionsOrDict | None = None) -> DtoGetNetworkHealthScoreResponse</code></summary>

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
try:
    response = client.sensor_insights_health_score.sensor_insights_get_network_health_score_response()
    # TODO: Handle 'response' of type DtoGetNetworkHealthScoreResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsGetNetworkHealthScoreResponseErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_health_score.sensor_insights_get_network_health_score_response()
    # TODO: Handle 'response' of type DtoGetNetworkHealthScoreResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsGetNetworkHealthScoreResponseErrorBody
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

**OnSuccess**: <code>[DtoGetNetworkHealthScoreResponse](verizon/models/dto_get_network_health_score_response.py)</code> -- Get a network health score

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsGetNetworkHealthScoreResponseErrorBody](verizon/errors/sensor_insights_get_network_health_score_response_error.py)&#93;</code>

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
<summary><code>def sensor_insights_health_score_summary(*, request_options: RequestOptionsOrDict | None = None) -> DtoHealthScoreSummary</code></summary>

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
try:
    response = client.sensor_insights_health_score.sensor_insights_health_score_summary()
    # TODO: Handle 'response' of type DtoHealthScoreSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsHealthScoreSummaryErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_health_score.sensor_insights_health_score_summary()
    # TODO: Handle 'response' of type DtoHealthScoreSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsHealthScoreSummaryErrorBody
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

**OnSuccess**: <code>[DtoHealthScoreSummary](verizon/models/dto_health_score_summary.py)</code> -- Get health score summary

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsHealthScoreSummaryErrorBody](verizon/errors/sensor_insights_health_score_summary_error.py)&#93;</code>

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
<summary><code>def sensor_insights_add_users_to_notification_group_request(body: DtoAddUsersToNotificationGroupRequest | DtoAddUsersToNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.sensor_insights_notification_groups.sensor_insights_add_users_to_notification_group_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsAddUsersToNotificationGroupRequestErrorBody
```

**Async**

```python
try:
    await async_client.sensor_insights_notification_groups.sensor_insights_add_users_to_notification_group_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsAddUsersToNotificationGroupRequestErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsAddUsersToNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_add_users_to_notification_group_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_create_notification_group_request(body: DtoCreateNotificationGroupRequest | DtoCreateNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoNotificationGroupResponseEntity</code></summary>

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
try:
    response = client.sensor_insights_notification_groups.sensor_insights_create_notification_group_request(body)
    # TODO: Handle 'response' of type DtoNotificationGroupResponseEntity
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsCreateNotificationGroupRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_notification_groups.sensor_insights_create_notification_group_request(
        body
    )
    # TODO: Handle 'response' of type DtoNotificationGroupResponseEntity
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsCreateNotificationGroupRequestErrorBody
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

**OnSuccess**: <code>[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsCreateNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_create_notification_group_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_delete_notification_group(payload: DtoDeleteNotificationGroupRequest | DtoDeleteNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.sensor_insights_notification_groups.sensor_insights_delete_notification_group(payload)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsDeleteNotificationGroupErrorBody
```

**Async**

```python
try:
    await async_client.sensor_insights_notification_groups.sensor_insights_delete_notification_group(payload)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsDeleteNotificationGroupErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsDeleteNotificationGroupErrorBody](verizon/errors/sensor_insights_delete_notification_group_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_notification_group_request(body: DtoListNotificationGroupRequest | DtoListNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[DtoNotificationGroupResponseEntity]</code></summary>

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
try:
    response = client.sensor_insights_notification_groups.sensor_insights_list_notification_group_request(body)
    # TODO: Handle 'response' of type list[DtoNotificationGroupResponseEntity]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListNotificationGroupRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_notification_groups.sensor_insights_list_notification_group_request(
        body
    )
    # TODO: Handle 'response' of type list[DtoNotificationGroupResponseEntity]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListNotificationGroupRequestErrorBody
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

**OnSuccess**: <code>list&#91;[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_list_notification_group_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_remove_users_from_notification_group_request(body: DtoRemoveUsersFromNotificationGroupRequest | DtoRemoveUsersFromNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.sensor_insights_notification_groups.sensor_insights_remove_users_from_notification_group_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody
```

**Async**

```python
try:
    await async_client.sensor_insights_notification_groups.sensor_insights_remove_users_from_notification_group_request(
        body
    )
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsRemoveUsersFromNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_remove_users_from_notification_group_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_update_notification_group_request(body: DtoUpdateNotificationGroupRequest | DtoUpdateNotificationGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoNotificationGroupResponseEntity</code></summary>

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
try:
    response = client.sensor_insights_notification_groups.sensor_insights_update_notification_group_request(body)
    # TODO: Handle 'response' of type DtoNotificationGroupResponseEntity
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsUpdateNotificationGroupRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_notification_groups.sensor_insights_update_notification_group_request(
        body
    )
    # TODO: Handle 'response' of type DtoNotificationGroupResponseEntity
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsUpdateNotificationGroupRequestErrorBody
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

**OnSuccess**: <code>[DtoNotificationGroupResponseEntity](verizon/models/dto_notification_group_response_entity.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsUpdateNotificationGroupRequestErrorBody](verizon/errors/sensor_insights_update_notification_group_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_rules_request(body: DtoListRulesRequest | DtoListRulesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[ResourceRule]</code></summary>

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
try:
    response = client.sensor_insights_rules.sensor_insights_list_rules_request(body)
    # TODO: Handle 'response' of type list[ResourceRule]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListRulesRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_rules.sensor_insights_list_rules_request(body)
    # TODO: Handle 'response' of type list[ResourceRule]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListRulesRequestErrorBody
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

**OnSuccess**: <code>list&#91;[ResourceRule](verizon/models/resource_rule.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListRulesRequestErrorBody](verizon/errors/sensor_insights_list_rules_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_overwrite_rule_request(body: DtoOverwriteRuleRequest | DtoOverwriteRuleRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ResourceRule</code></summary>

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
try:
    response = client.sensor_insights_rules.sensor_insights_overwrite_rule_request(body)
    # TODO: Handle 'response' of type ResourceRule
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsOverwriteRuleRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_rules.sensor_insights_overwrite_rule_request(body)
    # TODO: Handle 'response' of type ResourceRule
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsOverwriteRuleRequestErrorBody
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

**OnSuccess**: <code>[ResourceRule](verizon/models/resource_rule.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsOverwriteRuleRequestErrorBody](verizon/errors/sensor_insights_overwrite_rule_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_sensor_devices_request(body: DtoListSensorDevicesRequest | DtoListSensorDevicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[ResourceDevice]</code></summary>

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
try:
    response = client.sensor_insights_sensors.sensor_insights_list_sensor_devices_request(body)
    # TODO: Handle 'response' of type list[ResourceDevice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListSensorDevicesRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_sensors.sensor_insights_list_sensor_devices_request(body)
    # TODO: Handle 'response' of type list[ResourceDevice]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListSensorDevicesRequestErrorBody
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

**OnSuccess**: <code>list&#91;[ResourceDevice](verizon/models/resource_device.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListSensorDevicesRequestErrorBody](verizon/errors/sensor_insights_list_sensor_devices_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_off_board_sensor_request(body: DtoOffBoardSensorRequest | DtoOffBoardSensorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.sensor_insights_sensors.sensor_insights_off_board_sensor_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsOffBoardSensorRequestErrorBody
```

**Async**

```python
try:
    await async_client.sensor_insights_sensors.sensor_insights_off_board_sensor_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsOffBoardSensorRequestErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsOffBoardSensorRequestErrorBody](verizon/errors/sensor_insights_off_board_sensor_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_on_board_sensor_request(body: DtoOnBoardSensorRequest | DtoOnBoardSensorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.sensor_insights_sensors.sensor_insights_on_board_sensor_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsOnBoardSensorRequestErrorBody
```

**Async**

```python
try:
    await async_client.sensor_insights_sensors.sensor_insights_on_board_sensor_request(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsOnBoardSensorRequestErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsOnBoardSensorRequestErrorBody](verizon/errors/sensor_insights_on_board_sensor_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_sensor_off_boarding_status_request(body: DtoSensorOffBoardStatusRequest | DtoSensorOffBoardStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoSensorOffBoardingStatusResponse</code></summary>

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
try:
    response = client.sensor_insights_sensors.sensor_insights_sensor_off_boarding_status_request(body)
    # TODO: Handle 'response' of type DtoSensorOffBoardingStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsSensorOffBoardingStatusRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_sensors.sensor_insights_sensor_off_boarding_status_request(body)
    # TODO: Handle 'response' of type DtoSensorOffBoardingStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsSensorOffBoardingStatusRequestErrorBody
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

**OnSuccess**: <code>[DtoSensorOffBoardingStatusResponse](verizon/models/dto_sensor_off_boarding_status_response.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsSensorOffBoardingStatusRequestErrorBody](verizon/errors/sensor_insights_sensor_off_boarding_status_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_sensor_on_board_status_request(body: DtoSensorOnBoardStatusRequest | DtoSensorOnBoardStatusRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoSensorOnBoardingStatusResponse</code></summary>

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
try:
    response = client.sensor_insights_sensors.sensor_insights_sensor_on_board_status_request(body)
    # TODO: Handle 'response' of type DtoSensorOnBoardingStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsSensorOnBoardStatusRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_sensors.sensor_insights_sensor_on_board_status_request(body)
    # TODO: Handle 'response' of type DtoSensorOnBoardingStatusResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsSensorOnBoardStatusRequestErrorBody
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

**OnSuccess**: <code>[DtoSensorOnBoardingStatusResponse](verizon/models/dto_sensor_on_boarding_status_response.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsSensorOnBoardStatusRequestErrorBody](verizon/errors/sensor_insights_sensor_on_board_status_request_error.py)&#93;</code>

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
<summary><code>def sensorinsightsmetricsquery(body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None) -> DtoQueryMetricsResponse</code></summary>

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
try:
    response = client.sensor_insights_smart_alert_metrics.sensorinsightsmetricsquery(body)
    # TODO: Handle 'response' of type DtoQueryMetricsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorinsightsmetricsqueryErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_smart_alert_metrics.sensorinsightsmetricsquery(body)
    # TODO: Handle 'response' of type DtoQueryMetricsResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorinsightsmetricsqueryErrorBody
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

**OnSuccess**: <code>[DtoQueryMetricsResponse](verizon/models/dto_query_metrics_response.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorinsightsmetricsqueryErrorBody](verizon/errors/sensorinsightsmetricsquery_error.py)&#93;</code>

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
<summary><code>def sensor_insights_bulk_update(body: DtoBulkUpdate | DtoBulkUpdateDict, *, request_options: RequestOptionsOrDict | None = None) -> UserSmartAlert</code></summary>

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
try:
    response = client.sensor_insights_smart_alerts.sensor_insights_bulk_update(body)
    # TODO: Handle 'response' of type UserSmartAlert
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsBulkUpdateErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_smart_alerts.sensor_insights_bulk_update(body)
    # TODO: Handle 'response' of type UserSmartAlert
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsBulkUpdateErrorBody
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

**OnSuccess**: <code>[UserSmartAlert](verizon/models/user_smart_alert.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsBulkUpdateErrorBody](verizon/errors/sensor_insights_bulk_update_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_smart_alerts_request(body: DtoListSmartAlertsRequest | DtoListSmartAlertsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[UserSmartAlert]</code></summary>

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
try:
    response = client.sensor_insights_smart_alerts.sensor_insights_list_smart_alerts_request(body)
    # TODO: Handle 'response' of type list[UserSmartAlert]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListSmartAlertsRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_smart_alerts.sensor_insights_list_smart_alerts_request(body)
    # TODO: Handle 'response' of type list[UserSmartAlert]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListSmartAlertsRequestErrorBody
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

**OnSuccess**: <code>list&#91;[UserSmartAlert](verizon/models/user_smart_alert.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListSmartAlertsRequestErrorBody](verizon/errors/sensor_insights_list_smart_alerts_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_patch_smart_alert_request(body: DtoPatchSmartAlertRequest | DtoPatchSmartAlertRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> UserSmartAlert</code></summary>

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
try:
    response = client.sensor_insights_smart_alerts.sensor_insights_patch_smart_alert_request(body)
    # TODO: Handle 'response' of type UserSmartAlert
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsPatchSmartAlertRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_smart_alerts.sensor_insights_patch_smart_alert_request(body)
    # TODO: Handle 'response' of type UserSmartAlert
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsPatchSmartAlertRequestErrorBody
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

**OnSuccess**: <code>[UserSmartAlert](verizon/models/user_smart_alert.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsPatchSmartAlertRequestErrorBody](verizon/errors/sensor_insights_patch_smart_alert_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_create_user_request(body: DtoCreateUserRequest | DtoCreateUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ResourceUser</code></summary>

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
try:
    response = client.sensor_insights_users.sensor_insights_create_user_request(body)
    # TODO: Handle 'response' of type ResourceUser
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsCreateUserRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_users.sensor_insights_create_user_request(body)
    # TODO: Handle 'response' of type ResourceUser
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsCreateUserRequestErrorBody
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

**OnSuccess**: <code>[ResourceUser](verizon/models/resource_user.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsCreateUserRequestErrorBody](verizon/errors/sensor_insights_create_user_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_delete_user(deleterequestpayload: DtoDeleteUserRequest | DtoDeleteUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.sensor_insights_users.sensor_insights_delete_user(deleterequestpayload)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsDeleteUserErrorBody
```

**Async**

```python
try:
    await async_client.sensor_insights_users.sensor_insights_delete_user(deleterequestpayload)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsDeleteUserErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsDeleteUserErrorBody](verizon/errors/sensor_insights_delete_user_error.py)&#93;</code>

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
<summary><code>def sensor_insights_list_user_request(body: DtoListUserRequest | DtoListUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[ResourceUser]</code></summary>

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
try:
    response = client.sensor_insights_users.sensor_insights_list_user_request(body)
    # TODO: Handle 'response' of type list[ResourceUser]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListUserRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_users.sensor_insights_list_user_request(body)
    # TODO: Handle 'response' of type list[ResourceUser]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsListUserRequestErrorBody
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

**OnSuccess**: <code>list&#91;[ResourceUser](verizon/models/resource_user.py)&#93;</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsListUserRequestErrorBody](verizon/errors/sensor_insights_list_user_request_error.py)&#93;</code>

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
<summary><code>def sensor_insights_update_user_request(body: DtoUpdateUserRequest | DtoUpdateUserRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ResourceUser</code></summary>

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
try:
    response = client.sensor_insights_users.sensor_insights_update_user_request(body)
    # TODO: Handle 'response' of type ResourceUser
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsUpdateUserRequestErrorBody
```

**Async**

```python
try:
    response = await async_client.sensor_insights_users.sensor_insights_update_user_request(body)
    # TODO: Handle 'response' of type ResourceUser
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type SensorInsightsUpdateUserRequestErrorBody
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

**OnSuccess**: <code>[ResourceUser](verizon/models/resource_user.py)</code> -- OK

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[SensorInsightsUpdateUserRequestErrorBody](verizon/errors/sensor_insights_update_user_request_error.py)&#93;</code>

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
<summary><code>def get_device_check_in_history(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[CheckInHistoryItem]</code></summary>

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
try:
    response = client.server_logging.get_device_check_in_history(account, device_id)
    # TODO: Handle 'response' of type list[CheckInHistoryItem]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceCheckInHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.server_logging.get_device_check_in_history(account, device_id)
    # TODO: Handle 'response' of type list[CheckInHistoryItem]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceCheckInHistoryErrorBody
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

**OnSuccess**: <code>list&#91;[CheckInHistoryItem](verizon/models/check_in_history_item.py)&#93;</code> -- List of check-in history entries.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceCheckInHistoryErrorBody](verizon/errors/get_device_check_in_history_error.py)&#93;</code>

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
<summary><code>def list_account_service_plans(aname: str, *, request_options: RequestOptionsOrDict | None = None) -> list[ServicePlan]</code></summary>

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
try:
    response = client.service_plans.list_account_service_plans(aname)
    # TODO: Handle 'response' of type list[ServicePlan]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountServicePlansErrorBody
```

**Async**

```python
try:
    response = await async_client.service_plans.list_account_service_plans(aname)
    # TODO: Handle 'response' of type list[ServicePlan]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountServicePlansErrorBody
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

**OnSuccess**: <code>list&#91;[ServicePlan](verizon/models/service_plan.py)&#93;</code> -- The list of service plans associated with the account.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountServicePlansErrorBody](verizon/errors/list_account_service_plans_error.py)&#93;</code>

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
<summary><code>def end_connectivity_management_session(*, request_options: RequestOptionsOrDict | None = None) -> LogOutRequest</code></summary>

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
try:
    response = client.session_management.end_connectivity_management_session()
    # TODO: Handle 'response' of type LogOutRequest
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EndConnectivityManagementSessionErrorBody
```

**Async**

```python
try:
    response = await async_client.session_management.end_connectivity_management_session()
    # TODO: Handle 'response' of type LogOutRequest
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EndConnectivityManagementSessionErrorBody
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

**OnSuccess**: <code>[LogOutRequest](verizon/models/log_out_request.py)</code> -- VZ-M2M session token.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[EndConnectivityManagementSessionErrorBody](verizon/errors/end_connectivity_management_session_error.py)&#93;</code>

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
<summary><code>def reset_connectivity_management_password(body: SessionResetPasswordRequest | SessionResetPasswordRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> SessionResetPasswordResult</code></summary>

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
try:
    response = client.session_management.reset_connectivity_management_password(body)
    # TODO: Handle 'response' of type SessionResetPasswordResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResetConnectivityManagementPasswordErrorBody
```

**Async**

```python
try:
    response = await async_client.session_management.reset_connectivity_management_password(body)
    # TODO: Handle 'response' of type SessionResetPasswordResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ResetConnectivityManagementPasswordErrorBody
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

**OnSuccess**: <code>[SessionResetPasswordResult](verizon/models/session_reset_password_result.py)</code> -- Returns a new, randomly generated password for the current username.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ResetConnectivityManagementPasswordErrorBody](verizon/errors/reset_connectivity_management_password_error.py)&#93;</code>

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
<summary><code>def start_connectivity_management_session(*, body: LogInRequest | LogInRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> LogInResult</code></summary>

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
try:
    response = client.session_management.start_connectivity_management_session()
    # TODO: Handle 'response' of type LogInResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartConnectivityManagementSessionErrorBody
```

**Async**

```python
try:
    response = await async_client.session_management.start_connectivity_management_session()
    # TODO: Handle 'response' of type LogInResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type StartConnectivityManagementSessionErrorBody
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

**OnSuccess**: <code>[LogInResult](verizon/models/log_in_result.py)</code> -- VZ-M2M session token.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[StartConnectivityManagementSessionErrorBody](verizon/errors/start_connectivity_management_session_error.py)&#93;</code>

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
<summary><code>def deregister_callback3(account: str, service: CallbackServiceOrStr, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.software_management_callbacks_v1.deregister_callback3(account, service)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback3ErrorBody
```

**Async**

```python
try:
    await async_client.software_management_callbacks_v1.deregister_callback3(account, service)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback3ErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeregisterCallback3ErrorBody](verizon/errors/deregister_callback3_error.py)&#93;</code>

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
<summary><code>def list_registered_callbacks3(account: str, *, request_options: RequestOptionsOrDict | None = None) -> list[RegisteredCallbacks]</code></summary>

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
try:
    response = client.software_management_callbacks_v1.list_registered_callbacks3(account)
    # TODO: Handle 'response' of type list[RegisteredCallbacks]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks3ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v1.list_registered_callbacks3(account)
    # TODO: Handle 'response' of type list[RegisteredCallbacks]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks3ErrorBody
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

**OnSuccess**: <code>list&#91;[RegisteredCallbacks](verizon/models/registered_callbacks.py)&#93;</code> -- List of callbacks.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListRegisteredCallbacks3ErrorBody](verizon/errors/list_registered_callbacks3_error.py)&#93;</code>

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
<summary><code>def register_callback3(account: str, body: FotaV1CallbackRegistrationRequest | FotaV1CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FotaV1CallbackRegistrationResult</code></summary>

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
try:
    response = client.software_management_callbacks_v1.register_callback3(account, body)
    # TODO: Handle 'response' of type FotaV1CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback3ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v1.register_callback3(account, body)
    # TODO: Handle 'response' of type FotaV1CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback3ErrorBody
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

**OnSuccess**: <code>[FotaV1CallbackRegistrationResult](verizon/models/fota_v1_callback_registration_result.py)</code> -- Result of registering a callback.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterCallback3ErrorBody](verizon/errors/register_callback3_error.py)&#93;</code>

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
<summary><code>def deregister_callback4(account: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV2SuccessResult</code></summary>

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
try:
    response = client.software_management_callbacks_v2.deregister_callback4(account)
    # TODO: Handle 'response' of type FotaV2SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback4ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v2.deregister_callback4(account)
    # TODO: Handle 'response' of type FotaV2SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback4ErrorBody
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

**OnSuccess**: <code>[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py)</code> -- Result of deregistering a callback.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeregisterCallback4ErrorBody](verizon/errors/deregister_callback4_error.py)&#93;</code>

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
<summary><code>def list_registered_callbacks4(account: str, *, request_options: RequestOptionsOrDict | None = None) -> CallbackSummary</code></summary>

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
try:
    response = client.software_management_callbacks_v2.list_registered_callbacks4(account)
    # TODO: Handle 'response' of type CallbackSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks4ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v2.list_registered_callbacks4(account)
    # TODO: Handle 'response' of type CallbackSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks4ErrorBody
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

**OnSuccess**: <code>[CallbackSummary](verizon/models/callback_summary.py)</code> -- Return callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListRegisteredCallbacks4ErrorBody](verizon/errors/list_registered_callbacks4_error.py)&#93;</code>

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
<summary><code>def register_callback4(account: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV2CallbackRegistrationResult</code></summary>

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
try:
    response = client.software_management_callbacks_v2.register_callback4(account)
    # TODO: Handle 'response' of type FotaV2CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback4ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v2.register_callback4(account)
    # TODO: Handle 'response' of type FotaV2CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback4ErrorBody
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

**OnSuccess**: <code>[FotaV2CallbackRegistrationResult](verizon/models/fota_v2_callback_registration_result.py)</code> -- Return callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterCallback4ErrorBody](verizon/errors/register_callback4_error.py)&#93;</code>

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
<summary><code>def update_callback(account: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV2CallbackRegistrationResult</code></summary>

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
try:
    response = client.software_management_callbacks_v2.update_callback(account)
    # TODO: Handle 'response' of type FotaV2CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCallbackErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v2.update_callback(account)
    # TODO: Handle 'response' of type FotaV2CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCallbackErrorBody
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

**OnSuccess**: <code>[FotaV2CallbackRegistrationResult](verizon/models/fota_v2_callback_registration_result.py)</code> -- Return callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateCallbackErrorBody](verizon/errors/update_callback_error.py)&#93;</code>

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
<summary><code>def deregister_callback5(acc: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV3SuccessResult</code></summary>

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
try:
    response = client.software_management_callbacks_v3.deregister_callback5(acc)
    # TODO: Handle 'response' of type FotaV3SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback5ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v3.deregister_callback5(acc)
    # TODO: Handle 'response' of type FotaV3SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeregisterCallback5ErrorBody
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

**OnSuccess**: <code>[FotaV3SuccessResult](verizon/models/fota_v3_success_result.py)</code> -- Delete request result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeregisterCallback5ErrorBody](verizon/errors/deregister_callback5_error.py)&#93;</code>

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
<summary><code>def list_registered_callbacks5(acc: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV3CallbackSummary</code></summary>

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
try:
    response = client.software_management_callbacks_v3.list_registered_callbacks5(acc)
    # TODO: Handle 'response' of type FotaV3CallbackSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks5ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v3.list_registered_callbacks5(acc)
    # TODO: Handle 'response' of type FotaV3CallbackSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListRegisteredCallbacks5ErrorBody
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

**OnSuccess**: <code>[FotaV3CallbackSummary](verizon/models/fota_v3_callback_summary.py)</code> -- Return callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListRegisteredCallbacks5ErrorBody](verizon/errors/list_registered_callbacks5_error.py)&#93;</code>

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
<summary><code>def register_callback5(acc: str, body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FotaV3CallbackRegistrationResult</code></summary>

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
try:
    response = client.software_management_callbacks_v3.register_callback5(acc, body)
    # TODO: Handle 'response' of type FotaV3CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback5ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v3.register_callback5(acc, body)
    # TODO: Handle 'response' of type FotaV3CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RegisterCallback5ErrorBody
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

**OnSuccess**: <code>[FotaV3CallbackRegistrationResult](verizon/models/fota_v3_callback_registration_result.py)</code> -- Return callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RegisterCallback5ErrorBody](verizon/errors/register_callback5_error.py)&#93;</code>

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
<summary><code>def update_callback2(acc: str, body: FotaV3CallbackRegistrationRequest | FotaV3CallbackRegistrationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> FotaV3CallbackRegistrationResult</code></summary>

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
try:
    response = client.software_management_callbacks_v3.update_callback2(acc, body)
    # TODO: Handle 'response' of type FotaV3CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCallback2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_callbacks_v3.update_callback2(acc, body)
    # TODO: Handle 'response' of type FotaV3CallbackRegistrationResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateCallback2ErrorBody
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

**OnSuccess**: <code>[FotaV3CallbackRegistrationResult](verizon/models/fota_v3_callback_registration_result.py)</code> -- Return callback registration.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateCallback2ErrorBody](verizon/errors/update_callback2_error.py)&#93;</code>

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
<summary><code>def assign_licenses_to_devices(account: str, body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> V1LicensesAssignedRemovedResult</code></summary>

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
try:
    response = client.software_management_licenses_v1.assign_licenses_to_devices(account, body)
    # TODO: Handle 'response' of type V1LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicensesToDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v1.assign_licenses_to_devices(account, body)
    # TODO: Handle 'response' of type V1LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicensesToDevicesErrorBody
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

**OnSuccess**: <code>[V1LicensesAssignedRemovedResult](verizon/models/v1_licenses_assigned_removed_result.py)</code> -- List of licenses assigned.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AssignLicensesToDevicesErrorBody](verizon/errors/assign_licenses_to_devices_error.py)&#93;</code>

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
<summary><code>def create_list_of_licenses_to_remove(account: str, body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> V1ListOfLicensesToRemoveResult</code></summary>

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
try:
    response = client.software_management_licenses_v1.create_list_of_licenses_to_remove(account, body)
    # TODO: Handle 'response' of type V1ListOfLicensesToRemoveResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateListOfLicensesToRemoveErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v1.create_list_of_licenses_to_remove(account, body)
    # TODO: Handle 'response' of type V1ListOfLicensesToRemoveResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateListOfLicensesToRemoveErrorBody
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

**OnSuccess**: <code>[V1ListOfLicensesToRemoveResult](verizon/models/v1_list_of_licenses_to_remove_result.py)</code> -- List of licenses assigned.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateListOfLicensesToRemoveErrorBody](verizon/errors/create_list_of_licenses_to_remove_error.py)&#93;</code>

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
<summary><code>def delete_list_of_licenses_to_remove(account: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.software_management_licenses_v1.delete_list_of_licenses_to_remove(account)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteListOfLicensesToRemoveErrorBody
```

**Async**

```python
try:
    await async_client.software_management_licenses_v1.delete_list_of_licenses_to_remove(account)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteListOfLicensesToRemoveErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteListOfLicensesToRemoveErrorBody](verizon/errors/delete_list_of_licenses_to_remove_error.py)&#93;</code>

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
<summary><code>def list_licenses_to_remove(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> V1ListOfLicensesToRemove</code></summary>

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
try:
    response = client.software_management_licenses_v1.list_licenses_to_remove(account, start_index)
    # TODO: Handle 'response' of type V1ListOfLicensesToRemove
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListLicensesToRemoveErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v1.list_licenses_to_remove(account, start_index)
    # TODO: Handle 'response' of type V1ListOfLicensesToRemove
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListLicensesToRemoveErrorBody
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

**OnSuccess**: <code>[V1ListOfLicensesToRemove](verizon/models/v1_list_of_licenses_to_remove.py)</code> -- List of cancellation candidate devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListLicensesToRemoveErrorBody](verizon/errors/list_licenses_to_remove_error.py)&#93;</code>

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
<summary><code>def remove_licenses_from_devices(account: str, body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> V1LicensesAssignedRemovedResult</code></summary>

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
try:
    response = client.software_management_licenses_v1.remove_licenses_from_devices(account, body)
    # TODO: Handle 'response' of type V1LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveLicensesFromDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v1.remove_licenses_from_devices(account, body)
    # TODO: Handle 'response' of type V1LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveLicensesFromDevicesErrorBody
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

**OnSuccess**: <code>[V1LicensesAssignedRemovedResult](verizon/models/v1_licenses_assigned_removed_result.py)</code> -- List of devices with license removal status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RemoveLicensesFromDevicesErrorBody](verizon/errors/remove_licenses_from_devices_error.py)&#93;</code>

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
<summary><code>def assign_licenses_to_devices2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> V2LicensesAssignedRemovedResult</code></summary>

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
try:
    response = client.software_management_licenses_v2.assign_licenses_to_devices2(account)
    # TODO: Handle 'response' of type V2LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicensesToDevices2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v2.assign_licenses_to_devices2(account)
    # TODO: Handle 'response' of type V2LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicensesToDevices2ErrorBody
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

**OnSuccess**: <code>[V2LicensesAssignedRemovedResult](verizon/models/v2_licenses_assigned_removed_result.py)</code> -- License assignment result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AssignLicensesToDevices2ErrorBody](verizon/errors/assign_licenses_to_devices2_error.py)&#93;</code>

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
<summary><code>def create_list_of_licenses_to_remove2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> V2ListOfLicensesToRemoveResult</code></summary>

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
try:
    response = client.software_management_licenses_v2.create_list_of_licenses_to_remove2(account)
    # TODO: Handle 'response' of type V2ListOfLicensesToRemoveResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateListOfLicensesToRemove2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v2.create_list_of_licenses_to_remove2(account)
    # TODO: Handle 'response' of type V2ListOfLicensesToRemoveResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateListOfLicensesToRemove2ErrorBody
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

**OnSuccess**: <code>[V2ListOfLicensesToRemoveResult](verizon/models/v2_list_of_licenses_to_remove_result.py)</code> -- Return a created license cancellation device list.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateListOfLicensesToRemove2ErrorBody](verizon/errors/create_list_of_licenses_to_remove2_error.py)&#93;</code>

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
<summary><code>def delete_list_of_licenses_to_remove2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV2SuccessResult</code></summary>

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
try:
    response = client.software_management_licenses_v2.delete_list_of_licenses_to_remove2(account)
    # TODO: Handle 'response' of type FotaV2SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteListOfLicensesToRemove2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v2.delete_list_of_licenses_to_remove2(account)
    # TODO: Handle 'response' of type FotaV2SuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteListOfLicensesToRemove2ErrorBody
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

**OnSuccess**: <code>[FotaV2SuccessResult](verizon/models/fota_v2_success_result.py)</code> -- Result of deletion of candidate list of devices to remove.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteListOfLicensesToRemove2ErrorBody](verizon/errors/delete_list_of_licenses_to_remove2_error.py)&#93;</code>

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
<summary><code>def get_account_license_status2(account: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V2LicenseSummary</code></summary>

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
try:
    response = client.software_management_licenses_v2.get_account_license_status2(account)
    # TODO: Handle 'response' of type V2LicenseSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountLicenseStatus2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v2.get_account_license_status2(account)
    # TODO: Handle 'response' of type V2LicenseSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountLicenseStatus2ErrorBody
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

**OnSuccess**: <code>[V2LicenseSummary](verizon/models/v2_license_summary.py)</code> -- Summary of license assignment.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountLicenseStatus2ErrorBody](verizon/errors/get_account_license_status2_error.py)&#93;</code>

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
<summary><code>def list_licenses_to_remove2(account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V2ListOfLicensesToRemove</code></summary>

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
try:
    response = client.software_management_licenses_v2.list_licenses_to_remove2(account)
    # TODO: Handle 'response' of type V2ListOfLicensesToRemove
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListLicensesToRemove2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v2.list_licenses_to_remove2(account)
    # TODO: Handle 'response' of type V2ListOfLicensesToRemove
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListLicensesToRemove2ErrorBody
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

**OnSuccess**: <code>[V2ListOfLicensesToRemove](verizon/models/v2_list_of_licenses_to_remove.py)</code> -- A list of license cancellation candidate devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListLicensesToRemove2ErrorBody](verizon/errors/list_licenses_to_remove2_error.py)&#93;</code>

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
<summary><code>def remove_licenses_from_devices2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> V2LicensesAssignedRemovedResult</code></summary>

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
try:
    response = client.software_management_licenses_v2.remove_licenses_from_devices2(account)
    # TODO: Handle 'response' of type V2LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveLicensesFromDevices2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v2.remove_licenses_from_devices2(account)
    # TODO: Handle 'response' of type V2LicensesAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveLicensesFromDevices2ErrorBody
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

**OnSuccess**: <code>[V2LicensesAssignedRemovedResult](verizon/models/v2_licenses_assigned_removed_result.py)</code> -- License removal result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RemoveLicensesFromDevices2ErrorBody](verizon/errors/remove_licenses_from_devices2_error.py)&#93;</code>

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
<summary><code>def assign_licenses_to_devices3(acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> V3LicenseAssignedRemovedResult</code></summary>

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
try:
    response = client.software_management_licenses_v3.assign_licenses_to_devices3(acc, body)
    # TODO: Handle 'response' of type V3LicenseAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicensesToDevices3ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v3.assign_licenses_to_devices3(acc, body)
    # TODO: Handle 'response' of type V3LicenseAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type AssignLicensesToDevices3ErrorBody
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

**OnSuccess**: <code>[V3LicenseAssignedRemovedResult](verizon/models/v3_license_assigned_removed_result.py)</code> -- License assignment result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[AssignLicensesToDevices3ErrorBody](verizon/errors/assign_licenses_to_devices3_error.py)&#93;</code>

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
<summary><code>def get_account_licenses_status(acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V3LicenseSummary</code></summary>

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
try:
    response = client.software_management_licenses_v3.get_account_licenses_status(acc)
    # TODO: Handle 'response' of type V3LicenseSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountLicensesStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v3.get_account_licenses_status(acc)
    # TODO: Handle 'response' of type V3LicenseSummary
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountLicensesStatusErrorBody
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

**OnSuccess**: <code>[V3LicenseSummary](verizon/models/v3_license_summary.py)</code> -- Summary of license assignment.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountLicensesStatusErrorBody](verizon/errors/get_account_licenses_status_error.py)&#93;</code>

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
<summary><code>def remove_licenses_from_devices3(acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None) -> V3LicenseAssignedRemovedResult</code></summary>

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
try:
    response = client.software_management_licenses_v3.remove_licenses_from_devices3(acc, body)
    # TODO: Handle 'response' of type V3LicenseAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveLicensesFromDevices3ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_licenses_v3.remove_licenses_from_devices3(acc, body)
    # TODO: Handle 'response' of type V3LicenseAssignedRemovedResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RemoveLicensesFromDevices3ErrorBody
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

**OnSuccess**: <code>[V3LicenseAssignedRemovedResult](verizon/models/v3_license_assigned_removed_result.py)</code> -- License removal result.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RemoveLicensesFromDevices3ErrorBody](verizon/errors/remove_licenses_from_devices3_error.py)&#93;</code>

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
<summary><code>def get_device_firmware_upgrade_history(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceUpgradeHistory]</code></summary>

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
try:
    response = client.software_management_reports_v1.get_device_firmware_upgrade_history(account, device_id)
    # TODO: Handle 'response' of type list[DeviceUpgradeHistory]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceFirmwareUpgradeHistoryErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v1.get_device_firmware_upgrade_history(account, device_id)
    # TODO: Handle 'response' of type list[DeviceUpgradeHistory]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceFirmwareUpgradeHistoryErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceUpgradeHistory](verizon/models/device_upgrade_history.py)&#93;</code> -- Device upgrade history.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceFirmwareUpgradeHistoryErrorBody](verizon/errors/get_device_firmware_upgrade_history_error.py)&#93;</code>

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
<summary><code>def list_account_devices(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceListQueryResult</code></summary>

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
try:
    response = client.software_management_reports_v1.list_account_devices(account, start_index)
    # TODO: Handle 'response' of type DeviceListQueryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountDevicesErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v1.list_account_devices(account, start_index)
    # TODO: Handle 'response' of type DeviceListQueryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountDevicesErrorBody
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

**OnSuccess**: <code>[DeviceListQueryResult](verizon/models/device_list_query_result.py)</code> -- List of all devices in the specified account.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountDevicesErrorBody](verizon/errors/list_account_devices_error.py)&#93;</code>

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
<summary><code>def list_upgrades_for_specified_status(account: str, upgrade_status: UpgradeStatusOrStr, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> UpgradeListQueryResult</code></summary>

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
try:
    response = client.software_management_reports_v1.list_upgrades_for_specified_status(
        account, upgrade_status, start_index
    )
    # TODO: Handle 'response' of type UpgradeListQueryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListUpgradesForSpecifiedStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v1.list_upgrades_for_specified_status(
        account, upgrade_status, start_index
    )
    # TODO: Handle 'response' of type UpgradeListQueryResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListUpgradesForSpecifiedStatusErrorBody
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

**OnSuccess**: <code>[UpgradeListQueryResult](verizon/models/upgrade_list_query_result.py)</code> -- A list of all upgrades with a specified status.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListUpgradesForSpecifiedStatusErrorBody](verizon/errors/list_upgrades_for_specified_status_error.py)&#93;</code>

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
<summary><code>def get_campaign_device_status(account: str, campaign_id: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V2CampaignDevice</code></summary>

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
try:
    response = client.software_management_reports_v2.get_campaign_device_status(account, campaign_id)
    # TODO: Handle 'response' of type V2CampaignDevice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignDeviceStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v2.get_campaign_device_status(account, campaign_id)
    # TODO: Handle 'response' of type V2CampaignDevice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignDeviceStatusErrorBody
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

**OnSuccess**: <code>[V2CampaignDevice](verizon/models/v2_campaign_device.py)</code> -- Return list of campaign history.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCampaignDeviceStatusErrorBody](verizon/errors/get_campaign_device_status_error.py)&#93;</code>

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
<summary><code>def get_campaign_history_by_status(account: str, campaign_status: str, *, last_seen_campaign_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V2CampaignHistory</code></summary>

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
try:
    response = client.software_management_reports_v2.get_campaign_history_by_status(account, campaign_status)
    # TODO: Handle 'response' of type V2CampaignHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignHistoryByStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v2.get_campaign_history_by_status(
        account, campaign_status
    )
    # TODO: Handle 'response' of type V2CampaignHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignHistoryByStatusErrorBody
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

**OnSuccess**: <code>[V2CampaignHistory](verizon/models/v2_campaign_history.py)</code> -- Return list of campaign history.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCampaignHistoryByStatusErrorBody](verizon/errors/get_campaign_history_by_status_error.py)&#93;</code>

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
<summary><code>def get_device_firmware_upgrade_history2(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceSoftwareUpgrade]</code></summary>

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
try:
    response = client.software_management_reports_v2.get_device_firmware_upgrade_history2(account, device_id)
    # TODO: Handle 'response' of type list[DeviceSoftwareUpgrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceFirmwareUpgradeHistory2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v2.get_device_firmware_upgrade_history2(
        account, device_id
    )
    # TODO: Handle 'response' of type list[DeviceSoftwareUpgrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceFirmwareUpgradeHistory2ErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceSoftwareUpgrade](verizon/models/device_software_upgrade.py)&#93;</code> -- Return array of upgrades.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceFirmwareUpgradeHistory2ErrorBody](verizon/errors/get_device_firmware_upgrade_history2_error.py)&#93;</code>

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
<summary><code>def list_account_devices2(account: str, *, last_seen_device_id: str | None = None, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V2AccountDeviceList</code></summary>

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
try:
    response = client.software_management_reports_v2.list_account_devices2(account)
    # TODO: Handle 'response' of type V2AccountDeviceList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountDevices2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v2.list_account_devices2(account)
    # TODO: Handle 'response' of type V2AccountDeviceList
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAccountDevices2ErrorBody
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

**OnSuccess**: <code>[V2AccountDeviceList](verizon/models/v2_account_device_list.py)</code> -- Return array of devices.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAccountDevices2ErrorBody](verizon/errors/list_account_devices2_error.py)&#93;</code>

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
<summary><code>def list_available_software(account: str, *, distribution_type: str | None = None, request_options: RequestOptionsOrDict | None = None) -> list[SoftwarePackage]</code></summary>

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
try:
    response = client.software_management_reports_v2.list_available_software(account)
    # TODO: Handle 'response' of type list[SoftwarePackage]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAvailableSoftwareErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v2.list_available_software(account)
    # TODO: Handle 'response' of type list[SoftwarePackage]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type ListAvailableSoftwareErrorBody
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

**OnSuccess**: <code>list&#91;[SoftwarePackage](verizon/models/software_package.py)&#93;</code> -- Return array of software.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[ListAvailableSoftwareErrorBody](verizon/errors/list_available_software_error.py)&#93;</code>

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
<summary><code>def get_campaign_device_status2(acc: str, campaign_id: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V3CampaignDevice</code></summary>

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
try:
    response = client.software_management_reports_v3.get_campaign_device_status2(acc, campaign_id)
    # TODO: Handle 'response' of type V3CampaignDevice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignDeviceStatus2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v3.get_campaign_device_status2(acc, campaign_id)
    # TODO: Handle 'response' of type V3CampaignDevice
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignDeviceStatus2ErrorBody
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

**OnSuccess**: <code>[V3CampaignDevice](verizon/models/v3_campaign_device.py)</code> -- Returns an array of campaign history.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCampaignDeviceStatus2ErrorBody](verizon/errors/get_campaign_device_status2_error.py)&#93;</code>

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
<summary><code>def get_campaign_history_by_status2(acc: str, campaign_status: CampaignStatusOrStr, *, last_seen_campaign_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> V3CampaignHistory</code></summary>

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
try:
    response = client.software_management_reports_v3.get_campaign_history_by_status2(acc, campaign_status)
    # TODO: Handle 'response' of type V3CampaignHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignHistoryByStatus2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v3.get_campaign_history_by_status2(acc, campaign_status)
    # TODO: Handle 'response' of type V3CampaignHistory
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetCampaignHistoryByStatus2ErrorBody
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

**OnSuccess**: <code>[V3CampaignHistory](verizon/models/v3_campaign_history.py)</code> -- Return array of campaign history.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetCampaignHistoryByStatus2ErrorBody](verizon/errors/get_campaign_history_by_status2_error.py)&#93;</code>

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
<summary><code>def get_device_firmware_upgrade_history3(acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceFirmwareUpgrade]</code></summary>

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
try:
    response = client.software_management_reports_v3.get_device_firmware_upgrade_history3(acc, device_id)
    # TODO: Handle 'response' of type list[DeviceFirmwareUpgrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceFirmwareUpgradeHistory3ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_reports_v3.get_device_firmware_upgrade_history3(acc, device_id)
    # TODO: Handle 'response' of type list[DeviceFirmwareUpgrade]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetDeviceFirmwareUpgradeHistory3ErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceFirmwareUpgrade](verizon/models/device_firmware_upgrade.py)&#93;</code> -- Returns a list of firmware upgrades.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetDeviceFirmwareUpgradeHistory3ErrorBody](verizon/errors/get_device_firmware_upgrade_history3_error.py)&#93;</code>

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
<summary><code>def get_account_license_status(account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None) -> AccountLicenseInfo</code></summary>

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
try:
    response = client.software_management_subscriptions_v1.get_account_license_status(account, start_index)
    # TODO: Handle 'response' of type AccountLicenseInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountLicenseStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_subscriptions_v1.get_account_license_status(account, start_index)
    # TODO: Handle 'response' of type AccountLicenseInfo
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountLicenseStatusErrorBody
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

**OnSuccess**: <code>[AccountLicenseInfo](verizon/models/account_license_info.py)</code> -- Account license information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountLicenseStatusErrorBody](verizon/errors/get_account_license_status_error.py)&#93;</code>

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
<summary><code>def get_account_subscription_status(account: str, *, request_options: RequestOptionsOrDict | None = None) -> V1AccountSubscription</code></summary>

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
try:
    response = client.software_management_subscriptions_v1.get_account_subscription_status(account)
    # TODO: Handle 'response' of type V1AccountSubscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountSubscriptionStatusErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_subscriptions_v1.get_account_subscription_status(account)
    # TODO: Handle 'response' of type V1AccountSubscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountSubscriptionStatusErrorBody
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

**OnSuccess**: <code>[V1AccountSubscription](verizon/models/v1_account_subscription.py)</code> -- Account subscription information.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountSubscriptionStatusErrorBody](verizon/errors/get_account_subscription_status_error.py)&#93;</code>

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
<summary><code>def get_account_subscription_status2(account: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV2Subscription</code></summary>

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
try:
    response = client.software_management_subscriptions_v2.get_account_subscription_status2(account)
    # TODO: Handle 'response' of type FotaV2Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountSubscriptionStatus2ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_subscriptions_v2.get_account_subscription_status2(account)
    # TODO: Handle 'response' of type FotaV2Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountSubscriptionStatus2ErrorBody
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

**OnSuccess**: <code>[FotaV2Subscription](verizon/models/fota_v2_subscription.py)</code> -- FOTA Subscription.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountSubscriptionStatus2ErrorBody](verizon/errors/get_account_subscription_status2_error.py)&#93;</code>

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
<summary><code>def get_account_subscription_status3(acc: str, *, request_options: RequestOptionsOrDict | None = None) -> FotaV3Subscription</code></summary>

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
try:
    response = client.software_management_subscriptions_v3.get_account_subscription_status3(acc)
    # TODO: Handle 'response' of type FotaV3Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountSubscriptionStatus3ErrorBody
```

**Async**

```python
try:
    response = await async_client.software_management_subscriptions_v3.get_account_subscription_status3(acc)
    # TODO: Handle 'response' of type FotaV3Subscription
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAccountSubscriptionStatus3ErrorBody
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

**OnSuccess**: <code>[FotaV3Subscription](verizon/models/fota_v3_subscription.py)</code> -- FOTA Subscription.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAccountSubscriptionStatus3ErrorBody](verizon/errors/get_account_subscription_status3_error.py)&#93;</code>

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
<summary><code>def create_azure_central_io_t_application(billingaccount_id: str, body: CreateIoTapplicationRequest | CreateIoTapplicationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> CreateIoTapplicationResponse</code></summary>

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
try:
    response = client.targets.create_azure_central_io_t_application(billingaccount_id, body)
    # TODO: Handle 'response' of type CreateIoTapplicationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.targets.create_azure_central_io_t_application(billingaccount_id, body)
    # TODO: Handle 'response' of type CreateIoTapplicationResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[CreateIoTapplicationResponse](verizon/models/create_io_tapplication_response.py)</code> -- A success response includes the full subscription resource definition.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_target(body: CreateTargetRequest | CreateTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Target</code></summary>

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
try:
    response = client.targets.create_target(body)
    # TODO: Handle 'response' of type Target
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.targets.create_target(body)
    # TODO: Handle 'response' of type Target
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[Target](verizon/models/target.py)</code> -- A success response includes the full target resource definition.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_target(body: DeleteTargetRequest | DeleteTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.targets.delete_target(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    await async_client.targets.delete_target(body)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def generate_target_external_id(body: GenerateExternalIdrequest | GenerateExternalIdrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> GenerateExternalIdresult</code></summary>

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
try:
    response = client.targets.generate_target_external_id(body)
    # TODO: Handle 'response' of type GenerateExternalIdresult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.targets.generate_target_external_id(body)
    # TODO: Handle 'response' of type GenerateExternalIdresult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[GenerateExternalIdresult](verizon/models/generate_external_idresult.py)</code> -- Returns a new external ID.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def query_target(body: QueryTargetRequest | QueryTargetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[Target]</code></summary>

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
try:
    response = client.targets.query_target(body)
    # TODO: Handle 'response' of type list[Target]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.targets.query_target(body)
    # TODO: Handle 'response' of type list[Target]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>list&#91;[Target](verizon/models/target.py)&#93;</code> -- A success response includes an array of all matching targets. Each target includes the full target resource definition.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## ThingSpaceQualityOfServiceApiActions

> Source: [ThingSpaceQualityOfServiceApiActions](verizon/apis/thing_space_quality_of_service_api_actions.py)

<details>
<summary><code>def create_a_thing_space_quality_of_service_api_subscription(body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> Success201</code></summary>

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
try:
    response = client.thing_space_quality_of_service_api_actions.create_a_thing_space_quality_of_service_api_subscription(
        body
    )
    # TODO: Handle 'response' of type Success201
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.thing_space_quality_of_service_api_actions.create_a_thing_space_quality_of_service_api_subscription(
        body
    )
    # TODO: Handle 'response' of type Success201
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[Success201](verizon/models/success201.py)</code> -- Success Response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def stop_a_thing_space_quality_of_service_api_subscription(account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Success201</code></summary>

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
try:
    response = client.thing_space_quality_of_service_api_actions.stop_a_thing_space_quality_of_service_api_subscription(
        account_name, qos_subscription_id
    )
    # TODO: Handle 'response' of type Success201
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.thing_space_quality_of_service_api_actions.stop_a_thing_space_quality_of_service_api_subscription(
        account_name, qos_subscription_id
    )
    # TODO: Handle 'response' of type Success201
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[Success201](verizon/models/success201.py)</code> -- Success Response

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UpdatePricePlanTriggers

> Source: [UpdatePricePlanTriggers](verizon/apis/update_price_plan_triggers.py)

<details>
<summary><code>def update_trigger_rules(body: V2TriggersRequest1 | V2TriggersRequest1Dict, *, request_options: RequestOptionsOrDict | None = None) -> TriggerResponse</code></summary>

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
try:
    response = client.update_price_plan_triggers.update_trigger_rules(body)
    # TODO: Handle 'response' of type TriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.update_price_plan_triggers.update_trigger_rules(body)
    # TODO: Handle 'response' of type TriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[TriggerResponse](verizon/models/trigger_response.py)</code> -- Successful request

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UpdateTriggers

> Source: [UpdateTriggers](verizon/apis/update_triggers.py)

<details>
<summary><code>def update_all_available_triggers(*, body: RequestTrigger | RequestTriggerDict | None = None, request_options: RequestOptionsOrDict | None = None) -> SuccessModel</code></summary>

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
try:
    response = client.update_triggers.update_all_available_triggers()
    # TODO: Handle 'response' of type SuccessModel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.update_triggers.update_all_available_triggers()
    # TODO: Handle 'response' of type SuccessModel
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[SuccessModel](verizon/models/success_model.py)</code> -- Status of Request

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## UsageTriggerManagement

> Source: [UsageTriggerManagement](verizon/apis/usage_trigger_management.py)

<details>
<summary><code>def create_new_trigger(*, body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UsageTriggerResponse</code></summary>

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
try:
    response = client.usage_trigger_management.create_new_trigger()
    # TODO: Handle 'response' of type UsageTriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateNewTriggerErrorBody
```

**Async**

```python
try:
    response = await async_client.usage_trigger_management.create_new_trigger()
    # TODO: Handle 'response' of type UsageTriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type CreateNewTriggerErrorBody
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

**OnSuccess**: <code>[UsageTriggerResponse](verizon/models/usage_trigger_response.py)</code> -- Usage trigger Add result

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[CreateNewTriggerErrorBody](verizon/errors/create_new_trigger_error.py)&#93;</code>

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
<summary><code>def delete_trigger(account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None) -> DeviceLocationSuccessResult</code></summary>

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
try:
    response = client.usage_trigger_management.delete_trigger(account_name, trigger_id)
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteTriggerErrorBody
```

**Async**

```python
try:
    response = await async_client.usage_trigger_management.delete_trigger(account_name, trigger_id)
    # TODO: Handle 'response' of type DeviceLocationSuccessResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteTriggerErrorBody
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

**OnSuccess**: <code>[DeviceLocationSuccessResult](verizon/models/device_location_success_result.py)</code> -- Delete result

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteTriggerErrorBody](verizon/errors/delete_trigger_error.py)&#93;</code>

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
<summary><code>def update_trigger(trigger_id: str, *, body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None, request_options: RequestOptionsOrDict | None = None) -> UsageTriggerResponse</code></summary>

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
try:
    response = client.usage_trigger_management.update_trigger(trigger_id)
    # TODO: Handle 'response' of type UsageTriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateTriggerErrorBody
```

**Async**

```python
try:
    response = await async_client.usage_trigger_management.update_trigger(trigger_id)
    # TODO: Handle 'response' of type UsageTriggerResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type UpdateTriggerErrorBody
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

**OnSuccess**: <code>[UsageTriggerResponse](verizon/models/usage_trigger_response.py)</code> -- Usage trigger Modify result

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[UpdateTriggerErrorBody](verizon/errors/update_trigger_error.py)&#93;</code>

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
<summary><code>def device_experience30days_history(body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WnprequestResponse</code></summary>

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
try:
    response = client.wireless_network_performance.device_experience30days_history(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wireless_network_performance.device_experience30days_history(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def device_experience_bulk_latest(body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WnprequestResponse</code></summary>

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
try:
    response = client.wireless_network_performance.device_experience_bulk_latest(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wireless_network_performance.device_experience_bulk_latest(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def domestic4_g_and5_g_nationwide_network_coverage(body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WnprequestResponse</code></summary>

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
try:
    response = client.wireless_network_performance.domestic4_g_and5_g_nationwide_network_coverage(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wireless_network_performance.domestic4_g_and5_g_nationwide_network_coverage(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def near_real_time_network_conditions(body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WnprequestResponse</code></summary>

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
try:
    response = client.wireless_network_performance.near_real_time_network_conditions(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wireless_network_performance.near_real_time_network_conditions(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def site_proximity(body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> WnprequestResponse</code></summary>

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
try:
    response = client.wireless_network_performance.site_proximity(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
```

**Async**

```python
try:
    response = await async_client.wireless_network_performance.site_proximity(body)
    # TODO: Handle 'response' of type WnprequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type RawError
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

**OnSuccess**: <code>[WnprequestResponse](verizon/models/wnprequest_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[RawError](verizon/core/results.py)&#93;</code>

</dd>
</dl>

</dd>
</dl>

</details>

## DeviceRoleController

> Source: [DeviceRoleController](verizon/apis/device_role_controller.py)

<details>
<summary><code>def get_acl_rules_by_vendor_id(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> list[DeviceRole]</code></summary>

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
try:
    response = client.device_role_controller.get_acl_rules_by_vendor_id(vendor_id)
    # TODO: Handle 'response' of type list[DeviceRole]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAclrulesByVendorIdErrorBody
```

**Async**

```python
try:
    response = await async_client.device_role_controller.get_acl_rules_by_vendor_id(vendor_id)
    # TODO: Handle 'response' of type list[DeviceRole]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type GetAclrulesByVendorIdErrorBody
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

**OnSuccess**: <code>list&#91;[DeviceRole](verizon/models/device_role.py)&#93;</code> -- List of Access Rules

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[GetAclrulesByVendorIdErrorBody](verizon/errors/get_aclrules_by_vendor_id_error.py)&#93;</code>

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
<summary><code>def delete_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.e_uicc_device_profile_management.delete_local_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteLocalProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.e_uicc_device_profile_management.delete_local_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteLocalProfileErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteLocalProfileErrorBody](verizon/errors/delete_local_profile_error.py)&#93;</code>

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
<summary><code>def disable_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.e_uicc_device_profile_management.disable_local_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableLocalProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.e_uicc_device_profile_management.disable_local_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DisableLocalProfileErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DisableLocalProfileErrorBody](verizon/errors/disable_local_profile_error.py)&#93;</code>

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
<summary><code>def download_local_profile_to_disable(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.e_uicc_device_profile_management.download_local_profile_to_disable(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadLocalProfileToDisableErrorBody
```

**Async**

```python
try:
    response = await async_client.e_uicc_device_profile_management.download_local_profile_to_disable(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadLocalProfileToDisableErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DownloadLocalProfileToDisableErrorBody](verizon/errors/download_local_profile_to_disable_error.py)&#93;</code>

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
<summary><code>def download_local_profile_to_enable(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> DeviceManagementResult</code></summary>

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
try:
    response = client.e_uicc_device_profile_management.download_local_profile_to_enable(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadLocalProfileToEnableErrorBody
```

**Async**

```python
try:
    response = await async_client.e_uicc_device_profile_management.download_local_profile_to_enable(body)
    # TODO: Handle 'response' of type DeviceManagementResult
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadLocalProfileToEnableErrorBody
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

**OnSuccess**: <code>[DeviceManagementResult](verizon/models/device_management_result.py)</code> -- Request ID received on a successful response.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DownloadLocalProfileToEnableErrorBody](verizon/errors/download_local_profile_to_enable_error.py)&#93;</code>

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
<summary><code>def enable_local_profile(body: ProfileChangeStateRequest | ProfileChangeStateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> RequestResponse</code></summary>

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
try:
    response = client.e_uicc_device_profile_management.enable_local_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableLocalProfileErrorBody
```

**Async**

```python
try:
    response = await async_client.e_uicc_device_profile_management.enable_local_profile(body)
    # TODO: Handle 'response' of type RequestResponse
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type EnableLocalProfileErrorBody
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

**OnSuccess**: <code>[RequestResponse](verizon/models/request_response.py)</code> -- Request ID

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[EnableLocalProfileErrorBody](verizon/errors/enable_local_profile_error.py)&#93;</code>

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
<summary><code>def delete_map_message(region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None) -> None</code></summary>

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
try:
    client.map_message_controller.delete_map_message(region_id, i10nid)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMapMessageErrorBody
```

**Async**

```python
try:
    await async_client.map_message_controller.delete_map_message(region_id, i10nid)
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DeleteMapMessageErrorBody
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

**OnSuccess**: No content

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DeleteMapMessageErrorBody](verizon/errors/delete_map_message_error.py)&#93;</code>

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
<summary><code>def download_map_messages(geofence: GeofencePolygon | GeofencePolygonDict, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.map_message_controller.download_map_messages(geofence, vendor_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadMapmessagesErrorBody
```

**Async**

```python
try:
    response = await async_client.map_message_controller.download_map_messages(geofence, vendor_id)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type DownloadMapmessagesErrorBody
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

**OnSuccess**: <code>str</code> -- Line separated ASN.1 UPER J2735/ETSI base64 encoded MapData messages

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[DownloadMapmessagesErrorBody](verizon/errors/download_mapmessages_error.py)&#93;</code>

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
<summary><code>def ingest_map_messages(vendor_id: str, map_data_message_standard: EtxmessageStandardEnumOrStr, body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> str</code></summary>

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
try:
    response = client.map_message_controller.ingest_map_messages(vendor_id, map_data_message_standard, body)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IngestMapmessagesErrorBody
```

**Async**

```python
try:
    response = await async_client.map_message_controller.ingest_map_messages(vendor_id, map_data_message_standard, body)
    # TODO: Handle 'response' of type str
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type IngestMapmessagesErrorBody
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

**OnSuccess**: <code>str</code> -- Map message/s successfully uploaded

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[IngestMapmessagesErrorBody](verizon/errors/ingest_mapmessages_error.py)&#93;</code>

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
<summary><code>def query_map_messages(vendor_id: str, body: MapDataQueryRequest | MapDataQueryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> list[Any]</code></summary>

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
try:
    response = client.map_message_controller.query_map_messages(vendor_id, body)
    # TODO: Handle 'response' of type list[Any]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMapMessagesErrorBody
```

**Async**

```python
try:
    response = await async_client.map_message_controller.query_map_messages(vendor_id, body)
    # TODO: Handle 'response' of type list[Any]
except ApiError as e:
    ...  # TODO: Handle 'e.error' of type QueryMapMessagesErrorBody
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

**OnSuccess**: <code>list&#91;Any&#93;</code> -- Successfully retrieved MAP messages. Returns a JSON array where each element contains either a base64 string or parsed message object.

**OnError**: <code>[ApiError](verizon/core/exceptions.py)&#91;[QueryMapMessagesErrorBody](verizon/errors/query_map_messages_error.py)&#93;</code>

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

