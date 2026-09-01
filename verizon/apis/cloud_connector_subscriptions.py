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
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.create_subscription_request import CreateSubscriptionRequest, CreateSubscriptionRequestDict
from ..models.delete_subscription_request import DeleteSubscriptionRequest, DeleteSubscriptionRequestDict
from ..models.query_subscription_request import QuerySubscriptionRequest, QuerySubscriptionRequestDict
from ..models.subscription import Subscription
from ..server.server import Server


class CloudConnectorSubscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CloudConnectorSubscriptionsWithRawResponse(client, server, auth)

    def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Subscription:
        """Create a subscription to define a streaming channel that sends data from devices in the account to an
        endpoint defined in a target resource.

        Args:
            body: The request body provides the details of the subscription that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns full subscription resource definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_subscription(body, request_options=request_options).unwrap()

    def delete_subscription(
        self,
        body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a subscription from a ThingSpace account.

        Args:
            body: The request body identifies the subscription to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Subscription deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_subscription(body, request_options=request_options).unwrap()

    def query_subscription(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Subscription]:
        """Search for subscriptions by property values. Returns an array of all matching subscription resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of all matching subscriptions. Each subscription includes the full subscription resource
            definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.query_subscription(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CloudConnectorSubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncCloudConnectorSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCloudConnectorSubscriptionsWithRawResponse(client, server, auth)

    async def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> Subscription:
        """Create a subscription to define a streaming channel that sends data from devices in the account to an
        endpoint defined in a target resource.

        Args:
            body: The request body provides the details of the subscription that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns full subscription resource definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_subscription(body, request_options=request_options)).unwrap()

    async def delete_subscription(
        self,
        body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Remove a subscription from a ThingSpace account.

        Args:
            body: The request body identifies the subscription to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Subscription deleted successfully.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_subscription(body, request_options=request_options)).unwrap()

    async def query_subscription(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Subscription]:
        """Search for subscriptions by property values. Returns an array of all matching subscription resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Returns an array of all matching subscriptions. Each subscription includes the full subscription resource
            definition.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.query_subscription(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncCloudConnectorSubscriptionsWithRawResponse:
        return self._with_raw_response


class CloudConnectorSubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Subscription, RawError]:
        """Create a subscription to define a streaming channel that sends data from devices in the account to an
        endpoint defined in a target resource.

        Args:
            body: The request body provides the details of the subscription that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/subscriptions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Subscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_subscription(
        self,
        body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a subscription from a ThingSpace account.

        Args:
            body: The request body identifies the subscription to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/subscriptions/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteSubscriptionRequest | DeleteSubscriptionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def query_subscription(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Subscription], RawError]:
        """Search for subscriptions by property values. Returns an array of all matching subscription resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/subscriptions/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QuerySubscriptionRequest | QuerySubscriptionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Subscription]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCloudConnectorSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[Subscription, RawError]:
        """Create a subscription to define a streaming channel that sends data from devices in the account to an
        endpoint defined in a target resource.

        Args:
            body: The request body provides the details of the subscription that you want to create.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/subscriptions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Subscription],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_subscription(
        self,
        body: DeleteSubscriptionRequest | DeleteSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Remove a subscription from a ThingSpace account.

        Args:
            body: The request body identifies the subscription to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/subscriptions/actions/delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteSubscriptionRequest | DeleteSubscriptionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def query_subscription(
        self,
        body: QuerySubscriptionRequest | QuerySubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Subscription], RawError]:
        """Search for subscriptions by property values. Returns an array of all matching subscription resources.

        Args:
            body: The request body specifies fields and values to match.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.cloud_connector("/subscriptions/actions/query"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[QuerySubscriptionRequest | QuerySubscriptionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[Subscription]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
