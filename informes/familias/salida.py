"""Familia SALIDA: documentos que emite la empresa."""

from informes.abstractos import Compra, FabricaInformes, Factura


# FAMILIA SALIDA, producto factura.
class FacturaSalida(Factura):
    CATEGORIA = "SALIDA"

    def accion(self) -> str:
        return "emitiendo factura al cliente y registrando cuenta por cobrar"


# FAMILIA SALIDA, producto compra.
class CompraSalida(Compra):
    CATEGORIA = "SALIDA"

    def accion(self) -> str:
        return "enviando orden de compra al proveedor"


# FÁBRICA CONCRETA: solo entrega informes de salida.
class FabricaSalida(FabricaInformes):
    def crear_factura(self, nombre: str) -> Factura:
        return FacturaSalida(nombre)

    def crear_compra(self, nombre: str) -> Compra:
        return CompraSalida(nombre)
