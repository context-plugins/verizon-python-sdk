<!-- Generated file — do not edit; regenerated with the SDK. -->

# AccountServiceController — operations

Accessor: `client.account_service_controller` · Source: `verizon/apis/account_service_controller.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.account_service_controller.get_account_information_using_get

- **Route**: `GET /v1/accounts/{accountName}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def get_account_information_using_get(account_name: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_name`
- **Params**: `account_name` — path `accountName`
- **Returns (parsed)**: `GetAccountInformationResponseforplanner`
- **Returns (raw)**: `ApiResult[GetAccountInformationResponseforplanner, GetAccountInformationUsingGetErrorBody]`
- **Error**: `GetAccountInformationUsingGetErrorBody` — **Case A (typed)**
- **Error arms**: `RestErrorResponseforplanner` [400, 403, 404, 406, 429] · `AuthRestErrorResponseforplanner` [401] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `GetAccountInformationResponseforplanner` | `verizon/models/get_account_information_responseforplanner.py` |
| `GetAccountInformationUsingGetErrorBody` | `verizon/errors/get_account_information_using_get_error.py` |
| `RestErrorResponseforplanner` | `verizon/models/rest_error_responseforplanner.py` |
| `AuthRestErrorResponseforplanner` | `verizon/models/auth_rest_error_responseforplanner.py` |

