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
    text_decoder,
)
from ..errors.delete_map_message_error import DeleteMapMessageErrorBody, delete_map_message_error_mapper
from ..errors.download_mapmessages_error import DownloadMapmessagesErrorBody, download_mapmessages_error_mapper
from ..errors.ingest_mapmessages_error import IngestMapmessagesErrorBody, ingest_mapmessages_error_mapper
from ..errors.query_map_messages_error import QueryMapMessagesErrorBody, query_map_messages_error_mapper
from ..models.enums.etxmessage_standard_enum import EtxmessageStandardEnumOrStr
from ..models.etx_map_data_ingest_request import EtxMapDataIngestRequest, EtxMapDataIngestRequestDict
from ..models.geofence_polygon import GeofencePolygon, GeofencePolygonDict
from ..models.unions.map_data_query_request import MapDataQueryRequest, MapDataQueryRequestDict
from ..server.server import Server


class MapMessageController:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = MapMessageControllerWithRawResponse(client, server, auth)

    def delete_map_message(
        self, region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes a map message for the specified region and intersection ID.

        Args:
            region_id: Region ID to filter the map messages.
            i10nid: Intersection ID to filter the map messages.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deleted successfully (No Content)

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found Too many requests Internal server error ``error`` is
                ``MdmErrorResponse | RawError``."""
        return self._with_raw_response.delete_map_message(region_id, i10nid, request_options=request_options).unwrap()

    def download_map_messages(
        self,
        geofence: GeofencePolygon | GeofencePolygonDict,
        vendor_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """This endpoint is deprecated. (Use /api/v2/mapdata/query for new integrations).

        This endpoint allows user to download SAE J2735 or ETSI MAP messages in ASN.1 UPER base64 encoded format. The
        area for the MAP messages is needed to be defined in the query.


        **Required request header:** ``Accept`` — specifies the response format. Omitting this header will result in a
        ``400 Bad Request``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP messages (one per line)
        - ``application/json`` — JSON-encoded MAP messages

        Args:
            geofence: GeoJSON Polygon defining the area to retrieve MAP messages for.
            vendor_id: The VendorID set during the Vendor registration call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Line separated ASN.1 UPER J2735/ETSI base64 encoded MapData messages

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found Too many requests Internal server error ``error`` is
                ``MdmErrorResponse | RawError``."""
        return self._with_raw_response.download_map_messages(
            geofence, vendor_id, request_options=request_options
        ).unwrap()

    def ingest_map_messages(
        self,
        vendor_id: str,
        map_data_message_standard: EtxmessageStandardEnumOrStr,
        body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """This endpoint allows the user to upload map messages in ASN.1 UPER base64 encoded format or JER (JSON)
        formats. The MAP data message can have more than one intersections in it. Both SAE and ETSI defined MAP messages
        are supported. The SAE type MAP messages have to be wrapped in a MessageFrame, as defined in the SAE J2735
        standard. The ETSI type MAP messages are expected as MAPEM structures that include the ETSI header, as defined
        in the ETSI TS 103 301 standard. Note: The user needs to authenticate with their ThingSpace credentials using
        the Access/Bearer and Session/M2M tokens in order to call this API.

        **Required request header:** ``Content-Type`` — specifies the format of the request body. Omitting or sending an
        unsupported value will result in a ``415 Unsupported Media Type``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP message
        - ``application/json`` — JSON representation of the MAP message

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            map_data_message_standard: Select which V2X messaging standard will be used for the message generation. The
                following options are supported: - "etsi": The message will be generated using the ETSI (European)
                standard (e.g. MAPEM). - "sae": The message will be generated using the SAE J2735 (North American)
                standard (e.g. MAP). - if not sent while POST, defaults to "sae"
            body: UPER/ASN.1 J2735/ETSI base64 encoded MapData message or JSON representation of the MapData message.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Map message/s successfully uploaded

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Method not allowed Too many requests Internal server error
                ``error`` is ``MdmErrorResponse | RawError``."""
        return self._with_raw_response.ingest_map_messages(
            vendor_id, map_data_message_standard, body, request_options=request_options
        ).unwrap()

    def query_map_messages(
        self,
        vendor_id: str,
        body: MapDataQueryRequest | MapDataQueryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Any]:
        """This endpoint allows users to download SAE J2735 or ETSI MAP messages as a JSON list. Depending on the
        expectedType parameter, the response contains either ASN.1 UPER base64-encoded messages with their respective
        region and intersection IDs, or fully decoded JSON messages. The area for MAP message retrieval must be defined
        in the request body using one of two methods: An array of region and intersection ID pairs, or a GeoJSON
        geofence specification.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully retrieved MAP messages. Returns a JSON array where each element contains either a base64 string
            or parsed message object.

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Method not allowed Too many requests Internal server error
                ``error`` is ``MdmErrorResponse | RawError``."""
        return self._with_raw_response.query_map_messages(vendor_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> MapMessageControllerWithRawResponse:
        return self._with_raw_response


class AsyncMapMessageController:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncMapMessageControllerWithRawResponse(client, server, auth)

    async def delete_map_message(
        self, region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes a map message for the specified region and intersection ID.

        Args:
            region_id: Region ID to filter the map messages.
            i10nid: Intersection ID to filter the map messages.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Deleted successfully (No Content)

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found Too many requests Internal server error ``error`` is
                ``MdmErrorResponse | RawError``."""
        return (
            await self._with_raw_response.delete_map_message(region_id, i10nid, request_options=request_options)
        ).unwrap()

    async def download_map_messages(
        self,
        geofence: GeofencePolygon | GeofencePolygonDict,
        vendor_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """This endpoint is deprecated. (Use /api/v2/mapdata/query for new integrations).

        This endpoint allows user to download SAE J2735 or ETSI MAP messages in ASN.1 UPER base64 encoded format. The
        area for the MAP messages is needed to be defined in the query.


        **Required request header:** ``Accept`` — specifies the response format. Omitting this header will result in a
        ``400 Bad Request``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP messages (one per line)
        - ``application/json`` — JSON-encoded MAP messages

        Args:
            geofence: GeoJSON Polygon defining the area to retrieve MAP messages for.
            vendor_id: The VendorID set during the Vendor registration call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Line separated ASN.1 UPER J2735/ETSI base64 encoded MapData messages

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Not found Too many requests Internal server error ``error`` is
                ``MdmErrorResponse | RawError``."""
        return (
            await self._with_raw_response.download_map_messages(geofence, vendor_id, request_options=request_options)
        ).unwrap()

    async def ingest_map_messages(
        self,
        vendor_id: str,
        map_data_message_standard: EtxmessageStandardEnumOrStr,
        body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> str:
        """This endpoint allows the user to upload map messages in ASN.1 UPER base64 encoded format or JER (JSON)
        formats. The MAP data message can have more than one intersections in it. Both SAE and ETSI defined MAP messages
        are supported. The SAE type MAP messages have to be wrapped in a MessageFrame, as defined in the SAE J2735
        standard. The ETSI type MAP messages are expected as MAPEM structures that include the ETSI header, as defined
        in the ETSI TS 103 301 standard. Note: The user needs to authenticate with their ThingSpace credentials using
        the Access/Bearer and Session/M2M tokens in order to call this API.

        **Required request header:** ``Content-Type`` — specifies the format of the request body. Omitting or sending an
        unsupported value will result in a ``415 Unsupported Media Type``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP message
        - ``application/json`` — JSON representation of the MAP message

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            map_data_message_standard: Select which V2X messaging standard will be used for the message generation. The
                following options are supported: - "etsi": The message will be generated using the ETSI (European)
                standard (e.g. MAPEM). - "sae": The message will be generated using the SAE J2735 (North American)
                standard (e.g. MAP). - if not sent while POST, defaults to "sae"
            body: UPER/ASN.1 J2735/ETSI base64 encoded MapData message or JSON representation of the MapData message.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Map message/s successfully uploaded

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Method not allowed Too many requests Internal server error
                ``error`` is ``MdmErrorResponse | RawError``."""
        return (
            await self._with_raw_response.ingest_map_messages(
                vendor_id, map_data_message_standard, body, request_options=request_options
            )
        ).unwrap()

    async def query_map_messages(
        self,
        vendor_id: str,
        body: MapDataQueryRequest | MapDataQueryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[Any]:
        """This endpoint allows users to download SAE J2735 or ETSI MAP messages as a JSON list. Depending on the
        expectedType parameter, the response contains either ASN.1 UPER base64-encoded messages with their respective
        region and intersection IDs, or fully decoded JSON messages. The area for MAP message retrieval must be defined
        in the request body using one of two methods: An array of region and intersection ID pairs, or a GeoJSON
        geofence specification.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Successfully retrieved MAP messages. Returns a JSON array where each element contains either a base64 string
            or parsed message object.

        Raises:
            ApiError: Bad Request Unauthorized Forbidden Method not allowed Too many requests Internal server error
                ``error`` is ``MdmErrorResponse | RawError``."""
        return (
            await self._with_raw_response.query_map_messages(vendor_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncMapMessageControllerWithRawResponse:
        return self._with_raw_response


class MapMessageControllerWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_map_message(
        self, region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMapMessageErrorBody]:
        """Removes a map message for the specified region and intersection ID.

        Args:
            region_id: Region ID to filter the map messages.
            i10nid: Intersection ID to filter the map messages.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.imp_server("/api/v2/mapdata/regionid/{regionId}/i10nid/{i10nid}"),
            path_params=[param[str]("regionId", region_id), param[str]("i10nid", i10nid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=delete_map_message_error_mapper,
            request_options=request_options,
        )

    def download_map_messages(
        self,
        geofence: GeofencePolygon | GeofencePolygonDict,
        vendor_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, DownloadMapmessagesErrorBody]:
        """This endpoint is deprecated. (Use /api/v2/mapdata/query for new integrations).

        This endpoint allows user to download SAE J2735 or ETSI MAP messages in ASN.1 UPER base64 encoded format. The
        area for the MAP messages is needed to be defined in the query.


        **Required request header:** ``Accept`` — specifies the response format. Omitting this header will result in a
        ``400 Bad Request``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP messages (one per line)
        - ``application/json`` — JSON-encoded MAP messages

        Args:
            geofence: GeoJSON Polygon defining the area to retrieve MAP messages for.
            vendor_id: The VendorID set during the Vendor registration call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v2/mapdata"),
            query_params=[param[GeofencePolygon | GeofencePolygonDict]("Geofence", geofence)],
            headers=[param[str]("VendorID", vendor_id)],
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=text_decoder[str],
            error_mapper=download_mapmessages_error_mapper,
            request_options=request_options,
        )

    def ingest_map_messages(
        self,
        vendor_id: str,
        map_data_message_standard: EtxmessageStandardEnumOrStr,
        body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, IngestMapmessagesErrorBody]:
        """This endpoint allows the user to upload map messages in ASN.1 UPER base64 encoded format or JER (JSON)
        formats. The MAP data message can have more than one intersections in it. Both SAE and ETSI defined MAP messages
        are supported. The SAE type MAP messages have to be wrapped in a MessageFrame, as defined in the SAE J2735
        standard. The ETSI type MAP messages are expected as MAPEM structures that include the ETSI header, as defined
        in the ETSI TS 103 301 standard. Note: The user needs to authenticate with their ThingSpace credentials using
        the Access/Bearer and Session/M2M tokens in order to call this API.

        **Required request header:** ``Content-Type`` — specifies the format of the request body. Omitting or sending an
        unsupported value will result in a ``415 Unsupported Media Type``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP message
        - ``application/json`` — JSON representation of the MAP message

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            map_data_message_standard: Select which V2X messaging standard will be used for the message generation. The
                following options are supported: - "etsi": The message will be generated using the ETSI (European)
                standard (e.g. MAPEM). - "sae": The message will be generated using the SAE J2735 (North American)
                standard (e.g. MAP). - if not sent while POST, defaults to "sae"
            body: UPER/ASN.1 J2735/ETSI base64 encoded MapData message or JSON representation of the MapData message.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/mapdata"),
            headers=[
                param[str]("VendorID", vendor_id),
                param[EtxmessageStandardEnumOrStr]("MessageStandard", map_data_message_standard),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[EtxMapDataIngestRequest | EtxMapDataIngestRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=text_decoder[str],
            error_mapper=ingest_mapmessages_error_mapper,
            request_options=request_options,
        )

    def query_map_messages(
        self,
        vendor_id: str,
        body: MapDataQueryRequest | MapDataQueryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Any], QueryMapMessagesErrorBody]:
        """This endpoint allows users to download SAE J2735 or ETSI MAP messages as a JSON list. Depending on the
        expectedType parameter, the response contains either ASN.1 UPER base64-encoded messages with their respective
        region and intersection IDs, or fully decoded JSON messages. The area for MAP message retrieval must be defined
        in the request body using one of two methods: An array of region and intersection ID pairs, or a GeoJSON
        geofence specification.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/mapdata/query"),
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MapDataQueryRequest | MapDataQueryRequestDict](body),
            auth_scheme=AllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[Any]],
            error_mapper=query_map_messages_error_mapper,
            request_options=request_options,
        )


class AsyncMapMessageControllerWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_map_message(
        self, region_id: str, i10nid: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteMapMessageErrorBody]:
        """Removes a map message for the specified region and intersection ID.

        Args:
            region_id: Region ID to filter the map messages.
            i10nid: Intersection ID to filter the map messages.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.imp_server("/api/v2/mapdata/regionid/{regionId}/i10nid/{i10nid}"),
            path_params=[param[str]("regionId", region_id), param[str]("i10nid", i10nid)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=empty_response,
            error_mapper=delete_map_message_error_mapper,
            request_options=request_options,
        )

    async def download_map_messages(
        self,
        geofence: GeofencePolygon | GeofencePolygonDict,
        vendor_id: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, DownloadMapmessagesErrorBody]:
        """This endpoint is deprecated. (Use /api/v2/mapdata/query for new integrations).

        This endpoint allows user to download SAE J2735 or ETSI MAP messages in ASN.1 UPER base64 encoded format. The
        area for the MAP messages is needed to be defined in the query.


        **Required request header:** ``Accept`` — specifies the response format. Omitting this header will result in a
        ``400 Bad Request``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP messages (one per line)
        - ``application/json`` — JSON-encoded MAP messages

        Args:
            geofence: GeoJSON Polygon defining the area to retrieve MAP messages for.
            vendor_id: The VendorID set during the Vendor registration call.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.imp_server("/api/v2/mapdata"),
            query_params=[param[GeofencePolygon | GeofencePolygonDict]("Geofence", geofence)],
            headers=[param[str]("VendorID", vendor_id)],
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=text_decoder[str],
            error_mapper=download_mapmessages_error_mapper,
            request_options=request_options,
        )

    async def ingest_map_messages(
        self,
        vendor_id: str,
        map_data_message_standard: EtxmessageStandardEnumOrStr,
        body: EtxMapDataIngestRequest | EtxMapDataIngestRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[str, IngestMapmessagesErrorBody]:
        """This endpoint allows the user to upload map messages in ASN.1 UPER base64 encoded format or JER (JSON)
        formats. The MAP data message can have more than one intersections in it. Both SAE and ETSI defined MAP messages
        are supported. The SAE type MAP messages have to be wrapped in a MessageFrame, as defined in the SAE J2735
        standard. The ETSI type MAP messages are expected as MAPEM structures that include the ETSI header, as defined
        in the ETSI TS 103 301 standard. Note: The user needs to authenticate with their ThingSpace credentials using
        the Access/Bearer and Session/M2M tokens in order to call this API.

        **Required request header:** ``Content-Type`` — specifies the format of the request body. Omitting or sending an
        unsupported value will result in a ``415 Unsupported Media Type``. Supported values:
        - ``text/plain`` — ASN.1 UPER base64-encoded MAP message
        - ``application/json`` — JSON representation of the MAP message

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            map_data_message_standard: Select which V2X messaging standard will be used for the message generation. The
                following options are supported: - "etsi": The message will be generated using the ETSI (European)
                standard (e.g. MAPEM). - "sae": The message will be generated using the SAE J2735 (North American)
                standard (e.g. MAP). - if not sent while POST, defaults to "sae"
            body: UPER/ASN.1 J2735/ETSI base64 encoded MapData message or JSON representation of the MapData message.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/mapdata"),
            headers=[
                param[str]("VendorID", vendor_id),
                param[EtxmessageStandardEnumOrStr]("MessageStandard", map_data_message_standard),
                param[UUID]("Idempotency-Key", uuid4()),
            ],
            body=json_body[EtxMapDataIngestRequest | EtxMapDataIngestRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=text_decoder[str],
            error_mapper=ingest_mapmessages_error_mapper,
            request_options=request_options,
        )

    async def query_map_messages(
        self,
        vendor_id: str,
        body: MapDataQueryRequest | MapDataQueryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[Any], QueryMapMessagesErrorBody]:
        """This endpoint allows users to download SAE J2735 or ETSI MAP messages as a JSON list. Depending on the
        expectedType parameter, the response contains either ASN.1 UPER base64-encoded messages with their respective
        region and intersection IDs, or fully decoded JSON messages. The area for MAP message retrieval must be defined
        in the request body using one of two methods: An array of region and intersection ID pairs, or a GeoJSON
        geofence specification.

        Args:
            vendor_id: The VendorID set during the Vendor registration call.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.imp_server("/api/v2/mapdata/query"),
            headers=[param[str]("VendorID", vendor_id), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[MapDataQueryRequest | MapDataQueryRequestDict](body),
            auth_scheme=AsyncAllSchemes(self._auth.thingspace_oauth, self._auth.session_token),
            decoder=json_decoder[list[Any]],
            error_mapper=query_map_messages_error_mapper,
            request_options=request_options,
        )
