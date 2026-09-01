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
    json_body,
    json_decoder,
    param,
)
from ..errors.assign_licenses_to_devices_error import (
    AssignLicensesToDevicesErrorBody,
    assign_licenses_to_devices_error_mapper,
)
from ..errors.create_list_of_licenses_to_remove_error import (
    CreateListOfLicensesToRemoveErrorBody,
    create_list_of_licenses_to_remove_error_mapper,
)
from ..errors.delete_list_of_licenses_to_remove_error import (
    DeleteListOfLicensesToRemoveErrorBody,
    delete_list_of_licenses_to_remove_error_mapper,
)
from ..errors.list_licenses_to_remove_error import ListLicensesToRemoveErrorBody, list_licenses_to_remove_error_mapper
from ..errors.remove_licenses_from_devices_error import (
    RemoveLicensesFromDevicesErrorBody,
    remove_licenses_from_devices_error_mapper,
)
from ..models.v1_licenses_assigned_removed_request import (
    V1LicensesAssignedRemovedRequest,
    V1LicensesAssignedRemovedRequestDict,
)
from ..models.v1_licenses_assigned_removed_result import V1LicensesAssignedRemovedResult
from ..models.v1_list_of_licenses_to_remove import V1ListOfLicensesToRemove
from ..models.v1_list_of_licenses_to_remove_request import (
    V1ListOfLicensesToRemoveRequest,
    V1ListOfLicensesToRemoveRequestDict,
)
from ..models.v1_list_of_licenses_to_remove_result import V1ListOfLicensesToRemoveResult
from ..server.server import Server


