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
    json_decoder,
    param,
)
from ..errors.assign_licenses_to_devices2_error import (
    AssignLicensesToDevices2ErrorBody,
    assign_licenses_to_devices2_error_mapper,
)
from ..errors.create_list_of_licenses_to_remove2_error import (
    CreateListOfLicensesToRemove2ErrorBody,
    create_list_of_licenses_to_remove2_error_mapper,
)
from ..errors.delete_list_of_licenses_to_remove2_error import (
    DeleteListOfLicensesToRemove2ErrorBody,
    delete_list_of_licenses_to_remove2_error_mapper,
)
from ..errors.get_account_license_status2_error import (
    GetAccountLicenseStatus2ErrorBody,
    get_account_license_status2_error_mapper,
)
from ..errors.list_licenses_to_remove2_error import (
    ListLicensesToRemove2ErrorBody,
    list_licenses_to_remove2_error_mapper,
)
from ..errors.remove_licenses_from_devices2_error import (
    RemoveLicensesFromDevices2ErrorBody,
    remove_licenses_from_devices2_error_mapper,
)
from ..models.fota_v2_success_result import FotaV2SuccessResult
from ..models.v2_license_summary import V2LicenseSummary
from ..models.v2_licenses_assigned_removed_result import V2LicensesAssignedRemovedResult
from ..models.v2_list_of_licenses_to_remove import V2ListOfLicensesToRemove
from ..models.v2_list_of_licenses_to_remove_result import V2ListOfLicensesToRemoveResult
from ..server.server import Server


