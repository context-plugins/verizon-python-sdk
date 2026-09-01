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
from ..errors.add_devices_hyper_precise_error import (
    AddDevicesHyperPreciseErrorBody,
    add_devices_hyper_precise_error_mapper,
)
from ..models.hpl_add_devices_request import HplAddDevicesRequest, HplAddDevicesRequestDict
from ..server.server import Server


class HplDeviceManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = HplDeviceManagementWithRawResponse(client, server, auth)

    def add_devices_hyper_precise(
        self,
        body: HplAddDevicesRequest | HplAddDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[HplAddDevicesRequest]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add to the account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            For each device in the request, contains device identifiers and a success or failure response.

        Raises:
            ApiError: Bad Request. Unauthorized Forbidden Not Found / Does not exist Method Not Allowed Format / Request
                Unacceptable Too many requests Internal Server Error ``error`` is ``HyperPreciseLocationResult |
                RawError``."""
        return self._with_raw_response.add_devices_hyper_precise(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> HplDeviceManagementWithRawResponse:
        return self._with_raw_response


class AsyncHplDeviceManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncHplDeviceManagementWithRawResponse(client, server, auth)

    async def add_devices_hyper_precise(
        self,
        body: HplAddDevicesRequest | HplAddDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[HplAddDevicesRequest]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add to the account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            For each device in the request, contains device identifiers and a success or failure response.

        Raises:
            ApiError: Bad Request. Unauthorized Forbidden Not Found / Does not exist Method Not Allowed Format / Request
                Unacceptable Too many requests Internal Server Error ``error`` is ``HyperPreciseLocationResult |
                RawError``."""
        return (await self._with_raw_response.add_devices_hyper_precise(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncHplDeviceManagementWithRawResponse:
        return self._with_raw_response


class HplDeviceManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_devices_hyper_precise(
        self,
        body: HplAddDevicesRequest | HplAddDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[HplAddDevicesRequest], AddDevicesHyperPreciseErrorBody]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add to the account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/devices/actions/add"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[HplAddDevicesRequest | HplAddDevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[HplAddDevicesRequest]],
            error_mapper=add_devices_hyper_precise_error_mapper,
            request_options=request_options,
        )


class AsyncHplDeviceManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_devices_hyper_precise(
        self,
        body: HplAddDevicesRequest | HplAddDevicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[HplAddDevicesRequest], AddDevicesHyperPreciseErrorBody]:
        """Use this API if you want to manage some device settings before you are ready to activate service for the
        devices.

        Args:
            body: Devices to add to the account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/devices/actions/add"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[HplAddDevicesRequest | HplAddDevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[HplAddDevicesRequest]],
            error_mapper=add_devices_hyper_precise_error_mapper,
            request_options=request_options,
        )
