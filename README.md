# rs-abstract-factory-informes

Sistema para procesar informes con el patrón **Abstract Factory**.

Cada informe llega como un nombre `CAT_TIPO_nombre.txt`. La categoría elige la fábrica y el tipo elige el producto.

## Requisitos

- Python 3.9 o superior.
- Sin dependencias externas.

## Ejecutar

```bash
python3 main.py
```

## Pruebas

```bash
python3 -m unittest discover -v
```

## Categorías y tipos

| Prefijo | Categoría | Tipos |
|---|---|---|
| `ENT` | ENTRADA | `FAC`, `COM` |
| `SAL` | SALIDA | `FAC`, `COM` |
| `MIX` | MIXTA | `FAC`, `COM` |
