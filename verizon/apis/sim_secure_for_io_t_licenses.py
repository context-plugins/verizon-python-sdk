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
from ..errors.assign_license_to_devices_error import (
    AssignLicenseToDevicesErrorBody,
    assign_license_to_devices_error_mapper,
)
from ..errors.unassign_license_to_devices_error import (
    UnassignLicenseToDevicesErrorBody,
    unassign_license_to_devices_error_mapper,
)
from ..models.assign_license_request import AssignLicenseRequest, AssignLicenseRequestDict
from ..models.security_success_result import SecuritySuccessResult
from ..server.server import Server


class SimSecureForIoTLicenses:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SimSecureForIoTLicensesWithRawResponse(client, server, auth)

    def assign_license_to_devices(
        self,
        body: AssignLicenseRequest | AssignLicenseRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SecuritySuccessResult:
        """Assigns SIM-Secure for IoT licenses to SIMs.

        Args:
            body: Request to assign license to devices.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: Bad request. Unauthorized request. Request Forbidden. Not Found / Does not exist. Format / Request
                Unacceptable. Too many requests. ``error`` is ``SecurityResult | RawError``."""
        return self._with_raw_response.assign_license_to_devices(
            body, x_request_id=x_request_id, request_options=request_options
        ).unwrap()

    def unassign_license_to_devices(
        self, x_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SecuritySuccessResult:
        """Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from SIMs.

        Args:
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: Bad request. Unauthorized request. Request forbidden. Not Found / Does not exist. Format / Request
                Unacceptable. Too many requests. ``error`` is ``SecurityResult | RawError``."""
        return self._with_raw_response.unassign_license_to_devices(
            x_request_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SimSecureForIoTLicensesWithRawResponse:
        return self._with_raw_response


class AsyncSimSecureForIoTLicenses:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSimSecureForIoTLicensesWithRawResponse(client, server, auth)

    async def assign_license_to_devices(
        self,
        body: AssignLicenseRequest | AssignLicenseRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SecuritySuccessResult:
        """Assigns SIM-Secure for IoT licenses to SIMs.

        Args:
            body: Request to assign license to devices.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: Bad request. Unauthorized request. Request Forbidden. Not Found / Does not exist. Format / Request
                Unacceptable. Too many requests. ``error`` is ``SecurityResult | RawError``."""
        return (
            await self._with_raw_response.assign_license_to_devices(
                body, x_request_id=x_request_id, request_options=request_options
            )
        ).unwrap()

    async def unassign_license_to_devices(
        self, x_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SecuritySuccessResult:
        """Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from SIMs.

        Args:
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success response.

        Raises:
            ApiError: Bad request. Unauthorized request. Request forbidden. Not Found / Does not exist. Format / Request
                Unacceptable. Too many requests. ``error`` is ``SecurityResult | RawError``."""
        return (
            await self._with_raw_response.unassign_license_to_devices(x_request_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSimSecureForIoTLicensesWithRawResponse:
        return self._with_raw_response


class SimSecureForIoTLicensesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def assign_license_to_devices(
        self,
        body: AssignLicenseRequest | AssignLicenseRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SecuritySuccessResult, AssignLicenseToDevicesErrorBody]:
        """Assigns SIM-Secure for IoT licenses to SIMs.

        Args:
            body: Request to assign license to devices.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.m2_m("/v1/devices/license/actions/assign"),
            headers=[param[str | None]("X-Request-ID", x_request_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssignLicenseRequest | AssignLicenseRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SecuritySuccessResult],
            error_mapper=assign_license_to_devices_error_mapper,
            request_options=request_options,
        )

    def unassign_license_to_devices(
        self, x_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SecuritySuccessResult, UnassignLicenseToDevicesErrorBody]:
        """Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from SIMs.

        Args:
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.m2_m("/v1/devices/license/actions/assign"),
            headers=[param[str]("X-Request-ID", x_request_id), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SecuritySuccessResult],
            error_mapper=unassign_license_to_devices_error_mapper,
            request_options=request_options,
        )


class AsyncSimSecureForIoTLicensesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def assign_license_to_devices(
        self,
        body: AssignLicenseRequest | AssignLicenseRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SecuritySuccessResult, AssignLicenseToDevicesErrorBody]:
        """Assigns SIM-Secure for IoT licenses to SIMs.

        Args:
            body: Request to assign license to devices.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.m2_m("/v1/devices/license/actions/assign"),
            headers=[param[str | None]("X-Request-ID", x_request_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssignLicenseRequest | AssignLicenseRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SecuritySuccessResult],
            error_mapper=assign_license_to_devices_error_mapper,
            request_options=request_options,
        )

    async def unassign_license_to_devices(
        self, x_request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SecuritySuccessResult, UnassignLicenseToDevicesErrorBody]:
        """Unassigns SIM-Secure for IoT Flexible and Flexible Bundle license from SIMs.

        Args:
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.m2_m("/v1/devices/license/actions/assign"),
            headers=[param[str]("X-Request-ID", x_request_id), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SecuritySuccessResult],
            error_mapper=unassign_license_to_devices_error_mapper,
            request_options=request_options,
        )
