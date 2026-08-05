
# Geometry

## Data Type

`LineString | Polygon | MultiLineString | MultiPolygon`

## Cases

| Type |
|  --- |
| [`LineString`](../../../doc/models/line-string.md) |
| [`Polygon`](../../../doc/models/polygon.md) |
| [`MultiLineString`](../../../doc/models/multi-line-string.md) |
| [`MultiPolygon`](../../../doc/models/multi-polygon.md) |

## LineString

### Initialization Code

#### Example

```python
value = LineString(
    mtype=Type2Enum.LINESTRING,
    coordinates=[
        [
            51.53,
            51.54
        ],
        [
            51.53,
            51.54
        ]
    ]
)
```

## Polygon

### Initialization Code

#### Example

```python
value = Polygon(
    mtype=Type3Enum.POLYGON,
    coordinates=[
        [
            [
                180
            ]
        ]
    ]
)
```

## MultiLineString

### Initialization Code

#### Example

```python
value = MultiLineString(
    mtype=Type4Enum.MULTILINESTRING,
    coordinates=[
        [
            [
                180,
                180
            ],
            [
                180,
                180
            ]
        ],
        [
            [
                180,
                180
            ],
            [
                180,
                180
            ]
        ]
    ]
)
```

## MultiPolygon

### Initialization Code

#### Example

```python
value = MultiPolygon(
    mtype=Type5Enum.MULTIPOLYGON,
    coordinates=[
        [
            [
                [
                    46.55
                ]
            ]
        ]
    ]
)
```

