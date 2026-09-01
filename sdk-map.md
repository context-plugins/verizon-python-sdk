<!-- Generated file — do not edit; regenerated with the SDK. -->

# SDK map — Verizon (Python)

> A generated table of contents for this SDK. Consult this map and its sub-pages to learn signatures, error types, and server/auth wiring **by lookup**. Model shapes and enum values are *not* duplicated here — the map names the module declaring each type; read the shape there. Every name is the emitted spelling, so a wrong one fails at import rather than working silently.

|  |  |
| --- | --- |
| SDK display name | Verizon |
| Root package | `verizon` |
| Distribution name | `verizon` |
| Requires | Python 3.10 or later |
| API spec version | `v1.0` |
| Generator | APIMatic |

Staleness check: the API spec version above changes when the SDK is regenerated from a new spec, and the package version is what `pip show` reports for the installed SDK. If a lookup here fails at import, re-read the module named in the row.

All `Source` paths on this map and its sub-pages are relative to the **SDK root** — the directory holding this file and `pyproject.toml` — never to the page that carries them. Open them as-is from the SDK root; if the SDK sits under a subdirectory of a larger repo, prefix that subdirectory.

---

## Getting a client

### Synchronous client

```python
from verizon import VerizonClient
from verizon.core import ClientCredentials

client = VerizonClient(
    thingspace_oauth=ClientCredentials(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
    vz_m2_m_token="YOUR_API_KEY",
    session_token="YOUR_API_KEY",
    thingspace_oauth1=ClientCredentials(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
    environment="production",
)

# TODO: call endpoints here -- see api-reference.md

client.close()
```

Alternatively, scope it — `with VerizonClient(...) as client:` closes the pool on exit.

### Asynchronous client

```python
from asyncio import run

from verizon import AsyncVerizonClient
from verizon.core import ClientCredentials


async def main() -> None:
    client = AsyncVerizonClient(
        thingspace_oauth=ClientCredentials(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
        vz_m2_m_token="YOUR_API_KEY",
        session_token="YOUR_API_KEY",
        thingspace_oauth1=ClientCredentials(client_id="YOUR_CLIENT_ID", client_secret="YOUR_CLIENT_SECRET"),
        environment="production",
    )
    # TODO: call endpoints here, awaiting each -- see api-reference.md
    await client.aclose()


run(main())
```

Alternatively, scope it — `async with AsyncVerizonClient(...) as client:` closes the pool on exit.

`AsyncClient` (`verizon/async_client.py`) mirrors `Client` method for method, each endpoint method a coroutine. It takes the same keywords, except that each client accepts only its own transport and — where the **Async Type** column differs — only its own flavor.

`Client` and `AsyncClient` are aliases of `VerizonClient` and `AsyncVerizonClient` — the names tracebacks and `repr()` show; all four import from the root.

`close()` / `aclose()` closes the transport even when you supplied one via `custom_http_client=` / `custom_async_http_client=`, and a closed client cannot be reused.

Every API group is a property on the client (e.g. `client.gbi_device_actions5`). Every constructor argument is optional and keyword-only. Sources: `verizon/client.py`, `verizon/async_client.py`:

| Keyword | Sync Type | Async Type | Default |
| --- | --- | --- | --- |
| `environment` | `Environment` | `Environment` | `"production"` |
| `timeout` | `float` | `float` | `30.0` seconds |
| `server_config` | `ServerConfigOrDict \| None` | `ServerConfigOrDict \| None` | `None` |
| `custom_http_client` | `HttpClient \| None` | — | `None` |
| `custom_async_http_client` | — | `AsyncHttpClient \| None` | `None` |
| `thingspace_oauth` | `ClientCredentialsOrDict \| None` | `ClientCredentialsOrDict \| None` | `None` |
| `thingspace_oauth_token_source` | `TokenSource[ClientCredentials] \| None` | `AsyncTokenSource[ClientCredentials] \| None` | `None` |
| `vz_m2_m_token` | `str \| None` | `str \| None` | `None` |
| `session_token` | `str \| None` | `str \| None` | `None` |
| `thingspace_oauth1` | `ClientCredentialsOrDict \| None` | `ClientCredentialsOrDict \| None` | `None` |
| `thingspace_oauth1_token_source` | `TokenSource[ClientCredentials] \| None` | `AsyncTokenSource[ClientCredentials] \| None` | `None` |

