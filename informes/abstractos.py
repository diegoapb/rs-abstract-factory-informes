"""Contratos del patrón: productos abstractos y fábrica abstracta."""

from abc import ABC, abstractmethod


# PRODUCTO BASE: todo informe sabe procesarse y describirse igual.
class Informe(ABC):
    CATEGORIA = ""
    TIPO = ""

    def __init__(self, nombre: str) -> None:
        self.nombre = nombre

    def procesar(self) -> str:
        return f"[{self.CATEGORIA} · {self.TIPO}] {self.nombre}: {self.accion()}"

    @abstractmethod
    def accion(self) -> str:
        """Lo que hace el sistema con el informe, según su categoría y tipo."""


# PRIMER PRODUCTO ABSTRACTO: las facturas.
class Factura(Informe, ABC):
    TIPO = "FACTURA"


# SEGUNDO PRODUCTO ABSTRACTO: las compras.
class Compra(Informe, ABC):
    TIPO = "COMPRA"


# FÁBRICA ABSTRACTA: cada categoría crea su propia familia de informes.
class FabricaInformes(ABC):
    @abstractmethod
    def crear_factura(self, nombre: str) -> Factura:
        pass

    @abstractmethod
    def crear_compra(self, nombre: str) -> Compra:
        pass
