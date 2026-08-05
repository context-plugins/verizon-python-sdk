
# Connection Response V3

response for api/v3/clients/connection

## Structure

`ConnectionResponseV3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mqtt_ur_ls` | `List[str]` | Required | Array of full MQTT URLs including protocol, host, and port for each available MEC.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `20`, *Maximum Length*: `1024`, *Pattern*: `^(http?mqtt)://[^\s/$.?#].[^\s]*$` |
| `hosts` | `List[str]` | Optional | Array of hostnames corresponding to each MQTT URL.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `20`, *Maximum Length*: `1024`, *Pattern*: `^[a-zA-Z0-9\.\-_]+$` |
| `ports` | `List[int]` | Optional | Array of port numbers corresponding to each MQTT URL.<br><br>**Constraints**: *Minimum Items*: `1`, *Maximum Items*: `20`, `>= 1`, `<= 65535` |

## Example

```python
from verizon.models.connection_response_v3 import ConnectionResponseV3

connection_response_v3 = ConnectionResponseV3(
    mqtt_ur_ls=[
        'MqttURLs4',
        'MqttURLs5'
    ],
    hosts=[
        'imp-nyc-1.prod-us-east-1.thingspace.verizon.com'
    ],
    ports=[
        8883
    ]
)
```

