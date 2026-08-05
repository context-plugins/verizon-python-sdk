
# Download Time Window

## Structure

`DownloadTimeWindow`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_time` | `str` | Optional | Device IMEI list. |
| `end_time` | `str` | Optional | Device IMEI list. |

## Example

```python
from verizon.models.download_time_window import DownloadTimeWindow

download_time_window = DownloadTimeWindow(
    start_time='0',
    end_time='0'
)
```

