
# Retrieves Available Files Response List

## Structure

`RetrievesAvailableFilesResponseList`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `available_files_response` | [`List[RetrievesAvailableFilesResponse]`](../../doc/models/retrieves-available-files-response.md) | Optional | **Constraints**: *Maximum Items*: `100` |

## Example

```python
from verizon.models.retrieves_available_files_response import RetrievesAvailableFilesResponse
from verizon.models.retrieves_available_files_response_list import RetrievesAvailableFilesResponseList

retrieves_available_files_response_list = RetrievesAvailableFilesResponseList(
    available_files_response=[
        RetrievesAvailableFilesResponse(
            file_name='fileName2',
            file_version='fileVersion4',
            release_note='releaseNote0',
            make='make2',
            model='model6'
        ),
        RetrievesAvailableFilesResponse(
            file_name='fileName2',
            file_version='fileVersion4',
            release_note='releaseNote0',
            make='make2',
            model='model6'
        )
    ]
)
```

