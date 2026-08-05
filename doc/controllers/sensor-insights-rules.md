# Sensor Insights Rules

```python
sensor_insights_rules_controller = client.sensor_insights_rules
```

## Class Name

`SensorInsightsRulesController`

## Methods

* [Sensor Insights Overwrite Rule Request](../../doc/controllers/sensor-insights-rules.md#sensor-insights-overwrite-rule-request)
* [Sensor Insights List Rules Request](../../doc/controllers/sensor-insights-rules.md#sensor-insights-list-rules-request)


# Sensor Insights Overwrite Rule Request

```python
def sensor_insights_overwrite_rule_request(self,
                                          body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoOverwriteRuleRequest`](../../doc/models/dto-overwrite-rule-request.md) | Body, Required | Overwrite a rule |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ResourceRule`](../../doc/models/resource-rule.md).

## Example Usage

```python
body = DtoOverwriteRuleRequest(
    accountname='0000123456-00001',
    resourceidentifier=DtoResourceidentifier(
        id='7f5f610a-eeee-ffff-gggg-4d20cf3dcfbc'
    ),
    rule=ResourceRule(
        createdon=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
        foreignid='c1f178d3-eeee-ffff-gggg-0d6b7ae6022a',
        lastupdated=dateutil.parser.parse('2023-10-02T15:46:34.562Z'),
        rulechain=jsonpickle.decode('{}'),
        versionid='337bd2e8-eeee-ffff-gggg-5207992fd395',
        accountclientid='null',
        billingaccountid='The billing account ID',
        description='a short description',
        deviceid='The UUID of the device',
        disabled=True,
        id='bc5b5b5a-eeee-ffff-gggg-cb2cb2533d47',
        name='User defined name of the record',
        rulesyntax='The rule syntax',
        version='1.0'
    )
)

result = sensor_insights_rules_controller.sensor_insights_overwrite_rule_request(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 401 | UnAuthorized | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 404 | Not Found | [`M404ManagementErrorException`](../../doc/models/m404-management-error-exception.md) |
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`M500ManagementErrorException`](../../doc/models/m500-management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |


# Sensor Insights List Rules Request

```python
def sensor_insights_list_rules_request(self,
                                      body)
```

## Authentication

This endpoint requires [thingspace_oauth](../../doc/auth/oauth-2-client-credentials-grant.md) **AND** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DtoListRulesRequest`](../../doc/models/dto-list-rules-request.md) | Body, Required | Retrieve a rule |

## Response Type

**200**: OK

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`List[ResourceRule]`](../../doc/models/resource-rule.md).

## Example Usage

```python
body = DtoListRulesRequest(
    accountname='0000123456-00001',
    filter=DtoFilter(
        expand='device detail(s)',
        limitnumber=100,
        nopagination=True,
        page='The number of pages',
        pagenumber=100,
        projection=[
            'specific device fields requested'
        ],
        selection={
            'additionalProp1': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'additionalProp2': jsonpickle.decode('{"key1":"val1","key2":"val2"}'),
            'additionalProp3': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    resourceidentifier=DtoResourceidentifier(
        id='ffb86390-eeee-ffff-gggg-9d1180882d63'
    )
)

result = sensor_insights_rules_controller.sensor_insights_list_rules_request(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`M400ManagementErrorException`](../../doc/models/m400-management-error-exception.md) |
| 401 | UnAuthorized | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 403 | Forbidden | [`M403ManagementErrorException`](../../doc/models/m403-management-error-exception.md) |
| 404 | Not Found | [`M404ManagementErrorException`](../../doc/models/m404-management-error-exception.md) |
| 406 | Not Acceptable | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 415 | Unsupported media type | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 429 | Too many requests | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |
| 500 | Internal server error. | [`M500ManagementErrorException`](../../doc/models/m500-management-error-exception.md) |
| Default | Unexpected error | [`ManagementErrorException`](../../doc/models/management-error-exception.md) |

