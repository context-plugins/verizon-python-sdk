
# Hyper Precise Location Fault

Fault occurred while responding.

## Structure

`HyperPreciseLocationFault`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | Hyper precise location fault code. |
| `message` | `str` | Optional | Hyper precise location fault message. |
| `description` | `str` | Optional | Hyper precise location fault description. |

## Example

```python
from verizon.models.hyper_precise_location_fault import HyperPreciseLocationFault

hyper_precise_location_fault = HyperPreciseLocationFault(
    code='900906',
    message='No matching resource found in the API for the given request',
    description='Access failure for API. Check the API documentation and add a proper REST resource path to the invocation URL.'
)
```

