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
| `ENT` | ENTRADA | `FAC`, `COM`, `PED` |
| `SAL` | SALIDA | `FAC`, `COM` |
| `MIX` | MIXTA | `FAC`, `COM` |

## Módulos

| Archivo | Qué hace |
|---|---|
| `informes/abstractos.py` | Productos abstractos (`Informe`, `Factura`, `Compra`) y fábrica abstracta `FabricaInformes`. |
| `informes/pedidos.py` | Producto `Pedido` e interfaz `FabricaPedidos`, separada porque solo ENTRADA tiene pedidos. |
| `informes/familias/entrada.py` | Familia ENTRADA: su fábrica y sus productos. |
| `informes/familias/salida.py` | Familia SALIDA: su fábrica y sus productos. |
| `informes/familias/mixta.py` | Familia MIXTA: su fábrica y sus productos. |
| `informes/registro.py` | Relaciona cada prefijo con su fábrica y cada tipo con el contrato que lo crea. |
| `informes/procesador.py` | Cliente: interpreta el nombre, elige la fábrica y procesa el informe. |
| `informes/errores.py` | Errores del procesado. |
| `main.py` | Simula el procesado de una carpeta de informes. |
| `tests/` | Pruebas de cada versión. |

## Añadir una categoría

1. Crea un módulo en `informes/familias/`.
2. Define sus productos heredando de `Factura` y `Compra`.
3. Define su fábrica heredando de `FabricaInformes`.
4. Registra su prefijo en `FABRICAS`, dentro de `informes/registro.py`.

No hace falta tocar ninguna otra clase.

## Añadir un tipo de informe

1. Define el producto abstracto y su interfaz de fábrica en un módulo propio.
2. Haz que las fábricas que lo admiten implementen esa interfaz.
3. Registra el tipo en `TIPOS`, dentro de `informes/registro.py`.

Las categorías que no lo admiten responden «no soportado» sin cambios.

## Salida esperada

```text
Procesando carpeta de informes...
  [ENTRADA · FACTURA] ENT_FAC_001.txt: registrando factura de proveedor en cuentas por pagar
  [ENTRADA · COMPRA] ENT_COM_001.txt: dando entrada en almacén a la mercancía recibida
  [SALIDA · FACTURA] SAL_FAC_001.txt: emitiendo factura al cliente y registrando cuenta por cobrar
  [SALIDA · COMPRA] SAL_COM_001.txt: enviando orden de compra al proveedor
  [MIXTA · FACTURA] MIX_FAC_001.txt: compensando cobros y pagos de un mismo tercero
  [MIXTA · COMPRA] MIX_COM_001.txt: registrando compra con devolución parcial al proveedor
  [ENTRADA · PEDIDO] ENT_PED_001.txt: registrando pedido del cliente y reservando stock
  [ERROR] SAL_PED_001.txt: la categoría 'SAL' no admite el tipo 'PED'
  [ERROR] informe_sin_formato.txt: no sigue el formato CAT_TIPO_nombre.txt
```

## Evolución

| Etiqueta | Qué aporta |
|---|---|
| [`v1-base`](https://github.com/diegoapb/rs-abstract-factory-informes/tree/v1-base) | ENTRADA y SALIDA con FACTURA y COMPRA. |
| [`v2-mixta`](https://github.com/diegoapb/rs-abstract-factory-informes/tree/v2-mixta) | Nueva categoría MIXTA. Solo se añade código; ninguna clase existente cambia. |
| [`v3-pedido`](https://github.com/diegoapb/rs-abstract-factory-informes/tree/v3-pedido) | Nuevo tipo PEDIDO, solo en ENTRADA, con una interfaz segregada. |

Cambios entre versiones:

- [`v1-base...v2-mixta`](https://github.com/diegoapb/rs-abstract-factory-informes/compare/v1-base...v2-mixta)
- [`v2-mixta...v3-pedido`](https://github.com/diegoapb/rs-abstract-factory-informes/compare/v2-mixta...v3-pedido)