The types those columns name — where each imports from and, for a credentials dict, its keys:

| Type | Import from | Shape |
| --- | --- | --- |
| `Environment` | `verizon.server` | `Literal` of the Environments table's names |
| `ServerConfigOrDict` | `verizon.server` | keys as the Servers & auth tables read |
| `HttpClient` | `verizon.core` | protocol — `send(request: HttpRequest) -> HttpResponse` · `close()` |
| `ClientCredentialsOrDict` | `verizon.core` | `ClientCredentials` or a dict: `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `TokenSource` | `verizon.core` | protocol — `fetch(credentials) -> OAuthToken` |
| `ClientCredentials` | `verizon.core` | `client_id: str` · `client_secret: str` · `scopes: list[Scope] \| None` |
| `AsyncHttpClient` | `verizon.core` | protocol — `async send(request: HttpRequest) -> HttpResponse` · `async aclose()` |
| `AsyncTokenSource` | `verizon.core` | protocol — `async fetch(credentials) -> OAuthToken` |

---

## Error-handling model (read once — applies to every operation)

Every operation is reached in two response modes:

- **Parsed call.** Returns the decoded payload and raises `ApiError` on an error status, with the decoded body on `.error` and the status on `.status_code`.
- **Raw call.** Reached through `.with_raw_response`; returns `ApiResult` — `Success` or `Failure` — and never raises for an API error. Read `.payload` on a `Success` or `.error` on a `Failure`; both carry `.response`.

What `.error` holds is fixed per operation. There are two cases:

- **Case A — typed error.** The operation documents at least one error status, so `verizon/errors/` declares a union alias over the bodies those statuses map to — `RawError` is always its last arm, for any undocumented status — and `.error` is annotated with that alias. Narrow it with `isinstance`. The operation blocks name the alias and the status each arm maps from.
- **Case B — raw error.** The operation documents no error status; `.error` is `RawError` (`verizon/core/results.py`): `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse`.

Core runtime types (`verizon/core/`) — public members with their **declared types**, verbatim from source:

| Type | Public members | Source |
| --- | --- | --- |
| `ApiError` — raised by every parsed call; `.error` is a Case A alias from `verizon/errors/` or `RawError` | `error: E` · `status_code: int` · `response: HttpResponse` | `verizon/core/exceptions.py` |
| `ApiResult[T, E]` — returned by every raw call; the `Success[T] \| Failure[E]` union | `payload: T` (on `Success`) · `error: E` (on `Failure`) · `response: HttpResponse` (on both) | `verizon/core/results.py` |
| `RawError` | `status_code: int` · `content: bytes` · `text(encoding="utf-8"): str` · `json(): Any` · `response: HttpResponse` | `verizon/core/results.py` |

Typed error bodies (the arms of a Case A alias) are ordinary models — no special handling. The operation's **Type sources** table gives the module that declares each one; read field names, declared types and JSON aliases there, as for any other model.

```python
from verizon.core import ApiError, RawError
from verizon.models import FotaV3Result

try:
    response = client.account_devices.get_account_device_information(acc)
except ApiError as e:
    # Case A — typed error: e.error is GetAccountDeviceInformationErrorBody
    if isinstance(e.error, FotaV3Result):
        # Handle 400
        print(e.error)
    if isinstance(e.error, RawError):
        # Any other error status
        print(e.status_code, e.error.text())
