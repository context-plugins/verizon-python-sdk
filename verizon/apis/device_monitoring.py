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
from ..errors.device_reachability_error import DeviceReachabilityErrorBody, device_reachability_error_mapper
from ..errors.stop_device_reachability_error import (
    StopDeviceReachabilityErrorBody,
    stop_device_reachability_error_mapper,
)
from ..models.notification_report_request import NotificationReportRequest, NotificationReportRequestDict
from ..models.request_response import RequestResponse
from ..models.stop_monitor_request import StopMonitorRequest, StopMonitorRequestDict
from ..server.server import Server


class DeviceMonitoring:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceMonitoringWithRawResponse(client, server, auth)

    def device_reachability(
        self,
        body: NotificationReportRequest | NotificationReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Send a ``POST`` request.

        Args:
            body: Create Reachability Report Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.device_reachability(body, request_options=request_options).unwrap()

    def stop_device_reachability(
        self,
        stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Send a ``DELETE`` request.

        Args:
            stopreachabilitypayload: Payload for the Stop Device Reachability monitors request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return self._with_raw_response.stop_device_reachability(
            stopreachabilitypayload, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DeviceMonitoringWithRawResponse:
        return self._with_raw_response


class AsyncDeviceMonitoring:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceMonitoringWithRawResponse(client, server, auth)

    async def device_reachability(
        self,
        body: NotificationReportRequest | NotificationReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Send a ``POST`` request.

        Args:
            body: Create Reachability Report Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return (await self._with_raw_response.device_reachability(body, request_options=request_options)).unwrap()

    async def stop_device_reachability(
        self,
        stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RequestResponse:
        """Send a ``DELETE`` request.

        Args:
            stopreachabilitypayload: Payload for the Stop Device Reachability monitors request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Error Response ``error`` is ``RestErrorResponse | RawError``."""
        return (
            await self._with_raw_response.stop_device_reachability(
                stopreachabilitypayload, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceMonitoringWithRawResponse:
        return self._with_raw_response


class DeviceMonitoringWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def device_reachability(
        self,
        body: NotificationReportRequest | NotificationReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DeviceReachabilityErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Create Reachability Report Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/diagnostics/basic/devicereachability"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotificationReportRequest | NotificationReportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=device_reachability_error_mapper,
            request_options=request_options,
        )

    def stop_device_reachability(
        self,
        stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, StopDeviceReachabilityErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            stopreachabilitypayload: Payload for the Stop Device Reachability monitors request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/diagnostics/basic/devicereachability"),
            query_params=[
                param[StopMonitorRequest | StopMonitorRequestDict]("stopreachabilitypayload", stopreachabilitypayload)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=stop_device_reachability_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceMonitoringWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def device_reachability(
        self,
        body: NotificationReportRequest | NotificationReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, DeviceReachabilityErrorBody]:
        """Send a ``POST`` request.

        Args:
            body: Create Reachability Report Request
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/diagnostics/basic/devicereachability"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NotificationReportRequest | NotificationReportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=device_reachability_error_mapper,
            request_options=request_options,
        )

    async def stop_device_reachability(
        self,
        stopreachabilitypayload: StopMonitorRequest | StopMonitorRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RequestResponse, StopDeviceReachabilityErrorBody]:
        """Send a ``DELETE`` request.

        Args:
            stopreachabilitypayload: Payload for the Stop Device Reachability monitors request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/diagnostics/basic/devicereachability"),
            query_params=[
                param[StopMonitorRequest | StopMonitorRequestDict]("stopreachabilitypayload", stopreachabilitypayload)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[RequestResponse],
            error_mapper=stop_device_reachability_error_mapper,
            request_options=request_options,
        )
