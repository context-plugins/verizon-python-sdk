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
from ..errors.get_account_subscription_status3_error import (
    GetAccountSubscriptionStatus3ErrorBody,
    get_account_subscription_status3_error_mapper,
)
from ..models.fota_v3_subscription import FotaV3Subscription
from ..server.server import Server


class SoftwareManagementSubscriptionsV3:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementSubscriptionsV3WithRawResponse(client, server, auth)

    def get_account_subscription_status3(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3Subscription:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            FOTA Subscription.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return self._with_raw_response.get_account_subscription_status3(acc, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementSubscriptionsV3WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementSubscriptionsV3:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementSubscriptionsV3WithRawResponse(client, server, auth)

    async def get_account_subscription_status3(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> FotaV3Subscription:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            FOTA Subscription.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV3Result | RawError``."""
        return (
            await self._with_raw_response.get_account_subscription_status3(acc, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementSubscriptionsV3WithRawResponse:
        return self._with_raw_response


class SoftwareManagementSubscriptionsV3WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_subscription_status3(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3Subscription, GetAccountSubscriptionStatus3ErrorBody]:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/subscriptions/{acc}"),
            path_params=[param[str]("acc", acc)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3Subscription],
            error_mapper=get_account_subscription_status3_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementSubscriptionsV3WithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def get_account_subscription_status3(
        self, acc: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[FotaV3Subscription, GetAccountSubscriptionStatus3ErrorBody]:
        """This endpoint retrieves a FOTA subscription by account.

        Args:
            acc: Account identifier.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v3("/subscriptions/{acc}"),
            path_params=[param[str]("acc", acc)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[FotaV3Subscription],
            error_mapper=get_account_subscription_status3_error_mapper,
            request_options=request_options,
        )