```

**Raw (`.with_raw_response`) variants: present on every operation** — the same call returns `ApiResult` instead of raising, with the same body on `Failure.error`. Of **314 operations**, **229 are Case A (typed)** and **85 are Case B (raw)**.

---

## Operations — by controller (88 pages, 314 operations)

Each links to a sub-page with one block per operation, headed by its full accessor path: the HTTP verb and route (for a mock, a raw request or a provider-side log — never reconstruct it from the method name), the sync parsed signature with its required positional parameters, each parameter's role and — where it differs — wire name, both return types, and its error case — **Case A** names the alias and the status each arm maps from, **Case B** names `RawError`. Every block also carries a **Type sources** table — every type it names, with the module that declares it.

**Each block states what is specific to its operation. Everything below holds for every operation, and blocks never restate it — silence means the default applies.**

| Applies to every operation | Stated where |
| --- | --- |
| **Four spellings, one signature** — the same method name and parameters on `Client` and `AsyncClient`, each also reachable through `.with_raw_response`; the async twin is a coroutine to `await`, with the same return types and error case, and where the **Async Type** column differs, pass the type it names | Getting a client |
| **Parsed raises, raw returns** — `ApiError` versus `ApiResult` | Error-handling model |
| **Case B error is always `RawError`** — also the last arm of every Case A alias, where a block's **Error arms** bullet ends in it | Error-handling model |
| **A trailing `request_options`** — keyword-only and optional, for per-call overrides such as a timeout or extra headers; every signature ends with it | here (`verizon/core/request_options.py`) |
| **Each operation names its own server** — this SDK declares several, so every block carries a **Server** bullet with the server's key in `server_config=` | its block |
| **Parameter names are literal** — signatures are generated code verbatim, and everything behind the bare `*` must be passed by name | here |
| **A parameter's wire name is its Python name** — sent as-is on the path, query string, header or body, unless the block's **Params** bullet carries a wire name beside the role | here |

**The operation's behavioural prose lives on the operation itself**, as the method's docstring in the module named at the top of its page, and again in `api-reference.md` with a per-parameter description and a usage sample. Blocks here give you the contract — names, types, shapes, errors. Where an operation's *semantics* decide what you must pass, that is what the docstring settles; read it there rather than filling it in from memory.

Sub-pages chunk per `###` block: each block is self-contained given the table above, and assumes this page is loaded beside it.

