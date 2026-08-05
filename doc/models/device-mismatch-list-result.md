
# Device Mismatch List Result

Response to list of all 4G devices with an ICCID (SIM) that was not activated with the expected IMEI (hardware) during a specified time frame.

## Structure

`DeviceMismatchListResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `devices` | [`List[MismatchedDevice]`](../../doc/models/mismatched-device.md) | Optional | A list of specific devices that you want to check, specified by ICCID or MDN. |

## Example

```python
from verizon.models.device_mismatch_list_result import DeviceMismatchListResult
from verizon.models.mismatched_device import MismatchedDevice

device_mismatch_list_result = DeviceMismatchListResult(
    devices=[
        MismatchedDevice(
            account_name='0212398765-00001',
            mdn='5096300587',
            activation_date='2011-01-21T10:55:27-08:00',
            iccid='89148000000800784259',
            pre_imei='990003420535573',
            post_imei='987603420573553',
            sim_ota_date='2017-12-01T16:00:00-08:00'
        )
    ]
)
```

