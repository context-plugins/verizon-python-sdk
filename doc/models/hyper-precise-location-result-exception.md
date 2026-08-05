
# Hyper Precise Location Result Exception

Error response.

## Structure

`HyperPreciseLocationResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_code` | [`ErrorResponseCodeEnum`](../../doc/models/error-response-code-enum.md) | Optional | Error Code. |
| `message` | `str` | Optional | Error message. |
| `fault` | [`HyperPreciseLocationFault`](../../doc/models/hyper-precise-location-fault.md) | Optional | Fault occurred while responding. |

## Example

```python
try:
    # make the API call
except HyperPreciseLocationResultException as e:
    print(e)
except APIException as e:
    print(e)
```