| Controller | Ops | Page |
| --- | --- | --- |
| `client.gbi_device_actions5` | 3 | [map/operations/gbi_device_actions5.md](map/operations/gbi_device_actions5.md) |
| `client.account_devices` | 2 | [map/operations/account_devices.md](map/operations/account_devices.md) |
| `client.account_requests` | 1 | [map/operations/account_requests.md](map/operations/account_requests.md) |
| `client.account_service_controller` | 1 | [map/operations/account_service_controller.md](map/operations/account_service_controller.md) |
| `client.account_subscriptions` | 1 | [map/operations/account_subscriptions.md](map/operations/account_subscriptions.md) |
| `client.accounts` | 3 | [map/operations/accounts.md](map/operations/accounts.md) |
| `client.anomaly_settings` | 3 | [map/operations/anomaly_settings.md](map/operations/anomaly_settings.md) |
| `client.anomaly_triggers` | 5 | [map/operations/anomaly_triggers.md](map/operations/anomaly_triggers.md) |
| `client.anomaly_triggers_v2` | 3 | [map/operations/anomaly_triggers_v2.md](map/operations/anomaly_triggers_v2.md) |
| `client.billing` | 4 | [map/operations/billing.md](map/operations/billing.md) |
| `client.campaigns_v2` | 7 | [map/operations/campaigns_v2.md](map/operations/campaigns_v2.md) |
| `client.campaigns_v3` | 5 | [map/operations/campaigns_v3.md](map/operations/campaigns_v3.md) |
| `client.client_logging` | 6 | [map/operations/client_logging.md](map/operations/client_logging.md) |
| `client.cloud_connector_devices` | 6 | [map/operations/cloud_connector_devices.md](map/operations/cloud_connector_devices.md) |
| `client.cloud_connector_subscriptions` | 3 | [map/operations/cloud_connector_subscriptions.md](map/operations/cloud_connector_subscriptions.md) |
| `client.configuration_files` | 2 | [map/operations/configuration_files.md](map/operations/configuration_files.md) |
| `client.connectivity_callbacks` | 3 | [map/operations/connectivity_callbacks.md](map/operations/connectivity_callbacks.md) |
| `client.create_price_plan_triggers` | 1 | [map/operations/create_price_plan_triggers.md](map/operations/create_price_plan_triggers.md) |
| `client.device_actions` | 7 | [map/operations/device_actions.md](map/operations/device_actions.md) |
| `client.device_credential_management` | 4 | [map/operations/device_credential_management.md](map/operations/device_credential_management.md) |
| `client.device_diagnostics` | 2 | [map/operations/device_diagnostics.md](map/operations/device_diagnostics.md) |
| `client.device_groups` | 5 | [map/operations/device_groups.md](map/operations/device_groups.md) |
| `client.device_location_callbacks` | 4 | [map/operations/device_location_callbacks.md](map/operations/device_location_callbacks.md) |
| `client.device_management` | 29 | [map/operations/device_management.md](map/operations/device_management.md) |
| `client.device_monitoring` | 2 | [map/operations/device_monitoring.md](map/operations/device_monitoring.md) |
| `client.device_profile_management` | 4 | [map/operations/device_profile_management.md](map/operations/device_profile_management.md) |
| `client.device_reports` | 3 | [map/operations/device_reports.md](map/operations/device_reports.md) |
| `client.device_sms_messaging` | 4 | [map/operations/device_sms_messaging.md](map/operations/device_sms_messaging.md) |
| `client.device_service_management` | 2 | [map/operations/device_service_management.md](map/operations/device_service_management.md) |
| `client.devices_location_subscriptions` | 2 | [map/operations/devices_location_subscriptions.md](map/operations/devices_location_subscriptions.md) |
| `client.devices_locations` | 6 | [map/operations/devices_locations.md](map/operations/devices_locations.md) |
| `client.diagnostics_callbacks` | 3 | [map/operations/diagnostics_callbacks.md](map/operations/diagnostics_callbacks.md) |
| `client.diagnostics_factory_reset` | 1 | [map/operations/diagnostics_factory_reset.md](map/operations/diagnostics_factory_reset.md) |
| `client.diagnostics_history` | 1 | [map/operations/diagnostics_history.md](map/operations/diagnostics_history.md) |
| `client.diagnostics_observations` | 2 | [map/operations/diagnostics_observations.md](map/operations/diagnostics_observations.md) |
| `client.diagnostics_settings` | 1 | [map/operations/diagnostics_settings.md](map/operations/diagnostics_settings.md) |
| `client.diagnostics_subscriptions` | 1 | [map/operations/diagnostics_subscriptions.md](map/operations/diagnostics_subscriptions.md) |
| `client.etxapp_configuration` | 5 | [map/operations/etxapp_configuration.md](map/operations/etxapp_configuration.md) |
| `client.etxregistration` | 7 | [map/operations/etxregistration.md](map/operations/etxregistration.md) |
| `client.exclusions` | 6 | [map/operations/exclusions.md](map/operations/exclusions.md) |
| `client.firmware_v1` | 5 | [map/operations/firmware_v1.md](map/operations/firmware_v1.md) |
| `client.firmware_v3` | 3 | [map/operations/firmware_v3.md](map/operations/firmware_v3.md) |
| `client.global_reporting` | 2 | [map/operations/global_reporting.md](map/operations/global_reporting.md) |
| `client.hpl_device_management` | 1 | [map/operations/hpl_device_management.md](map/operations/hpl_device_management.md) |
| `client.hyper_precise_location_callbacks` | 3 | [map/operations/hyper_precise_location_callbacks.md](map/operations/hyper_precise_location_callbacks.md) |
| `client.intelligence_service_controller` | 2 | [map/operations/intelligence_service_controller.md](map/operations/intelligence_service_controller.md) |
| `client.managing_e_sim_profiles` | 10 | [map/operations/managing_e_sim_profiles.md](map/operations/managing_e_sim_profiles.md) |
| `client.pwn` | 7 | [map/operations/pwn.md](map/operations/pwn.md) |
| `client.promotion_period_information` | 2 | [map/operations/promotion_period_information.md](map/operations/promotion_period_information.md) |
| `client.retrieve_rate_plan_list` | 1 | [map/operations/retrieve_rate_plan_list.md](map/operations/retrieve_rate_plan_list.md) |
| `client.retrieve_the_triggers` | 4 | [map/operations/retrieve_the_triggers.md](map/operations/retrieve_the_triggers.md) |
| `client.sim_actions` | 3 | [map/operations/sim_actions.md](map/operations/sim_actions.md) |
| `client.sim_secure_for_io_t_licenses` | 2 | [map/operations/sim_secure_for_io_t_licenses.md](map/operations/sim_secure_for_io_t_licenses.md) |
| `client.sms` | 3 | [map/operations/sms.md](map/operations/sms.md) |
| `client.sensor_insights_device_profile` | 4 | [map/operations/sensor_insights_device_profile.md](map/operations/sensor_insights_device_profile.md) |
| `client.sensor_insights_devices` | 6 | [map/operations/sensor_insights_devices.md](map/operations/sensor_insights_devices.md) |
| `client.sensor_insights_gateways` | 1 | [map/operations/sensor_insights_gateways.md](map/operations/sensor_insights_gateways.md) |
| `client.sensor_insights_health_score` | 2 | [map/operations/sensor_insights_health_score.md](map/operations/sensor_insights_health_score.md) |
| `client.sensor_insights_notification_groups` | 6 | [map/operations/sensor_insights_notification_groups.md](map/operations/sensor_insights_notification_groups.md) |
| `client.sensor_insights_rules` | 2 | [map/operations/sensor_insights_rules.md](map/operations/sensor_insights_rules.md) |
| `client.sensor_insights_sensors` | 5 | [map/operations/sensor_insights_sensors.md](map/operations/sensor_insights_sensors.md) |
| `client.sensor_insights_smart_alert_metrics` | 1 | [map/operations/sensor_insights_smart_alert_metrics.md](map/operations/sensor_insights_smart_alert_metrics.md) |
| `client.sensor_insights_smart_alerts` | 3 | [map/operations/sensor_insights_smart_alerts.md](map/operations/sensor_insights_smart_alerts.md) |
| `client.sensor_insights_users` | 4 | [map/operations/sensor_insights_users.md](map/operations/sensor_insights_users.md) |
| `client.server_logging` | 1 | [map/operations/server_logging.md](map/operations/server_logging.md) |
| `client.service_plans` | 1 | [map/operations/service_plans.md](map/operations/service_plans.md) |
| `client.session_management` | 3 | [map/operations/session_management.md](map/operations/session_management.md) |
| `client.software_management_callbacks_v1` | 3 | [map/operations/software_management_callbacks_v1.md](map/operations/software_management_callbacks_v1.md) |
| `client.software_management_callbacks_v2` | 4 | [map/operations/software_management_callbacks_v2.md](map/operations/software_management_callbacks_v2.md) |
| `client.software_management_callbacks_v3` | 4 | [map/operations/software_management_callbacks_v3.md](map/operations/software_management_callbacks_v3.md) |
| `client.software_management_licenses_v1` | 5 | [map/operations/software_management_licenses_v1.md](map/operations/software_management_licenses_v1.md) |
| `client.software_management_licenses_v2` | 6 | [map/operations/software_management_licenses_v2.md](map/operations/software_management_licenses_v2.md) |
| `client.software_management_licenses_v3` | 3 | [map/operations/software_management_licenses_v3.md](map/operations/software_management_licenses_v3.md) |
| `client.software_management_reports_v1` | 3 | [map/operations/software_management_reports_v1.md](map/operations/software_management_reports_v1.md) |
| `client.software_management_reports_v2` | 5 | [map/operations/software_management_reports_v2.md](map/operations/software_management_reports_v2.md) |
| `client.software_management_reports_v3` | 3 | [map/operations/software_management_reports_v3.md](map/operations/software_management_reports_v3.md) |
| `client.software_management_subscriptions_v1` | 2 | [map/operations/software_management_subscriptions_v1.md](map/operations/software_management_subscriptions_v1.md) |
| `client.software_management_subscriptions_v2` | 1 | [map/operations/software_management_subscriptions_v2.md](map/operations/software_management_subscriptions_v2.md) |
| `client.software_management_subscriptions_v3` | 1 | [map/operations/software_management_subscriptions_v3.md](map/operations/software_management_subscriptions_v3.md) |
| `client.targets` | 5 | [map/operations/targets.md](map/operations/targets.md) |
| `client.thing_space_quality_of_service_api_actions` | 2 | [map/operations/thing_space_quality_of_service_api_actions.md](map/operations/thing_space_quality_of_service_api_actions.md) |
| `client.update_price_plan_triggers` | 1 | [map/operations/update_price_plan_triggers.md](map/operations/update_price_plan_triggers.md) |
| `client.update_triggers` | 1 | [map/operations/update_triggers.md](map/operations/update_triggers.md) |
| `client.usage_trigger_management` | 3 | [map/operations/usage_trigger_management.md](map/operations/usage_trigger_management.md) |
| `client.wireless_network_performance` | 5 | [map/operations/wireless_network_performance.md](map/operations/wireless_network_performance.md) |
| `client.device_role_controller` | 1 | [map/operations/device_role_controller.md](map/operations/device_role_controller.md) |
| `client.e_uicc_device_profile_management` | 5 | [map/operations/e_uicc_device_profile_management.md](map/operations/e_uicc_device_profile_management.md) |
| `client.map_message_controller` | 4 | [map/operations/map_message_controller.md](map/operations/map_message_controller.md) |

