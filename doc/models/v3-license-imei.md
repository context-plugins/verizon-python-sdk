
# V3 License IMEI

List of devices.

## Structure

`V3LicenseIMEI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.v3_license_imei import V3LicenseIMEI

v3_license_imei = V3LicenseIMEI(
    device_list=[
        '15-digit IMEI',
        '15-digit IMEI'
    ]
)
```

