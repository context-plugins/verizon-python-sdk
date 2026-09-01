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
from ..errors.get_account_information_error import GetAccountInformationErrorBody, get_account_information_error_mapper
from ..errors.list_account_leads_error import ListAccountLeadsErrorBody, list_account_leads_error_mapper
from ..errors.list_account_states_and_services_error import (
    ListAccountStatesAndServicesErrorBody,
    list_account_states_and_services_error_mapper,
)
from ..models.account import Account
from ..models.account_leads_result import AccountLeadsResult
from ..models.account_states_and_services import AccountStatesAndServices
from ..server.server import Server


class Accounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = AccountsWithRawResponse(client, server, auth)

    def get_account_information(self, aname: str, *, request_options: RequestOptionsOrDict | None = None) -> Account:
        """Returns information about a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The account information.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.get_account_information(aname, request_options=request_options).unwrap()

    def list_account_leads(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AccountLeadsResult:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /leads/{aname}?next={token}. This URL can be used to request the next set of leads.

        Args:
            aname: Account name.
            next: Continue the previous query from the pageUrl in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of leads associated with the account.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_account_leads(aname, next=next, request_options=request_options).unwrap()

    def list_account_states_and_services(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountStatesAndServices:
        """Returns a list and details of all custom services and states defined for a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The account's engagements, services, and states.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_account_states_and_services(aname, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountsWithRawResponse:
        return self._with_raw_response


class AsyncAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncAccountsWithRawResponse(client, server, auth)

    async def get_account_information(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> Account:
        """Returns information about a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The account information.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.get_account_information(aname, request_options=request_options)).unwrap()

    async def list_account_leads(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> AccountLeadsResult:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /leads/{aname}?next={token}. This URL can be used to request the next set of leads.

        Args:
            aname: Account name.
            next: Continue the previous query from the pageUrl in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of leads associated with the account.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_account_leads(aname, next=next, request_options=request_options)
        ).unwrap()

    async def list_account_states_and_services(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountStatesAndServices:
        """Returns a list and details of all custom services and states defined for a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The account's engagements, services, and states.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_account_states_and_services(aname, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountsWithRawResponse:
        return self._with_raw_response


class AccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_account_information(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Account, GetAccountInformationErrorBody]:
        """Returns information about a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/accounts/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Account],
            error_mapper=get_account_information_error_mapper,
            request_options=request_options,
        )

    def list_account_leads(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountLeadsResult, ListAccountLeadsErrorBody]:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /leads/{aname}?next={token}. This URL can be used to request the next set of leads.

        Args:
            aname: Account name.
            next: Continue the previous query from the pageUrl in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/leads/{aname}"),
            path_params=[param[str]("aname", aname)],
            query_params=[param[int | None]("next", next)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountLeadsResult],
            error_mapper=list_account_leads_error_mapper,
            request_options=request_options,
        )

    def list_account_states_and_services(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountStatesAndServices, ListAccountStatesAndServicesErrorBody]:
        """Returns a list and details of all custom services and states defined for a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/accounts/{aname}/statesandservices"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountStatesAndServices],
            error_mapper=list_account_states_and_services_error_mapper,
            request_options=request_options,
        )


class AsyncAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_account_information(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Account, GetAccountInformationErrorBody]:
        """Returns information about a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/accounts/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Account],
            error_mapper=get_account_information_error_mapper,
            request_options=request_options,
        )

    async def list_account_leads(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountLeadsResult, ListAccountLeadsErrorBody]:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /leads/{aname}?next={token}. This URL can be used to request the next set of leads.

        Args:
            aname: Account name.
            next: Continue the previous query from the pageUrl in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/leads/{aname}"),
            path_params=[param[str]("aname", aname)],
            query_params=[param[int | None]("next", next)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountLeadsResult],
            error_mapper=list_account_leads_error_mapper,
            request_options=request_options,
        )

    async def list_account_states_and_services(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountStatesAndServices, ListAccountStatesAndServicesErrorBody]:
        """Returns a list and details of all custom services and states defined for a specified account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/accounts/{aname}/statesandservices"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountStatesAndServices],
            error_mapper=list_account_states_and_services_error_mapper,
            request_options=request_options,
        )
