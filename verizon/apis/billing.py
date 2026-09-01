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
from ..errors.add_account_error import AddAccountErrorBody, add_account_error_mapper
from ..errors.cancel_managed_account_action_error import (
    CancelManagedAccountActionErrorBody,
    cancel_managed_account_action_error_mapper,
)
from ..errors.list_managed_account_error import ListManagedAccountErrorBody, list_managed_account_error_mapper
from ..errors.managed_account_action_error import ManagedAccountActionErrorBody, managed_account_action_error_mapper
from ..models.managed_account_cancel_request import ManagedAccountCancelRequest, ManagedAccountCancelRequestDict
from ..models.managed_account_cancel_response import ManagedAccountCancelResponse
from ..models.managed_accounts_add_request import ManagedAccountsAddRequest, ManagedAccountsAddRequestDict
from ..models.managed_accounts_add_response import ManagedAccountsAddResponse
from ..models.managed_accounts_get_all_response import ManagedAccountsGetAllResponse
from ..models.managed_accounts_provision_request import (
    ManagedAccountsProvisionRequest,
    ManagedAccountsProvisionRequestDict,
)
from ..models.managed_accounts_provision_response import ManagedAccountsProvisionResponse
from ..server.server import Server


class Billing:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BillingWithRawResponse(client, server, auth)

    def add_account(
        self,
        body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagedAccountsAddResponse:
        """This endpoint allows user to add managed accounts to a primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Add managed accounts response

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.add_account(body, request_options=request_options).unwrap()

    def cancel_managed_account_action(
        self,
        body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagedAccountCancelResponse:
        """Deactivates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed account cancel response

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.cancel_managed_account_action(body, request_options=request_options).unwrap()

    def list_managed_account(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManagedAccountsGetAllResponse:
        """This endpoint allows user to retrieve the list of all accounts managed by a primary account.

        Args:
            account_name: Primary account identifier
            service_name: Service name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of managed accounts

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.list_managed_account(
            account_name, service_name, request_options=request_options
        ).unwrap()

    def managed_account_action(
        self,
        body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagedAccountsProvisionResponse:
        """Activates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed account provision response

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.managed_account_action(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BillingWithRawResponse:
        return self._with_raw_response


class AsyncBilling:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBillingWithRawResponse(client, server, auth)

    async def add_account(
        self,
        body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagedAccountsAddResponse:
        """This endpoint allows user to add managed accounts to a primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Add managed accounts response

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (await self._with_raw_response.add_account(body, request_options=request_options)).unwrap()

    async def cancel_managed_account_action(
        self,
        body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagedAccountCancelResponse:
        """Deactivates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed account cancel response

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.cancel_managed_account_action(body, request_options=request_options)
        ).unwrap()

    async def list_managed_account(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ManagedAccountsGetAllResponse:
        """This endpoint allows user to retrieve the list of all accounts managed by a primary account.

        Args:
            account_name: Primary account identifier
            service_name: Service name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            List of managed accounts

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.list_managed_account(
                account_name, service_name, request_options=request_options
            )
        ).unwrap()

    async def managed_account_action(
        self,
        body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ManagedAccountsProvisionResponse:
        """Activates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Managed account provision response

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (await self._with_raw_response.managed_account_action(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncBillingWithRawResponse:
        return self._with_raw_response


class BillingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_account(
        self,
        body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagedAccountsAddResponse, AddAccountErrorBody]:
        """This endpoint allows user to add managed accounts to a primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/managedaccounts/actions/add"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ManagedAccountsAddRequest | ManagedAccountsAddRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountsAddResponse],
            error_mapper=add_account_error_mapper,
            request_options=request_options,
        )

    def cancel_managed_account_action(
        self,
        body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagedAccountCancelResponse, CancelManagedAccountActionErrorBody]:
        """Deactivates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/managedaccounts/actions/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ManagedAccountCancelRequest | ManagedAccountCancelRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountCancelResponse],
            error_mapper=cancel_managed_account_action_error_mapper,
            request_options=request_options,
        )

    def list_managed_account(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManagedAccountsGetAllResponse, ListManagedAccountErrorBody]:
        """This endpoint allows user to retrieve the list of all accounts managed by a primary account.

        Args:
            account_name: Primary account identifier
            service_name: Service name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.subscription_server("/managedaccounts/{accountName}/service/{serviceName}"),
            path_params=[param[str]("accountName", account_name), param[str]("serviceName", service_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountsGetAllResponse],
            error_mapper=list_managed_account_error_mapper,
            request_options=request_options,
        )

    def managed_account_action(
        self,
        body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagedAccountsProvisionResponse, ManagedAccountActionErrorBody]:
        """Activates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/managedaccounts/actions/provision"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountsProvisionResponse],
            error_mapper=managed_account_action_error_mapper,
            request_options=request_options,
        )


class AsyncBillingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_account(
        self,
        body: ManagedAccountsAddRequest | ManagedAccountsAddRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagedAccountsAddResponse, AddAccountErrorBody]:
        """This endpoint allows user to add managed accounts to a primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/managedaccounts/actions/add"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ManagedAccountsAddRequest | ManagedAccountsAddRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountsAddResponse],
            error_mapper=add_account_error_mapper,
            request_options=request_options,
        )

    async def cancel_managed_account_action(
        self,
        body: ManagedAccountCancelRequest | ManagedAccountCancelRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagedAccountCancelResponse, CancelManagedAccountActionErrorBody]:
        """Deactivates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/managedaccounts/actions/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ManagedAccountCancelRequest | ManagedAccountCancelRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountCancelResponse],
            error_mapper=cancel_managed_account_action_error_mapper,
            request_options=request_options,
        )

    async def list_managed_account(
        self, account_name: str, service_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ManagedAccountsGetAllResponse, ListManagedAccountErrorBody]:
        """This endpoint allows user to retrieve the list of all accounts managed by a primary account.

        Args:
            account_name: Primary account identifier
            service_name: Service name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.subscription_server("/managedaccounts/{accountName}/service/{serviceName}"),
            path_params=[param[str]("accountName", account_name), param[str]("serviceName", service_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountsGetAllResponse],
            error_mapper=list_managed_account_error_mapper,
            request_options=request_options,
        )

    async def managed_account_action(
        self,
        body: ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ManagedAccountsProvisionResponse, ManagedAccountActionErrorBody]:
        """Activates a managed billing service relationship between a managed account and the primary account.

        Args:
            body: Service name and list of accounts to add
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/managedaccounts/actions/provision"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ManagedAccountsProvisionRequest | ManagedAccountsProvisionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ManagedAccountsProvisionResponse],
            error_mapper=managed_account_action_error_mapper,
            request_options=request_options,
        )
