"""Familia ENTRADA: documentos que llegan a la empresa."""

from informes.abstractos import Compra, FabricaInformes, Factura
from informes.pedidos import FabricaPedidos, Pedido


# FAMILIA ENTRADA, producto factura.
class FacturaEntrada(Factura):
    CATEGORIA = "ENTRADA"

    def accion(self) -> str:
        return "registrando factura de proveedor en cuentas por pagar"


# FAMILIA ENTRADA, producto compra.
class CompraEntrada(Compra):
    CATEGORIA = "ENTRADA"

    def accion(self) -> str:
        return "dando entrada en almacén a la mercancía recibida"


# FAMILIA ENTRADA, producto pedido.
class PedidoEntrada(Pedido):
    CATEGORIA = "ENTRADA"

    def accion(self) -> str:
        return "registrando pedido del cliente y reservando stock"


# FÁBRICA CONCRETA: solo entrega informes de entrada; además sabe crear pedidos.
class FabricaEntrada(FabricaInformes, FabricaPedidos):
    def crear_factura(self, nombre: str) -> Factura:
        return FacturaEntrada(nombre)

    def crear_compra(self, nombre: str) -> Compra:
        return CompraEntrada(nombre)

    def crear_pedido(self, nombre: str) -> Pedido:
        return PedidoEntrada(nombre)
