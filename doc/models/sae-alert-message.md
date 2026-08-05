
# Sae Alert Message

Road Side Alert (RSA) message and its mandatory fields. This message is used to send alerts for nearby hazards to travelers. This message is defined in the SAE J2735 Standard. The system supports all mandatory fields, but only a subset of the optional fields.

## Structure

`SaeAlertMessage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `sae_alert` | [`SaeAlertPayload`](../../doc/models/sae-alert-payload.md) | Required | Road Side Alert (RSA) message payload as defined in SAE J2735. |

## Example

```python
from verizon.models.sae_alert_message import SaeAlertMessage
from verizon.models.sae_alert_payload import SaeAlertPayload

sae_alert_message = SaeAlertMessage(
    sae_alert=SaeAlertPayload(
        type_event=160,
        msg_cnt=0,
        description=[
            15,
            16
        ]
    )
)
```

