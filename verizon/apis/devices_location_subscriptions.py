from __future__ import annotations

from typing import Any
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
    json_decoder,
    param,
)
from ..errors.get_location_service_subscription_status_error import (
    GetLocationServiceSubscriptionStatusErrorBody,
    get_location_service_subscription_status_error_mapper,
)
from ..errors.get_location_service_usage_error import (
    GetLocationServiceUsageErrorBody,
    get_location_service_usage_error_mapper,
)
from ..models.device_location_subscription import DeviceLocationSubscription
from ..server.server import Server


class DevicesLocationSubscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DevicesLocationSubscriptionsWithRawResponse(client, server, auth)

    def get_location_service_subscription_status(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSubscription:
        """This subscriptions endpoint retrieves an account's current location subscription status.

        Args:
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device location subscription information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.get_location_service_subscription_status(
            account_name, request_options=request_options
        ).unwrap()

    def get_location_service_usage(self, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """This endpoint allows user to search for billable usage for accounts based on the provided date range.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Billable usage report.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return self._with_raw_response.get_location_service_usage(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DevicesLocationSubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncDevicesLocationSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDevicesLocationSubscriptionsWithRawResponse(client, server, auth)

    async def get_location_service_subscription_status(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceLocationSubscription:
        """This subscriptions endpoint retrieves an account's current location subscription status.

        Args:
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Device location subscription information.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return (
            await self._with_raw_response.get_location_service_subscription_status(
                account_name, request_options=request_options
            )
        ).unwrap()

    async def get_location_service_usage(self, *, request_options: RequestOptionsOrDict | None = None) -> Any:
        """This endpoint allows user to search for billable usage for accounts based on the provided date range.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Billable usage report.

        Raises:
            ApiError: Unexpected error. ``error`` is ``DeviceLocationResult | RawError``."""
        return (await self._with_raw_response.get_location_service_usage(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDevicesLocationSubscriptionsWithRawResponse:
        return self._with_raw_response


class DevicesLocationSubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_location_service_subscription_status(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSubscription, GetLocationServiceSubscriptionStatusErrorBody]:
        """This subscriptions endpoint retrieves an account's current location subscription status.

        Args:
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/subscriptions/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSubscription],
            error_mapper=get_location_service_subscription_status_error_mapper,
            request_options=request_options,
        )

    def get_location_service_usage(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetLocationServiceUsageErrorBody]:
        """This endpoint allows user to search for billable usage for accounts based on the provided date range.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/usage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Any],
            error_mapper=get_location_service_usage_error_mapper,
            request_options=request_options,
        )


class AsyncDevicesLocationSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_location_service_subscription_status(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceLocationSubscription, GetLocationServiceSubscriptionStatusErrorBody]:
        """This subscriptions endpoint retrieves an account's current location subscription status.

        Args:
            account_name: Account identifier in "##########-#####".
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.device_location("/subscriptions/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceLocationSubscription],
            error_mapper=get_location_service_subscription_status_error_mapper,
            request_options=request_options,
        )

    async def get_location_service_usage(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[Any, GetLocationServiceUsageErrorBody]:
        """This endpoint allows user to search for billable usage for accounts based on the provided date range.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.device_location("/usage"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[Any],
            error_mapper=get_location_service_usage_error_mapper,
            request_options=request_options,
        )
