# Retrieve Rate Plan List

```python
retrieve_rate_plan_list_controller = client.retrieve_rate_plan_list
```

## Class Name

`RetrieveRatePlanListController`


# Get Rate Plan List

Retrieves the rate plans and rate plan details for a profile ID.

```python
def get_rate_plan_list(self,
                      ecpd_id)
```

## Authentication

This endpoint requires [thingspace_oauth1](../../doc/auth/oauth-2-client-credentials-grant-1.md) **OR** [VZ-M2M-Token](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ecpd_id` | `str` | Template, Required | The Enterprise Customer Profile Database ID. This is the same as the accountName value |

## Response Type

**200**: This is a syncronous response showing the rate plans associated.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Rateplan`](../../doc/models/rateplan.md).

## Example Usage

```python
ecpd_id = '0000123456-00001'

result = retrieve_rate_plan_list_controller.get_rate_plan_list(ecpd_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "ratePlanGroup": [
    {
      "ratePlanGroupDescription": "AGS Description_73",
      "ratePlanType": "AccountShareGroup",
      "ratePlan": [
        {
          "description": "PlanDescription 2",
          "sizeKb": "1048576",
          "carrierRatePlanCode": "Service plan code value",
          "zeroDollarBilling": false,
          "promotionOffered": false,
          "promotionDays": -2147483648,
          "ratePlanType": "accountShare",
          "account": [
            {
              "accountName": "0000123456-00001",
              "mtasAccountNumber": "0000123456-00001"
            },
            {
              "accountName": "0000123456-00001",
              "mtasAccountNumber": "0000123456-00001"
            }
          ]
        }
      ]
    },
    {
      "description": "PlanDescription 2",
      "sizeKb": "1048576",
      "carrierRatePlanCode": "Service plan code value",
      "zeroDollarBilling": false,
      "promotionOffered": false,
      "promotionDays": -2147483648,
      "ratePlanType": "accountShare",
      "account": [
        {
          "accountName": "0000123456-00001",
          "mtasAccountNumber": "0000123456-00001"
        },
        {
          "accountName": "0000123456-00001",
          "mtasAccountNumber": "0000123456-00001"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| Default | Error response | [`RuleRestErrorResponseException`](../../doc/models/rule-rest-error-response-exception.md) |

