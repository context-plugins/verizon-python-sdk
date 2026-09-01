<!-- Generated file — do not edit; regenerated with the SDK. -->

# DeviceCredentialManagement — operations

Accessor: `client.device_credential_management` · Source: `verizon/apis/device_credential_management.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.device_credential_management.drop_credentials

- **Route**: `POST /credentials/drop`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def drop_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DropResponse`
- **Returns (raw)**: `ApiResult[DropResponse, DropCredentialsErrorBody]`
- **Error**: `DropCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CredentialsRequest` | `verizon/models/credentials_request.py` |
| `CredentialsRequestDict` | `verizon/models/credentials_request.py` |
| `DropResponse` | `verizon/models/drop_response.py` |
| `DropCredentialsErrorBody` | `verizon/errors/drop_credentials_error.py` |
| `ErrorResponse` | `verizon/models/error_response.py` |

### client.device_credential_management.generate_credentials

- **Route**: `POST /credentials/generate`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def generate_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenerateResponse`
- **Returns (raw)**: `ApiResult[GenerateResponse, GenerateCredentialsErrorBody]`
- **Error**: `GenerateCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CredentialsRequest` | `verizon/models/credentials_request.py` |
| `CredentialsRequestDict` | `verizon/models/credentials_request.py` |
| `GenerateResponse` | `verizon/models/generate_response.py` |
| `GenerateCredentialsErrorBody` | `verizon/errors/generate_credentials_error.py` |
| `ErrorResponse` | `verizon/models/error_response.py` |

### client.device_credential_management.reset_credentials

- **Route**: `POST /credentials/reset`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def reset_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `GenerateResponse`
- **Returns (raw)**: `ApiResult[GenerateResponse, ResetCredentialsErrorBody]`
- **Error**: `ResetCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `CredentialsRequest` | `verizon/models/credentials_request.py` |
| `CredentialsRequestDict` | `verizon/models/credentials_request.py` |
| `GenerateResponse` | `verizon/models/generate_response.py` |
| `ResetCredentialsErrorBody` | `verizon/errors/reset_credentials_error.py` |
| `ErrorResponse` | `verizon/models/error_response.py` |

### client.device_credential_management.retrieve_credentials

- **Route**: `POST /credentials/retrieve`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `hyper_precise_credentials`
- **Signature**: `def retrieve_credentials(body: CredentialsRequest | CredentialsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RetrieveResponse`
- **Returns (raw)**: `ApiResult[RetrieveResponse, RetrieveCredentialsErrorBody]`
- **Error**: `RetrieveCredentialsErrorBody` — **Case A (typed)**
- **Error arms**: `ErrorResponse` [400] · `RawError` [401, anything unmapped]

| Type | Source |
| --- | --- |
| `CredentialsRequest` | `verizon/models/credentials_request.py` |
| `CredentialsRequestDict` | `verizon/models/credentials_request.py` |
| `RetrieveResponse` | `verizon/models/retrieve_response.py` |
| `RetrieveCredentialsErrorBody` | `verizon/errors/retrieve_credentials_error.py` |
| `ErrorResponse` | `verizon/models/error_response.py` |

