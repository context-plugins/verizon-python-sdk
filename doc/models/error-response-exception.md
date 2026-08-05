
# Error Response Exception

## Structure

`ErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `response_code` | `str` | Optional | - |
| `message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except ErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

