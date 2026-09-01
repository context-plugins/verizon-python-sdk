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
from ..errors.get_account_information_using_get_error import (
    GetAccountInformationUsingGetErrorBody,
    get_account_information_using_get_error_mapper,
)
from ..models.get_account_information_responseforplanner import GetAccountInformationResponseforplanner
from ..server.server import Server


class AccountServiceController:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountServiceControllerWithRawResponse(client, server, auth)

    def get_account_information_using_get(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetAccountInformationResponseforplanner:
        """Returns aaccount information associated with a specified account.

        Args:
            account_name: The account's numeric name, including leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The account information related to an account.

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``RestErrorResponseforplanner | AuthRestErrorResponseforplanner |
                RawError``."""
        return self._with_raw_response.get_account_information_using_get(
            account_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> AccountServiceControllerWithRawResponse:
        return self._with_raw_response


class AsyncAccountServiceController:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountServiceControllerWithRawResponse(client, server, auth)

    async def get_account_information_using_get(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetAccountInformationResponseforplanner:
        """Returns aaccount information associated with a specified account.

        Args:
            account_name: The account's numeric name, including leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The account information related to an account.

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``RestErrorResponseforplanner | AuthRestErrorResponseforplanner |
                RawError``."""
        return (
            await self._with_raw_response.get_account_information_using_get(
                account_name, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountServiceControllerWithRawResponse:
        return self._with_raw_response


class AccountServiceControllerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_information_using_get(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAccountInformationResponseforplanner, GetAccountInformationUsingGetErrorBody]:
        """Returns aaccount information associated with a specified account.

        Args:
            account_name: The account's numeric name, including leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v1/accounts/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetAccountInformationResponseforplanner],
            error_mapper=get_account_information_using_get_error_mapper,
            request_options=request_options,
        )


class AsyncAccountServiceControllerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_information_using_get(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetAccountInformationResponseforplanner, GetAccountInformationUsingGetErrorBody]:
        """Returns aaccount information associated with a specified account.

        Args:
            account_name: The account's numeric name, including leading zeroes.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v1/accounts/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GetAccountInformationResponseforplanner],
            error_mapper=get_account_information_using_get_error_mapper,
            request_options=request_options,
        )
