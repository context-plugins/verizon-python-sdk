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
    json_body,
    json_decoder,
    param,
)
from ..errors.list_available_firmware2_error import (
    ListAvailableFirmware2ErrorBody,
    list_available_firmware2_error_mapper,
)
from ..errors.report_device_firmware_error import ReportDeviceFirmwareErrorBody, report_device_firmware_error_mapper
from ..errors.synchronize_device_firmware_error import (
    SynchronizeDeviceFirmwareErrorBody,
    synchronize_device_firmware_error_mapper,
)
from ..models.device_firmware_list import DeviceFirmwareList
from ..models.device_firmware_version_update_result import DeviceFirmwareVersionUpdateResult
from ..models.enums.firmware_protocol import FirmwareProtocolOrStr
from ..models.firmware_imei import FirmwareImei, FirmwareImeiDict
from ..models.firmware_package import FirmwarePackage
from ..server.server import Server


class FirmwareV3:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = FirmwareV3WithRawResponse(client, server, auth)

    def list_available_firmware2(
        self, acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[FirmwarePackage]:
        """This endpoint allows user to list the firmware of an account.

        Args:
            acc: Account identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of firmware objects.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.list_available_firmware2(acc, protocol, request_options=request_options).unwrap()

    def report_device_firmware(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceFirmwareVersionUpdateResult:
        """Ask a device to report its firmware version asynchronously.

        Args:
            acc: Account identifier.
            device_id: Device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device firmware version update request.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.report_device_firmware(acc, device_id, request_options=request_options).unwrap()

    def synchronize_device_firmware(
        self, acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceFirmwareList:
        """Synchronize ThingSpace with the FOTA server for up to 100 devices.

        Args:
            acc: Account identifier.
            body: DeviceIds to get firmware info synchronously.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns device firmware information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.synchronize_device_firmware(acc, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> FirmwareV3WithRawResponse:
        return self._with_raw_response


class AsyncFirmwareV3:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncFirmwareV3WithRawResponse(client, server, auth)

    async def list_available_firmware2(
        self, acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[FirmwarePackage]:
        """This endpoint allows user to list the firmware of an account.

        Args:
            acc: Account identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of firmware objects.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.list_available_firmware2(acc, protocol, request_options=request_options)
        ).unwrap()

    async def report_device_firmware(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceFirmwareVersionUpdateResult:
        """Ask a device to report its firmware version asynchronously.

        Args:
            acc: Account identifier.
            device_id: Device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device firmware version update request.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.report_device_firmware(acc, device_id, request_options=request_options)
        ).unwrap()

    async def synchronize_device_firmware(
        self, acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceFirmwareList:
        """Synchronize ThingSpace with the FOTA server for up to 100 devices.

        Args:
            acc: Account identifier.
            body: DeviceIds to get firmware info synchronously.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns device firmware information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.synchronize_device_firmware(acc, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncFirmwareV3WithRawResponse:
        return self._with_raw_response


class FirmwareV3WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_available_firmware2(
        self, acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FirmwarePackage], ListAvailableFirmware2ErrorBody]:
        """This endpoint allows user to list the firmware of an account.

        Args:
            acc: Account identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/firmware/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[param[FirmwareProtocolOrStr]("protocol", protocol)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[FirmwarePackage]],
            error_mapper=list_available_firmware2_error_mapper,
            request_options=request_options,
        )

    def report_device_firmware(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceFirmwareVersionUpdateResult, ReportDeviceFirmwareErrorBody]:
        """Ask a device to report its firmware version asynchronously.

        Args:
            acc: Account identifier.
            device_id: Device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/firmware/{acc}/async/{deviceId}"),
            path_params=[param[str]("acc", acc), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceFirmwareVersionUpdateResult],
            error_mapper=report_device_firmware_error_mapper,
            request_options=request_options,
        )

    def synchronize_device_firmware(
        self, acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceFirmwareList, SynchronizeDeviceFirmwareErrorBody]:
        """Synchronize ThingSpace with the FOTA server for up to 100 devices.

        Args:
            acc: Account identifier.
            body: DeviceIds to get firmware info synchronously.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/firmware/{acc}/devices"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FirmwareImei | FirmwareImeiDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceFirmwareList],
            error_mapper=synchronize_device_firmware_error_mapper,
            request_options=request_options,
        )


class AsyncFirmwareV3WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_available_firmware2(
        self, acc: str, protocol: FirmwareProtocolOrStr, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[FirmwarePackage], ListAvailableFirmware2ErrorBody]:
        """This endpoint allows user to list the firmware of an account.

        Args:
            acc: Account identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/firmware/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[param[FirmwareProtocolOrStr]("protocol", protocol)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[FirmwarePackage]],
            error_mapper=list_available_firmware2_error_mapper,
            request_options=request_options,
        )

    async def report_device_firmware(
        self, acc: str, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceFirmwareVersionUpdateResult, ReportDeviceFirmwareErrorBody]:
        """Ask a device to report its firmware version asynchronously.

        Args:
            acc: Account identifier.
            device_id: Device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/firmware/{acc}/async/{deviceId}"),
            path_params=[param[str]("acc", acc), param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceFirmwareVersionUpdateResult],
            error_mapper=report_device_firmware_error_mapper,
            request_options=request_options,
        )

    async def synchronize_device_firmware(
        self, acc: str, body: FirmwareImei | FirmwareImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceFirmwareList, SynchronizeDeviceFirmwareErrorBody]:
        """Synchronize ThingSpace with the FOTA server for up to 100 devices.

        Args:
            acc: Account identifier.
            body: DeviceIds to get firmware info synchronously.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.software_management_v3("/firmware/{acc}/devices"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FirmwareImei | FirmwareImeiDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceFirmwareList],
            error_mapper=synchronize_device_firmware_error_mapper,
            request_options=request_options,
        )
