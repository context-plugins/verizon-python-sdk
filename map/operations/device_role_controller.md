<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceRoleController — operations

Accessor: `client.device_role_controller` · Source: `verizon/apis/device_role_controller.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_role_controller.get_acl_rules_by_vendor_id

- **Route**: `GET /api/v1/device-roles/vendor`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def get_acl_rules_by_vendor_id(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`
- **Params**: `vendor_id` — query `VendorID`
- **Returns (parsed)**: `list[DeviceRole]`
- **Returns (raw)**: `ApiResult[list[DeviceRole], GetAclrulesByVendorIdErrorBody]`
- **Error**: `GetAclrulesByVendorIdErrorBody` — **Case A (typed)**
- **Error arms**: `str` [400, 401, 403, 406, 429] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DeviceRole` | `verizon/models/device_role.py` |
| `GetAclrulesByVendorIdErrorBody` | `verizon/errors/get_aclrules_by_vendor_id_error.py` |

