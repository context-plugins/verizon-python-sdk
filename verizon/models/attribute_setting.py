from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, RFC3339DateTime, SdkBaseModel
from .enums.attribute_identifier import AttributeIdentifierOrStr
from .numerical_data import NumericalData, NumericalDataDict


class AttributeSetting(SdkBaseModel):
    """Describes an attribute being observed and the frequency with which the attribute is being observed."""

    name: Optional[AttributeIdentifierOrStr] = UNSET
    """Attribute identifier."""

    value: Optional[str] = UNSET
    """Attribute value."""

    created_on: Optional[RFC3339DateTime] = Field(default=UNSET, alias="createdOn")
    """Date and time request was created."""

    is_observable: Optional[bool] = Field(default=UNSET, alias="isObservable")
    """Is the attribute observable?"""

    is_observing: Optional[bool] = Field(default=UNSET, alias="isObserving")
    """Is the attribute being observed?"""

    frequency: Optional[NumericalData] = UNSET
    """Describes value and unit of time."""


class AttributeSettingDict(TypedDict):
    name: NotRequired[AttributeIdentifierOrStr]
    value: NotRequired[str]
    created_on: NotRequired[RFC3339DateTime]
    is_observable: NotRequired[bool]
    is_observing: NotRequired[bool]
    frequency: NotRequired[NumericalData | NumericalDataDict]
