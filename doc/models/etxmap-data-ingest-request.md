
# ETXMAP Data Ingest Request

JSON representation of a J2735/ETSI MapData message for ingestion. The value field must contain a valid MAP message body conforming to the SAE J2735 or ETSI TS 103 301 standard.

## Structure

`ETXMAPDataIngestRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `message_id` | `int` | Required | SAE J2735 DSRCmsgID for the MAP message type.<br><br>**Constraints**: `>= 0`, `<= 32767` |
| `value` | `Any` | Required | The decoded MAP message body containing intersection and lane data. |
| `msg_issue_revision` | `int` | Optional | Issue revision number of the MAP message.<br><br>**Constraints**: `>= 0`, `<= 255` |

## Example

```python
import jsonpickle

from verizon.models.etxmap_data_ingest_request import ETXMAPDataIngestRequest

etx_map_data_ingest_request = ETXMAPDataIngestRequest(
    message_id=18,
    value=jsonpickle.decode('{"intersections":[{"id":{"region":0,"id":156},"laneWidth":366,"refPoint":{"lat":389284111,"long":-772410713},"revision":3}],"msgIssueRevision":3}'),
    msg_issue_revision=232
)
```

