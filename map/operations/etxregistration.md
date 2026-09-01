<!-- Generated file — do not edit; regenerated with the SDK. -->

# Etxregistration — operations

Accessor: `client.etxregistration` · Source: `verizon/apis/etxregistration.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.etxregistration.get_etx_client_certificate

- **Route**: `GET /api/v2/clients/registration`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def get_etx_client_certificate(id: EtxclientIdlookup | EtxclientIdlookupDict, vendor_id: str, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `vendor_id`
- **Params**: `id` — query `ID` · `vendor_id` — header `VendorID` · `x_transaction_id` — header `X-Transaction-Id`
- **Returns (parsed)**: `ClientPersistenceResponse`
- **Returns (raw)**: `ApiResult[ClientPersistenceResponse, GetEtxclientCertificateErrorBody]`
- **Error**: `GetEtxclientCertificateErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 403, 404, 429, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `EtxclientIdlookup` | `verizon/models/etxclient_idlookup.py` |
| `EtxclientIdlookupDict` | `verizon/models/etxclient_idlookup.py` |
| `ClientPersistenceResponse` | `verizon/models/client_persistence_response.py` |
| `GetEtxclientCertificateErrorBody` | `verizon/errors/get_etxclient_certificate_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

### client.etxregistration.get_etx_connection_url

- **Route**: `POST /api/v2/clients/connection`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def get_etx_connection_url(vendor_id: str, body: ConnectionRequest | ConnectionRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`, `body`
- **Params**: `vendor_id` — header `VendorID` · `x_transaction_id` — header `X-Transaction-Id` · `body` — JSON body
- **Returns (parsed)**: `ConnectionResponse`
- **Returns (raw)**: `ApiResult[ConnectionResponse, GetEtxconnectionUrlErrorBody]`
- **Error**: `GetEtxconnectionUrlErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 403, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConnectionRequest` | `verizon/models/connection_request.py` |
| `ConnectionRequestDict` | `verizon/models/connection_request.py` |
| `ConnectionResponse` | `verizon/models/connection_response.py` |
| `GetEtxconnectionUrlErrorBody` | `verizon/errors/get_etxconnection_url_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

### client.etxregistration.get_etx_connection_url_multi_mec

- **Route**: `POST /api/v3/clients/connection`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def get_etx_connection_url_multi_mec(vendor_id: str, body: ConnectionRequest | ConnectionRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`, `body`
- **Params**: `vendor_id` — header `VendorID` · `x_transaction_id` — header `X-Transaction-Id` · `body` — JSON body
- **Returns (parsed)**: `ConnectionResponseV3`
- **Returns (raw)**: `ApiResult[ConnectionResponseV3, GetEtxconnectionUrlMultiMecErrorBody]`
- **Error**: `GetEtxconnectionUrlMultiMecErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 403, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ConnectionRequest` | `verizon/models/connection_request.py` |
| `ConnectionRequestDict` | `verizon/models/connection_request.py` |
| `ConnectionResponseV3` | `verizon/models/connection_response_v3.py` |
| `GetEtxconnectionUrlMultiMecErrorBody` | `verizon/errors/get_etxconnection_url_multi_mec_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

### client.etxregistration.query_etx_devices

- **Route**: `POST /api/v1/clients/query`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def query_etx_devices(body: DevicesRequest | DevicesRequestDict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `x_transaction_id` — header `X-Transaction-Id` · `body` — JSON body
- **Returns (parsed)**: `list[DevicesResponse]`
- **Returns (raw)**: `ApiResult[list[DevicesResponse], QueryEtxdevicesErrorBody]`
- **Error**: `QueryEtxdevicesErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 500] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `DevicesRequest` | `verizon/models/devices_request.py` |
| `DevicesRequestDict` | `verizon/models/devices_request.py` |
| `DevicesResponse` | `verizon/models/devices_response.py` |
| `QueryEtxdevicesErrorBody` | `verizon/errors/query_etxdevices_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

### client.etxregistration.register_etx_client

- **Route**: `POST /api/v2/clients/registration`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def register_etx_client(body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `x_transaction_id` — header `X-Transaction-Id` · `body` — JSON body
- **Returns (parsed)**: `ClientRegistrationResponse`
- **Returns (raw)**: `ApiResult[ClientRegistrationResponse, RegisterEtxclientErrorBody]`
- **Error**: `RegisterEtxclientErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 403, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClientRegistrationRequestV2` | `verizon/models/client_registration_request_v2.py` |
| `ClientRegistrationRequestV2Dict` | `verizon/models/client_registration_request_v2.py` |
| `ClientRegistrationResponse` | `verizon/models/client_registration_response.py` |
| `RegisterEtxclientErrorBody` | `verizon/errors/register_etxclient_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

### client.etxregistration.renew_etx_client_certificate

- **Route**: `PUT /api/v2/clients/registration`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def renew_etx_client_certificate(device_id: UUID, vendor_id: str, *, x_transaction_id: UUID | None = None, body: Any | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`, `vendor_id`
- **Params**: `device_id` — header `DeviceID` · `vendor_id` — header `VendorID` · `x_transaction_id` — header `X-Transaction-Id` · `body` — JSON body
- **Returns (parsed)**: `ClientRegistrationResponse`
- **Returns (raw)**: `ApiResult[ClientRegistrationResponse, RenewEtxclientCertificateErrorBody]`
- **Error**: `RenewEtxclientCertificateErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 403, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `ClientRegistrationResponse` | `verizon/models/client_registration_response.py` |
| `RenewEtxclientCertificateErrorBody` | `verizon/errors/renew_etxclient_certificate_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

### client.etxregistration.unregister_etx_clients

- **Route**: `DELETE /api/v2/clients/registration`
- **Auth**: `thingspace_oauth` AND `session_token`
- **Server**: `imp_server`
- **Signature**: `def unregister_etx_clients(device_ids: list[UUID], vendor_id: str, *, x_transaction_id: UUID | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_ids`, `vendor_id`
- **Params**: `device_ids` — query `DeviceIDs` · `vendor_id` — header `VendorID` · `x_transaction_id` — header `X-Transaction-Id`
- **Returns (parsed)**: `None`
- **Returns (raw)**: `ApiResult[None, UnregisterEtxclientsErrorBody]`
- **Error**: `UnregisterEtxclientsErrorBody` — **Case A (typed)**
- **Error arms**: `EtxrespondingError` [400, 401, 403, 429, 503] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UnregisterEtxclientsErrorBody` | `verizon/errors/unregister_etxclients_error.py` |
| `EtxrespondingError` | `verizon/models/etxresponding_error.py` |

