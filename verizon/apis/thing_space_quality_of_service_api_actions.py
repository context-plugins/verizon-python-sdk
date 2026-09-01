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
from ..models.subscribe_request import SubscribeRequest, SubscribeRequestDict
from ..models.success201 import Success201
from ..server.server import Server


class ThingSpaceQualityOfServiceApiActions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ThingSpaceQualityOfServiceApiActionsWithRawResponse(client, server, auth)

    def create_a_thing_space_quality_of_service_api_subscription(
        self, body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Success201:
        """Creates a QoS elevation subscription ID and activates the subscription.

        Args:
            body: The request details to create a ThingSpace Quality of Service API subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success Response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_a_thing_space_quality_of_service_api_subscription(
            body, request_options=request_options
        ).unwrap()

    def stop_a_thing_space_quality_of_service_api_subscription(
        self, account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Success201:
        """Stops an active ThingSpace Quality of Service API subscription using the account name and the subscription
        ID.

        Args:
            account_name: Value sent with the request.
            qos_subscription_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success Response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.stop_a_thing_space_quality_of_service_api_subscription(
            account_name, qos_subscription_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ThingSpaceQualityOfServiceApiActionsWithRawResponse:
        return self._with_raw_response


class AsyncThingSpaceQualityOfServiceApiActions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncThingSpaceQualityOfServiceApiActionsWithRawResponse(client, server, auth)

    async def create_a_thing_space_quality_of_service_api_subscription(
        self, body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> Success201:
        """Creates a QoS elevation subscription ID and activates the subscription.

        Args:
            body: The request details to create a ThingSpace Quality of Service API subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success Response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_a_thing_space_quality_of_service_api_subscription(
                body, request_options=request_options
            )
        ).unwrap()

    async def stop_a_thing_space_quality_of_service_api_subscription(
        self, account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Success201:
        """Stops an active ThingSpace Quality of Service API subscription using the account name and the subscription
        ID.

        Args:
            account_name: Value sent with the request.
            qos_subscription_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success Response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.stop_a_thing_space_quality_of_service_api_subscription(
                account_name, qos_subscription_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncThingSpaceQualityOfServiceApiActionsWithRawResponse:
        return self._with_raw_response


class ThingSpaceQualityOfServiceApiActionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_a_thing_space_quality_of_service_api_subscription(
        self, body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Success201, RawError]:
        """Creates a QoS elevation subscription ID and activates the subscription.

        Args:
            body: The request details to create a ThingSpace Quality of Service API subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/enhanceQoS"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscribeRequest | SubscribeRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Success201],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def stop_a_thing_space_quality_of_service_api_subscription(
        self, account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Success201, RawError]:
        """Stops an active ThingSpace Quality of Service API subscription using the account name and the subscription
        ID.

        Args:
            account_name: Value sent with the request.
            qos_subscription_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/enhanceQoS"),
            query_params=[
                param[str]("accountName", account_name), param[str]("qosSubscriptionId", qos_subscription_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Success201],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncThingSpaceQualityOfServiceApiActionsWithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def create_a_thing_space_quality_of_service_api_subscription(
        self, body: SubscribeRequest | SubscribeRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Success201, RawError]:
        """Creates a QoS elevation subscription ID and activates the subscription.

        Args:
            body: The request details to create a ThingSpace Quality of Service API subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/enhanceQoS"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubscribeRequest | SubscribeRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Success201],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def stop_a_thing_space_quality_of_service_api_subscription(
        self, account_name: str, qos_subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Success201, RawError]:
        """Stops an active ThingSpace Quality of Service API subscription using the account name and the subscription
        ID.

        Args:
            account_name: Value sent with the request.
            qos_subscription_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/actions/enhanceQoS"),
            query_params=[
                param[str]("accountName", account_name), param[str]("qosSubscriptionId", qos_subscription_id)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Success201],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
