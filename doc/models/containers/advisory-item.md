
# Advisory Item

The use of ITIS codes interspersed with free text. The complete set of ITIS codes can be found in Volume Two of the SAE J2540 standard.

## Data Type

`ITISItemWrapper | TextItemWrapper`

## Cases

| Type |
|  --- |
| [`ITISItemWrapper`](../../../doc/models/itis-item-wrapper.md) |
| [`TextItemWrapper`](../../../doc/models/text-item-wrapper.md) |

## ITISItemWrapper

### Initialization Code

#### Example

```python
value = ITISItemWrapper(
    item=ITISItemContent(
        itis=10
    )
)
```

## TextItemWrapper

### Initialization Code

#### Example

```python
value = TextItemWrapper(
    item=TextItemContent(
        text='text2'
    )
)
```

