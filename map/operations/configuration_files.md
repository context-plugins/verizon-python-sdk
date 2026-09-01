<!-- Generated file — do not edit; regenerated with the SDK. -->

# ConfigurationFiles — operations

Accessor: `client.configuration_files` · Source: `verizon/apis/configuration_files.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.configuration_files.get_list_of_files

- **Route**: `GET /files/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def get_list_of_files(acc: str, distribution_type: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`, `distribution_type`
- **Params**: `acc` — path · `distribution_type` — query `distributionType`
- **Returns (parsed)**: `RetrievesAvailableFilesResponseList`
- **Returns (raw)**: `ApiResult[RetrievesAvailableFilesResponseList, GetListOfFilesErrorBody]`
- **Error**: `GetListOfFilesErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `RetrievesAvailableFilesResponseList` | `verizon/models/retrieves_available_files_response_list.py` |
| `GetListOfFilesErrorBody` | `verizon/errors/get_list_of_files_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

### client.configuration_files.upload_config_file

- **Route**: `POST /files/{acc}`
- **Auth**: `thingspace_oauth` AND `vz_m2_m_token`
- **Server**: `software_management_v2`
- **Signature**: `def upload_config_file(acc: str, *, file_version: str | None = None, make: str | None = None, model: str | None = None, local_target_path: str | None = None, fileupload: bytes | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `acc`
- **Params**: `acc` — path · `file_version` — multipart field `fileVersion` · `make` — multipart field · `model` — multipart field · `local_target_path` — multipart field `localTargetPath` · `fileupload` — multipart file
- **Returns (parsed)**: `UploadConfigurationFilesResponse`
- **Returns (raw)**: `ApiResult[UploadConfigurationFilesResponse, UploadConfigFileErrorBody]`
- **Error**: `UploadConfigFileErrorBody` — **Case A (typed)**
- **Error arms**: `FotaV2Result` [400] · `RawError` [anything unmapped]

| Type | Source |
| --- | --- |
| `UploadConfigurationFilesResponse` | `verizon/models/upload_configuration_files_response.py` |
| `UploadConfigFileErrorBody` | `verizon/errors/upload_config_file_error.py` |
| `FotaV2Result` | `verizon/models/fota_v2_result.py` |