class SoftwareManagementLicensesV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementLicensesV2WithRawResponse(client, server, auth)

    def assign_licenses_to_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2LicensesAssignedRemovedResult:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License assignment result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.assign_licenses_to_devices2(account, request_options=request_options).unwrap()

    def create_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2ListOfLicensesToRemoveResult:
        """The license cancel endpoint allows user to create a list of license cancellation candidate devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return a created license cancellation device list.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.create_list_of_licenses_to_remove2(
            account, request_options=request_options
        ).unwrap()

    def delete_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2SuccessResult:
        """This endpoint allows user to delete a created cancel candidate device list.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of deletion of candidate list of devices to remove.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.delete_list_of_licenses_to_remove2(
            account, request_options=request_options
        ).unwrap()

    def get_account_license_status2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2LicenseSummary:
        """The endpoint allows user to list license usage.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of license assignment.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_account_license_status2(
            account, last_seen_device_id=last_seen_device_id, request_options=request_options
        ).unwrap()

    def list_licenses_to_remove2(
        self, account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> V2ListOfLicensesToRemove:
        """The license cancel endpoint allows user to list registered license cancellation candidate devices.

        Args:
            account: Account identifier.
            start_index: Start index to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of license cancellation candidate devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.list_licenses_to_remove2(
            account, start_index=start_index, request_options=request_options
        ).unwrap()

    def remove_licenses_from_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2LicensesAssignedRemovedResult:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License removal result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.remove_licenses_from_devices2(account, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementLicensesV2WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementLicensesV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementLicensesV2WithRawResponse(client, server, auth)

    async def assign_licenses_to_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2LicensesAssignedRemovedResult:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License assignment result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.assign_licenses_to_devices2(account, request_options=request_options)
        ).unwrap()

    async def create_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2ListOfLicensesToRemoveResult:
        """The license cancel endpoint allows user to create a list of license cancellation candidate devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Return a created license cancellation device list.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.create_list_of_licenses_to_remove2(account, request_options=request_options)
        ).unwrap()

    async def delete_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2SuccessResult:
        """This endpoint allows user to delete a created cancel candidate device list.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Result of deletion of candidate list of devices to remove.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.delete_list_of_licenses_to_remove2(account, request_options=request_options)
        ).unwrap()

    async def get_account_license_status2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V2LicenseSummary:
        """The endpoint allows user to list license usage.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of license assignment.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_account_license_status2(
                account, last_seen_device_id=last_seen_device_id, request_options=request_options
            )
        ).unwrap()

    async def list_licenses_to_remove2(
        self, account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> V2ListOfLicensesToRemove:
        """The license cancel endpoint allows user to list registered license cancellation candidate devices.

        Args:
            account: Account identifier.
            start_index: Start index to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A list of license cancellation candidate devices.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.list_licenses_to_remove2(
                account, start_index=start_index, request_options=request_options
            )
        ).unwrap()

    async def remove_licenses_from_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V2LicensesAssignedRemovedResult:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License removal result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.remove_licenses_from_devices2(account, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementLicensesV2WithRawResponse:
        return self._with_raw_response


class SoftwareManagementLicensesV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def assign_licenses_to_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2LicensesAssignedRemovedResult, AssignLicensesToDevices2ErrorBody]:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/licenses/{account}/assign"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2LicensesAssignedRemovedResult],
            error_mapper=assign_licenses_to_devices2_error_mapper,
            request_options=request_options,
        )

    def create_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2ListOfLicensesToRemoveResult, CreateListOfLicensesToRemove2ErrorBody]:
        """The license cancel endpoint allows user to create a list of license cancellation candidate devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2ListOfLicensesToRemoveResult],
            error_mapper=create_list_of_licenses_to_remove2_error_mapper,
            request_options=request_options,
        )

    def delete_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2SuccessResult, DeleteListOfLicensesToRemove2ErrorBody]:
        """This endpoint allows user to delete a created cancel candidate device list.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2SuccessResult],
            error_mapper=delete_list_of_licenses_to_remove2_error_mapper,
            request_options=request_options,
        )

    def get_account_license_status2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2LicenseSummary, GetAccountLicenseStatus2ErrorBody]:
        """The endpoint allows user to list license usage.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/licenses/{account}"),
            path_params=[param[str]("account", account)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2LicenseSummary],
            error_mapper=get_account_license_status2_error_mapper,
            request_options=request_options,
        )

    def list_licenses_to_remove2(
        self, account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2ListOfLicensesToRemove, ListLicensesToRemove2ErrorBody]:
        """The license cancel endpoint allows user to list registered license cancellation candidate devices.

        Args:
            account: Account identifier.
            start_index: Start index to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            query_params=[param[str | None]("startIndex", start_index)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2ListOfLicensesToRemove],
            error_mapper=list_licenses_to_remove2_error_mapper,
            request_options=request_options,
        )

    def remove_licenses_from_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2LicensesAssignedRemovedResult, RemoveLicensesFromDevices2ErrorBody]:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/licenses/{account}/remove"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2LicensesAssignedRemovedResult],
            error_mapper=remove_licenses_from_devices2_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementLicensesV2WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def assign_licenses_to_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2LicensesAssignedRemovedResult, AssignLicensesToDevices2ErrorBody]:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/licenses/{account}/assign"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2LicensesAssignedRemovedResult],
            error_mapper=assign_licenses_to_devices2_error_mapper,
            request_options=request_options,
        )

    async def create_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2ListOfLicensesToRemoveResult, CreateListOfLicensesToRemove2ErrorBody]:
        """The license cancel endpoint allows user to create a list of license cancellation candidate devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2ListOfLicensesToRemoveResult],
            error_mapper=create_list_of_licenses_to_remove2_error_mapper,
            request_options=request_options,
        )

    async def delete_list_of_licenses_to_remove2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2SuccessResult, DeleteListOfLicensesToRemove2ErrorBody]:
        """This endpoint allows user to delete a created cancel candidate device list.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.software_management_v2("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2SuccessResult],
            error_mapper=delete_list_of_licenses_to_remove2_error_mapper,
            request_options=request_options,
        )

    async def get_account_license_status2(
        self,
        account: str,
        *,
        last_seen_device_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V2LicenseSummary, GetAccountLicenseStatus2ErrorBody]:
        """The endpoint allows user to list license usage.

        Args:
            account: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/licenses/{account}"),
            path_params=[param[str]("account", account)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2LicenseSummary],
            error_mapper=get_account_license_status2_error_mapper,
            request_options=request_options,
        )

    async def list_licenses_to_remove2(
        self, account: str, *, start_index: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2ListOfLicensesToRemove, ListLicensesToRemove2ErrorBody]:
        """The license cancel endpoint allows user to list registered license cancellation candidate devices.

        Args:
            account: Account identifier.
            start_index: Start index to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/licenses/{account}/cancel"),
            path_params=[param[str]("account", account)],
            query_params=[param[str | None]("startIndex", start_index)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2ListOfLicensesToRemove],
            error_mapper=list_licenses_to_remove2_error_mapper,
            request_options=request_options,
        )

    async def remove_licenses_from_devices2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V2LicensesAssignedRemovedResult, RemoveLicensesFromDevices2ErrorBody]:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v2("/licenses/{account}/remove"),
            path_params=[param[str]("account", account)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V2LicensesAssignedRemovedResult],
            error_mapper=remove_licenses_from_devices2_error_mapper,
            request_options=request_options,
        )
