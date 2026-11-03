"""Cliente del patrón: procesa informes a partir de su nombre."""

import re
from typing import Dict, Iterable, List, Optional, Tuple

from informes import registro
from informes.abstractos import FabricaInformes, Informe
from informes.errores import (
    CategoriaDesconocida,
    ErrorInforme,
    NombreNoValido,
    TipoDesconocido,
    TipoNoSoportado,
)

# FORMATO: CAT_TIPO_nombre.txt, con CAT y TIPO de tres letras.
FORMATO = re.compile(r"^([A-Z]{3})_([A-Z]{3})_(\w+)\.txt$")


# CLIENTE: depende de los contratos y del registro, nunca de una familia concreta.
class ProcesadorInformes:
    def __init__(
        self,
        fabricas: Optional[Dict[str, FabricaInformes]] = None,
        tipos: Optional[Dict[str, Tuple[type, str]]] = None,
    ) -> None:
        self.fabricas = registro.FABRICAS if fabricas is None else fabricas
        self.tipos = registro.TIPOS if tipos is None else tipos

    def crear(self, nombre: str) -> Informe:
        """Elige la fábrica por la categoría y le pide el producto del tipo."""
        partes = FORMATO.match(nombre)
        if partes is None:
            raise NombreNoValido("no sigue el formato CAT_TIPO_nombre.txt")
        categoria, tipo, _ = partes.groups()

        fabrica = self.fabricas.get(categoria)
        if fabrica is None:
            raise CategoriaDesconocida(f"categoría '{categoria}' no registrada")
        if tipo not in self.tipos:
            raise TipoDesconocido(f"tipo '{tipo}' no registrado")

        contrato, metodo = self.tipos[tipo]
        if not isinstance(fabrica, contrato):
            raise TipoNoSoportado(f"la categoría '{categoria}' no admite el tipo '{tipo}'")
        return getattr(fabrica, metodo)(nombre)

    def procesar(self, nombre: str) -> str:
        return self.crear(nombre).procesar()

    def procesar_lote(self, nombres: Iterable[str]) -> List[str]:
        """Procesa todos los nombres; un error no detiene el resto del lote."""
        salida = []
        for nombre in nombres:
            try:
                salida.append(self.procesar(nombre))
            except ErrorInforme as error:
                salida.append(f"[ERROR] {nombre}: {error}")
        return salida
