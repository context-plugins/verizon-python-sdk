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
from ..errors.list_account_subscriptions_error import (
    ListAccountSubscriptionsErrorBody,
    list_account_subscriptions_error_mapper,
)
from ..models.security_subscription_request import SecuritySubscriptionRequest, SecuritySubscriptionRequestDict
from ..models.security_subscription_result import SecuritySubscriptionResult
from ..server.server import Server


class AccountSubscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountSubscriptionsWithRawResponse(client, server, auth)

    def list_account_subscriptions(
        self,
        body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SecuritySubscriptionResult:
        """Retrieves the total number of SIM-Secure for IoT subscription licenses purchased for your account by license
        type, and lists the number of licenses assigned and available for each license type.

        Args:
            body: Request for account subscription.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Security subscription result.

        Raises:
            ApiError: Bad request. Unauthorized request. Request forbidden. Not Found / Does not exist. Format / Request
                Unacceptable. Too many requests. ``error`` is ``SecurityResult | RawError``."""
        return self._with_raw_response.list_account_subscriptions(
            body, x_request_id=x_request_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountSubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncAccountSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountSubscriptionsWithRawResponse(client, server, auth)

    async def list_account_subscriptions(
        self,
        body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SecuritySubscriptionResult:
        """Retrieves the total number of SIM-Secure for IoT subscription licenses purchased for your account by license
        type, and lists the number of licenses assigned and available for each license type.

        Args:
            body: Request for account subscription.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Security subscription result.

        Raises:
            ApiError: Bad request. Unauthorized request. Request forbidden. Not Found / Does not exist. Format / Request
                Unacceptable. Too many requests. ``error`` is ``SecurityResult | RawError``."""
        return (
            await self._with_raw_response.list_account_subscriptions(
                body, x_request_id=x_request_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountSubscriptionsWithRawResponse:
        return self._with_raw_response


class AccountSubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_account_subscriptions(
        self,
        body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SecuritySubscriptionResult, ListAccountSubscriptionsErrorBody]:
        """Retrieves the total number of SIM-Secure for IoT subscription licenses purchased for your account by license
        type, and lists the number of licenses assigned and available for each license type.

        Args:
            body: Request for account subscription.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.m2_m("/v1/accounts/subscriptions/actions/list"),
            headers=[param[str | None]("X-Request-ID", x_request_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SecuritySubscriptionRequest | SecuritySubscriptionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SecuritySubscriptionResult],
            error_mapper=list_account_subscriptions_error_mapper,
            request_options=request_options,
        )


class AsyncAccountSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_account_subscriptions(
        self,
        body: SecuritySubscriptionRequest | SecuritySubscriptionRequestDict,
        *,
        x_request_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SecuritySubscriptionResult, ListAccountSubscriptionsErrorBody]:
        """Retrieves the total number of SIM-Secure for IoT subscription licenses purchased for your account by license
        type, and lists the number of licenses assigned and available for each license type.

        Args:
            body: Request for account subscription.
            x_request_id: Transaction Id.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.m2_m("/v1/accounts/subscriptions/actions/list"),
            headers=[param[str | None]("X-Request-ID", x_request_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SecuritySubscriptionRequest | SecuritySubscriptionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SecuritySubscriptionResult],
            error_mapper=list_account_subscriptions_error_mapper,
            request_options=request_options,
        )
