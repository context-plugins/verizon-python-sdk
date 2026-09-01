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
from ..errors.device_reachability_status_using_post_error import (
    DeviceReachabilityStatusUsingPostErrorBody,
    device_reachability_status_using_post_error_mapper,
)
from ..errors.retrieve_active_monitors_using_post_error import (
    RetrieveActiveMonitorsUsingPostErrorBody,
    retrieve_active_monitors_using_post_error_mapper,
)
from ..models.device_management_result import DeviceManagementResult
from ..models.notification_report_status_request import (
    NotificationReportStatusRequest,
    NotificationReportStatusRequestDict,
)
from ..models.retrieve_monitors_request import RetrieveMonitorsRequest, RetrieveMonitorsRequestDict
from ..server.server import Server


class DeviceDiagnostics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceDiagnosticsWithRawResponse(client, server, auth)

    def device_reachability_status_using_post(
        self,
        body: NotificationReportStatusRequest | NotificationReportStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Retrieve Reachability Report Status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.device_reachability_status_using_post(
            body, request_options=request_options
        ).unwrap()

    def retrieve_active_monitors_using_post(
        self,
        body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Retrieve all the active monitors.

        Args:
            body: Retrieve Monitor Request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.retrieve_active_monitors_using_post(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DeviceDiagnosticsWithRawResponse:
        return self._with_raw_response


class AsyncDeviceDiagnostics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceDiagnosticsWithRawResponse(client, server, auth)

    async def device_reachability_status_using_post(
        self,
        body: NotificationReportStatusRequest | NotificationReportStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Retrieve Reachability Report Status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.device_reachability_status_using_post(body, request_options=request_options)
        ).unwrap()

    async def retrieve_active_monitors_using_post(
        self,
        body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeviceManagementResult:
        """Retrieve all the active monitors.

        Args:
            body: Retrieve Monitor Request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.retrieve_active_monitors_using_post(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceDiagnosticsWithRawResponse:
        return self._with_raw_response


class DeviceDiagnosticsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def device_reachability_status_using_post(
        self,
        body: NotificationReportStatusRequest | NotificationReportStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DeviceReachabilityStatusUsingPostErrorBody]:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Retrieve Reachability Report Status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/diagnostics/basic/devicereachability/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotificationReportStatusRequest | NotificationReportStatusRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=device_reachability_status_using_post_error_mapper,
            request_options=request_options,
        )

    def retrieve_active_monitors_using_post(
        self,
        body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, RetrieveActiveMonitorsUsingPostErrorBody]:
        """Retrieve all the active monitors.

        Args:
            body: Retrieve Monitor Request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/diagnostics/basic/devicereachability/monitors"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RetrieveMonitorsRequest | RetrieveMonitorsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=retrieve_active_monitors_using_post_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceDiagnosticsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def device_reachability_status_using_post(
        self,
        body: NotificationReportStatusRequest | NotificationReportStatusRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, DeviceReachabilityStatusUsingPostErrorBody]:
        """If the devices do not already exist in the account, this API resource adds them before activation.

        Args:
            body: Retrieve Reachability Report Status for a device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/diagnostics/basic/devicereachability/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotificationReportStatusRequest | NotificationReportStatusRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=device_reachability_status_using_post_error_mapper,
            request_options=request_options,
        )

    async def retrieve_active_monitors_using_post(
        self,
        body: RetrieveMonitorsRequest | RetrieveMonitorsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeviceManagementResult, RetrieveActiveMonitorsUsingPostErrorBody]:
        """Retrieve all the active monitors.

        Args:
            body: Retrieve Monitor Request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/diagnostics/basic/devicereachability/monitors"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RetrieveMonitorsRequest | RetrieveMonitorsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=retrieve_active_monitors_using_post_error_mapper,
            request_options=request_options,
        )
