
# Device Location Result Exception

Will be empty if there was no error.

## Structure

`DeviceLocationResultException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Required | - |
| `error_message` | `str` | Required | - |

## Example

```python
try:
    # make the API call
except DeviceLocationResultException as e:
    print(e)
except APIException as e:
    print(e)
```

