
# Cause Code Choice

The main cause of a detected event. Each entry is of a different type and represents the sub cause code.

## Data Type

`TrafficConditionCauseCode | AccidentCauseCode | RoadworksCauseCode | ImpassabilityCauseCode | WrongWayDrivingCauseCode | EmergencyVehicleApproachingCauseCode`

## Cases

| Type |
|  --- |
| [`TrafficConditionCauseCode`](../../../doc/models/traffic-condition-cause-code.md) |
| [`AccidentCauseCode`](../../../doc/models/accident-cause-code.md) |
| [`RoadworksCauseCode`](../../../doc/models/roadworks-cause-code.md) |
| [`ImpassabilityCauseCode`](../../../doc/models/impassability-cause-code.md) |
| [`WrongWayDrivingCauseCode`](../../../doc/models/wrong-way-driving-cause-code.md) |
| [`EmergencyVehicleApproachingCauseCode`](../../../doc/models/emergency-vehicle-approaching-cause-code.md) |

## TrafficConditionCauseCode

### Initialization Code

#### Example

```python
value = TrafficConditionCauseCode(
    traffic_condition_1=26
)
```

## AccidentCauseCode

### Initialization Code

#### Example

```python
value = AccidentCauseCode(
    accident_2=80
)
```

## RoadworksCauseCode

### Initialization Code

#### Example

```python
value = RoadworksCauseCode(
    roadworks_3=180
)
```

## ImpassabilityCauseCode

### Initialization Code

#### Example

```python
value = ImpassabilityCauseCode(
    impassability_5=80
)
```

## WrongWayDrivingCauseCode

### Initialization Code

#### Example

```python
value = WrongWayDrivingCauseCode(
    wrong_way_driving_14=172
)
```

## EmergencyVehicleApproachingCauseCode

### Initialization Code

#### Example

```python
value = EmergencyVehicleApproachingCauseCode(
    emergency_vehicle_approaching_95=88
)
```

