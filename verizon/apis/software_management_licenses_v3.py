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
from ..errors.assign_licenses_to_devices3_error import (
    AssignLicensesToDevices3ErrorBody,
    assign_licenses_to_devices3_error_mapper,
)
from ..errors.get_account_licenses_status_error import (
    GetAccountLicensesStatusErrorBody,
    get_account_licenses_status_error_mapper,
)
from ..errors.remove_licenses_from_devices3_error import (
    RemoveLicensesFromDevices3ErrorBody,
    remove_licenses_from_devices3_error_mapper,
)
from ..models.v3_license_assigned_removed_result import V3LicenseAssignedRemovedResult
from ..models.v3_license_imei import V3LicenseImei, V3LicenseImeiDict
from ..models.v3_license_summary import V3LicenseSummary
from ..server.server import Server


class SoftwareManagementLicensesV3:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementLicensesV3WithRawResponse(client, server, auth)

    def assign_licenses_to_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> V3LicenseAssignedRemovedResult:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            acc: Account identifier.
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License assignment result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.assign_licenses_to_devices3(acc, body, request_options=request_options).unwrap()

    def get_account_licenses_status(
        self, acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> V3LicenseSummary:
        """The endpoint allows user to list license usage.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of license assignment.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_account_licenses_status(
            acc, last_seen_device_id=last_seen_device_id, request_options=request_options
        ).unwrap()

    def remove_licenses_from_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> V3LicenseAssignedRemovedResult:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            acc: Account identifier.
            body: License removal.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License removal result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.remove_licenses_from_devices3(
            acc, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementLicensesV3WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementLicensesV3:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementLicensesV3WithRawResponse(client, server, auth)

    async def assign_licenses_to_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> V3LicenseAssignedRemovedResult:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            acc: Account identifier.
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License assignment result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.assign_licenses_to_devices3(acc, body, request_options=request_options)
        ).unwrap()

    async def get_account_licenses_status(
        self, acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> V3LicenseSummary:
        """The endpoint allows user to list license usage.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Summary of license assignment.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_account_licenses_status(
                acc, last_seen_device_id=last_seen_device_id, request_options=request_options
            )
        ).unwrap()

    async def remove_licenses_from_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> V3LicenseAssignedRemovedResult:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            acc: Account identifier.
            body: License removal.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            License removal result.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.remove_licenses_from_devices3(acc, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementLicensesV3WithRawResponse:
        return self._with_raw_response


class SoftwareManagementLicensesV3WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def assign_licenses_to_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V3LicenseAssignedRemovedResult, AssignLicensesToDevices3ErrorBody]:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            acc: Account identifier.
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/licenses/{acc}/assign"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3LicenseImei | V3LicenseImeiDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3LicenseAssignedRemovedResult],
            error_mapper=assign_licenses_to_devices3_error_mapper,
            request_options=request_options,
        )

    def get_account_licenses_status(
        self, acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V3LicenseSummary, GetAccountLicensesStatusErrorBody]:
        """The endpoint allows user to list license usage.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/licenses/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3LicenseSummary],
            error_mapper=get_account_licenses_status_error_mapper,
            request_options=request_options,
        )

    def remove_licenses_from_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V3LicenseAssignedRemovedResult, RemoveLicensesFromDevices3ErrorBody]:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            acc: Account identifier.
            body: License removal.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/licenses/{acc}/remove"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3LicenseImei | V3LicenseImeiDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3LicenseAssignedRemovedResult],
            error_mapper=remove_licenses_from_devices3_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementLicensesV3WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def assign_licenses_to_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V3LicenseAssignedRemovedResult, AssignLicensesToDevices3ErrorBody]:
        """This endpoint allows user to assign licenses to a list of devices.

        Args:
            acc: Account identifier.
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/licenses/{acc}/assign"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3LicenseImei | V3LicenseImeiDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3LicenseAssignedRemovedResult],
            error_mapper=assign_licenses_to_devices3_error_mapper,
            request_options=request_options,
        )

    async def get_account_licenses_status(
        self, acc: str, *, last_seen_device_id: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V3LicenseSummary, GetAccountLicensesStatusErrorBody]:
        """The endpoint allows user to list license usage.

        Args:
            acc: Account identifier.
            last_seen_device_id: Last seen device identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/licenses/{acc}"),
            path_params=[param[str]("acc", acc)],
            query_params=[param[str | None]("lastSeenDeviceId", last_seen_device_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3LicenseSummary],
            error_mapper=get_account_licenses_status_error_mapper,
            request_options=request_options,
        )

    async def remove_licenses_from_devices3(
        self, acc: str, body: V3LicenseImei | V3LicenseImeiDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V3LicenseAssignedRemovedResult, RemoveLicensesFromDevices3ErrorBody]:
        """This endpoint allows user to remove licenses from a list of devices.

        Args:
            acc: Account identifier.
            body: License removal.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.software_management_v3("/licenses/{acc}/remove"),
            path_params=[param[str]("acc", acc)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V3LicenseImei | V3LicenseImeiDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V3LicenseAssignedRemovedResult],
            error_mapper=remove_licenses_from_devices3_error_mapper,
            request_options=request_options,
        )
