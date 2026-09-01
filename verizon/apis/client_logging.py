from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_decoder,
    param,
)
from ..errors.disable_device_logging_error import DisableDeviceLoggingErrorBody, disable_device_logging_error_mapper
from ..errors.disable_logging_for_devices_error import (
    DisableLoggingForDevicesErrorBody,
    disable_logging_for_devices_error_mapper,
)
from ..errors.enable_device_logging_error import EnableDeviceLoggingErrorBody, enable_device_logging_error_mapper
from ..errors.enable_logging_for_devices_error import (
    EnableLoggingForDevicesErrorBody,
    enable_logging_for_devices_error_mapper,
)
from ..errors.list_device_logs_error import ListDeviceLogsErrorBody, list_device_logs_error_mapper
from ..errors.list_devices_with_logging_enabled_error import (
    ListDevicesWithLoggingEnabledErrorBody,
    list_devices_with_logging_enabled_error_mapper,
)
from ..models.device_log import DeviceLog
from ..models.device_logging_status import DeviceLoggingStatus
from ..server.server import Server


class ClientLogging:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ClientLoggingWithRawResponse(client, server, auth)

    def disable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Disables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.disable_device_logging(
            account, device_id, request_options=request_options
        ).unwrap()

    def disable_logging_for_devices(
        self, account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Turn logging off for a list of devices.

        Args:
            account: Account identifier.
            device_ids: The list of device IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.disable_logging_for_devices(
            account, device_ids, request_options=request_options
        ).unwrap()

    def enable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLoggingStatus:
        """Enables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device logging status information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.enable_device_logging(
            account, device_id, request_options=request_options
        ).unwrap()

    def enable_logging_for_devices(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLoggingStatus]:
        """Each customer may have a maximum of 20 devices enabled for logging.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List containing device logging status information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.enable_logging_for_devices(account, request_options=request_options).unwrap()

    def list_device_logs(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLog]:
        """Gets logs for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of device logs.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.list_device_logs(account, device_id, request_options=request_options).unwrap()

    def list_devices_with_logging_enabled(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLoggingStatus]:
        """Returns an array of all devices in the specified account for which logging is enabled.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List containing device logging status information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.list_devices_with_logging_enabled(
            account, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ClientLoggingWithRawResponse:
        return self._with_raw_response


class AsyncClientLogging:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncClientLoggingWithRawResponse(client, server, auth)

    async def disable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Disables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.disable_device_logging(account, device_id, request_options=request_options)
        ).unwrap()

    async def disable_logging_for_devices(
        self, account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Turn logging off for a list of devices.

        Args:
            account: Account identifier.
            device_ids: The list of device IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.disable_logging_for_devices(
                account, device_ids, request_options=request_options
            )
        ).unwrap()

    async def enable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLoggingStatus:
        """Enables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device logging status information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.enable_device_logging(account, device_id, request_options=request_options)
        ).unwrap()

    async def enable_logging_for_devices(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLoggingStatus]:
        """Each customer may have a maximum of 20 devices enabled for logging.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List containing device logging status information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.enable_logging_for_devices(account, request_options=request_options)
        ).unwrap()

    async def list_device_logs(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLog]:
        """Gets logs for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of device logs.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.list_device_logs(account, device_id, request_options=request_options)
        ).unwrap()

    async def list_devices_with_logging_enabled(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceLoggingStatus]:
        """Returns an array of all devices in the specified account for which logging is enabled.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List containing device logging status information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.list_devices_with_logging_enabled(account, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncClientLoggingWithRawResponse:
        return self._with_raw_response


class ClientLoggingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def disable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DisableDeviceLoggingErrorBody]:
        """Disables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=disable_device_logging_error_mapper,
            request_options=request_options,
        )

    def disable_logging_for_devices(
        self, account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DisableLoggingForDevicesErrorBody]:
        """Turn logging off for a list of devices.

        Args:
            account: Account identifier.
            device_ids: The list of device IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/logging/{account}/devices"),
            path_params=[param[str]("account", account)],
            query_params=[param[str]("deviceIds", device_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=disable_logging_for_devices_error_mapper,
            request_options=request_options,
        )

    def enable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLoggingStatus, EnableDeviceLoggingErrorBody]:
        """Enables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLoggingStatus],
            error_mapper=enable_device_logging_error_mapper,
            request_options=request_options,
        )

    def enable_logging_for_devices(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLoggingStatus], EnableLoggingForDevicesErrorBody]:
        """Each customer may have a maximum of 20 devices enabled for logging.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/logging/{account}/devices"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLoggingStatus]],
            error_mapper=enable_logging_for_devices_error_mapper,
            request_options=request_options,
        )

    def list_device_logs(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLog], ListDeviceLogsErrorBody]:
        """Gets logs for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}/logs"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLog]],
            error_mapper=list_device_logs_error_mapper,
            request_options=request_options,
        )

    def list_devices_with_logging_enabled(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLoggingStatus], ListDevicesWithLoggingEnabledErrorBody]:
        """Returns an array of all devices in the specified account for which logging is enabled.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/logging/{account}/devices"),
            path_params=[param[str]("account", account)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLoggingStatus]],
            error_mapper=list_devices_with_logging_enabled_error_mapper,
            request_options=request_options,
        )


class AsyncClientLoggingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def disable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DisableDeviceLoggingErrorBody]:
        """Disables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=disable_device_logging_error_mapper,
            request_options=request_options,
        )

    async def disable_logging_for_devices(
        self, account: str, device_ids: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DisableLoggingForDevicesErrorBody]:
        """Turn logging off for a list of devices.

        Args:
            account: Account identifier.
            device_ids: The list of device IDs.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/logging/{account}/devices"),
            path_params=[param[str]("account", account)],
            query_params=[param[str]("deviceIds", device_ids)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=disable_logging_for_devices_error_mapper,
            request_options=request_options,
        )

    async def enable_device_logging(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLoggingStatus, EnableDeviceLoggingErrorBody]:
        """Enables logging for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLoggingStatus],
            error_mapper=enable_device_logging_error_mapper,
            request_options=request_options,
        )

    async def enable_logging_for_devices(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLoggingStatus], EnableLoggingForDevicesErrorBody]:
        """Each customer may have a maximum of 20 devices enabled for logging.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v2("/logging/{account}/devices"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLoggingStatus]],
            error_mapper=enable_logging_for_devices_error_mapper,
            request_options=request_options,
        )

    async def list_device_logs(
        self, account: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLog], ListDeviceLogsErrorBody]:
        """Gets logs for a specific device.

        Args:
            account: Account identifier.
            device_id: Device IMEI identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/logging/{account}/devices/{deviceId}/logs"),
            path_params=[param[str]("account", account), param[str]("deviceId", device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLog]],
            error_mapper=list_device_logs_error_mapper,
            request_options=request_options,
        )

    async def list_devices_with_logging_enabled(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceLoggingStatus], ListDevicesWithLoggingEnabledErrorBody]:
        """Returns an array of all devices in the specified account for which logging is enabled.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/logging/{account}/devices"),
            path_params=[param[str]("account", account)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceLoggingStatus]],
            error_mapper=list_devices_with_logging_enabled_error_mapper,
            request_options=request_options,
        )
