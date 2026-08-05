
# Asynchronous Request Result

A successful request returns the request ID and the current status.

## Structure

`AsynchronousRequestResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `request_id` | `str` | Optional | The unique ID of the asynchronous request. |
| `status` | [`RequestStatusEnum`](../../doc/models/request-status-enum.md) | Optional | The current status of the callback response. |

## Example

```python
from verizon.models.asynchronous_request_result import AsynchronousRequestResult
from verizon.models.request_status_enum import RequestStatusEnum

asynchronous_request_result = AsynchronousRequestResult(
    request_id='86c83330-4bf5-4235-9c4e-a83f93aeae4c',
    status=RequestStatusEnum.SUCCESS
)
```

