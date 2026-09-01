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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.create_configuration_error import CreateConfigurationErrorBody, create_configuration_error_mapper
from ..errors.delete_configuration_error import DeleteConfigurationErrorBody, delete_configuration_error_mapper
from ..errors.get_configuration_error import GetConfigurationErrorBody, get_configuration_error_mapper
from ..errors.get_configuration_list_error import GetConfigurationListErrorBody, get_configuration_list_error_mapper
from ..errors.update_configuration_error import UpdateConfigurationErrorBody, update_configuration_error_mapper
from ..models.configuration_list_item import ConfigurationListItem
from ..models.geo_fence_configuration_request import GeoFenceConfigurationRequest, GeoFenceConfigurationRequestDict
from ..models.geo_fence_configuration_response import GeoFenceConfigurationResponse
from ..models.geo_fence_configuration_update_request import (
    GeoFenceConfigurationUpdateRequest,
    GeoFenceConfigurationUpdateRequestDict,
)
from ..server.server import Server


class EtxappConfiguration:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EtxappConfigurationWithRawResponse(client, server, auth)

    def create_configuration(
        self,
        vendor_id: str,
        body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GeoFenceConfigurationResponse:
        """This endpoint creates a new configuration in the system. The data for the new configuration should be
        provided as JSON in the body of the POST request. The system will return with a unique ID for the configuration,
        which is needed for any further manipulation (update or delete) of the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration created

        Raises:
            ApiError: Invalid configuration Forbidden Too many requests ``error`` is ``ResponseError | RawError``."""
        return self._with_raw_response.create_configuration(vendor_id, body, request_options=request_options).unwrap()

    def delete_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint deletes a specific configuration from the system. It requires the configuration ID parameter,
        which was provided by the POST (create) operation.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration deleted

        Raises:
            ApiError: Forbidden Too many requests ``error`` is ``ResponseError | RawError``."""
        return self._with_raw_response.delete_configuration(id, vendor_id, request_options=request_options).unwrap()

    def get_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GeoFenceConfigurationResponse:
        """This endpoint fetches and returns a specific configuration's details. The configuration ID parameter, which
        was provided when the configuration was created through the POST request, is need to retrieve the configuration
        details.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration found

        Raises:
            ApiError: Forbidden Configuration not found Too many requests ``error`` is ``ResponseError | RawError``."""
        return self._with_raw_response.get_configuration(id, vendor_id, request_options=request_options).unwrap()

    def get_configuration_list(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ConfigurationListItem]:
        """This endpoint fetches and returns the list of configurations defined by the Vendor. The list contains the
        configurations' identifier, name, description, and active flag. The vendor ID is provided when the configuration
        is created through the POST request.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration list was queried successfully

        Raises:
            ApiError: Forbidden Configuration not found Too many requests ``error`` is ``ResponseError | RawError``."""
        return self._with_raw_response.get_configuration_list(vendor_id, request_options=request_options).unwrap()

    def update_configuration(
        self,
        id: str,
        vendor_id: str,
        body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint updates an existing configuration. Similar to POST, the updated data for the configuration
        should be provided as JSON in the body of the PUT request. The configuration ID parameter, which was provided by
        the POST (create) operation, is required to do any updates on the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration applied

        Raises:
            ApiError: Invalid configuration Forbidden Configuration not found Too many requests ``error`` is
                ``ResponseError | RawError``."""
        return self._with_raw_response.update_configuration(
            id, vendor_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> EtxappConfigurationWithRawResponse:
        return self._with_raw_response


class AsyncEtxappConfiguration:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEtxappConfigurationWithRawResponse(client, server, auth)

    async def create_configuration(
        self,
        vendor_id: str,
        body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GeoFenceConfigurationResponse:
        """This endpoint creates a new configuration in the system. The data for the new configuration should be
        provided as JSON in the body of the POST request. The system will return with a unique ID for the configuration,
        which is needed for any further manipulation (update or delete) of the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration created

        Raises:
            ApiError: Invalid configuration Forbidden Too many requests ``error`` is ``ResponseError | RawError``."""
        return (
            await self._with_raw_response.create_configuration(vendor_id, body, request_options=request_options)
        ).unwrap()

    async def delete_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """This endpoint deletes a specific configuration from the system. It requires the configuration ID parameter,
        which was provided by the POST (create) operation.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration deleted

        Raises:
            ApiError: Forbidden Too many requests ``error`` is ``ResponseError | RawError``."""
        return (
            await self._with_raw_response.delete_configuration(id, vendor_id, request_options=request_options)
        ).unwrap()

    async def get_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GeoFenceConfigurationResponse:
        """This endpoint fetches and returns a specific configuration's details. The configuration ID parameter, which
        was provided when the configuration was created through the POST request, is need to retrieve the configuration
        details.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration found

        Raises:
            ApiError: Forbidden Configuration not found Too many requests ``error`` is ``ResponseError | RawError``."""
        return (
            await self._with_raw_response.get_configuration(id, vendor_id, request_options=request_options)
        ).unwrap()

    async def get_configuration_list(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> list[ConfigurationListItem]:
        """This endpoint fetches and returns the list of configurations defined by the Vendor. The list contains the
        configurations' identifier, name, description, and active flag. The vendor ID is provided when the configuration
        is created through the POST request.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration list was queried successfully

        Raises:
            ApiError: Forbidden Configuration not found Too many requests ``error`` is ``ResponseError | RawError``."""
        return (
            await self._with_raw_response.get_configuration_list(vendor_id, request_options=request_options)
        ).unwrap()

    async def update_configuration(
        self,
        id: str,
        vendor_id: str,
        body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """This endpoint updates an existing configuration. Similar to POST, the updated data for the configuration
        should be provided as JSON in the body of the PUT request. The configuration ID parameter, which was provided by
        the POST (create) operation, is required to do any updates on the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Configuration applied

        Raises:
            ApiError: Invalid configuration Forbidden Configuration not found Too many requests ``error`` is
                ``ResponseError | RawError``."""
        return (
            await self._with_raw_response.update_configuration(id, vendor_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncEtxappConfigurationWithRawResponse:
        return self._with_raw_response


class EtxappConfigurationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_configuration(
        self,
        vendor_id: str,
        body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GeoFenceConfigurationResponse, CreateConfigurationErrorBody]:
        """This endpoint creates a new configuration in the system. The data for the new configuration should be
        provided as JSON in the body of the POST request. The system will return with a unique ID for the configuration,
        which is needed for any further manipulation (update or delete) of the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[GeoFenceConfigurationResponse],
            error_mapper=create_configuration_error_mapper,
            request_options=request_options,
        )

    def delete_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteConfigurationErrorBody]:
        """This endpoint deletes a specific configuration from the system. It requires the configuration ID parameter,
        which was provided by the POST (create) operation.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=delete_configuration_error_mapper,
            request_options=request_options,
        )

    def get_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GeoFenceConfigurationResponse, GetConfigurationErrorBody]:
        """This endpoint fetches and returns a specific configuration's details. The configuration ID parameter, which
        was provided when the configuration was created through the POST request, is need to retrieve the configuration
        details.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("VendorID", vendor_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[GeoFenceConfigurationResponse],
            error_mapper=get_configuration_error_mapper,
            request_options=request_options,
        )

    def get_configuration_list(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ConfigurationListItem], GetConfigurationListErrorBody]:
        """This endpoint fetches and returns the list of configurations defined by the Vendor. The list contains the
        configurations' identifier, name, description, and active flag. The vendor ID is provided when the configuration
        is created through the POST request.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence/ids"),
            headers=[param[str]("VendorID", vendor_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[ConfigurationListItem]],
            error_mapper=get_configuration_list_error_mapper,
            request_options=request_options,
        )

    def update_configuration(
        self,
        id: str,
        vendor_id: str,
        body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateConfigurationErrorBody]:
        """This endpoint updates an existing configuration. Similar to POST, the updated data for the configuration
        should be provided as JSON in the body of the PUT request. The configuration ID parameter, which was provided by
        the POST (create) operation, is required to do any updates on the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=update_configuration_error_mapper,
            request_options=request_options,
        )


class AsyncEtxappConfigurationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_configuration(
        self,
        vendor_id: str,
        body: GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GeoFenceConfigurationResponse, CreateConfigurationErrorBody]:
        """This endpoint creates a new configuration in the system. The data for the new configuration should be
        provided as JSON in the body of the POST request. The system will return with a unique ID for the configuration,
        which is needed for any further manipulation (update or delete) of the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeoFenceConfigurationRequest | GeoFenceConfigurationRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[GeoFenceConfigurationResponse],
            error_mapper=create_configuration_error_mapper,
            request_options=request_options,
        )

    async def delete_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteConfigurationErrorBody]:
        """This endpoint deletes a specific configuration from the system. It requires the configuration ID parameter,
        which was provided by the POST (create) operation.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=delete_configuration_error_mapper,
            request_options=request_options,
        )

    async def get_configuration(
        self, id: str, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GeoFenceConfigurationResponse, GetConfigurationErrorBody]:
        """This endpoint fetches and returns a specific configuration's details. The configuration ID parameter, which
        was provided when the configuration was created through the POST request, is need to retrieve the configuration
        details.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("VendorID", vendor_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[GeoFenceConfigurationResponse],
            error_mapper=get_configuration_error_mapper,
            request_options=request_options,
        )

    async def get_configuration_list(
        self, vendor_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[list[ConfigurationListItem], GetConfigurationListErrorBody]:
        """This endpoint fetches and returns the list of configurations defined by the Vendor. The list contains the
        configurations' identifier, name, description, and active flag. The vendor ID is provided when the configuration
        is created through the POST request.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            vendor_id: The vendor's identifier
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence/ids"),
            headers=[param[str]("VendorID", vendor_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[ConfigurationListItem]],
            error_mapper=get_configuration_list_error_mapper,
            request_options=request_options,
        )

    async def update_configuration(
        self,
        id: str,
        vendor_id: str,
        body: GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, UpdateConfigurationErrorBody]:
        """This endpoint updates an existing configuration. Similar to POST, the updated data for the configuration
        should be provided as JSON in the body of the PUT request. The configuration ID parameter, which was provided by
        the POST (create) operation, is required to do any updates on the configuration.

        Note: The user needs to authenticate with their ThingSpace credentials using the Access/Bearer and Session/M2M
        tokens in order to call this API.

        Args:
            id: The configuration identifier
            vendor_id: The vendor's identifier
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.imp_server("/api/v1/application/configurations/geofence"),
            query_params=[param[str]("id", id)],
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GeoFenceConfigurationUpdateRequest | GeoFenceConfigurationUpdateRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=update_configuration_error_mapper,
            request_options=request_options,
        )
