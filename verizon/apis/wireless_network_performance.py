from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.get_device_experience_score_bulk_request import (
    GetDeviceExperienceScoreBulkRequest,
    GetDeviceExperienceScoreBulkRequestDict,
)
from ..models.get_device_experience_score_history_request import (
    GetDeviceExperienceScoreHistoryRequest,
    GetDeviceExperienceScoreHistoryRequestDict,
)
from ..models.get_network_conditions_request import GetNetworkConditionsRequest, GetNetworkConditionsRequestDict
from ..models.unions.m2_mv1_intelligence_wireless_coverage_request import (
    M2MV1IntelligenceWirelessCoverageRequest,
    M2MV1IntelligenceWirelessCoverageRequestDict,
)
from ..models.wnprequest_response import WnprequestResponse
from ..server.server import Server


class WirelessNetworkPerformance:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WirelessNetworkPerformanceWithRawResponse(client, server, auth)

    def device_experience30days_history(
        self,
        body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """A report of a specific device's service scores over a 30 day period.

        Args:
            body: Request for a device's 30 day experience.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.device_experience30days_history(body, request_options=request_options).unwrap()

    def device_experience_bulk_latest(
        self,
        body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """Run a report to view the latest device experience score for specific devices.

        Args:
            body: Request for bulk latest history details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.device_experience_bulk_latest(body, request_options=request_options).unwrap()

    def domestic4_g_and5_g_nationwide_network_coverage(
        self,
        body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """Run a report for FWA Address qualification or to determine network types available and available coverage.
        Network types covered include: CAT-M, NB-IOT, LTE, LTE-AWS, 5GNW, MMWAVE and C-BAND.

        Args:
            body: Request for network coverage details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.domestic4_g_and5_g_nationwide_network_coverage(
            body, request_options=request_options
        ).unwrap()

    def near_real_time_network_conditions(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """WNP Query for current network condition.

        Args:
            body: Request for current network health.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.near_real_time_network_conditions(body, request_options=request_options).unwrap()

    def site_proximity(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """Identify the direction and general distance of nearby cell sites and the technology supported by the
        equipment.

        Args:
            body: Request for cell site proximity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.site_proximity(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> WirelessNetworkPerformanceWithRawResponse:
        return self._with_raw_response


class AsyncWirelessNetworkPerformance:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWirelessNetworkPerformanceWithRawResponse(client, server, auth)

    async def device_experience30days_history(
        self,
        body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """A report of a specific device's service scores over a 30 day period.

        Args:
            body: Request for a device's 30 day experience.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.device_experience30days_history(body, request_options=request_options)
        ).unwrap()

    async def device_experience_bulk_latest(
        self,
        body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """Run a report to view the latest device experience score for specific devices.

        Args:
            body: Request for bulk latest history details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.device_experience_bulk_latest(body, request_options=request_options)
        ).unwrap()

    async def domestic4_g_and5_g_nationwide_network_coverage(
        self,
        body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """Run a report for FWA Address qualification or to determine network types available and available coverage.
        Network types covered include: CAT-M, NB-IOT, LTE, LTE-AWS, 5GNW, MMWAVE and C-BAND.

        Args:
            body: Request for network coverage details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.domestic4_g_and5_g_nationwide_network_coverage(
                body, request_options=request_options
            )
        ).unwrap()

    async def near_real_time_network_conditions(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """WNP Query for current network condition.

        Args:
            body: Request for current network health.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.near_real_time_network_conditions(body, request_options=request_options)
        ).unwrap()

    async def site_proximity(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> WnprequestResponse:
        """Identify the direction and general distance of nearby cell sites and the technology supported by the
        equipment.

        Args:
            body: Request for cell site proximity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.site_proximity(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncWirelessNetworkPerformanceWithRawResponse:
        return self._with_raw_response


class WirelessNetworkPerformanceWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def device_experience30days_history(
        self,
        body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """A report of a specific device's service scores over a 30 day period.

        Args:
            body: Request for a device's 30 day experience.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/intelligence/device-experience/history/30-days"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def device_experience_bulk_latest(
        self,
        body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """Run a report to view the latest device experience score for specific devices.

        Args:
            body: Request for bulk latest history details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/device-experience/bulk/latest"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def domestic4_g_and5_g_nationwide_network_coverage(
        self,
        body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """Run a report for FWA Address qualification or to determine network types available and available coverage.
        Network types covered include: CAT-M, NB-IOT, LTE, LTE-AWS, 5GNW, MMWAVE and C-BAND.

        Args:
            body: Request for network coverage details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/wireless-coverage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict](
                body
            ),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def near_real_time_network_conditions(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """WNP Query for current network condition.

        Args:
            body: Request for current network health.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/network-conditions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetNetworkConditionsRequest | GetNetworkConditionsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def site_proximity(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """Identify the direction and general distance of nearby cell sites and the technology supported by the
        equipment.

        Args:
            body: Request for cell site proximity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/site-proximity/action/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetNetworkConditionsRequest | GetNetworkConditionsRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWirelessNetworkPerformanceWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def device_experience30days_history(
        self,
        body: GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """A report of a specific device's service scores over a 30 day period.

        Args:
            body: Request for a device's 30 day experience.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v1/intelligence/device-experience/history/30-days"
            ),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceExperienceScoreHistoryRequest | GetDeviceExperienceScoreHistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def device_experience_bulk_latest(
        self,
        body: GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """Run a report to view the latest device experience score for specific devices.

        Args:
            body: Request for bulk latest history details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/device-experience/bulk/latest"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceExperienceScoreBulkRequest | GetDeviceExperienceScoreBulkRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def domestic4_g_and5_g_nationwide_network_coverage(
        self,
        body: M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """Run a report for FWA Address qualification or to determine network types available and available coverage.
        Network types covered include: CAT-M, NB-IOT, LTE, LTE-AWS, 5GNW, MMWAVE and C-BAND.

        Args:
            body: Request for network coverage details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/wireless-coverage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[M2MV1IntelligenceWirelessCoverageRequest | M2MV1IntelligenceWirelessCoverageRequestDict](
                body
            ),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def near_real_time_network_conditions(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """WNP Query for current network condition.

        Args:
            body: Request for current network health.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/network-conditions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetNetworkConditionsRequest | GetNetworkConditionsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def site_proximity(
        self,
        body: GetNetworkConditionsRequest | GetNetworkConditionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[WnprequestResponse, RawError]:
        """Identify the direction and general distance of nearby cell sites and the technology supported by the
        equipment.

        Args:
            body: Request for cell site proximity.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/intelligence/site-proximity/action/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetNetworkConditionsRequest | GetNetworkConditionsRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[WnprequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
