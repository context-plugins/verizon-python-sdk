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
from ..errors.create_device_group_error import CreateDeviceGroupErrorBody, create_device_group_error_mapper
from ..errors.delete_device_group_error import DeleteDeviceGroupErrorBody, delete_device_group_error_mapper
from ..errors.get_device_group_information_error import (
    GetDeviceGroupInformationErrorBody,
    get_device_group_information_error_mapper,
)
from ..errors.list_device_groups_error import ListDeviceGroupsErrorBody, list_device_groups_error_mapper
from ..errors.update_device_group_error import UpdateDeviceGroupErrorBody, update_device_group_error_mapper
from ..models.connectivity_management_success_result import ConnectivityManagementSuccessResult
from ..models.create_device_group_request import CreateDeviceGroupRequest, CreateDeviceGroupRequestDict
from ..models.device_group import DeviceGroup
from ..models.device_group_devices_data import DeviceGroupDevicesData
from ..models.device_group_update_request import DeviceGroupUpdateRequest, DeviceGroupUpdateRequestDict
from ..server.server import Server


class DeviceGroups:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceGroupsWithRawResponse(client, server, auth)

    def create_device_group(
        self,
        body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectivityManagementSuccessResult:
        """Create a new device group and optionally add devices to the group. Device groups can make it easier to manage
        similar devices and to get reports on their usage.

        Args:
            body: A request to create a new device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response, Creates a new device group.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.create_device_group(body, request_options=request_options).unwrap()

    def delete_device_group(
        self, aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConnectivityManagementSuccessResult:
        """Deletes a device group from the account. Devices in the group are moved to the default device group and are
        not deleted from the account.

        Args:
            aname: Account name.
            gname: Group name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.delete_device_group(aname, gname, request_options=request_options).unwrap()

    def get_device_group_information(
        self, aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceGroupDevicesData:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

        Args:
            aname: Account name.
            gname: Group name.
            next: Continue the previous query from the pageUrl pagetoken.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.get_device_group_information(
            aname, gname, next=next, request_options=request_options
        ).unwrap()

    def list_device_groups(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceGroup]:
        """Returns a list of all device groups in a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of device groups in the account.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_device_groups(aname, request_options=request_options).unwrap()

    def update_device_group(
        self,
        aname: str,
        gname: str,
        body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectivityManagementSuccessResult:
        """Make changes to a device group, including changing the name and description, and adding or removing devices.

        Args:
            aname: Account name.
            gname: Group name.
            body: Request to update device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.update_device_group(aname, gname, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceGroupsWithRawResponse:
        return self._with_raw_response


class AsyncDeviceGroups:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceGroupsWithRawResponse(client, server, auth)

    async def create_device_group(
        self,
        body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectivityManagementSuccessResult:
        """Create a new device group and optionally add devices to the group. Device groups can make it easier to manage
        similar devices and to get reports on their usage.

        Args:
            body: A request to create a new device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response, Creates a new device group.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.create_device_group(body, request_options=request_options)).unwrap()

    async def delete_device_group(
        self, aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConnectivityManagementSuccessResult:
        """Deletes a device group from the account. Devices in the group are moved to the default device group and are
        not deleted from the account.

        Args:
            aname: Account name.
            gname: Group name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.delete_device_group(aname, gname, request_options=request_options)
        ).unwrap()

    async def get_device_group_information(
        self, aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceGroupDevicesData:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

        Args:
            aname: Account name.
            gname: Group name.
            next: Continue the previous query from the pageUrl pagetoken.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.get_device_group_information(
                aname, gname, next=next, request_options=request_options
            )
        ).unwrap()

    async def list_device_groups(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceGroup]:
        """Returns a list of all device groups in a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of device groups in the account.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.list_device_groups(aname, request_options=request_options)).unwrap()

    async def update_device_group(
        self,
        aname: str,
        gname: str,
        body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectivityManagementSuccessResult:
        """Make changes to a device group, including changing the name and description, and adding or removing devices.

        Args:
            aname: Account name.
            gname: Group name.
            body: Request to update device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.update_device_group(aname, gname, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceGroupsWithRawResponse:
        return self._with_raw_response


class DeviceGroupsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_device_group(
        self,
        body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectivityManagementSuccessResult, CreateDeviceGroupErrorBody]:
        """Create a new device group and optionally add devices to the group. Device groups can make it easier to manage
        similar devices and to get reports on their usage.

        Args:
            body: A request to create a new device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateDeviceGroupRequest | CreateDeviceGroupRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=create_device_group_error_mapper,
            request_options=request_options,
        )

    def delete_device_group(
        self, aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConnectivityManagementSuccessResult, DeleteDeviceGroupErrorBody]:
        """Deletes a device group from the account. Devices in the group are moved to the default device group and are
        not deleted from the account.

        Args:
            aname: Account name.
            gname: Group name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}/name/{gname}"),
            path_params=[param[str]("aname", aname), param[str]("gname", gname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=delete_device_group_error_mapper,
            request_options=request_options,
        )

    def get_device_group_information(
        self, aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceGroupDevicesData, GetDeviceGroupInformationErrorBody]:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

        Args:
            aname: Account name.
            gname: Group name.
            next: Continue the previous query from the pageUrl pagetoken.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}/name/{gname}"),
            path_params=[param[str]("aname", aname), param[str]("gname", gname)],
            query_params=[param[int | None]("next", next)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceGroupDevicesData],
            error_mapper=get_device_group_information_error_mapper,
            request_options=request_options,
        )

    def list_device_groups(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceGroup], ListDeviceGroupsErrorBody]:
        """Returns a list of all device groups in a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceGroup]],
            error_mapper=list_device_groups_error_mapper,
            request_options=request_options,
        )

    def update_device_group(
        self,
        aname: str,
        gname: str,
        body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectivityManagementSuccessResult, UpdateDeviceGroupErrorBody]:
        """Make changes to a device group, including changing the name and description, and adding or removing devices.

        Args:
            aname: Account name.
            gname: Group name.
            body: Request to update device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}/name/{gname}"),
            path_params=[param[str]("aname", aname), param[str]("gname", gname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=update_device_group_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceGroupsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_device_group(
        self,
        body: CreateDeviceGroupRequest | CreateDeviceGroupRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectivityManagementSuccessResult, CreateDeviceGroupErrorBody]:
        """Create a new device group and optionally add devices to the group. Device groups can make it easier to manage
        similar devices and to get reports on their usage.

        Args:
            body: A request to create a new device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateDeviceGroupRequest | CreateDeviceGroupRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=create_device_group_error_mapper,
            request_options=request_options,
        )

    async def delete_device_group(
        self, aname: str, gname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConnectivityManagementSuccessResult, DeleteDeviceGroupErrorBody]:
        """Deletes a device group from the account. Devices in the group are moved to the default device group and are
        not deleted from the account.

        Args:
            aname: Account name.
            gname: Group name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}/name/{gname}"),
            path_params=[param[str]("aname", aname), param[str]("gname", gname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=delete_device_group_error_mapper,
            request_options=request_options,
        )

    async def get_device_group_information(
        self, aname: str, gname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceGroupDevicesData, GetDeviceGroupInformationErrorBody]:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /groups/{aname}/name/{gname}/?next={token}. This URL can be used to request the next set of groups.

        Args:
            aname: Account name.
            gname: Group name.
            next: Continue the previous query from the pageUrl pagetoken.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}/name/{gname}"),
            path_params=[param[str]("aname", aname), param[str]("gname", gname)],
            query_params=[param[int | None]("next", next)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceGroupDevicesData],
            error_mapper=get_device_group_information_error_mapper,
            request_options=request_options,
        )

    async def list_device_groups(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceGroup], ListDeviceGroupsErrorBody]:
        """Returns a list of all device groups in a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[DeviceGroup]],
            error_mapper=list_device_groups_error_mapper,
            request_options=request_options,
        )

    async def update_device_group(
        self,
        aname: str,
        gname: str,
        body: DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectivityManagementSuccessResult, UpdateDeviceGroupErrorBody]:
        """Make changes to a device group, including changing the name and description, and adding or removing devices.

        Args:
            aname: Account name.
            gname: Group name.
            body: Request to update device group.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/groups/{aname}/name/{gname}"),
            path_params=[param[str]("aname", aname), param[str]("gname", gname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeviceGroupUpdateRequest | DeviceGroupUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=update_device_group_error_mapper,
            request_options=request_options,
        )
