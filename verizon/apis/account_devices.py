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
from ..errors.get_account_device_information_error import (
    GetAccountDeviceInformationErrorBody,
    get_account_device_information_error_mapper,
)
from ..errors.list_account_devices_information_error import (
    ListAccountDevicesInformationErrorBody,
    list_account_devices_information_error_mapper,
)
from ..models.device_imei import DeviceImei, DeviceImeiDict
from ..models.device_list_result import DeviceListResult
from ..models.enums.devices_protocol import DevicesProtocolOrStr
from ..models.v3_account_device_list import V3AccountDeviceList
from ..server.server import Server


class AccountDevices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountDevicesWithRawResponse(client, server, auth)

    def get_account_device_information(
        self,
        acc: str,
        *,
        last_seen_device_id: str | None = None,
        protocol: DevicesProtocolOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3AccountDeviceList:
        """Retrieve account device information such as reported firmware on the devices.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_account_device_information(
            acc, last_seen_device_id=last_seen_device_id, protocol=protocol, request_options=request_options
        ).unwrap()

    def list_account_devices_information(
        self, acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceListResult:
        """Retrieve device information for a list of devices on an account.

        Args:
            acc: Account identifier.
            body: Request device list information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Get device list information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.list_account_devices_information(
            acc, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountDevicesWithRawResponse:
        return self._with_raw_response


class AsyncAccountDevices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountDevicesWithRawResponse(client, server, auth)

    async def get_account_device_information(
        self,
        acc: str,
        *,
        last_seen_device_id: str | None = None,
        protocol: DevicesProtocolOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V3AccountDeviceList:
        """Retrieve account device information such as reported firmware on the devices.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_account_device_information(
                acc, last_seen_device_id=last_seen_device_id, protocol=protocol, request_options=request_options
            )
        ).unwrap()

    async def list_account_devices_information(
        self, acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceListResult:
        """Retrieve device information for a list of devices on an account.

        Args:
            acc: Account identifier.
            body: Request device list information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Get device list information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.list_account_devices_information(acc, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountDevicesWithRawResponse:
        return self._with_raw_response


class AccountDevicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_device_information(
        self,
        acc: str,
        *,
        last_seen_device_id: str | None = None,
        protocol: DevicesProtocolOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3AccountDeviceList, GetAccountDeviceInformationErrorBody]:
        """Retrieve account device information such as reported firmware on the devices.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/devices/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[
                param[str | None]("lastSeenDeviceId", last_seen_device_id),
                param[DevicesProtocolOrStr | None]("protocol", protocol),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3AccountDeviceList],
            error_mapper=get_account_device_information_error_mapper,
            request_options=request_options,
        )

    def list_account_devices_information(
        self, acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceListResult, ListAccountDevicesInformationErrorBody]:
        """Retrieve device information for a list of devices on an account.

        Args:
            acc: Account identifier.
            body: Request device list information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/devices/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceImei | DeviceImeiDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceListResult],
            error_mapper=list_account_devices_information_error_mapper,
            request_options=request_options,
        )


class AsyncAccountDevicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_device_information(
        self,
        acc: str,
        *,
        last_seen_device_id: str | None = None,
        protocol: DevicesProtocolOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V3AccountDeviceList, GetAccountDeviceInformationErrorBody]:
        """Retrieve account device information such as reported firmware on the devices.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            protocol: Filter to retrieve a specific protocol type used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/devices/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[
                param[str | None]("lastSeenDeviceId", last_seen_device_id),
                param[DevicesProtocolOrStr | None]("protocol", protocol),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3AccountDeviceList],
            error_mapper=get_account_device_information_error_mapper,
            request_options=request_options,
        )

    async def list_account_devices_information(
        self, acc: str, body: DeviceImei | DeviceImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceListResult, ListAccountDevicesInformationErrorBody]:
        """Retrieve device information for a list of devices on an account.

        Args:
            acc: Account identifier.
            body: Request device list information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/devices/{acc}"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceImei | DeviceImeiDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceListResult],
            error_mapper=list_account_devices_information_error_mapper,
            request_options=request_options,
        )
