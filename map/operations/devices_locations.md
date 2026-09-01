<!-- Generated file — do not edit; regenerated with the SDK. -->

# DevicesLocations — operations

Accessor: `client.devices_locations` · Source: `verizon/apis/devices_locations.py` · 6 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.devices_locations.cancel_queued_location_report_generation

- **Route**: `DELETE /locationreports/{accountName}/report/{txid}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def cancel_queued_location_report_generation(account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `txid`
- **Params**: `account_name` — path `accountName` · `txid` — path
- **Returns (parsed)**: `TransactionId`
- **Returns (raw)**: `ApiResult[TransactionId, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TransactionId` | `verizon/models/transaction_id.py` |

### client.devices_locations.create_location_report

- **Route**: `POST /locationreports`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def create_location_report(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `AsynchronousLocationRequestResult`
- **Returns (raw)**: `ApiResult[AsynchronousLocationRequestResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AsynchronousLocationRequestResult` | `verizon/models/asynchronous_location_request_result.py` |

### client.devices_locations.get_location_report_status

- **Route**: `GET /locationreports/{accountName}/report/{txid}/status`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def get_location_report_status(account_name: str, txid: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `txid`
- **Params**: `account_name` — path `accountName` · `txid` — path
- **Returns (parsed)**: `LocationReportStatus`
- **Returns (raw)**: `ApiResult[LocationReportStatus, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LocationReportStatus` | `verizon/models/location_report_status.py` |

### client.devices_locations.list_devices_locations_asynchronous

- **Route**: `POST /devicelocations`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def list_devices_locations_asynchronous(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `SynchronousLocationRequestResult`
- **Returns (raw)**: `ApiResult[SynchronousLocationRequestResult, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SynchronousLocationRequestResult` | `verizon/models/synchronous_location_request_result.py` |

### client.devices_locations.list_devices_locations_synchronous

- **Route**: `POST /locations`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def list_devices_locations_synchronous(body: LocationRequest | LocationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `list[Location]`
- **Returns (raw)**: `ApiResult[list[Location], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LocationRequest` | `verizon/models/location_request.py` |
| `LocationRequestDict` | `verizon/models/location_request.py` |
| `Location` | `verizon/models/location.py` |

### client.devices_locations.retrieve_location_report

- **Route**: `GET /locationreports/{accountName}/report/{txid}/index/{startindex}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `device_location`
- **Signature**: `def retrieve_location_report(account_name: str, txid: str, startindex: int, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`, `txid`, `startindex`
- **Params**: `account_name` — path `accountName` · `txid` — path · `startindex` — path
- **Returns (parsed)**: `LocationReport`
- **Returns (raw)**: `ApiResult[LocationReport, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LocationReport` | `verizon/models/location_report.py` |

