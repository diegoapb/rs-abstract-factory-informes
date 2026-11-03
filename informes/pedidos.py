"""Contratos para los pedidos, separados de la fábrica abstracta.

No todas las categorías tienen pedidos. Por eso es una interfaz aparte:
solo la implementa la fábrica que de verdad sabe crearlos.
"""

from abc import ABC, abstractmethod

from informes.abstractos import Informe


# TERCER PRODUCTO ABSTRACTO: los pedidos.
class Pedido(Informe, ABC):
    TIPO = "PEDIDO"


# INTERFAZ SEGREGADA: capacidad opcional de crear pedidos.
class FabricaPedidos(ABC):
    @abstractmethod
    def crear_pedido(self, nombre: str) -> Pedido:
        pass
