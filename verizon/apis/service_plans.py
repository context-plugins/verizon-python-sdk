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
from ..errors.list_account_service_plans_error import (
    ListAccountServicePlansErrorBody,
    list_account_service_plans_error_mapper,
)
from ..models.service_plan import ServicePlan
from ..server.server import Server


class ServicePlans:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ServicePlansWithRawResponse(client, server, auth)

    def list_account_service_plans(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ServicePlan]:
        """Returns a list of all data service plans that are associated with a specified billing account. When you send
        a request to /devices/actions/activate to activate a line of service you must specify the code for one of the
        service plans associated with your account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of service plans associated with the account.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_account_service_plans(aname, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ServicePlansWithRawResponse:
        return self._with_raw_response


class AsyncServicePlans:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncServicePlansWithRawResponse(client, server, auth)

    async def list_account_service_plans(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ServicePlan]:
        """Returns a list of all data service plans that are associated with a specified billing account. When you send
        a request to /devices/actions/activate to activate a line of service you must specify the code for one of the
        service plans associated with your account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The list of service plans associated with the account.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_account_service_plans(aname, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncServicePlansWithRawResponse:
        return self._with_raw_response


class ServicePlansWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_account_service_plans(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ServicePlan], ListAccountServicePlansErrorBody]:
        """Returns a list of all data service plans that are associated with a specified billing account. When you send
        a request to /devices/actions/activate to activate a line of service you must specify the code for one of the
        service plans associated with your account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/plans/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ServicePlan]],
            error_mapper=list_account_service_plans_error_mapper,
            request_options=request_options,
        )


class AsyncServicePlansWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_account_service_plans(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ServicePlan], ListAccountServicePlansErrorBody]:
        """Returns a list of all data service plans that are associated with a specified billing account. When you send
        a request to /devices/actions/activate to activate a line of service you must specify the code for one of the
        service plans associated with your account.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/plans/{aname}"),
            path_params=[param[str]("aname", aname)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[list[ServicePlan]],
            error_mapper=list_account_service_plans_error_mapper,
            request_options=request_options,
        )
