from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
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
from ..models.gbi_request_response5 import GbiRequestResponse5
from ..models.gbiactivate_request5 import GbiactivateRequest5, GbiactivateRequest5Dict
from ..models.gbichange_request5 import GbichangeRequest5, GbichangeRequest5Dict
from ..models.gbidevice_detailsresponse5 import GbideviceDetailsresponse5
from ..models.gbidevice_id5 import GbideviceId5, GbideviceId5Dict
from ..server.server import Server


class GbiDeviceActions5:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GbiDeviceActions5WithRawResponse(client, server, auth)

    def business_internet_serviceplanchange(
        self, body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GbiRequestResponse5:
        """Change a device's service plan to use 5G BI.

        Args:
            body: This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service
                plan can change for an active device up to four times per month but will require address validation for
                each change. The service plan cannot be changed for a device while its service is suspended.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A request ID is returned as a successful response. Use a callback to see the details associated with the
            request ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.business_internet_serviceplanchange(
            body, request_options=request_options
        ).unwrap()

    def business_internetactivate_using_post(
        self,
        body: GbiactivateRequest5 | GbiactivateRequest5Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GbiRequestResponse5:
        """Uses the device's ICCID and IMEI to activate service.

        Args:
            body: Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is
                required for activating as Public Static. Leave <code>publicIpRestriction</code> undefined to activate
                as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile
                Private Network (MPN).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A request ID is returned as a successful response. Use a callback to see the details associated with the
            request ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.business_internetactivate_using_post(
            body, request_options=request_options
        ).unwrap()

    def business_internetlist_device_information(
        self, body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GbideviceDetailsresponse5:
        """Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's
        properties.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The device's details will be returned from a successful request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.business_internetlist_device_information(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> GbiDeviceActions5WithRawResponse:
        return self._with_raw_response


class AsyncGbiDeviceActions5:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGbiDeviceActions5WithRawResponse(client, server, auth)

    async def business_internet_serviceplanchange(
        self, body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GbiRequestResponse5:
        """Change a device's service plan to use 5G BI.

        Args:
            body: This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service
                plan can change for an active device up to four times per month but will require address validation for
                each change. The service plan cannot be changed for a device while its service is suspended.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A request ID is returned as a successful response. Use a callback to see the details associated with the
            request ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.business_internet_serviceplanchange(body, request_options=request_options)
        ).unwrap()

    async def business_internetactivate_using_post(
        self,
        body: GbiactivateRequest5 | GbiactivateRequest5Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GbiRequestResponse5:
        """Uses the device's ICCID and IMEI to activate service.

        Args:
            body: Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is
                required for activating as Public Static. Leave <code>publicIpRestriction</code> undefined to activate
                as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile
                Private Network (MPN).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            A request ID is returned as a successful response. Use a callback to see the details associated with the
            request ID.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.business_internetactivate_using_post(body, request_options=request_options)
        ).unwrap()

    async def business_internetlist_device_information(
        self, body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> GbideviceDetailsresponse5:
        """Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's
        properties.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            The device's details will be returned from a successful request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.business_internetlist_device_information(
                body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGbiDeviceActions5WithRawResponse:
        return self._with_raw_response


class GbiDeviceActions5WithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def business_internet_serviceplanchange(
        self, body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GbiRequestResponse5, RawError]:
        """Change a device's service plan to use 5G BI.

        Args:
            body: This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service
                plan can change for an active device up to four times per month but will require address validation for
                each change. The service plan cannot be changed for a device while its service is suspended.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/actions/plan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbichangeRequest5 | GbichangeRequest5Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GbiRequestResponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def business_internetactivate_using_post(
        self,
        body: GbiactivateRequest5 | GbiactivateRequest5Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GbiRequestResponse5, RawError]:
        """Uses the device's ICCID and IMEI to activate service.

        Args:
            body: Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is
                required for activating as Public Static. Leave <code>publicIpRestriction</code> undefined to activate
                as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile
                Private Network (MPN).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbiactivateRequest5 | GbiactivateRequest5Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GbiRequestResponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def business_internetlist_device_information(
        self, body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GbideviceDetailsresponse5, RawError]:
        """Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's
        properties.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbideviceId5 | GbideviceId5Dict](body),
            auth_scheme=AnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GbideviceDetailsresponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncGbiDeviceActions5WithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def business_internet_serviceplanchange(
        self, body: GbichangeRequest5 | GbichangeRequest5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GbiRequestResponse5, RawError]:
        """Change a device's service plan to use 5G BI.

        Args:
            body: This endpoint is for use when changing a device's service plan to a 5G BI service plan. The service
                plan can change for an active device up to four times per month but will require address validation for
                each change. The service plan cannot be changed for a device while its service is suspended.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.hyper_precise_credentials("/actions/plan"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbichangeRequest5 | GbichangeRequest5Dict](body),
            auth_scheme=AsyncAnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GbiRequestResponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def business_internetactivate_using_post(
        self,
        body: GbiactivateRequest5 | GbiactivateRequest5Dict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GbiRequestResponse5, RawError]:
        """Uses the device's ICCID and IMEI to activate service.

        Args:
            body: Activate 5G BI service. Defining <code>publicIpRestriction</code> as "Unrestricted" or "Restricted" is
                required for activating as Public Static. Leave <code>publicIpRestriction</code> undefined to activate
                as Public Dynamic. Removing <code>publicIpRestriction</code> from the request will activate as Mobile
                Private Network (MPN).
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/actions/activate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbiactivateRequest5 | GbiactivateRequest5Dict](body),
            auth_scheme=AsyncAnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GbiRequestResponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def business_internetlist_device_information(
        self, body: GbideviceId5 | GbideviceId5Dict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GbideviceDetailsresponse5, RawError]:
        """Uses the decive's Integrated Circuit Card Identification Number (ICCID) to retrive and display the device's
        properties.

        Args:
            body: Device Profile Query
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.hyper_precise_credentials("/actions/list"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GbideviceId5 | GbideviceId5Dict](body),
            auth_scheme=AsyncAnySchemes(self._auth.thingspace_oauth, self._auth.vz_m2_m_token),
            decoder=json_decoder[GbideviceDetailsresponse5],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
