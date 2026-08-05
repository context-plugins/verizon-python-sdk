# Create Price Plan Triggers

```python
create_price_plan_triggers_controller = client.create_price_plan_triggers
```

## Class Name

`CreatePricePlanTriggersController`


# Create Trigger Rules

Create a usage trigger at the account level, device level or a price plan trigger for all devices on the account

```python
def create_trigger_rules(self,
                        body)
```

## Authentication

This endpoint requires [thingspace_oauth1](../../doc/auth/oauth-2-client-credentials-grant-1.md) **OR** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [accountLevelCreateTriggerRequest](../../doc/models/account-level-create-trigger-request.md) \| [accountLevelObject](../../doc/models/account-level-object.md) \| [deviceLevelCreateTriggerRequest](../../doc/models/device-level-create-trigger-request.md) \| [accountGroupShareCreateTriggerRequest](../../doc/models/account-group-share-create-trigger-request.md) \| [accountShareCreateTriggerRequest](../../doc/models/account-share-create-trigger-request.md) \| [payAsYouGoCreateTriggerRequest](../../doc/models/pay-as-you-go-create-trigger-request.md) \| [createtriggerchunk](../../doc/models/createtriggerchunk.md) | Body, Required | This is a container for any-of cases. |

## Response Type

**200**: Successful request

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TriggerResponse`](../../doc/models/trigger-response.md).

## Example Usage

```python
body = AccountLevelObject()

result = create_price_plan_triggers_controller.create_trigger_rules(body)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "triggerId": "be1b5958-ffff-eeee-gggg-b1b7618c0035"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RuleRestErrorResponseException`](../../doc/models/rule-rest-error-response-exception.md) |

