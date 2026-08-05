
# WNP Rest Error Response Exception

Wireless network performance rest error response.

## Structure

`WNPRestErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `error_code` | `str` | Optional | Rest error response.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3`, *Pattern*: `^[0-9]{3,3}$` |
| `error_message` | `str` | Optional | Error message details.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `64`, *Pattern*: `^[A-Za-z0-9 ]{3,64}$` |

## Example

```python
try:
    # make the API call
except WNPRestErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

