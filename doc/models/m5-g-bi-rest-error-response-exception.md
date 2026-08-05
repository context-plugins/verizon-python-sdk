
# M5 G Bi Rest Error Response Exception

## Structure

`M5gBiRestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | - |
| `error_message` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except M5gBiRestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

