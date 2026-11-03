"""Simula el procesado de una carpeta de informes."""

from informes.procesador import ProcesadorInformes

# CARPETA DE ENTRADA: nombres de los informes a procesar.
INFORMES = [
    "ENT_FAC_001.txt",
    "ENT_COM_001.txt",
    "SAL_FAC_001.txt",
    "SAL_COM_001.txt",
    "MIX_FAC_001.txt",
    "MIX_COM_001.txt",
    "informe_sin_formato.txt",
]


def main() -> None:
    print("Procesando carpeta de informes...")
    for linea in ProcesadorInformes().procesar_lote(INFORMES):
        print(f"  {linea}")


if __name__ == "__main__":
    main()