---

## Models — where they live, how to build them

**Shapes live only in the source.** Every module under `verizon/models/` declares one type plus its input companion, and every module under `verizon/errors/` one alias plus the mapper that builds it; no two share a name. Take a type's module from the operation's **Type sources** table. When no retrieved chunk names it, the module is the type name in snake_case under the kind's directory below (`Success201` ↔ `success201.py`; an error alias drops its `Body` suffix: `ActivateDeviceThroughProfileErrorBody` ↔ `activate_device_through_profile_error.py`). Never grep for a type.

| Group | Count | Directory (module = `<type_name>.py`) |
| --- | --- | --- |
| Models (`SdkBaseModel` pydantic classes) | 781 | `verizon/models/` |
| Enums (`Enum` over `str` / `int`) — Python member names + wire values | 61 | `verizon/models/enums/` |
| Unions (plain) — `TypeAlias` over the arms | 50 | `verizon/models/unions/` |
| Error aliases (one per Case A operation) | 229 | `verizon/errors/` |

Conventions: a model is a `SdkBaseModel` (pydantic) class; a field whose wire name differs from its Python name carries it as `Field(alias=…)` (`request_id` ↔ `"requestId"`) — read the alias off the field rather than deriving it. An omittable field is annotated `Optional[T]` and defaults to `UNSET`, and one that may also be explicitly null is `OptionalNullable[T]`; both come from `core` and neither is `typing.Optional` — there is no `None` arm unless the spec declared the property nullable, so passing `None` to the first is a type error rather than a value that serializes.

