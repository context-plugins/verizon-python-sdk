from __future__ import annotations

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
from ..errors.get_account_subscription_status2_error import (
    GetAccountSubscriptionStatus2ErrorBody,
    get_account_subscription_status2_error_mapper,
)
from ..models.fota_v2_subscription import FotaV2Subscription
from ..server.server import Server


class SoftwareManagementSubscriptionsV2:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementSubscriptionsV2WithRawResponse(client, server, auth)

    def get_account_subscription_status2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2Subscription:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            FOTA Subscription.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return self._with_raw_response.get_account_subscription_status2(
            account, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementSubscriptionsV2WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementSubscriptionsV2:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementSubscriptionsV2WithRawResponse(client, server, auth)

    async def get_account_subscription_status2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV2Subscription:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            FOTA Subscription.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV2Result | RawError``."""
        return (
            await self._with_raw_response.get_account_subscription_status2(account, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementSubscriptionsV2WithRawResponse:
        return self._with_raw_response


class SoftwareManagementSubscriptionsV2WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_subscription_status2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2Subscription, GetAccountSubscriptionStatus2ErrorBody]:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/subscriptions/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2Subscription],
            error_mapper=get_account_subscription_status2_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementSubscriptionsV2WithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def get_account_subscription_status2(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV2Subscription, GetAccountSubscriptionStatus2ErrorBody]:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            account: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v2("/subscriptions/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV2Subscription],
            error_mapper=get_account_subscription_status2_error_mapper,
            request_options=request_options,
        )
