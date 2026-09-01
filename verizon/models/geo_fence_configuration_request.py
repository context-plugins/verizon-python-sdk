from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .enums.message_standard import MessageStandardOrStr
from .geo_fence import GeoFence, GeoFenceDict
from .message import Message, MessageDict


class GeoFenceConfigurationRequest(SdkBaseModel):
    """Request for /api/v1/application/configurations/geofence POST endpoint. It requires the vendorId, geofence,
    messageStandard, messages and isActive fields to be populated."""

    name: Optional[str] = UNSET
    """Name of the configuration."""

    description: Optional[str] = UNSET
    """Description of the configuration."""

    geo_fence: GeoFence = Field(alias="geoFence")
    """The GeoJSON representation of geofence. Geofence supports the following geometry types: LineString, Polygon,
    MultiLineString, and MultiPolygon. The system only supports a single Feature in the FeatureCollection, so only one
    Line, Polygon, MultiLine or MultiPolygon can be defined within one Geofencing configuration."""

    message_standard: Optional[MessageStandardOrStr] = Field(default=UNSET, alias="messageStandard")
    """Select which V2X messaging standard will be used for the message generation. The following options are supported:
      - "etsi": The message will be generated using the ETSI (European) standard (e.g. DENM).
      - "sae": The message will be generated using the SAE J2735 (North American) standard (e.g. RSA, TIM).
      - if not sent while POST, defaults to "sae"
      - mandatory to send "etsi" standard here, if ETSI messages are being sent in config"""

    messages: list[Message]
    """List of predefined messages that belongs to the geofence. These are the messages that are sent out by the system
    when the Trigger Condition for the message is met."""

    is_active: bool = Field(alias="isActive")


class GeoFenceConfigurationRequestDict(TypedDict):
    name: NotRequired[str]
    description: NotRequired[str]
    geo_fence: GeoFence | GeoFenceDict
    message_standard: NotRequired[MessageStandardOrStr]
    messages: list[Message | MessageDict]
    is_active: bool
