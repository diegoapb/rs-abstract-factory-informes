"""Familia ENTRADA: documentos que llegan a la empresa."""

from informes.abstractos import Compra, FabricaInformes, Factura


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


# FÁBRICA CONCRETA: solo entrega informes de entrada.
class FabricaEntrada(FabricaInformes):
    def crear_factura(self, nombre: str) -> Factura:
        return FacturaEntrada(nombre)

    def crear_compra(self, nombre: str) -> Compra:
        return CompraEntrada(nombre)
