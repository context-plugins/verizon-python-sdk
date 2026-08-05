
# Device Logging Status

Device logging status information.

## Structure

`DeviceLoggingStatus`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_id` | `str` | Required | Device IMEI. |
| `expiry_date` | `date` | Required | The date when device logging expires. |

## Example

```python
import dateutil.parser

from verizon.models.device_logging_status import DeviceLoggingStatus

device_logging_status = DeviceLoggingStatus(
    device_id='990013907835573',
    expiry_date=dateutil.parser.parse('2020-10-19').date()
)
```

