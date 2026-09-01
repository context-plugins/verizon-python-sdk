from __future__ import annotations

from typing import TypeAlias

from ..accident_cause_code import AccidentCauseCode, AccidentCauseCodeDict
from ..emergency_vehicle_approaching_cause_code import (
    EmergencyVehicleApproachingCauseCode,
    EmergencyVehicleApproachingCauseCodeDict,
)
from ..impassability_cause_code import ImpassabilityCauseCode, ImpassabilityCauseCodeDict
from ..roadworks_cause_code import RoadworksCauseCode, RoadworksCauseCodeDict
from ..traffic_condition_cause_code import TrafficConditionCauseCode, TrafficConditionCauseCodeDict
from ..wrong_way_driving_cause_code import WrongWayDrivingCauseCode, WrongWayDrivingCauseCodeDict

CauseCodeChoice: TypeAlias = (
    TrafficConditionCauseCode
    | AccidentCauseCode
    | RoadworksCauseCode
    | ImpassabilityCauseCode
    | WrongWayDrivingCauseCode
    | EmergencyVehicleApproachingCauseCode
)
"""The main cause of a detected event. Each entry is of a different type and represents the sub cause code."""

CauseCodeChoiceDict: TypeAlias = (
    TrafficConditionCauseCodeDict
    | AccidentCauseCodeDict
    | RoadworksCauseCodeDict
    | ImpassabilityCauseCodeDict
    | WrongWayDrivingCauseCodeDict
    | EmergencyVehicleApproachingCauseCodeDict
)
