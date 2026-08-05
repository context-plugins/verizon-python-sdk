
# Retrieves Available Files Response

## Structure

`RetrievesAvailableFilesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `file_name` | `str` | Optional | ThingSpace-generated name of the file. You will use this name when listing or scheduling campaigns for the file. |
| `file_version` | `str` | Optional | Version of the file. |
| `release_note` | `str` | Optional | Software release note. |
| `make` | `str` | Optional | The software-applicable device make. |
| `model` | `str` | Optional | The software-applicable device model. |
| `local_target_path` | `str` | Optional | Local target path on the device. |
| `distribution_type` | `str` | Optional | Valid values |
| `device_platform_id` | `str` | Optional | The platform (Android, iOS, etc.,) that the software can be applied to. |

## Example

```python
from verizon.models.retrieves_available_files_response import RetrievesAvailableFilesResponse

retrieves_available_files_response = RetrievesAvailableFilesResponse(
    file_name='configfile-Verizon_VZW1_hello-world.txt',
    file_version='1.0',
    release_note='Hello world initial file',
    make='Verizon',
    model='VZW1',
    local_target_path='/VZWFOTA/hello-world.txt',
    distribution_type='HTTP',
    device_platform_id='IoT'
)
```

