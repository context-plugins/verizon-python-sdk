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
from ..errors.deviceprovhistory_using_post_error import (
    DeviceprovhistoryUsingPostErrorBody,
    deviceprovhistory_using_post_error_mapper,
)
from ..errors.retrieve_global_list_error import RetrieveGlobalListErrorBody, retrieve_global_list_error_mapper
from ..models.e_simglobal_device_list import ESimglobalDeviceList, ESimglobalDeviceListDict
from ..models.e_simprovhistory_request import ESimprovhistoryRequest, ESimprovhistoryRequestDict
from ..models.e_simrequest_response import ESimrequestResponse
from ..server.server import Server


class GlobalReporting:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GlobalReportingWithRawResponse(client, server, auth)

    def retrieve_global_list(
        self,
        body: ESimglobalDeviceList | ESimglobalDeviceListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ESimrequestResponse:
        """Retrieve a list of all devices associated with an account.

        Args:
            body: Device List
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return self._with_raw_response.retrieve_global_list(body, request_options=request_options).unwrap()

    def deviceprovhistory_using_post(
        self,
        body: ESimprovhistoryRequest | ESimprovhistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ESimrequestResponse:
        """Retrieve the provisioning history of a specific device or devices.

        Args:
            body: Device Provisioning History
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return self._with_raw_response.deviceprovhistory_using_post(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GlobalReportingWithRawResponse:
        return self._with_raw_response


class AsyncGlobalReporting:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGlobalReportingWithRawResponse(client, server, auth)

    async def retrieve_global_list(
        self,
        body: ESimglobalDeviceList | ESimglobalDeviceListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ESimrequestResponse:
        """Retrieve a list of all devices associated with an account.

        Args:
            body: Device List
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return (await self._with_raw_response.retrieve_global_list(body, request_options=request_options)).unwrap()

    async def deviceprovhistory_using_post(
        self,
        body: ESimprovhistoryRequest | ESimprovhistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ESimrequestResponse:
        """Retrieve the provisioning history of a specific device or devices.

        Args:
            body: Device Provisioning History
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Request ID

        Raises:
            ApiError: Bad request Unauthorized Forbidden Not Found / Does not exist Format / Request Unacceptable Too
                many requests ``error`` is ``ESimrestErrorResponse | RawError``."""
        return (
            await self._with_raw_response.deviceprovhistory_using_post(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGlobalReportingWithRawResponse:
        return self._with_raw_response


class GlobalReportingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def retrieve_global_list(
        self,
        body: ESimglobalDeviceList | ESimglobalDeviceListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ESimrequestResponse, RetrieveGlobalListErrorBody]:
        """Retrieve a list of all devices associated with an account.

        Args:
            body: Device List
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/devices/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ESimglobalDeviceList | ESimglobalDeviceListDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=retrieve_global_list_error_mapper,
            request_options=request_options,
        )

    def deviceprovhistory_using_post(
        self,
        body: ESimprovhistoryRequest | ESimprovhistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ESimrequestResponse, DeviceprovhistoryUsingPostErrorBody]:
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
            body=json_body[ESimprovhistoryRequest | ESimprovhistoryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=deviceprovhistory_using_post_error_mapper,
            request_options=request_options,
        )


class AsyncGlobalReportingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def retrieve_global_list(
        self,
        body: ESimglobalDeviceList | ESimglobalDeviceListDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ESimrequestResponse, RetrieveGlobalListErrorBody]:
        """Retrieve a list of all devices associated with an account.

        Args:
            body: Device List
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/m2m/v2/devices/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ESimglobalDeviceList | ESimglobalDeviceListDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=retrieve_global_list_error_mapper,
            request_options=request_options,
        )

    async def deviceprovhistory_using_post(
        self,
        body: ESimprovhistoryRequest | ESimprovhistoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ESimrequestResponse, DeviceprovhistoryUsingPostErrorBody]:
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
            body=json_body[ESimprovhistoryRequest | ESimprovhistoryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[ESimrequestResponse],
            error_mapper=deviceprovhistory_using_post_error_mapper,
            request_options=request_options,
        )
