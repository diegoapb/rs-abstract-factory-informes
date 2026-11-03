"""Pruebas de la evolución v2: nueva categoría MIXTA."""

import unittest

from informes.familias.mixta import CompraMixta, FacturaMixta
from informes.procesador import ProcesadorInformes


class PruebasMixta(unittest.TestCase):
    def setUp(self) -> None:
        self.procesador = ProcesadorInformes()

    def test_mixta_crea_sus_dos_productos(self) -> None:
        self.assertIsInstance(self.procesador.crear("MIX_FAC_001.txt"), FacturaMixta)
        self.assertIsInstance(self.procesador.crear("MIX_COM_001.txt"), CompraMixta)

    def test_la_salida_indica_mixta(self) -> None:
        linea = self.procesador.procesar("MIX_FAC_001.txt")
        self.assertIn("MIXTA", linea)
        self.assertIn("FACTURA", linea)


if __name__ == "__main__":
    unittest.main()
