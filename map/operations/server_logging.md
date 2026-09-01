<!-- Generated file — do not edit; regenerated with the SDK. -->

# ServerLogging — operations

Accessor: `client.server_logging` · Source: `verizon/apis/server_logging.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.server_logging.get_device_check_in_history

- **Route**: `GET /logging/{account}/devices/{deviceId}/checkInHistory`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_device_check_in_history(account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account`, `device_id`
- **Params**: `account` — path · `device_id` — path `deviceId`
- **Returns (parsed)**: `list[CheckInHistoryItem]`
- **Returns (raw)**: `ApiResult[list[CheckInHistoryItem], GetDeviceCheckInHistoryErrorBody]`
- **Error**: `GetDeviceCheckInHistoryErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CheckInHistoryItem` | `verizon/models/check_in_history_item.py` |
| `GetDeviceCheckInHistoryErrorBody` | `verizon/errors/get_device_check_in_history_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

