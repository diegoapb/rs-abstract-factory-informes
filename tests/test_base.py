"""Pruebas del sistema base: ENTRADA y SALIDA con FACTURA y COMPRA."""

import unittest

from informes.abstractos import Compra, Factura
from informes.errores import CategoriaDesconocida, NombreNoValido, TipoDesconocido
from informes.familias.entrada import CompraEntrada, FacturaEntrada
from informes.familias.salida import CompraSalida, FacturaSalida
from informes.procesador import ProcesadorInformes


class PruebasBase(unittest.TestCase):
    def setUp(self) -> None:
        self.procesador = ProcesadorInformes()

    def test_cada_combinacion_crea_su_producto(self) -> None:
        casos = {
            "ENT_FAC_001.txt": (FacturaEntrada, Factura),
            "ENT_COM_001.txt": (CompraEntrada, Compra),
            "SAL_FAC_001.txt": (FacturaSalida, Factura),
            "SAL_COM_001.txt": (CompraSalida, Compra),
        }
        for nombre, (concreto, abstracto) in casos.items():
            with self.subTest(nombre=nombre):
                informe = self.procesador.crear(nombre)
                self.assertIsInstance(informe, concreto)
                self.assertIsInstance(informe, abstracto)

    def test_la_salida_indica_categoria_tipo_y_archivo(self) -> None:
        linea = self.procesador.procesar("SAL_COM_001.txt")
        self.assertIn("SALIDA", linea)
        self.assertIn("COMPRA", linea)
        self.assertIn("SAL_COM_001.txt", linea)

    def test_nombre_sin_formato(self) -> None:
        with self.assertRaises(NombreNoValido):
            self.procesador.crear("informe.txt")

    def test_categoria_desconocida(self) -> None:
        with self.assertRaises(CategoriaDesconocida):
            self.procesador.crear("XYZ_FAC_001.txt")

    def test_tipo_desconocido(self) -> None:
        with self.assertRaises(TipoDesconocido):
            self.procesador.crear("ENT_XYZ_001.txt")

    def test_un_error_no_detiene_el_lote(self) -> None:
        salida = self.procesador.procesar_lote(["malo.txt", "ENT_FAC_001.txt"])
        self.assertTrue(salida[0].startswith("[ERROR]"))
        self.assertIn("ENT_FAC_001.txt", salida[1])


if __name__ == "__main__":
    unittest.main()