Every model, enum and union also has an **input companion**, exported beside it from the same package (`Success201` ↔ `Success201Dict`). Wherever a signature names the companion you may pass either the model instance or a plain dict with the same keys, whichever reads better at the call site. An enum is a real `Enum` subclass over `str` / `int`; its companion is spelled `<Name>OrStr` or `<Name>OrInt` (`AccuracyMode` ↔ `AccuracyModeOrStr`) and additionally accepts a wire value this SDK version does not know. A union is a `TypeAlias` over its arms.

Import paths by content type (`from <package> import <Name>`):

| Contents | Import from |
| --- | --- |
| Client (root) | `verizon` |
| Operation controllers | `verizon.apis` |
| Models | `verizon.models` |
| Enums | `verizon.models.enums` |
| Unions | `verizon.models.unions`, `verizon.models` |
| Error aliases | `verizon.errors` |
| Core runtime (`ApiError`, `ApiResult`, `RawError`, …) | `verizon.core` |

---

## Servers & auth

**OAuth2 (client credentials).** Pass `thingspace_oauth` your client id and secret; tokens come from `/oauth2/token` on the `o_auth_server` server.

**API key (header `VZ-M2M-Token`).** Pass `vz_m2_m_token="<api_key>"`; sent as the `VZ-M2M-Token` request header.

