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
from ..errors.calculate_aggregated_report_asynchronous_error import (
    CalculateAggregatedReportAsynchronousErrorBody,
    calculate_aggregated_report_asynchronous_error_mapper,
)
from ..errors.calculate_aggregated_report_synchronous_error import (
    CalculateAggregatedReportSynchronousErrorBody,
    calculate_aggregated_report_synchronous_error_mapper,
)
from ..errors.get_sessions_report_error import GetSessionsReportErrorBody, get_sessions_report_error_mapper
from ..models.aggregate_session_report import AggregateSessionReport
from ..models.aggregate_session_report_request import AggregateSessionReportRequest, AggregateSessionReportRequestDict
from ..models.aggregated_report_callback_result import AggregatedReportCallbackResult
from ..models.session_report import SessionReport
from ..models.session_report_request import SessionReportRequest, SessionReportRequestDict
from ..server.server import Server


class DeviceReports:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceReportsWithRawResponse(client, server, auth)

    def calculate_aggregated_report_asynchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AggregatedReportCallbackResult:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive an
        asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

        Args:
            body: Aggregated session report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response shows the request is queued with a unique ``txid`` to identify the report data with.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.calculate_aggregated_report_asynchronous(
            body, request_options=request_options
        ).unwrap()

    def calculate_aggregated_report_synchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AggregateSessionReport:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive
        synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

        Args:
            body: Aggregated report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response shows session and usage details for up to 10 devices.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.calculate_aggregated_report_synchronous(
            body, request_options=request_options
        ).unwrap()

    def get_sessions_report(
        self,
        body: SessionReportRequest | SessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SessionReport:
        """Detailed report of session duration and number of bytes transferred per day.

        Args:
            body: Request for sessions report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response includes the session information for an individual device.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return self._with_raw_response.get_sessions_report(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceReportsWithRawResponse:
        return self._with_raw_response


class AsyncDeviceReports:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceReportsWithRawResponse(client, server, auth)

    async def calculate_aggregated_report_asynchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AggregatedReportCallbackResult:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive an
        asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

        Args:
            body: Aggregated session report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response shows the request is queued with a unique ``txid`` to identify the report data with.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.calculate_aggregated_report_asynchronous(
                body, request_options=request_options
            )
        ).unwrap()

    async def calculate_aggregated_report_synchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AggregateSessionReport:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive
        synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

        Args:
            body: Aggregated report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response shows session and usage details for up to 10 devices.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (
            await self._with_raw_response.calculate_aggregated_report_synchronous(body, request_options=request_options)
        ).unwrap()

    async def get_sessions_report(
        self,
        body: SessionReportRequest | SessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SessionReport:
        """Detailed report of session duration and number of bytes transferred per day.

        Args:
            body: Request for sessions report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A successful response includes the session information for an individual device.

        Raises:
            ApiError: Bad request. Unauthorized request. Access token is missing or invalid. Forbidden request. Bad
                request. Not found. Bad request. Conflict state. Internal Server Error. ``error`` is
                ``HyperPreciseLocationResult | RawError``."""
        return (await self._with_raw_response.get_sessions_report(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceReportsWithRawResponse:
        return self._with_raw_response


class DeviceReportsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def calculate_aggregated_report_asynchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AggregatedReportCallbackResult, CalculateAggregatedReportAsynchronousErrorBody]:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive an
        asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

        Args:
            body: Aggregated session report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/report/async/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AggregateSessionReportRequest | AggregateSessionReportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AggregatedReportCallbackResult],
            error_mapper=calculate_aggregated_report_asynchronous_error_mapper,
            request_options=request_options,
        )

    def calculate_aggregated_report_synchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AggregateSessionReport, CalculateAggregatedReportSynchronousErrorBody]:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive
        synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

        Args:
            body: Aggregated report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/report/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AggregateSessionReportRequest | AggregateSessionReportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AggregateSessionReport],
            error_mapper=calculate_aggregated_report_synchronous_error_mapper,
            request_options=request_options,
        )

    def get_sessions_report(
        self,
        body: SessionReportRequest | SessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SessionReport, GetSessionsReportErrorBody]:
        """Detailed report of session duration and number of bytes transferred per day.

        Args:
            body: Request for sessions report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/report/sessions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SessionReportRequest | SessionReportRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SessionReport],
            error_mapper=get_sessions_report_error_mapper,
            request_options=request_options,
        )


class AsyncDeviceReportsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def calculate_aggregated_report_asynchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AggregatedReportCallbackResult, CalculateAggregatedReportAsynchronousErrorBody]:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive an
        asynchronous callback for the specified list of devices (Max 10000) and date range (Max 180 days).

        Args:
            body: Aggregated session report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/report/async/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AggregateSessionReportRequest | AggregateSessionReportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AggregatedReportCallbackResult],
            error_mapper=calculate_aggregated_report_asynchronous_error_mapper,
            request_options=request_options,
        )

    async def calculate_aggregated_report_synchronous(
        self,
        body: AggregateSessionReportRequest | AggregateSessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AggregateSessionReport, CalculateAggregatedReportSynchronousErrorBody]:
        """Calculate aggregated report per day with number of sessions and usage information. User will receive
        synchronous response for specified list of devices (Max 10) and date range (Max 180 days).

        Args:
            body: Aggregated report request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/report/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AggregateSessionReportRequest | AggregateSessionReportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AggregateSessionReport],
            error_mapper=calculate_aggregated_report_synchronous_error_mapper,
            request_options=request_options,
        )

    async def get_sessions_report(
        self,
        body: SessionReportRequest | SessionReportRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SessionReport, GetSessionsReportErrorBody]:
        """Detailed report of session duration and number of bytes transferred per day.

        Args:
            body: Request for sessions report.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_location("/report/sessions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SessionReportRequest | SessionReportRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SessionReport],
            error_mapper=get_sessions_report_error_mapper,
            request_options=request_options,
        )
