
# Management Error Exception

## Structure

`ManagementErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error` | `str` | Optional | - |
| `error_description` | `str` | Optional | **Constraints**: *Maximum Length*: `1000` |
| `cause` | `str` | Optional | - |

## Example

```python
try:
    # make the API call
except ManagementErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

