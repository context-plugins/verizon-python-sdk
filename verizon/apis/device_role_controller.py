from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_aclrules_by_vendor_id_error import (
    GetAclrulesByVendorIdErrorBody,
    get_aclrules_by_vendor_id_error_mapper,
)
from ..models.device_role import DeviceRole
from ..server.server import Server


class DeviceRoleController:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceRoleControllerWithRawResponse(client, server, auth)

    def get_acl_rules_by_vendor_id(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceRole]:
        """This API allows the user to get the access control rules defined for them.

        Args:
            vendor_id: The user's Vendor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Access Rules

        Raises:
            ApiError: Unauthorized Bad Request Forbidden Not Acceptable Too many requests ``error`` is ``str |
                RawError``."""
        return self._with_raw_response.get_acl_rules_by_vendor_id(vendor_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceRoleControllerWithRawResponse:
        return self._with_raw_response


class AsyncDeviceRoleController:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceRoleControllerWithRawResponse(client, server, auth)

    async def get_acl_rules_by_vendor_id(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[DeviceRole]:
        """This API allows the user to get the access control rules defined for them.

        Args:
            vendor_id: The user's Vendor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of Access Rules

        Raises:
            ApiError: Unauthorized Bad Request Forbidden Not Acceptable Too many requests ``error`` is ``str |
                RawError``."""
        return (
            await self._with_raw_response.get_acl_rules_by_vendor_id(vendor_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceRoleControllerWithRawResponse:
        return self._with_raw_response


class DeviceRoleControllerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_acl_rules_by_vendor_id(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceRole], GetAclrulesByVendorIdErrorBody]:
        """This API allows the user to get the access control rules defined for them.

        Args:
            vendor_id: The user's Vendor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v1/device-roles/vendor"),
            query_params=[param[str]("VendorID", vendor_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[DeviceRole]],
            error_mapper=get_aclrules_by_vendor_id_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceRoleControllerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_acl_rules_by_vendor_id(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[DeviceRole], GetAclrulesByVendorIdErrorBody]:
        """This API allows the user to get the access control rules defined for them.

        Args:
            vendor_id: The user's Vendor ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v1/device-roles/vendor"),
            query_params=[param[str]("VendorID", vendor_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[DeviceRole]],
            error_mapper=get_aclrules_by_vendor_id_error_mapper,
            request_options=request_options,
        )
