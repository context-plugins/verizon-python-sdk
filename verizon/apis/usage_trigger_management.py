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
from ..errors.create_new_trigger_error import CreateNewTriggerErrorBody, create_new_trigger_error_mapper
from ..errors.delete_trigger_error import DeleteTriggerErrorBody, delete_trigger_error_mapper
from ..errors.update_trigger_error import UpdateTriggerErrorBody, update_trigger_error_mapper
from ..models.device_location_success_result import DeviceLocationSuccessResult
from ..models.usage_trigger_add_request import UsageTriggerAddRequest, UsageTriggerAddRequestDict
from ..models.usage_trigger_response import UsageTriggerResponse
from ..models.usage_trigger_update_request import UsageTriggerUpdateRequest, UsageTriggerUpdateRequestDict
from ..server.server import Server


class UsageTriggerManagement:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UsageTriggerManagementWithRawResponse(client, server, auth)

    def create_new_trigger(
        self,
        *,
        body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageTriggerResponse:
        """Create a new usage trigger, which will send an alert when the number of device location service transactions
        reaches a specified percentage of the monthly subscription amount.

        Args:
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage trigger Add result

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.create_new_trigger(body=body, request_options=request_options).unwrap()

    def delete_trigger(
        self, account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSuccessResult:
        """eletes the specified usage trigger from the given account

        Args:
            account_name: Account name
            trigger_id: Usage trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete result

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.delete_trigger(
            account_name, trigger_id, request_options=request_options
        ).unwrap()

    def update_trigger(
        self,
        trigger_id: str,
        *,
        body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageTriggerResponse:
        """Update an existing usage trigger

        Args:
            trigger_id: Usage trigger ID
            body: New trigger values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage trigger Modify result

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.update_trigger(trigger_id, body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UsageTriggerManagementWithRawResponse:
        return self._with_raw_response


class AsyncUsageTriggerManagement:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUsageTriggerManagementWithRawResponse(client, server, auth)

    async def create_new_trigger(
        self,
        *,
        body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageTriggerResponse:
        """Create a new usage trigger, which will send an alert when the number of device location service transactions
        reaches a specified percentage of the monthly subscription amount.

        Args:
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage trigger Add result

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (await self._with_raw_response.create_new_trigger(body=body, request_options=request_options)).unwrap()

    async def delete_trigger(
        self, account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSuccessResult:
        """eletes the specified usage trigger from the given account

        Args:
            account_name: Account name
            trigger_id: Usage trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Delete result

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.delete_trigger(account_name, trigger_id, request_options=request_options)
        ).unwrap()

    async def update_trigger(
        self,
        trigger_id: str,
        *,
        body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UsageTriggerResponse:
        """Update an existing usage trigger

        Args:
            trigger_id: Usage trigger ID
            body: New trigger values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Usage trigger Modify result

        Raises:
            ApiError: Unexpected error ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.update_trigger(trigger_id, body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncUsageTriggerManagementWithRawResponse:
        return self._with_raw_response


class UsageTriggerManagementWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_new_trigger(
        self,
        *,
        body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageTriggerResponse, CreateNewTriggerErrorBody]:
        """Create a new usage trigger, which will send an alert when the number of device location service transactions
        reaches a specified percentage of the monthly subscription amount.

        Args:
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/usage/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsageTriggerAddRequest | UsageTriggerAddRequestDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UsageTriggerResponse],
            error_mapper=create_new_trigger_error_mapper,
            request_options=request_options,
        )

    def delete_trigger(
        self, account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSuccessResult, DeleteTriggerErrorBody]:
        """eletes the specified usage trigger from the given account

        Args:
            account_name: Account name
            trigger_id: Usage trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.subscription_server("/usage/accounts/{accountName}/triggers/{triggerId}"),
            path_params=[param[str]("accountName", account_name), param[str]("triggerId", trigger_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=delete_trigger_error_mapper,
            request_options=request_options,
        )

    def update_trigger(
        self,
        trigger_id: str,
        *,
        body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageTriggerResponse, UpdateTriggerErrorBody]:
        """Update an existing usage trigger

        Args:
            trigger_id: Usage trigger ID
            body: New trigger values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/usage/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UsageTriggerResponse],
            error_mapper=update_trigger_error_mapper,
            request_options=request_options,
        )


class AsyncUsageTriggerManagementWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_new_trigger(
        self,
        *,
        body: UsageTriggerAddRequest | UsageTriggerAddRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageTriggerResponse, CreateNewTriggerErrorBody]:
        """Create a new usage trigger, which will send an alert when the number of device location service transactions
        reaches a specified percentage of the monthly subscription amount.

        Args:
            body: License assignment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/usage/triggers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsageTriggerAddRequest | UsageTriggerAddRequestDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UsageTriggerResponse],
            error_mapper=create_new_trigger_error_mapper,
            request_options=request_options,
        )

    async def delete_trigger(
        self, account_name: str, trigger_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSuccessResult, DeleteTriggerErrorBody]:
        """eletes the specified usage trigger from the given account

        Args:
            account_name: Account name
            trigger_id: Usage trigger ID
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.subscription_server("/usage/accounts/{accountName}/triggers/{triggerId}"),
            path_params=[param[str]("accountName", account_name), param[str]("triggerId", trigger_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSuccessResult],
            error_mapper=delete_trigger_error_mapper,
            request_options=request_options,
        )

    async def update_trigger(
        self,
        trigger_id: str,
        *,
        body: UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UsageTriggerResponse, UpdateTriggerErrorBody]:
        """Update an existing usage trigger

        Args:
            trigger_id: Usage trigger ID
            body: New trigger values
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.subscription_server("/usage/triggers/{triggerId}"),
            path_params=[param[str]("triggerId", trigger_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UsageTriggerUpdateRequest | UsageTriggerUpdateRequestDict | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[UsageTriggerResponse],
            error_mapper=update_trigger_error_mapper,
            request_options=request_options,
        )
