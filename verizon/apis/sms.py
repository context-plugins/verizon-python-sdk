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
from ..errors.list_devices_smsmessages_error import (
    ListDevicesSmsmessagesErrorBody,
    list_devices_smsmessages_error_mapper,
)
from ..errors.send_smsto_device_error import SendSmstoDeviceErrorBody, send_smsto_device_error_mapper
from ..errors.start_queued_smsdelivery_error import (
    StartQueuedSmsdeliveryErrorBody,
    start_queued_smsdelivery_error_mapper,
)
from ..models.connectivity_management_success_result import ConnectivityManagementSuccessResult
from ..models.device_management_result import DeviceManagementResult
from ..models.smsmessages_query_result import SmsmessagesQueryResult
from ..models.smssend_request import SmssendRequest, SmssendRequestDict
from ..server.server import Server


class Sms:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SmsWithRawResponse(client, server, auth)

    def list_devices_sms_messages(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SmsmessagesQueryResult:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

        Args:
            aname: Account name.
            next: Continue the previous query from the URL in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.list_devices_sms_messages(
            aname, next=next, request_options=request_options
        ).unwrap()

    def send_sms_to_device(
        self, body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceManagementResult:
        """The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due
        to traffic and routing considerations.

        Args:
            body: Request to send SMS.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.send_sms_to_device(body, request_options=request_options).unwrap()

    def start_queued_sms_delivery(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConnectivityManagementSuccessResult:
        """Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the
        EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by
        your application, either by callback or synchronously with GET /sms/{accountName}/history.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return self._with_raw_response.start_queued_sms_delivery(aname, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SmsWithRawResponse:
        return self._with_raw_response


class AsyncSms:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSmsWithRawResponse(client, server, auth)

    async def list_devices_sms_messages(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SmsmessagesQueryResult:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

        Args:
            aname: Account name.
            next: Continue the previous query from the URL in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.list_devices_sms_messages(aname, next=next, request_options=request_options)
        ).unwrap()

    async def send_sms_to_device(
        self, body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeviceManagementResult:
        """The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due
        to traffic and routing considerations.

        Args:
            body: Request to send SMS.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID received on a successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (await self._with_raw_response.send_sms_to_device(body, request_options=request_options)).unwrap()

    async def start_queued_sms_delivery(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ConnectivityManagementSuccessResult:
        """Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the
        EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by
        your application, either by callback or synchronously with GET /sms/{accountName}/history.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response.

        Raises:
            ApiError: Error response. ``error`` is ``ConnectivityManagementResult | RawError``."""
        return (
            await self._with_raw_response.start_queued_sms_delivery(aname, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSmsWithRawResponse:
        return self._with_raw_response


class SmsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_devices_sms_messages(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SmsmessagesQueryResult, ListDevicesSmsmessagesErrorBody]:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

        Args:
            aname: Account name.
            next: Continue the previous query from the URL in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{aname}/history"),
            path_params=[param[str]("aname", aname)],
            query_params=[param[int | None]("next", next)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SmsmessagesQueryResult],
            error_mapper=list_devices_smsmessages_error_mapper,
            request_options=request_options,
        )

    def send_sms_to_device(
        self, body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceManagementResult, SendSmstoDeviceErrorBody]:
        """The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due
        to traffic and routing considerations.

        Args:
            body: Request to send SMS.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SmssendRequest | SmssendRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=send_smsto_device_error_mapper,
            request_options=request_options,
        )

    def start_queued_sms_delivery(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConnectivityManagementSuccessResult, StartQueuedSmsdeliveryErrorBody]:
        """Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the
        EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by
        your application, either by callback or synchronously with GET /sms/{accountName}/history.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{aname}/startCallbacks"),
            path_params=[param[str]("aname", aname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=start_queued_smsdelivery_error_mapper,
            request_options=request_options,
        )


class AsyncSmsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_devices_sms_messages(
        self, aname: str, *, next: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SmsmessagesQueryResult, ListDevicesSmsmessagesErrorBody]:
        """When HTTP status is 202, a URL will be returned in the Location header of the form
        /sms/{aname}/history?next={token}. This URL can be used to request the next set of messages.

        Args:
            aname: Account name.
            next: Continue the previous query from the URL in Location Header.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{aname}/history"),
            path_params=[param[str]("aname", aname)],
            query_params=[param[int | None]("next", next)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SmsmessagesQueryResult],
            error_mapper=list_devices_smsmessages_error_mapper,
            request_options=request_options,
        )

    async def send_sms_to_device(
        self, body: SmssendRequest | SmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeviceManagementResult, SendSmstoDeviceErrorBody]:
        """The messages are queued on the ThingSpace Platform and sent as soon as possible, but they may be delayed due
        to traffic and routing considerations.

        Args:
            body: Request to send SMS.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SmssendRequest | SmssendRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[DeviceManagementResult],
            error_mapper=send_smsto_device_error_mapper,
            request_options=request_options,
        )

    async def start_queued_sms_delivery(
        self, aname: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ConnectivityManagementSuccessResult, StartQueuedSmsdeliveryErrorBody]:
        """Tells the ThingSpace Platform to start sending mobile-originated SMS messages through the
        EnhancedConnectivityService callback service. SMS messages from devices are queued until they are retrieved by
        your application, either by callback or synchronously with GET /sms/{accountName}/history.

        Args:
            aname: Account name.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{aname}/startCallbacks"),
            path_params=[param[str]("aname", aname)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ConnectivityManagementSuccessResult],
            error_mapper=start_queued_smsdelivery_error_mapper,
            request_options=request_options,
        )
