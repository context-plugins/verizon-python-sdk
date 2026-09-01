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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_etxclient_certificate_error import (
    GetEtxclientCertificateErrorBody,
    get_etxclient_certificate_error_mapper,
)
from ..errors.get_etxconnection_url_error import GetEtxconnectionUrlErrorBody, get_etxconnection_url_error_mapper
from ..errors.get_etxconnection_url_multi_mec_error import (
    GetEtxconnectionUrlMultiMecErrorBody,
    get_etxconnection_url_multi_mec_error_mapper,
)
from ..errors.query_etxdevices_error import QueryEtxdevicesErrorBody, query_etxdevices_error_mapper
from ..errors.register_etxclient_error import RegisterEtxclientErrorBody, register_etxclient_error_mapper
from ..errors.renew_etxclient_certificate_error import (
    RenewEtxclientCertificateErrorBody,
    renew_etxclient_certificate_error_mapper,
)
from ..errors.unregister_etxclients_error import UnregisterEtxclientsErrorBody, unregister_etxclients_error_mapper
from ..models.client_persistence_response import ClientPersistenceResponse
from ..models.client_registration_request_v2 import ClientRegistrationRequestV2, ClientRegistrationRequestV2Dict
from ..models.client_registration_response import ClientRegistrationResponse
from ..models.connection_request import ConnectionRequest, ConnectionRequestDict
from ..models.connection_response import ConnectionResponse
from ..models.connection_response_v3 import ConnectionResponseV3
from ..models.devices_request import DevicesRequest, DevicesRequestDict
from ..models.devices_response import DevicesResponse
from ..models.etxclient_idlookup import EtxclientIdlookup, EtxclientIdlookupDict
from ..server.server import Server


