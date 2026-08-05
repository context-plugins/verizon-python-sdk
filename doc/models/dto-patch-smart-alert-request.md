
# Dto Patch Smart Alert Request

## Structure

`DtoPatchSmartAlertRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `accountname` | `str` | Optional | The numeric account name, which must include leading zeros |
| `resourceidentifier` | [`DtoResourceidentifier`](../../doc/models/dto-resourceidentifier.md) | Optional | - |
| `smartalert` | [`UserSmartAlert`](../../doc/models/user-smart-alert.md) | Optional | - |

## Example

```python
import dateutil.parser

from verizon.models.dto_patch_smart_alert_request import DtoPatchSmartAlertRequest
from verizon.models.dto_resourceidentifier import DtoResourceidentifier
from verizon.models.user_smart_alert import UserSmartAlert

dto_patch_smart_alert_request = DtoPatchSmartAlertRequest(
    accountname='0000123456-00001',
    resourceidentifier=DtoResourceidentifier(
        id='id4'
    ),
    smartalert=UserSmartAlert(
        createdon=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        lastupdated=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        versionid='versionid2',
        accountclientid='accountclientid6',
        billingaccountid='billingaccountid6',
        category='category8',
        condition=154,
        description='description0'
    )
)
```

