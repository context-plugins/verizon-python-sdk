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
from ..models.giorequest_response import GiorequestResponse
from ..models.giosmssend_request import GiosmssendRequest, GiosmssendRequestDict
from ..models.sms_messages_response import SmsMessagesResponse
from ..models.smsevent_history_request import SmseventHistoryRequest, SmseventHistoryRequestDict
from ..models.success_response import SuccessResponse
from ..server.server import Server


class DeviceSmsMessaging:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DeviceSmsMessagingWithRawResponse(client, server, auth)

    def get_sms_messages(
        self, account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SmsMessagesResponse:
        """Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

        Args:
            account_name: Numeric account name
            next: Continue the previous query from the pageUrl in Location Header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_sms_messages(
            account_name, next=next, request_options=request_options
        ).unwrap()

    def list_sms_message_history(
        self,
        body: SmseventHistoryRequest | SmseventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Returns a list of sms history for a given device during a specified time frame.

        Args:
            body: Device Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sms_message_history(body, request_options=request_options).unwrap()

    def send_an_sms_message(
        self, body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible,
        but they may be delayed due to traffic and routing considerations.

        Args:
            body: SMS message to an indiividual device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.send_an_sms_message(body, request_options=request_options).unwrap()

    def start_sms_message_delivery(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Starts delivery of SMS messages for the specified account.

        Args:
            account_name: Numeric account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request Success Message

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.start_sms_message_delivery(
            account_name, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DeviceSmsMessagingWithRawResponse:
        return self._with_raw_response


class AsyncDeviceSmsMessaging:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDeviceSmsMessagingWithRawResponse(client, server, auth)

    async def get_sms_messages(
        self, account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> SmsMessagesResponse:
        """Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

        Args:
            account_name: Numeric account name
            next: Continue the previous query from the pageUrl in Location Header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful response

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_sms_messages(account_name, next=next, request_options=request_options)
        ).unwrap()

    async def list_sms_message_history(
        self,
        body: SmseventHistoryRequest | SmseventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GiorequestResponse:
        """Returns a list of sms history for a given device during a specified time frame.

        Args:
            body: Device Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_sms_message_history(body, request_options=request_options)).unwrap()

    async def send_an_sms_message(
        self, body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GiorequestResponse:
        """Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible,
        but they may be delayed due to traffic and routing considerations.

        Args:
            body: SMS message to an indiividual device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.send_an_sms_message(body, request_options=request_options)).unwrap()

    async def start_sms_message_delivery(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SuccessResponse:
        """Starts delivery of SMS messages for the specified account.

        Args:
            account_name: Numeric account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request Success Message

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.start_sms_message_delivery(account_name, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDeviceSmsMessagingWithRawResponse:
        return self._with_raw_response


class DeviceSmsMessagingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_sms_messages(
        self, account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SmsMessagesResponse, RawError]:
        """Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

        Args:
            account_name: Numeric account name
            next: Continue the previous query from the pageUrl in Location Header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{accountName}/history"),
            path_params=[param[str]("accountName", account_name)],
            query_params=[param[str | None]("next", next)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SmsMessagesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_sms_message_history(
        self,
        body: SmseventHistoryRequest | SmseventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Returns a list of sms history for a given device during a specified time frame.

        Args:
            body: Device Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/sms/history/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SmseventHistoryRequest | SmseventHistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def send_an_sms_message(
        self, body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible,
        but they may be delayed due to traffic and routing considerations.

        Args:
            body: SMS message to an indiividual device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GiosmssendRequest | GiosmssendRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def start_sms_message_delivery(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, RawError]:
        """Starts delivery of SMS messages for the specified account.

        Args:
            account_name: Numeric account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{accountName}/startCallbacks"),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SuccessResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDeviceSmsMessagingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_sms_messages(
        self, account_name: str, *, next: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SmsMessagesResponse, RawError]:
        """Retrieves queued SMS messages sent by all M2M MC devices associated with an account.

        Args:
            account_name: Numeric account name
            next: Continue the previous query from the pageUrl in Location Header
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{accountName}/history"),
            path_params=[param[str]("accountName", account_name)],
            query_params=[param[str | None]("next", next)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SmsMessagesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_sms_message_history(
        self,
        body: SmseventHistoryRequest | SmseventHistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Returns a list of sms history for a given device during a specified time frame.

        Args:
            body: Device Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/devices/sms/history/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SmseventHistoryRequest | SmseventHistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def send_an_sms_message(
        self, body: GiosmssendRequest | GiosmssendRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GiorequestResponse, RawError]:
        """Sends an SMS message to one device. Messages are queued on the M2M MC Platform and sent as soon as possible,
        but they may be delayed due to traffic and routing considerations.

        Args:
            body: SMS message to an indiividual device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GiosmssendRequest | GiosmssendRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GiorequestResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def start_sms_message_delivery(
        self, account_name: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SuccessResponse, RawError]:
        """Starts delivery of SMS messages for the specified account.

        Args:
            account_name: Numeric account name
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/m2m/v1/sms/{accountName}/startCallbacks"),
            path_params=[param[str]("accountName", account_name)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[SuccessResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
