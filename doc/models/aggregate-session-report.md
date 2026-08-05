
# Aggregate Session Report

Session and usage details for up to 10 devices.

## Structure

`AggregateSessionReport`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `txid` | `str` | Optional | A unique string (UUID) that associates the request with the location report information that is sent in asynchronous callback message.ThingSpace will send a separate callback message for each device that was in the request. All of the callback messages will have a txid. |
| `usage` | [`List[AggregateUsageItem]`](../../doc/models/aggregate-usage-item.md) | Optional | Contains usage per device.<br><br>**Constraints**: *Unique Items Required* |
| `errors` | [`List[AggregateUsageError]`](../../doc/models/aggregate-usage-error.md) | Optional | An object containing any errors reported by the device.<br><br>**Constraints**: *Unique Items Required* |

## Example

```python
from verizon.models.aggregate_session_report import AggregateSessionReport
from verizon.models.aggregate_usage_error import AggregateUsageError
from verizon.models.aggregate_usage_item import AggregateUsageItem
from verizon.models.error_response_code_enum import ErrorResponseCodeEnum
from verizon.models.http_status_code_enum import HttpStatusCodeEnum
from verizon.models.i_error_message import IErrorMessage

aggregate_session_report = AggregateSessionReport(
    txid='60c07fff-eeee-ffff-gggg-75e6a7c238f6',
    usage=[
        AggregateUsageItem(
            imei='15-digit IMEI',
            number_of_sessions=1,
            bytes_transferred=2057
        )
    ],
    errors=[
        AggregateUsageError(
            imei='imei6',
            error_message='errorMessage8',
            error_response=IErrorMessage(
                error_code=ErrorResponseCodeEnum.INVALID_PARAMETER,
                error_message='errorMessage4',
                http_status_code=HttpStatusCodeEnum.ENUM_423_LOCKED,
                detail_error_message='detailErrorMessage6'
            )
        )
    ]
)
```

