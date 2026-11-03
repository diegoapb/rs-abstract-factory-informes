"""Pruebas de la evolución v3: nuevo tipo PEDIDO solo en ENTRADA."""

import unittest

from informes.errores import TipoNoSoportado
from informes.familias.entrada import PedidoEntrada
from informes.pedidos import Pedido
from informes.procesador import ProcesadorInformes


class PruebasPedido(unittest.TestCase):
    def setUp(self) -> None:
        self.procesador = ProcesadorInformes()

    def test_entrada_crea_pedidos(self) -> None:
        informe = self.procesador.crear("ENT_PED_001.txt")
        self.assertIsInstance(informe, PedidoEntrada)
        self.assertIsInstance(informe, Pedido)

    def test_salida_y_mixta_no_admiten_pedidos(self) -> None:
        for nombre in ("SAL_PED_001.txt", "MIX_PED_001.txt"):
            with self.subTest(nombre=nombre):
                with self.assertRaises(TipoNoSoportado):
                    self.procesador.crear(nombre)

    def test_pedido_no_soportado_no_detiene_el_lote(self) -> None:
        salida = self.procesador.procesar_lote(["SAL_PED_001.txt", "ENT_PED_001.txt"])
        self.assertTrue(salida[0].startswith("[ERROR]"))
        self.assertIn("PEDIDO", salida[1])


if __name__ == "__main__":
    unittest.main()
