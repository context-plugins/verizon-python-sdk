
# V2 License IMEI

IMEIs of the devices to assign or remove licenses.

## Structure

`V2LicenseIMEI`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_name` | `str` | Optional | Account name. |
| `device_list` | `List[str]` | Required | Device IMEI list. |

## Example

```python
from verizon.models.v2_license_imei import V2LicenseIMEI

v2_license_imei = V2LicenseIMEI(
    device_list=[
        '990003425730524',
        '990000473475967'
    ],
    account_name='accountName0'
)
```

