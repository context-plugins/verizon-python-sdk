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
from ..errors.sensorinsightsmetricsquery_error import (
    SensorinsightsmetricsqueryErrorBody,
    sensorinsightsmetricsquery_error_mapper,
)
from ..models.dto_query_metrics import DtoQueryMetrics, DtoQueryMetricsDict
from ..models.dto_query_metrics_response import DtoQueryMetricsResponse
from ..server.server import Server


class SensorInsightsSmartAlertMetrics:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsSmartAlertMetricsWithRawResponse(client, server, auth)

    def sensorinsightsmetricsquery(
        self, body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DtoQueryMetricsResponse:
        """Get Device Alerts for the most recent daily period, up to 30 days.

        Args:
            body: Daily period requested, up to 30 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return self._with_raw_response.sensorinsightsmetricsquery(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsSmartAlertMetricsWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsSmartAlertMetrics:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsSmartAlertMetricsWithRawResponse(client, server, auth)

    async def sensorinsightsmetricsquery(
        self, body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DtoQueryMetricsResponse:
        """Get Device Alerts for the most recent daily period, up to 30 days.

        Args:
            body: Daily period requested, up to 30 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Internal server error. ``error`` is ``ManagementError400 |
                ManagementError | ManagementError403 | ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensorinsightsmetricsquery(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsSmartAlertMetricsWithRawResponse:
        return self._with_raw_response


class SensorInsightsSmartAlertMetricsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensorinsightsmetricsquery(
        self, body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DtoQueryMetricsResponse, SensorinsightsmetricsqueryErrorBody]:
        """Get Device Alerts for the most recent daily period, up to 30 days.

        Args:
            body: Daily period requested, up to 30 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts/actions/metrics"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoQueryMetrics | DtoQueryMetricsDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoQueryMetricsResponse],
            error_mapper=sensorinsightsmetricsquery_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsSmartAlertMetricsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensorinsightsmetricsquery(
        self, body: DtoQueryMetrics | DtoQueryMetricsDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DtoQueryMetricsResponse, SensorinsightsmetricsqueryErrorBody]:
        """Get Device Alerts for the most recent daily period, up to 30 days.

        Args:
            body: Daily period requested, up to 30 days.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/smartAlerts/actions/metrics"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DtoQueryMetrics | DtoQueryMetricsDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoQueryMetricsResponse],
            error_mapper=sensorinsightsmetricsquery_error_mapper,
            request_options=request_options,
        )
