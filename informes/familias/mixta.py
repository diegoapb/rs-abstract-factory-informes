"""Familia MIXTA: documentos que combinan entrada y salida."""

from informes.abstractos import Compra, FabricaInformes, Factura


# FAMILIA MIXTA, producto factura.
class FacturaMixta(Factura):
    CATEGORIA = "MIXTA"

    def accion(self) -> str:
        return "compensando cobros y pagos de un mismo tercero"


# FAMILIA MIXTA, producto compra.
class CompraMixta(Compra):
    CATEGORIA = "MIXTA"

    def accion(self) -> str:
        return "registrando compra con devolución parcial al proveedor"


# FÁBRICA CONCRETA: solo entrega informes mixtos.
class FabricaMixta(FabricaInformes):
    def crear_factura(self, nombre: str) -> Factura:
        return FacturaMixta(nombre)

    def crear_compra(self, nombre: str) -> Compra:
        return CompraMixta(nombre)
