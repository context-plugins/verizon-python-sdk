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
from ..models.a_request_body_for_usage import ARequestBodyForUsage, ARequestBodyForUsageDict
from ..models.request_body_for_usage import RequestBodyForUsage, RequestBodyForUsageDict
from ..models.response_to_usage_query import ResponseToUsageQuery
from ..models.usage_request_response import UsageRequestResponse
from ..server.server import Server


class PromotionPeriodInformation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PromotionPeriodInformationWithRawResponse(client, server, auth)

    def get_promo_device_aggregate_usage_history(
        self,
        body: RequestBodyForUsage | RequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageRequestResponse:
        """Retrieves the aggregate usage for an account using pseudo-MDN during the promotional period using a callback.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_promo_device_aggregate_usage_history(
            body, request_options=request_options
        ).unwrap()

    def get_promo_device_usage_history(
        self,
        body: ARequestBodyForUsage | ARequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResponseToUsageQuery:
        """Retrieves the usage history of a device during the promotion period.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage History

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_promo_device_usage_history(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PromotionPeriodInformationWithRawResponse:
        return self._with_raw_response


class AsyncPromotionPeriodInformation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPromotionPeriodInformationWithRawResponse(client, server, auth)

    async def get_promo_device_aggregate_usage_history(
        self,
        body: RequestBodyForUsage | RequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageRequestResponse:
        """Retrieves the aggregate usage for an account using pseudo-MDN during the promotional period using a callback.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_promo_device_aggregate_usage_history(
                body, request_options=request_options
            )
        ).unwrap()

    async def get_promo_device_usage_history(
        self,
        body: ARequestBodyForUsage | ARequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResponseToUsageQuery:
        """Retrieves the usage history of a device during the promotion period.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage History

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_promo_device_usage_history(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPromotionPeriodInformationWithRawResponse:
        return self._with_raw_response


class PromotionPeriodInformationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_promo_device_aggregate_usage_history(
        self,
        body: RequestBodyForUsage | RequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageRequestResponse, RawError]:
        """Retrieves the aggregate usage for an account using pseudo-MDN during the promotional period using a callback.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/promoaggregateusage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RequestBodyForUsage | RequestBodyForUsageDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UsageRequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_promo_device_usage_history(
        self,
        body: ARequestBodyForUsage | ARequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResponseToUsageQuery, RawError]:
        """Retrieves the usage history of a device during the promotion period.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/promodeviceusage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ARequestBodyForUsage | ARequestBodyForUsageDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResponseToUsageQuery],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPromotionPeriodInformationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_promo_device_aggregate_usage_history(
        self,
        body: RequestBodyForUsage | RequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageRequestResponse, RawError]:
        """Retrieves the aggregate usage for an account using pseudo-MDN during the promotional period using a callback.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/promoaggregateusage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RequestBodyForUsage | RequestBodyForUsageDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UsageRequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_promo_device_usage_history(
        self,
        body: ARequestBodyForUsage | ARequestBodyForUsageDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResponseToUsageQuery, RawError]:
        """Retrieves the usage history of a device during the promotion period.

        Args:
            body: Retrieve Aggregate Usage
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/usage/actions/promodeviceusage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ARequestBodyForUsage | ARequestBodyForUsageDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ResponseToUsageQuery],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
