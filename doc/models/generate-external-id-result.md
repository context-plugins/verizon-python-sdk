
# Generate External ID Result

A new external ID.

## Structure

`GenerateExternalIDResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `externalid` | `str` | Optional | Newly created security string. |

## Example

```python
from verizon.models.generate_external_id_result import GenerateExternalIDResult

generate_external_id_result = GenerateExternalIDResult(
    externalid='ZlJnih8BfqsosZrEEkfPuR3aGOk2i-HIr6tXN275ioJF6bezIrQB9EbzpTRep8J7RmV7QH=='
)
```

