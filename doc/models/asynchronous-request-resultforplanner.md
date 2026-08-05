
# Asynchronous Request Resultforplanner

A successful request returns the request ID (UUID) and the current status.

## Structure

`AsynchronousRequestResultforplanner`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | The unique ID of a request. This is a UUID value. |

## Example

```python
from verizon.models.asynchronous_request_resultforplanner import AsynchronousRequestResultforplanner

asynchronous_request_resultforplanner = AsynchronousRequestResultforplanner(
    request_id='d24cc6e4-eeee-ffff-gggg-0ffbb091c076'
)
```

