"""Errores del procesado de informes."""


class ErrorInforme(Exception):
    """Base de todos los errores al procesar un informe."""


class NombreNoValido(ErrorInforme):
    """El nombre no sigue el formato CAT_TIPO_nombre.txt."""


class CategoriaDesconocida(ErrorInforme):
    """No hay ninguna fábrica registrada para la categoría."""


class TipoDesconocido(ErrorInforme):
    """No hay ningún tipo de informe registrado con ese código."""


class TipoNoSoportado(ErrorInforme):
    """La categoría existe, pero su fábrica no crea ese tipo de informe."""
