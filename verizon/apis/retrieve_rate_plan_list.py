from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.rateplan import Rateplan
from ..server.server import Server


class RetrieveRatePlanList:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RetrieveRatePlanListWithRawResponse(client, server, auth)

    def get_rate_plan_list(self, ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None) -> Rateplan:
        """Retrieves the rate plans and rate plan details for a profile ID.

        Args:
            ecpd_id: The Enterprise Customer Profile Database ID. This is the same as the accountName value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            This is a syncronous response showing the rate plans associated.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_rate_plan_list(ecpd_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> RetrieveRatePlanListWithRawResponse:
        return self._with_raw_response


class AsyncRetrieveRatePlanList:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRetrieveRatePlanListWithRawResponse(client, server, auth)

    async def get_rate_plan_list(
        self, ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Rateplan:
        """Retrieves the rate plans and rate plan details for a profile ID.

        Args:
            ecpd_id: The Enterprise Customer Profile Database ID. This is the same as the accountName value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            This is a syncronous response showing the rate plans associated.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_rate_plan_list(ecpd_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncRetrieveRatePlanListWithRawResponse:
        return self._with_raw_response


class RetrieveRatePlanListWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_rate_plan_list(
        self, ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Rateplan, RawError]:
        """Retrieves the rate plans and rate plan details for a profile ID.

        Args:
            ecpd_id: The Enterprise Customer Profile Database ID. This is the same as the accountName value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v2/triggers/rateplanlist/{ecpdId}"),
            path_params=[param[str]("ecpdId", ecpd_id)],
            auth_scheme=AnySchemes(self._auth.thingspace_oauth1, self._auth.vz_m2_m_token),
            decoder=json_decoder[Rateplan],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRetrieveRatePlanListWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_rate_plan_list(
        self, ecpd_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Rateplan, RawError]:
        """Retrieves the rate plans and rate plan details for a profile ID.

        Args:
            ecpd_id: The Enterprise Customer Profile Database ID. This is the same as the accountName value
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v2/triggers/rateplanlist/{ecpdId}"),
            path_params=[param[str]("ecpdId", ecpd_id)],
            auth_scheme=AsyncAnySchemes(self._auth.thingspace_oauth1, self._auth.vz_m2_m_token),
            decoder=json_decoder[Rateplan],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
