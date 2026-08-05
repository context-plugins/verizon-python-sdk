
# Default Response Exception

## Structure

`DefaultResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except DefaultResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

