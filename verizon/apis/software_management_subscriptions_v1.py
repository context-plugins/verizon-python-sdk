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
from ..errors.get_account_license_status_error import (
    GetAccountLicenseStatusErrorBody,
    get_account_license_status_error_mapper,
)
from ..errors.get_account_subscription_status_error import (
    GetAccountSubscriptionStatusErrorBody,
    get_account_subscription_status_error_mapper,
)
from ..models.account_license_info import AccountLicenseInfo
from ..models.v1_account_subscription import V1AccountSubscription
from ..server.server import Server


class SoftwareManagementSubscriptionsV1:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SoftwareManagementSubscriptionsV1WithRawResponse(client, server, auth)

    def get_account_license_status(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountLicenseInfo:
        """Returns information about an account's Software Management Services licenses and a list of licensed devices.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account license information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.get_account_license_status(
            account, start_index, request_options=request_options
        ).unwrap()

    def get_account_subscription_status(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1AccountSubscription:
        """This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account subscription information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return self._with_raw_response.get_account_subscription_status(
            account, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SoftwareManagementSubscriptionsV1WithRawResponse:
        return self._with_raw_response


class AsyncSoftwareManagementSubscriptionsV1:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSoftwareManagementSubscriptionsV1WithRawResponse(client, server, auth)

    async def get_account_license_status(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountLicenseInfo:
        """Returns information about an account's Software Management Services licenses and a list of licensed devices.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account license information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.get_account_license_status(
                account, start_index, request_options=request_options
            )
        ).unwrap()

    async def get_account_subscription_status(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1AccountSubscription:
        """This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account subscription information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``FotaV1Result | RawError``."""
        return (
            await self._with_raw_response.get_account_subscription_status(account, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSoftwareManagementSubscriptionsV1WithRawResponse:
        return self._with_raw_response


class SoftwareManagementSubscriptionsV1WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_license_status(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountLicenseInfo, GetAccountLicenseStatusErrorBody]:
        """Returns information about an account's Software Management Services licenses and a list of licensed devices.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/licenses/{account}/index/{startIndex}"),
            path_params=[param[str]("account", account), param[str]("startIndex", start_index)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountLicenseInfo],
            error_mapper=get_account_license_status_error_mapper,
            request_options=request_options,
        )

    def get_account_subscription_status(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1AccountSubscription, GetAccountSubscriptionStatusErrorBody]:
        """This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/subscriptions/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1AccountSubscription],
            error_mapper=get_account_subscription_status_error_mapper,
            request_options=request_options,
        )


class AsyncSoftwareManagementSubscriptionsV1WithRawResponse(
    SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]
):
    async def get_account_license_status(
        self, account: str, start_index: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountLicenseInfo, GetAccountLicenseStatusErrorBody]:
        """Returns information about an account's Software Management Services licenses and a list of licensed devices.

        Args:
            account: Account identifier in "##########-#####".
            start_index: The zero-based number of the first record to return. Set startIndex=0 for the first request. If
                there are more than 1,000 devices in the response, set startIndex=1000 for the second request, 2000 for
                the third request, etc.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/licenses/{account}/index/{startIndex}"),
            path_params=[param[str]("account", account), param[str]("startIndex", start_index)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountLicenseInfo],
            error_mapper=get_account_license_status_error_mapper,
            request_options=request_options,
        )

    async def get_account_subscription_status(
        self, account: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1AccountSubscription, GetAccountSubscriptionStatusErrorBody]:
        """This subscriptions endpoint retrieves an account's current Software Management Service subscription status.

        Args:
            account: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.software_management_v1("/subscriptions/{account}"),
            path_params=[param[str]("account", account)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[V1AccountSubscription],
            error_mapper=get_account_subscription_status_error_mapper,
            request_options=request_options,
        )
