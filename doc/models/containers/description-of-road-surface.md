
# Description of Road Surface

Indicates the composition of the surface of the roadway for use in estimation of friction.

## Data Type

`DescriptionOfRoadSurfacePortlandCement | DescriptionOfRoadSurfaceAsphaltOrTar | DescriptionOfRoadSurfaceGravel | DescriptionOfRoadSurfaceGrass | DescriptionOfRoadSurfaceCinders | DescriptionOfRoadSurfaceRock | DescriptionOfRoadSurfaceIce | DescriptionOfRoadSurfaceSnow`

## Cases

| Type |
|  --- |
| [`DescriptionOfRoadSurfacePortlandCement`](../../../doc/models/description-of-road-surface-portland-cement.md) |
| [`DescriptionOfRoadSurfaceAsphaltOrTar`](../../../doc/models/description-of-road-surface-asphalt-or-tar.md) |
| [`DescriptionOfRoadSurfaceGravel`](../../../doc/models/description-of-road-surface-gravel.md) |
| [`DescriptionOfRoadSurfaceGrass`](../../../doc/models/description-of-road-surface-grass.md) |
| [`DescriptionOfRoadSurfaceCinders`](../../../doc/models/description-of-road-surface-cinders.md) |
| [`DescriptionOfRoadSurfaceRock`](../../../doc/models/description-of-road-surface-rock.md) |
| [`DescriptionOfRoadSurfaceIce`](../../../doc/models/description-of-road-surface-ice.md) |
| [`DescriptionOfRoadSurfaceSnow`](../../../doc/models/description-of-road-surface-snow.md) |

## DescriptionOfRoadSurfacePortlandCement

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfacePortlandCement(
    portland_cement=PortlandCement(
        mtype=Type6Enum.TRAVELED
    )
)
```

## DescriptionOfRoadSurfaceAsphaltOrTar

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceAsphaltOrTar(
    asphalt_or_tar=AsphaltOrTar()
)
```

## DescriptionOfRoadSurfaceGravel

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceGravel(
    gravel=Gravel()
)
```

## DescriptionOfRoadSurfaceGrass

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceGrass(
    grass=Grass()
)
```

## DescriptionOfRoadSurfaceCinders

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceCinders(
    cinders=Cinders()
)
```

## DescriptionOfRoadSurfaceRock

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceRock(
    rock=Rock()
)
```

## DescriptionOfRoadSurfaceIce

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceIce(
    ice=Ice()
)
```

## DescriptionOfRoadSurfaceSnow

### Initialization Code

#### Example

```python
value = DescriptionOfRoadSurfaceSnow(
    snow=Snow()
)
```

