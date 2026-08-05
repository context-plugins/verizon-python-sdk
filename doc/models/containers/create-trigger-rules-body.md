
# Create Trigger Rules Body

## Data Type

`AccountLevelCreateTriggerRequest | AccountLevelObject | DeviceLevelCreateTriggerRequest | AccountGroupShareCreateTriggerRequest | AccountShareCreateTriggerRequest | PayAsYouGoCreateTriggerRequest | Createtriggerchunk`

## Cases

| Type |
|  --- |
| [`AccountLevelCreateTriggerRequest`](../../../doc/models/account-level-create-trigger-request.md) |
| [`AccountLevelObject`](../../../doc/models/account-level-object.md) |
| [`DeviceLevelCreateTriggerRequest`](../../../doc/models/device-level-create-trigger-request.md) |
| [`AccountGroupShareCreateTriggerRequest`](../../../doc/models/account-group-share-create-trigger-request.md) |
| [`AccountShareCreateTriggerRequest`](../../../doc/models/account-share-create-trigger-request.md) |
| [`PayAsYouGoCreateTriggerRequest`](../../../doc/models/pay-as-you-go-create-trigger-request.md) |
| [`Createtriggerchunk`](../../../doc/models/createtriggerchunk.md) |

## AccountLevelCreateTriggerRequest

### Initialization Code

#### Example

```python
value = AccountLevelCreateTriggerRequest(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    notification_type='PerEvent',
    callback=True,
    email_notification=False,
    notification_group_name='Notification Group Name (User defined)',
    notification_frequency_factor=3,
    notification_frequency_interval='Daily',
    external_email_recipients='Email addresses',
    sms_notification=True,
    reminder=True,
    severity='Notify',
    active=ActiveEnum.TRUE
)
```

## AccountLevelObject

### Initialization Code

#### Example

```python
value = AccountLevelObject(
    action=AccountLevelActionEnum.NOTIFY
)
```

## DeviceLevelCreateTriggerRequest

### Initialization Code

#### Example

```python
value = DeviceLevelCreateTriggerRequest(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

## AccountGroupShareCreateTriggerRequest

### Initialization Code

#### Example

```python
value = AccountGroupShareCreateTriggerRequest(
    trigger_name='name of the trigger',
    account_name='0000123456-00001',
    active=ActiveEnum.TRUE
)
```

## AccountShareCreateTriggerRequest

### Initialization Code

#### Example

```python
value = AccountShareCreateTriggerRequest(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

## PayAsYouGoCreateTriggerRequest

### Initialization Code

#### Example

```python
value = PayAsYouGoCreateTriggerRequest(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

## Createtriggerchunk

### Initialization Code

#### Example

```python
value = Createtriggerchunk(
    trigger_name='name of the trigger',
    ecpd_id='Verizon profile ID',
    active=ActiveEnum.TRUE
)
```

