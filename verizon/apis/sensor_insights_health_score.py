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
from ..errors.sensor_insights_get_network_health_score_response_error import (
    SensorInsightsGetNetworkHealthScoreResponseErrorBody,
    sensor_insights_get_network_health_score_response_error_mapper,
)
from ..errors.sensor_insights_health_score_summary_error import (
    SensorInsightsHealthScoreSummaryErrorBody,
    sensor_insights_health_score_summary_error_mapper,
)
from ..models.dto_get_network_health_score_response import DtoGetNetworkHealthScoreResponse
from ..models.dto_health_score_summary import DtoHealthScoreSummary
from ..server.server import Server


class SensorInsightsHealthScore:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SensorInsightsHealthScoreWithRawResponse(client, server, auth)

    def sensor_insights_get_network_health_score_response(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DtoGetNetworkHealthScoreResponse:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Get a network health score

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_get_network_health_score_response(
            request_options=request_options
        ).unwrap()

    def sensor_insights_health_score_summary(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DtoHealthScoreSummary:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Get health score summary

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return self._with_raw_response.sensor_insights_health_score_summary(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SensorInsightsHealthScoreWithRawResponse:
        return self._with_raw_response


class AsyncSensorInsightsHealthScore:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSensorInsightsHealthScoreWithRawResponse(client, server, auth)

    async def sensor_insights_get_network_health_score_response(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DtoGetNetworkHealthScoreResponse:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Get a network health score

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_get_network_health_score_response(
                request_options=request_options
            )
        ).unwrap()

    async def sensor_insights_health_score_summary(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> DtoHealthScoreSummary:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Get health score summary

        Raises:
            ApiError: Bad Request UnAuthorized Forbidden Not Acceptable Unsupported media type Too many requests
                Internal server error. ``error`` is ``ManagementError400 | ManagementError | ManagementError403 |
                ManagementError500 | RawError``."""
        return (
            await self._with_raw_response.sensor_insights_health_score_summary(request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSensorInsightsHealthScoreWithRawResponse:
        return self._with_raw_response


class SensorInsightsHealthScoreWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def sensor_insights_get_network_health_score_response(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DtoGetNetworkHealthScoreResponse, SensorInsightsGetNetworkHealthScoreResponseErrorBody]:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/healthscore/network"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoGetNetworkHealthScoreResponse],
            error_mapper=sensor_insights_get_network_health_score_response_error_mapper,
            request_options=request_options,
        )

    def sensor_insights_health_score_summary(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DtoHealthScoreSummary, SensorInsightsHealthScoreSummaryErrorBody]:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/healthscore/summary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoHealthScoreSummary],
            error_mapper=sensor_insights_health_score_summary_error_mapper,
            request_options=request_options,
        )


class AsyncSensorInsightsHealthScoreWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def sensor_insights_get_network_health_score_response(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DtoGetNetworkHealthScoreResponse, SensorInsightsGetNetworkHealthScoreResponseErrorBody]:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/healthscore/network"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoGetNetworkHealthScoreResponse],
            error_mapper=sensor_insights_get_network_health_score_response_error_mapper,
            request_options=request_options,
        )

    async def sensor_insights_health_score_summary(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DtoHealthScoreSummary, SensorInsightsHealthScoreSummaryErrorBody]:
        """Send a ``POST`` request.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/dm/v1/healthscore/summary"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DtoHealthScoreSummary],
            error_mapper=sensor_insights_health_score_summary_error_mapper,
            request_options=request_options,
        )