class SoftwareManagementLicensesV1:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementLicensesV1WithRawResponse(client, server, auth)

    def assign_licenses_to_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1LicensesAssignedRemovedResult:
        """Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to assign licenses to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of licenses assigned.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.assign_licenses_to_devices(
            account, body, request_options=request_options
        ).unwrap()

    def create_list_of_licenses_to_remove(
        self,
        account: str,
        body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1ListOfLicensesToRemoveResult:
        """Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            body: Cancellation candidate device list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of licenses assigned.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.create_list_of_licenses_to_remove(
            account, body, request_options=request_options
        ).unwrap()

    def delete_list_of_licenses_to_remove(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes the entire list of cancellation candidate devices.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upgrade canceled.

        Raises:
            ApiError: Unexpected error. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_list_of_licenses_to_remove(
            account, request_options=request_options
        ).unwrap()

    def list_licenses_to_remove(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1ListOfLicensesToRemove:
        """Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of cancellation candidate devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.list_licenses_to_remove(
            account, start_index, request_options=request_options
        ).unwrap()

    def remove_licenses_from_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1LicensesAssignedRemovedResult:
        """Remove unused licenses from device.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to remove licenses from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of devices with license removal status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.remove_licenses_from_devices(
            account, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementLicensesV1WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementLicensesV1:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementLicensesV1WithRawResponse(client, server, auth)

    async def assign_licenses_to_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1LicensesAssignedRemovedResult:
        """Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to assign licenses to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of licenses assigned.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.assign_licenses_to_devices(account, body, request_options=request_options)
        ).unwrap()

    async def create_list_of_licenses_to_remove(
        self,
        account: str,
        body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1ListOfLicensesToRemoveResult:
        """Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            body: Cancellation candidate device list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of licenses assigned.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.create_list_of_licenses_to_remove(
                account, body, request_options=request_options
            )
        ).unwrap()

    async def delete_list_of_licenses_to_remove(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes the entire list of cancellation candidate devices.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Upgrade canceled.

        Raises:
            ApiError: Unexpected error. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_list_of_licenses_to_remove(account, request_options=request_options)
        ).unwrap()

    async def list_licenses_to_remove(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1ListOfLicensesToRemove:
        """Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of cancellation candidate devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.list_licenses_to_remove(account, start_index, request_options=request_options)
        ).unwrap()

    async def remove_licenses_from_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1LicensesAssignedRemovedResult:
        """Remove unused licenses from device.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to remove licenses from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of devices with license removal status.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.remove_licenses_from_devices(account, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementLicensesV1WithRawResponse:
        return self._with_raw_response


class SoftwareManagementLicensesV1WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def assign_licenses_to_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1LicensesAssignedRemovedResult, AssignLicensesToDevicesErrorBody]:
        """Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to assign licenses to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/licenses/{account}/assign"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1LicensesAssignedRemovedResult],
            error_mapper=assign_licenses_to_devices_error_mapper,
            request_options=request_options,
        )

    def create_list_of_licenses_to_remove(
        self,
        account: str,
        body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1ListOfLicensesToRemoveResult, CreateListOfLicensesToRemoveErrorBody]:
        """Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            body: Cancellation candidate device list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1ListOfLicensesToRemoveResult],
            error_mapper=create_list_of_licenses_to_remove_error_mapper,
            request_options=request_options,
        )

    def delete_list_of_licenses_to_remove(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteListOfLicensesToRemoveErrorBody]:
        """Deletes the entire list of cancellation candidate devices.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v1("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=delete_list_of_licenses_to_remove_error_mapper,
            request_options=request_options,
        )

    def list_licenses_to_remove(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1ListOfLicensesToRemove, ListLicensesToRemoveErrorBody]:
        """Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/licenses/{account}/cancel/index/{startIndex}"),
            path_params=[param[str]("account", account), param[str]("startIndex", start_index)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1ListOfLicensesToRemove],
            error_mapper=list_licenses_to_remove_error_mapper,
            request_options=request_options,
        )

    def remove_licenses_from_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1LicensesAssignedRemovedResult, RemoveLicensesFromDevicesErrorBody]:
        """Remove unused licenses from device.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to remove licenses from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/licenses/{account}/remove"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1LicensesAssignedRemovedResult],
            error_mapper=remove_licenses_from_devices_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementLicensesV1WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def assign_licenses_to_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1LicensesAssignedRemovedResult, AssignLicensesToDevicesErrorBody]:
        """Assigns licenses to a specified list of devices so that firmware upgrades can be scheduled for those devices.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to assign licenses to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/licenses/{account}/assign"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1LicensesAssignedRemovedResult],
            error_mapper=assign_licenses_to_devices_error_mapper,
            request_options=request_options,
        )

    async def create_list_of_licenses_to_remove(
        self,
        account: str,
        body: V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1ListOfLicensesToRemoveResult, CreateListOfLicensesToRemoveErrorBody]:
        """Creates a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            body: Cancellation candidate device list.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1ListOfLicensesToRemoveRequest | V1ListOfLicensesToRemoveRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1ListOfLicensesToRemoveResult],
            error_mapper=create_list_of_licenses_to_remove_error_mapper,
            request_options=request_options,
        )

    async def delete_list_of_licenses_to_remove(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteListOfLicensesToRemoveErrorBody]:
        """Deletes the entire list of cancellation candidate devices.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v1("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=delete_list_of_licenses_to_remove_error_mapper,
            request_options=request_options,
        )

    async def list_licenses_to_remove(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1ListOfLicensesToRemove, ListLicensesToRemoveErrorBody]:
        """Returns a list of devices from which licenses will be removed if the number of MRC licenses becomes less than
        the number of assigned licenses.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/licenses/{account}/cancel/index/{startIndex}"),
            path_params=[param[str]("account", account), param[str]("startIndex", start_index)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1ListOfLicensesToRemove],
            error_mapper=list_licenses_to_remove_error_mapper,
            request_options=request_options,
        )

    async def remove_licenses_from_devices(
        self,
        account: str,
        body: V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1LicensesAssignedRemovedResult, RemoveLicensesFromDevicesErrorBody]:
        """Remove unused licenses from device.

        Args:
            account: Account identifier in "##########-#####".
            body: IMEIs of the devices to remove licenses from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v1("/licenses/{account}/remove"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1LicensesAssignedRemovedRequest | V1LicensesAssignedRemovedRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1LicensesAssignedRemovedResult],
            error_mapper=remove_licenses_from_devices_error_mapper,
            request_options=request_options,
        )