class Etxregistration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EtxregistrationWithRawResponse(client, server, auth)

    def get_etx_client_certificate(
        self,
        id: EtxclientIdlookup | EtxclientIdlookupDict,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientPersistenceResponse:
        """With this API call the user can check the certificate of the device. At least one of the DeviceID, IMEI,
        ICCID or IMSI is required to make the call.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: One of the following IDs is required- DeviceID, IMEI, ICCID, IMSI. If more than one ID is provided, the
                API will return the certificate for the first ID found. The IDs are evaluated in the following order:
                DeviceID, IMEI, ICCID, IMSI. If the first provided ID is not found, the API will return an error.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Invalid request Unauthorized Forbidden Request Not Found Too Many Requests Internal server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return self._with_raw_response.get_etx_client_certificate(
            id, vendor_id, x_transaction_id=x_transaction_id, request_options=request_options
        ).unwrap()

    def get_etx_connection_url(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectionResponse:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Invalid request Unauthorized Forbidden Request Too Many Requests Internal server Error ``error``
                is ``EtxrespondingError | RawError``."""
        return self._with_raw_response.get_etx_connection_url(
            vendor_id, body, x_transaction_id=x_transaction_id, request_options=request_options
        ).unwrap()

    def get_etx_connection_url_multi_mec(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectionResponseV3:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        If there are multiple MECs that serve the location of the client all options are provided in the response, and
        the client is free to choose which MEC they want to connect.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Invalid request Unauthorized Forbidden Request Too Many Requests Internal server Error ``error``
                is ``EtxrespondingError | RawError``."""
        return self._with_raw_response.get_etx_connection_url_multi_mec(
            vendor_id, body, x_transaction_id=x_transaction_id, request_options=request_options
        ).unwrap()

    def query_etx_devices(
        self,
        body: DevicesRequest | DevicesRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DevicesResponse]:
        """This API allows retrieving devices by vendor ID and optional filters. The request should include the VendorID
        and any filters to apply.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval of devices

        Raises:
            ApiError: Invalid Request Unauthorized Request Internal Server Error ``error`` is ``EtxrespondingError |
                RawError``."""
        return self._with_raw_response.query_etx_devices(
            body, x_transaction_id=x_transaction_id, request_options=request_options
        ).unwrap()

    def register_etx_client(
        self,
        body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientRegistrationResponse:
        """With this API call the user (client) registers its device or software service to the ETX system. Therefore,
        when a connection is initiated from the device or software service to the ETX system along with the credential
        provided by this registration call, then the connection will be authorized.

        - The user can register multiple devices or software services, which can all be used at the same time.
        - There rules set in the system that limit the type and subtype of the clients that are allowed to be registered
            under the VendorID. The rules are created based ont he agreement between the Vendor and Verizon.
        - The user will only be able to register a limited number of devices or software services under the same
            VendorID. This registration limit is specified by the agreement between the Vendor and Verizon.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful Registration

        Raises:
            ApiError: Invalid Request Unauthorized Request Forbidden Request Too Many Requests Internal Server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return self._with_raw_response.register_etx_client(
            body, x_transaction_id=x_transaction_id, request_options=request_options
        ).unwrap()

    def renew_etx_client_certificate(
        self,
        device_id: UUID,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientRegistrationResponse:
        """With this API call the user (client) can:
        - renew the certificate of a device or software service in the ETX system if the original certificate has
            expired. If the client's certificate expired or going to expire within 30 days and new certificate will be
            issued. If the certificate expires more than 30 days, the current certificate will be returned to the
            client.
        - complete its device or software service registration to the ETX system if the original registration request
            was not successful because of a pending certificate generation. Whenever the user receives a "client
            registration is pending" response (HTTP 202) from POST /clients/registration call. The client should
            initiate this PUT API call to finish the registration process and get the required certificate.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_id: Value sent with the request.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful Registration

        Raises:
            ApiError: Invalid Request Unauthorized Request Forbidden Request Too Many Requests Internal Server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return self._with_raw_response.renew_etx_client_certificate(
            device_id, vendor_id, x_transaction_id=x_transaction_id, body=body, request_options=request_options
        ).unwrap()

    def unregister_etx_clients(
        self,
        device_ids: list[UUID],
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """With this API call the user (client) can unregister its devices and software services from the ETX system.
        The unregistered devices and services will no longer be able to use the ETX Message Exchange.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_ids: The list of device IDs and software service IDs to be unregistered
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful Deletion

        Raises:
            ApiError: Invalid Request Unauthorized Request Forbidden Request Too Many Requests Internal Server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return self._with_raw_response.unregister_etx_clients(
            device_ids, vendor_id, x_transaction_id=x_transaction_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EtxregistrationWithRawResponse:
        return self._with_raw_response


class AsyncEtxregistration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEtxregistrationWithRawResponse(client, server, auth)

    async def get_etx_client_certificate(
        self,
        id: EtxclientIdlookup | EtxclientIdlookupDict,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientPersistenceResponse:
        """With this API call the user can check the certificate of the device. At least one of the DeviceID, IMEI,
        ICCID or IMSI is required to make the call.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: One of the following IDs is required- DeviceID, IMEI, ICCID, IMSI. If more than one ID is provided, the
                API will return the certificate for the first ID found. The IDs are evaluated in the following order:
                DeviceID, IMEI, ICCID, IMSI. If the first provided ID is not found, the API will return an error.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Invalid request Unauthorized Forbidden Request Not Found Too Many Requests Internal server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return (
            await self._with_raw_response.get_etx_client_certificate(
                id, vendor_id, x_transaction_id=x_transaction_id, request_options=request_options
            )
        ).unwrap()

    async def get_etx_connection_url(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectionResponse:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Invalid request Unauthorized Forbidden Request Too Many Requests Internal server Error ``error``
                is ``EtxrespondingError | RawError``."""
        return (
            await self._with_raw_response.get_etx_connection_url(
                vendor_id, body, x_transaction_id=x_transaction_id, request_options=request_options
            )
        ).unwrap()

    async def get_etx_connection_url_multi_mec(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ConnectionResponseV3:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        If there are multiple MECs that serve the location of the client all options are provided in the response, and
        the client is free to choose which MEC they want to connect.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval

        Raises:
            ApiError: Invalid request Unauthorized Forbidden Request Too Many Requests Internal server Error ``error``
                is ``EtxrespondingError | RawError``."""
        return (
            await self._with_raw_response.get_etx_connection_url_multi_mec(
                vendor_id, body, x_transaction_id=x_transaction_id, request_options=request_options
            )
        ).unwrap()

    async def query_etx_devices(
        self,
        body: DevicesRequest | DevicesRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[DevicesResponse]:
        """This API allows retrieving devices by vendor ID and optional filters. The request should include the VendorID
        and any filters to apply.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful retrieval of devices

        Raises:
            ApiError: Invalid Request Unauthorized Request Internal Server Error ``error`` is ``EtxrespondingError |
                RawError``."""
        return (
            await self._with_raw_response.query_etx_devices(
                body, x_transaction_id=x_transaction_id, request_options=request_options
            )
        ).unwrap()

    async def register_etx_client(
        self,
        body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientRegistrationResponse:
        """With this API call the user (client) registers its device or software service to the ETX system. Therefore,
        when a connection is initiated from the device or software service to the ETX system along with the credential
        provided by this registration call, then the connection will be authorized.

        - The user can register multiple devices or software services, which can all be used at the same time.
        - There rules set in the system that limit the type and subtype of the clients that are allowed to be registered
            under the VendorID. The rules are created based ont he agreement between the Vendor and Verizon.
        - The user will only be able to register a limited number of devices or software services under the same
            VendorID. This registration limit is specified by the agreement between the Vendor and Verizon.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful Registration

        Raises:
            ApiError: Invalid Request Unauthorized Request Forbidden Request Too Many Requests Internal Server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return (
            await self._with_raw_response.register_etx_client(
                body, x_transaction_id=x_transaction_id, request_options=request_options
            )
        ).unwrap()

    async def renew_etx_client_certificate(
        self,
        device_id: UUID,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ClientRegistrationResponse:
        """With this API call the user (client) can:
        - renew the certificate of a device or software service in the ETX system if the original certificate has
            expired. If the client's certificate expired or going to expire within 30 days and new certificate will be
            issued. If the certificate expires more than 30 days, the current certificate will be returned to the
            client.
        - complete its device or software service registration to the ETX system if the original registration request
            was not successful because of a pending certificate generation. Whenever the user receives a "client
            registration is pending" response (HTTP 202) from POST /clients/registration call. The client should
            initiate this PUT API call to finish the registration process and get the required certificate.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_id: Value sent with the request.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful Registration

        Raises:
            ApiError: Invalid Request Unauthorized Request Forbidden Request Too Many Requests Internal Server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return (
            await self._with_raw_response.renew_etx_client_certificate(
                device_id, vendor_id, x_transaction_id=x_transaction_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def unregister_etx_clients(
        self,
        device_ids: list[UUID],
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """With this API call the user (client) can unregister its devices and software services from the ETX system.
        The unregistered devices and services will no longer be able to use the ETX Message Exchange.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_ids: The list of device IDs and software service IDs to be unregistered
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successful Deletion

        Raises:
            ApiError: Invalid Request Unauthorized Request Forbidden Request Too Many Requests Internal Server Error
                ``error`` is ``EtxrespondingError | RawError``."""
        return (
            await self._with_raw_response.unregister_etx_clients(
                device_ids, vendor_id, x_transaction_id=x_transaction_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEtxregistrationWithRawResponse:
        return self._with_raw_response


class EtxregistrationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_etx_client_certificate(
        self,
        id: EtxclientIdlookup | EtxclientIdlookupDict,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientPersistenceResponse, GetEtxclientCertificateErrorBody]:
        """With this API call the user can check the certificate of the device. At least one of the DeviceID, IMEI,
        ICCID or IMSI is required to make the call.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: One of the following IDs is required- DeviceID, IMEI, ICCID, IMSI. If more than one ID is provided, the
                API will return the certificate for the first ID found. The IDs are evaluated in the following order:
                DeviceID, IMEI, ICCID, IMSI. If the first provided ID is not found, the API will return an error.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            query_params=[param[EtxclientIdlookup | EtxclientIdlookupDict]("ID", id)],
            headers=[param[str]("VendorID", vendor_id), param[UUID | None]("X-Transaction-Id", x_transaction_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ClientPersistenceResponse],
            error_mapper=get_etxclient_certificate_error_mapper,
            request_options=request_options,
        )

    def get_etx_connection_url(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectionResponse, GetEtxconnectionUrlErrorBody]:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/clients/connection"),
            headers=[
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ConnectionRequest | ConnectionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ConnectionResponse],
            error_mapper=get_etxconnection_url_error_mapper,
            request_options=request_options,
        )

    def get_etx_connection_url_multi_mec(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectionResponseV3, GetEtxconnectionUrlMultiMecErrorBody]:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        If there are multiple MECs that serve the location of the client all options are provided in the response, and
        the client is free to choose which MEC they want to connect.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v3/clients/connection"),
            headers=[
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ConnectionRequest | ConnectionRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ConnectionResponseV3],
            error_mapper=get_etxconnection_url_multi_mec_error_mapper,
            request_options=request_options,
        )

    def query_etx_devices(
        self,
        body: DevicesRequest | DevicesRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DevicesResponse], QueryEtxdevicesErrorBody]:
        """This API allows retrieving devices by vendor ID and optional filters. The request should include the VendorID
        and any filters to apply.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v1/clients/query"),
            headers=[param[UUID | None]("X-Transaction-Id", x_transaction_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DevicesRequest | DevicesRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[DevicesResponse]],
            error_mapper=query_etxdevices_error_mapper,
            request_options=request_options,
        )

    def register_etx_client(
        self,
        body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientRegistrationResponse, RegisterEtxclientErrorBody]:
        """With this API call the user (client) registers its device or software service to the ETX system. Therefore,
        when a connection is initiated from the device or software service to the ETX system along with the credential
        provided by this registration call, then the connection will be authorized.

        - The user can register multiple devices or software services, which can all be used at the same time.
        - There rules set in the system that limit the type and subtype of the clients that are allowed to be registered
            under the VendorID. The rules are created based ont he agreement between the Vendor and Verizon.
        - The user will only be able to register a limited number of devices or software services under the same
            VendorID. This registration limit is specified by the agreement between the Vendor and Verizon.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            headers=[param[UUID | None]("X-Transaction-Id", x_transaction_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ClientRegistrationResponse],
            error_mapper=register_etxclient_error_mapper,
            request_options=request_options,
        )

    def renew_etx_client_certificate(
        self,
        device_id: UUID,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientRegistrationResponse, RenewEtxclientCertificateErrorBody]:
        """With this API call the user (client) can:
        - renew the certificate of a device or software service in the ETX system if the original certificate has
            expired. If the client's certificate expired or going to expire within 30 days and new certificate will be
            issued. If the certificate expires more than 30 days, the current certificate will be returned to the
            client.
        - complete its device or software service registration to the ETX system if the original registration request
            was not successful because of a pending certificate generation. Whenever the user receives a "client
            registration is pending" response (HTTP 202) from POST /clients/registration call. The client should
            initiate this PUT API call to finish the registration process and get the required certificate.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_id: Value sent with the request.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            headers=[
                param[UUID]("DeviceID", device_id),
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[Any | None](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ClientRegistrationResponse],
            error_mapper=renew_etxclient_certificate_error_mapper,
            request_options=request_options,
        )

    def unregister_etx_clients(
        self,
        device_ids: list[UUID],
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UnregisterEtxclientsErrorBody]:
        """With this API call the user (client) can unregister its devices and software services from the ETX system.
        The unregistered devices and services will no longer be able to use the ETX Message Exchange.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_ids: The list of device IDs and software service IDs to be unregistered
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            query_params=[param[list[UUID]]("DeviceIDs", device_ids)],
            headers=[
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=unregister_etxclients_error_mapper,
            request_options=request_options,
        )


class AsyncEtxregistrationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_etx_client_certificate(
        self,
        id: EtxclientIdlookup | EtxclientIdlookupDict,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientPersistenceResponse, GetEtxclientCertificateErrorBody]:
        """With this API call the user can check the certificate of the device. At least one of the DeviceID, IMEI,
        ICCID or IMSI is required to make the call.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: One of the following IDs is required- DeviceID, IMEI, ICCID, IMSI. If more than one ID is provided, the
                API will return the certificate for the first ID found. The IDs are evaluated in the following order:
                DeviceID, IMEI, ICCID, IMSI. If the first provided ID is not found, the API will return an error.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            query_params=[param[EtxclientIdlookup | EtxclientIdlookupDict]("ID", id)],
            headers=[param[str]("VendorID", vendor_id), param[UUID | None]("X-Transaction-Id", x_transaction_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ClientPersistenceResponse],
            error_mapper=get_etxclient_certificate_error_mapper,
            request_options=request_options,
        )

    async def get_etx_connection_url(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectionResponse, GetEtxconnectionUrlErrorBody]:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/clients/connection"),
            headers=[
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ConnectionRequest | ConnectionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ConnectionResponse],
            error_mapper=get_etxconnection_url_error_mapper,
            request_options=request_options,
        )

    async def get_etx_connection_url_multi_mec(
        self,
        vendor_id: str,
        body: ConnectionRequest | ConnectionRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ConnectionResponseV3, GetEtxconnectionUrlMultiMecErrorBody]:
        """With this API call the device or software service requests the MQTT URL for the location that it needs to
        connect. To determine the proper URL the device or software service needs to provide its ID (the one that was
        provided in the registration request), location (GPS coordinates), and whether it is on the Verizon cellular
        network or not.

        If there are multiple MECs that serve the location of the client all options are provided in the response, and
        the client is free to choose which MEC they want to connect.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v3/clients/connection"),
            headers=[
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[ConnectionRequest | ConnectionRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ConnectionResponseV3],
            error_mapper=get_etxconnection_url_multi_mec_error_mapper,
            request_options=request_options,
        )

    async def query_etx_devices(
        self,
        body: DevicesRequest | DevicesRequestDict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[DevicesResponse], QueryEtxdevicesErrorBody]:
        """This API allows retrieving devices by vendor ID and optional filters. The request should include the VendorID
        and any filters to apply.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v1/clients/query"),
            headers=[param[UUID | None]("X-Transaction-Id", x_transaction_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DevicesRequest | DevicesRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[DevicesResponse]],
            error_mapper=query_etxdevices_error_mapper,
            request_options=request_options,
        )

    async def register_etx_client(
        self,
        body: ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientRegistrationResponse, RegisterEtxclientErrorBody]:
        """With this API call the user (client) registers its device or software service to the ETX system. Therefore,
        when a connection is initiated from the device or software service to the ETX system along with the credential
        provided by this registration call, then the connection will be authorized.

        - The user can register multiple devices or software services, which can all be used at the same time.
        - There rules set in the system that limit the type and subtype of the clients that are allowed to be registered
            under the VendorID. The rules are created based ont he agreement between the Vendor and Verizon.
        - The user will only be able to register a limited number of devices or software services under the same
            VendorID. This registration limit is specified by the agreement between the Vendor and Verizon.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            body: The request body.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            headers=[param[UUID | None]("X-Transaction-Id", x_transaction_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ClientRegistrationRequestV2 | ClientRegistrationRequestV2Dict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ClientRegistrationResponse],
            error_mapper=register_etxclient_error_mapper,
            request_options=request_options,
        )

    async def renew_etx_client_certificate(
        self,
        device_id: UUID,
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        body: Any | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ClientRegistrationResponse, RenewEtxclientCertificateErrorBody]:
        """With this API call the user (client) can:
        - renew the certificate of a device or software service in the ETX system if the original certificate has
            expired. If the client's certificate expired or going to expire within 30 days and new certificate will be
            issued. If the certificate expires more than 30 days, the current certificate will be returned to the
            client.
        - complete its device or software service registration to the ETX system if the original registration request
            was not successful because of a pending certificate generation. Whenever the user receives a "client
            registration is pending" response (HTTP 202) from POST /clients/registration call. The client should
            initiate this PUT API call to finish the registration process and get the required certificate.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_id: Value sent with the request.
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            headers=[
                param[UUID]("DeviceID", device_id),
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[Any | None](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[ClientRegistrationResponse],
            error_mapper=renew_etxclient_certificate_error_mapper,
            request_options=request_options,
        )

    async def unregister_etx_clients(
        self,
        device_ids: list[UUID],
        vendor_id: str,
        *,
        x_transaction_id: UUID | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UnregisterEtxclientsErrorBody]:
        """With this API call the user (client) can unregister its devices and software services from the ETX system.
        The unregistered devices and services will no longer be able to use the ETX Message Exchange.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            device_ids: The list of device IDs and software service IDs to be unregistered
            vendor_id: The VendorID set during the Vendor registration call.
            x_transaction_id: Optional transaction identifier for tracing requests. If not provided, the application
                will generate one.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.imp_server("/api/v2/clients/registration"),
            query_params=[param[list[UUID]]("DeviceIDs", device_ids)],
            headers=[
                param[str]("VendorID", vendor_id),
                param[UUID | None]("X-Transaction-Id", x_transaction_id),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=unregister_etxclients_error_mapper,
            request_options=request_options,
        )
