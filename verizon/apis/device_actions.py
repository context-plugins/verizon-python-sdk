from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AllSchemes,
    ApiResult,
    AsyncAllSchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.account_details import AccountDetails
from ..models.aggregate_usage import AggregateUsage, AggregateUsageDict
from ..models.daily_usage import DailyUsage, DailyUsageDict
from ..models.daily_usage_response import DailyUsageResponse
from ..models.get_device_list_with_profiles_request import (
    GetDeviceListWithProfilesRequest,
    GetDeviceListWithProfilesRequestDict,
)
from ..models.giorequest_response import GiorequestResponse
from ..models.provhistory_request import ProvhistoryRequest, ProvhistoryRequestDict
from ..models.status_response import StatusResponse
from ..server.server import Server


class DeviceActions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceActionsWithRawResponse(client, server, auth)

    def account_information(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountDetails:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account details **Note:** The response will have placeholders. You can identify the placeholders by
            ``"sizeKb":0`` and that the record will only have ``name`` and ``sizeKb`` values.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.account_information(account_name, request_options=request_options).unwrap()

    def aggregate_usage(
        self, body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Retrieve the aggregate usage for a device or a number of devices.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.aggregate_usage(body, request_options=request_options).unwrap()

    def daily_usage(
        self, body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DailyUsageResponse:
        """Retrieve the daily usage for a device, for a specified period of time, segmented by day

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Syncronous response of device usage

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.daily_usage(body, request_options=request_options).unwrap()

    def get_asynchronous_request_status(
        self, account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StatusResponse:
        """Get the status of an asynchronous request made with the Device Actions.

        Args:
            account_name: Value sent with the request.
            request_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_asynchronous_request_status(
            account_name, request_id, request_options=request_options
        ).unwrap()

    def retrieve_device_provisioning_history(
        self, body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Retrieve the provisioning history of a specific device or devices.

        Args:
            body: Device Provisioning History
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_device_provisioning_history(
            body, request_options=request_options
        ).unwrap()

    def retrieve_the_global_device_list(
        self,
        body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Allows the profile to fetch the complete device list. This works with Verizon US and Global profiles.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_the_global_device_list(body, request_options=request_options).unwrap()

    def service_plan_list(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountDetails:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account details **Note:** The response will have placeholders. You can identify the placeholders by
            ``"sizeKb":0`` and that the record will only have ``name`` and ``sizeKb`` values.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.service_plan_list(account_name, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DeviceActionsWithRawResponse:
        return self._with_raw_response


class AsyncDeviceActions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceActionsWithRawResponse(client, server, auth)

    async def account_information(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountDetails:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account details **Note:** The response will have placeholders. You can identify the placeholders by
            ``"sizeKb":0`` and that the record will only have ``name`` and ``sizeKb`` values.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.account_information(account_name, request_options=request_options)
        ).unwrap()

    async def aggregate_usage(
        self, body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Retrieve the aggregate usage for a device or a number of devices.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.aggregate_usage(body, request_options=request_options)).unwrap()

    async def daily_usage(
        self, body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DailyUsageResponse:
        """Retrieve the daily usage for a device, for a specified period of time, segmented by day

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Syncronous response of device usage

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.daily_usage(body, request_options=request_options)).unwrap()

    async def get_asynchronous_request_status(
        self, account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> StatusResponse:
        """Get the status of an asynchronous request made with the Device Actions.

        Args:
            account_name: Value sent with the request.
            request_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_asynchronous_request_status(
                account_name, request_id, request_options=request_options
            )
        ).unwrap()

    async def retrieve_device_provisioning_history(
        self, body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Retrieve the provisioning history of a specific device or devices.

        Args:
            body: Device Provisioning History
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_device_provisioning_history(body, request_options=request_options)
        ).unwrap()

    async def retrieve_the_global_device_list(
        self,
        body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Allows the profile to fetch the complete device list. This works with Verizon US and Global profiles.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_the_global_device_list(body, request_options=request_options)
        ).unwrap()

    async def service_plan_list(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountDetails:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Account details **Note:** The response will have placeholders. You can identify the placeholders by
            ``"sizeKb":0`` and that the record will only have ``name`` and ``sizeKb`` values.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.service_plan_list(account_name, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceActionsWithRawResponse:
        return self._with_raw_response


class DeviceActionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def account_information(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountDetails, RawError]:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v1/accounts/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountDetails],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def aggregate_usage(
        self, body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Retrieve the aggregate usage for a device or a number of devices.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/devices/usage/actions/list/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AggregateUsage | AggregateUsageDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def daily_usage(
        self, body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DailyUsageResponse, RawError]:
        """Retrieve the daily usage for a device, for a specified period of time, segmented by day

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/devices/usage/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DailyUsage | DailyUsageDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DailyUsageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_asynchronous_request_status(
        self, account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StatusResponse, RawError]:
        """Get the status of an asynchronous request made with the Device Actions.

        Args:
            account_name: Value sent with the request.
            request_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v2/accounts/{accountName}/requests/{requestID}/status"
            ),
            path_params=[param[str]("accountName", account_name), param[str]("requestID", request_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[StatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_device_provisioning_history(
        self, body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Retrieve the provisioning history of a specific device or devices.

        Args:
            body: Device Provisioning History
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/devices/history/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProvhistoryRequest | ProvhistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_the_global_device_list(
        self,
        body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Allows the profile to fetch the complete device list. This works with Verizon US and Global profiles.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/devices/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def service_plan_list(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountDetails, RawError]:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v1/plans/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountDetails],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDeviceActionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def account_information(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountDetails, RawError]:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v1/accounts/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountDetails],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def aggregate_usage(
        self, body: AggregateUsage | AggregateUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Retrieve the aggregate usage for a device or a number of devices.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/devices/usage/actions/list/aggregate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AggregateUsage | AggregateUsageDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def daily_usage(
        self, body: DailyUsage | DailyUsageDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DailyUsageResponse, RawError]:
        """Retrieve the daily usage for a device, for a specified period of time, segmented by day

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/v1/devices/usage/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DailyUsage | DailyUsageDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DailyUsageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_asynchronous_request_status(
        self, account_name: str, request_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[StatusResponse, RawError]:
        """Get the status of an asynchronous request made with the Device Actions.

        Args:
            account_name: Value sent with the request.
            request_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials(
                "/m2m/v2/accounts/{accountName}/requests/{requestID}/status"
            ),
            path_params=[param[str]("accountName", account_name), param[str]("requestID", request_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[StatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_device_provisioning_history(
        self, body: ProvhistoryRequest | ProvhistoryRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Retrieve the provisioning history of a specific device or devices.

        Args:
            body: Device Provisioning History
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/devices/history/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProvhistoryRequest | ProvhistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_the_global_device_list(
        self,
        body: GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Allows the profile to fetch the complete device list. This works with Verizon US and Global profiles.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/devices/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetDeviceListWithProfilesRequest | GetDeviceListWithProfilesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def service_plan_list(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountDetails, RawError]:
        """Retrieve all of the service plans, features and carriers associated with the account specified.

        Args:
            account_name: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/v1/plans/{accountName}"),
            path_params=[param[str]("accountName", account_name)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[AccountDetails],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
