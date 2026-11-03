"""Registro de categorías y tipos.

Es el único sitio que conoce las fábricas concretas.
Para añadir una categoría basta con registrar aquí su fábrica.
"""

from informes.abstractos import FabricaInformes
from informes.familias.entrada import FabricaEntrada
from informes.familias.mixta import FabricaMixta
from informes.familias.salida import FabricaSalida
from informes.pedidos import FabricaPedidos

# CATEGORÍAS: prefijo del nombre -> fábrica de esa familia.
FABRICAS = {
    "ENT": FabricaEntrada(),
    "SAL": FabricaSalida(),
    "MIX": FabricaMixta(),
}

# TIPOS: código del nombre -> (contrato que debe cumplir la fábrica, método que lo crea).
TIPOS = {
    "FAC": (FabricaInformes, "crear_factura"),
    "COM": (FabricaInformes, "crear_compra"),
    "PED": (FabricaPedidos, "crear_pedido"),
}
