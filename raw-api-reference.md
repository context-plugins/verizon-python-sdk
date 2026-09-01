# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [ApiEndpointsFor5GBusinessInternet5GBiClient](api_endpoints_for_5_g_business_internet_5_g_bi/client.py)

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
result = client.with_raw_response.business_internet_serviceplanchange(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbiRequestResponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.business_internet_serviceplanchange(body)
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
| <code>body</code> | <code>[GbichangeRequest5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbichange_request5.py) \| [GbichangeRequest5Dict](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbichange_request5.py)</code> | This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service plan can change for an active device up to four times per month but will require address validation for each change. The service plan cannot be changed for a device while its service is suspended. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_endpoints_for_5_g_business_internet_5_g_bi/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)&#91;[GbiRequestResponse5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbi_request_response5.py), [RawError](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GbiRequestResponse5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbi_request_response5.py)</code> -- A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

**On `Failure`**: `error` is <code>[RawError](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)</code>

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
result = client.with_raw_response.business_internetactivate_using_post(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbiRequestResponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.business_internetactivate_using_post(body)
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
| <code>body</code> | <code>[GbiactivateRequest5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbiactivate_request5.py) \| [GbiactivateRequest5Dict](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbiactivate_request5.py)</code> | Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is required for activating as Public Static. Leave  <code>publicIpRestriction</code> undefined to activate as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile Private Network (MPN). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_endpoints_for_5_g_business_internet_5_g_bi/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)&#91;[GbiRequestResponse5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbi_request_response5.py), [RawError](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GbiRequestResponse5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbi_request_response5.py)</code> -- A request ID is returned as a successful response. Use a callback to see the details associated with the request ID.

**On `Failure`**: `error` is <code>[RawError](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)</code>

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
result = client.with_raw_response.business_internetlist_device_information(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GbideviceDetailsresponse5
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.with_raw_response.business_internetlist_device_information(body)
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
| <code>body</code> | <code>[GbideviceId5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_id5.py) \| [GbideviceId5Dict](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_id5.py)</code> | Device Profile Query |
| <code>request_options</code> | <code>[RequestOptionsOrDict](api_endpoints_for_5_g_business_internet_5_g_bi/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)&#91;[GbideviceDetailsresponse5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_detailsresponse5.py), [RawError](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GbideviceDetailsresponse5](api_endpoints_for_5_g_business_internet_5_g_bi/models/gbidevice_detailsresponse5.py)</code> -- The device's details will be returned from a successful request.

**On `Failure`**: `error` is <code>[RawError](api_endpoints_for_5_g_business_internet_5_g_bi/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