**API key (header `SessionToken`).** Pass `session_token="<api_key>"`; sent as the `SessionToken` request header.

**OAuth2 (client credentials).** Pass `thingspace_oauth1` your client id and secret; tokens come from `/` on the `o_auth_server` server.

Operation blocks name their scheme in an **Auth** bullet; an operation whose spec declares no scheme carries no such bullet.

- `AND` — every scheme listed must be configured for the call to succeed.
- `OR` — any one of the schemes listed can be used; the first one you configured is the one sent, in the order listed.

A scheme you did not configure is skipped silently rather than raising, and the request is sent anyway — so an authentication failure can mean no credential was sent rather than a bad one.

**Environments.** `environment=` selects the target environment (`verizon/server/environment.py`):

| Environment | Hosting |
| --- | --- |
| `"production"` *(default)* | — |
| `"staging"` | — |
| `"dev"` | — |
| `"qa"` | — |
| `"mock_server_for_limited_availability_see_quick_start"` | — |

**15 servers.** Base-URL templates and override points (`verizon/server/server_config.py`):

| Server | `"production"` base URL | `"staging"` base URL | `"dev"` base URL | `"qa"` base URL | `"mock_server_for_limited_availability_see_quick_start"` base URL | Override point |
| --- | --- | --- | --- | --- | --- | --- |
| `hyper_precise_credentials` | `https://thingspace.verizon.com/api/auth/v1` | `https://staging.thingspace.verizon.com/api/auth/v1` | `https://staging.thingspace.verizon.com/api/auth/v1` | `https://thingspace.verizon.com/api/auth/v1` | `https://staging.thingspace.verizon.com/api/auth/v1` | `{"hyper_precise_credentials": {"production": {"base_url": …}}}` (and the other environments) |
| `imp_server` | `https://imp.thingspace.verizon.com` | `https://imp-staging.thingspace.verizon.com` | `https://devmanagement-staging.imp.thingspace.verizon.com` | `https://tsd-nginx-qa-us-east-1.imp.thingspace.verizon.com` | `https://mock-staging.thingspace.verizon.com` | `{"imp_server": {"production": {"base_url": …}}}` (and the other environments) |
| `thingspace` | `https://thingspace.verizon.com/api` | `https://staging.thingspace.verizon.com/api` | `https://devmanagement-staging.thingspace.verizon.com/api` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api` | `https://mock-staging.thingspace.verizon.com/api` | `{"thingspace": {"production": {"base_url": …}}}` (and the other environments) |
| `o_auth_server` | `https://thingspace.verizon.com/api/ts/v1` | `https://staging.thingspace.verizon.com/api/ts/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/ts/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/ts/v1` | `https://mock-staging.thingspace.verizon.com/api/ts/v1` | `{"o_auth_server": {"production": {"base_url": …}}}` (and the other environments) |
| `m2_m` | `https://thingspace.verizon.com/api/m2m` | `https://staging.thingspace.verizon.com/api/m2m` | `https://devmanagement-staging.thingspace.verizon.com:80/m2m` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/m2m` | `https://mock-staging.thingspace.verizon.com/api/m2m` | `{"m2_m": {"production": {"base_url": …}}}` (and the other environments) |
| `device_location` | `https://thingspace.verizon.com/api/loc/v1` | `https://staging.thingspace.verizon.com/api/loc/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/loc/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/loc/v1` | `https://mock-staging.thingspace.verizon.com/api/loc/v1` | `{"device_location": {"production": {"base_url": …}}}` (and the other environments) |
| `subscription_server` | `https://thingspace.verizon.com/api/subsc/v1` | `https://staging.thingspace.verizon.com/api/subsc/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/subsc/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/subsc/v1` | `https://mock-staging.thingspace.verizon.com/api/subsc/v1` | `{"subscription_server": {"production": {"base_url": …}}}` (and the other environments) |
| `software_management_v1` | `https://thingspace.verizon.com/api/fota/v1` | `https://staging.thingspace.verizon.com/api/fota/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/fota/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/fota/v1` | `https://mock-staging.thingspace.verizon.com/api/fota/v1` | `{"software_management_v1": {"production": {"base_url": …}}}` (and the other environments) |
| `software_management_v2` | `https://thingspace.verizon.com/api/fota/v2` | `https://staging.thingspace.verizon.com/api/fota/v2` | `https://devmanagement-staging.thingspace.verizon.com:80/fota/v2` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/fota/v2` | `https://mock-staging.thingspace.verizon.com/api/fota/v2` | `{"software_management_v2": {"production": {"base_url": …}}}` (and the other environments) |
| `software_management_v3` | `https://thingspace.verizon.com/api/fota/v3` | `https://staging.thingspace.verizon.com/api/fota/v3` | `https://devmanagement-staging.thingspace.verizon.com:80/fota/v3` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/fota/v3` | `https://mock-staging.thingspace.verizon.com/api/fota/v3` | `{"software_management_v3": {"production": {"base_url": …}}}` (and the other environments) |
| `device_diagnostics` | `https://thingspace.verizon.com/api/diagnostics/v1` | `https://staging.thingspace.verizon.com/api/diagnostics/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/diagnostics/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/diagnostics/v1` | `https://mock-staging.thingspace.verizon.com/api/diagnostics/v1` | `{"device_diagnostics": {"production": {"base_url": …}}}` (and the other environments) |
| `cloud_connector` | `https://thingspace.verizon.com/api/cc/v1` | `https://staging.thingspace.verizon.com/api/cc/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/cc/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/cc/v1` | `https://mock-staging.thingspace.verizon.com/api/cc/v1` | `{"cloud_connector": {"production": {"base_url": …}}}` (and the other environments) |
| `hyper_precise_location` | `https://thingspace.verizon.com/api/hyper-precise/v1` | `https://staging.thingspace.verizon.com/api/hyper-precise/v1` | `https://devmanagement-staging.thingspace.verizon.com:80/hyper-precise/v1` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/hyper-precise/v1` | `https://mock-staging.thingspace.verizon.com/api/hyper-precise/v1` | `{"hyper_precise_location": {"production": {"base_url": …}}}` (and the other environments) |
| `services` | `https://5gedge.verizon.com/api/mec/services` | `https://staging.5gedge.verizon.com/api/mec/services` | `https://devmanagement-staging.5gedge.verizon.com:80/mec/services` | `https://tsd-nginx-qa-us-east-1.5gedge.verizon.com/api/mec/services` | `https://mock-staging.thingspace.verizon.com/api/mec/services` | `{"services": {"production": {"base_url": …}}}` (and the other environments) |
| `quality_of_service` | `https://thingspace.verizon.com/api/m2m/v1/devices` | `https://staging.thingspace.verizon.com/api/m2m/v1/devices` | `https://devmanagement-staging.thingspace.verizon.com/api/m2m/v1/devices` | `https://tsd-nginx-qa-us-east-1.thingspace.verizon.com/api/m2m/v1/devices` | `https://mock-staging.thingspace.verizon.com/api/m2m/v1/devices` | `{"quality_of_service": {"production": {"base_url": …}}}` (and the other environments) |

Pick a row with `environment=`, and override any of these by passing `server_config=` a dict nested exactly as the columns above read — `{"hyper_precise_credentials": {"production": {"base_url": …}}}` — with each row's variables sitting beside its `base_url`.

