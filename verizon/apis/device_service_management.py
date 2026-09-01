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
from ..errors.get_device_hyper_precise_status_error import (
    GetDeviceHyperPreciseStatusErrorBody,
    get_device_hyper_precise_status_error_mapper,
)
from ..errors.update_device_hyper_precise_status_error import (
    UpdateDeviceHyperPreciseStatusErrorBody,
    update_device_hyper_precise_status_error_mapper,
)
from ..models.bullseye_service_request import BullseyeServiceRequest, BullseyeServiceRequestDict
from ..models.bullseye_service_result import BullseyeServiceResult
from ..server.server import Server


class DeviceServiceManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceServiceManagementWithRawResponse(client, server, auth)

    def get_device_hyper_precise_status(
        self, imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BullseyeServiceResult:
        """Gets the list of a status for hyper-precise location devices.

        Args:
            imei: The International Mobile Equipment Identifier of the device.
            account_number: The numeric name of the account and must include leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns the status of Hyper Precise Location on the device.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.get_device_hyper_precise_status(
            imei, account_number, request_options=request_options
        ).unwrap()

    def update_device_hyper_precise_status(
        self,
        body: BullseyeServiceRequest | BullseyeServiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BullseyeServiceResult:
        """Enable/disable hyper-precise service for a device.

        Args:
            body: List of devices and hyper-precise required statuses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.update_device_hyper_precise_status(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DeviceServiceManagementWithRawResponse:
        return self._with_raw_response


class AsyncDeviceServiceManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceServiceManagementWithRawResponse(client, server, auth)

    async def get_device_hyper_precise_status(
        self, imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> BullseyeServiceResult:
        """Gets the list of a status for hyper-precise location devices.

        Args:
            imei: The International Mobile Equipment Identifier of the device.
            account_number: The numeric name of the account and must include leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns the status of Hyper Precise Location on the device.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.get_device_hyper_precise_status(
                imei, account_number, request_options=request_options
            )
        ).unwrap()

    async def update_device_hyper_precise_status(
        self,
        body: BullseyeServiceRequest | BullseyeServiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BullseyeServiceResult:
        """Enable/disable hyper-precise service for a device.

        Args:
            body: List of devices and hyper-precise required statuses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.update_device_hyper_precise_status(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceServiceManagementWithRawResponse:
        return self._with_raw_response


class DeviceServiceManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_device_hyper_precise_status(
        self, imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BullseyeServiceResult, GetDeviceHyperPreciseStatusErrorBody]:
        """Gets the list of a status for hyper-precise location devices.

        Args:
            imei: The International Mobile Equipment Identifier of the device.
            account_number: The numeric name of the account and must include leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_location("/devices/services"),
            query_params=[param[str]("imei", imei), param[str]("accountNumber", account_number)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[BullseyeServiceResult],
            error_mapper=get_device_hyper_precise_status_error_mapper,
            request_options=request_options,
        )

    def update_device_hyper_precise_status(
        self,
        body: BullseyeServiceRequest | BullseyeServiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BullseyeServiceResult, UpdateDeviceHyperPreciseStatusErrorBody]:
        """Enable/disable hyper-precise service for a device.

        Args:
            body: List of devices and hyper-precise required statuses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_location("/devices/services"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BullseyeServiceRequest | BullseyeServiceRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[BullseyeServiceResult],
            error_mapper=update_device_hyper_precise_status_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceServiceManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_device_hyper_precise_status(
        self, imei: str, account_number: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[BullseyeServiceResult, GetDeviceHyperPreciseStatusErrorBody]:
        """Gets the list of a status for hyper-precise location devices.

        Args:
            imei: The International Mobile Equipment Identifier of the device.
            account_number: The numeric name of the account and must include leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_location("/devices/services"),
            query_params=[param[str]("imei", imei), param[str]("accountNumber", account_number)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[BullseyeServiceResult],
            error_mapper=get_device_hyper_precise_status_error_mapper,
            request_options=request_options,
        )

    async def update_device_hyper_precise_status(
        self,
        body: BullseyeServiceRequest | BullseyeServiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BullseyeServiceResult, UpdateDeviceHyperPreciseStatusErrorBody]:
        """Enable/disable hyper-precise service for a device.

        Args:
            body: List of devices and hyper-precise required statuses.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_location("/devices/services"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BullseyeServiceRequest | BullseyeServiceRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[BullseyeServiceResult],
            error_mapper=update_device_hyper_precise_status_error_mapper,
            request_options=request_options,
        )
