# -*- coding: utf-8 -*-
"""
Script: depurar_nombres_universidades.py
Descripción:
    Lee 'datos_sucios.xlsx' (misma carpeta), toma la tercera columna (índice 2)
    empezando desde la segunda fila (se salta la fila 1 / index 0),
    reemplaza los nombres que coincidan con las VARIANTES definidas en
    'Nombres universidades y variantes.txt' por el NOMBRE UNIVERSIDAD ORIGINAL correspondiente,
    y guarda el resultado en 'datos_depurados.xlsx'.

Notas importantes:
    - La comparación/matching se hace **exacta** (sensible a mayúsculas/minúsculas, acentos y espacios),
      porque el archivo de variantes contiene múltiples variantes intencionales.
    - Si deseas comportamiento **no** sensible (p. ej. ignorar mayúsculas o acentos), puedo
      darte una versión alternativa que normalice cadenas antes de comparar.
Requisitos: pandas, openpyxl
    pip install pandas openpyxl
"""

from pathlib import Path
import pandas as pd
import sys

# Rutas / nombres de archivos (se asume que están en la misma carpeta que este script)
INPUT_XLSX = Path("datos_sucios.xlsx")
OUTPUT_XLSX = Path("datos_depurados.xlsx")
MAPPING_TXT = Path("Nombres universidades y variantes.txt")  # archivo que subiste (ver: :contentReference[oaicite:1]{index=1})

# Índice de la columna a procesar (tercera columna -> índice 2, 0-based)
COL_INDEX = 2

def parse_mapping_file(path: Path):
    """
    Parsea el archivo de mapeo y devuelve un diccionario { variante_str -> nombre_universidad_original }.
    El parser respeta exactamente los caracteres (no normaliza mayúsculas/acentos/espacios).
    Formato esperado en el archivo (ejemplo):
        **NOMBRE UNIVERSIDAD ORIGINAL**
        Nombre Universidad Original
        **VARIANTES**
        Variante 1
        Variante 2
        ...
    """
    if not path.exists():
        raise FileNotFoundError(f"No se encontró el archivo de mapeo: {path}")

    mapping = {}          # resultado: variante -> original
    originals_seen = []   # lista de originales (por si quieres inspeccionar)

    with path.open("r", encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    n = len(lines)

    while i < n:
        line = lines[i].rstrip("\n")  # quitamos solo el salto de línea, no espacios
        # Detectar marcador de inicio de bloque de "NOMBRE UNIVERSIDAD ORIGINAL"
        if line.strip().upper().startswith("**NOMBRE") and "ORIGINAL" in line.upper():
            # buscar la siguiente línea no vacía (esa debería ser el nombre original)
            i += 1
            while i < n and lines[i].strip() == "":
                i += 1
            if i >= n:
                break
            original = lines[i].rstrip("\n")
            originals_seen.append(original)
            i += 1

            # avanzar hasta encontrar el marcador **VARIANTES** (si existe)
            while i < n and not (lines[i].strip().upper().startswith("**VARIANTES")):
                # si hay otras líneas inesperadas vacías, saltarlas
                if lines[i].strip() == "":
                    i += 1
                else:
                    # Si no hay marcador y hay contenido, avanzar (defensivo)
                    i += 1

            # si hay marcador de VARIANTES, leerlas hasta el próximo bloque o EOF
            if i < n and lines[i].strip().upper().startswith("**VARIANTES"):
                i += 1
                # leer variantes hasta encontrar otro bloque **NOMBRE...** o EOF
                while i < n and not (lines[i].strip().upper().startswith("**NOMBRE") and "ORIGINAL" in lines[i].upper()):
                    variant_line = lines[i].rstrip("\n")
                    # si la línea no está vacía, la consideramos una variante
                    if variant_line.strip() != "":
                        # agregar la variante al mapping apuntando al original
                        # importantísimo: no hacemos strip() ni lower() para mantener sensibilidad
                        mapping[variant_line] = original
                    i += 1
            else:
                # No se encontró sección VARIANTES: todavía registramos el original para si acaso
                # (en este caso no habrá variantes mapeadas)
                continue
        else:
            # Si no es un marcador, simplemente avanzar
            i += 1

    # Opcional: mapea también el nombre original a sí mismo (útil si en el Excel ya aparece la forma "original")
    for orig in originals_seen:
        # sólo agregar si orig no está ya en mapping como variante
        if orig not in mapping:
            mapping[orig] = orig

    return mapping

def depurar_excel(input_xlsx: Path, output_xlsx: Path, mapping: dict, col_index: int):
    """
    Lee el Excel, corrige la columna indicada según mapping, y guarda el resultado.
    - input_xlsx: Path del archivo de entrada
    - output_xlsx: Path del archivo de salida
    - mapping: dict de variantes -> original
    - col_index: índice 0-based de la columna a procesar (aquí: 2)
    """
    if not input_xlsx.exists():
        raise FileNotFoundError(f"No se encontró el archivo de entrada: {input_xlsx}")

    # Leer Excel sin header (header=None) para mantener indexación por filas exacta
    df = pd.read_excel(input_xlsx, header=None, engine="openpyxl")

    # Verificar que exista la columna solicitada
    if df.shape[1] <= col_index:
        raise IndexError(f"El archivo tiene {df.shape[1]} columnas; se requiere al menos la columna índice {col_index} (tercera columna).")

    # Contadores para el resumen
    total_procesados = 0
    total_reemplazados = 0
    total_sin_coincidencia = 0

    # Trabajamos sobre una copia para no alterar la original en memoria (por claridad)
    df_out = df.copy()

    # Iterar filas desde la segunda fila (index 1 de pandas) hasta el final
    for idx in df.index[1:]:
        valor = df.at[idx, col_index]  # valor tal cual está en la celda
        # Si el valor es NaN -> no procesar (lo dejamos como está)
        if pd.isna(valor):
            continue

        total_procesados += 1

        # Convertir a string para comparar con las claves del mapping
        # IMPORTANTE: no hacer .strip() ni lower() -> mantenemos sensibilidad a espacios, mayúsculas y acentos.
        valor_str = str(valor)

        if valor_str in mapping:
            # reemplazar por el NOMBRE UNIVERSIDAD ORIGINAL
            df_out.at[idx, col_index] = mapping[valor_str]
            total_reemplazados += 1
        else:
            # si no hay match exacto, dejamos el valor tal cual
            total_sin_coincidencia += 1
            # (si quieres identificar las filas sin coincidencia, podríamos almacenarlas en una lista)
            # ej: sin_coincidencias.append((idx, valor_str))

    # Guardar el DataFrame resultante en un nuevo archivo Excel (sin índice)
    df_out.to_excel(output_xlsx, index=False, header=False, engine="openpyxl")

    return {
        "total_procesados": total_procesados,
        "total_reemplazados": total_reemplazados,
        "total_sin_coincidencia": total_sin_coincidencia,
        "total_filas": len(df)
    }

def main():
    try:
        print("Parseando archivo de mapeo:", MAPPING_TXT)
        mapping = parse_mapping_file(MAPPING_TXT)
        print(f"Mapeo cargado. Variantes registradas: {len(mapping)}")

        print("Procesando archivo Excel:", INPUT_XLSX)
        resumen = depurar_excel(INPUT_XLSX, OUTPUT_XLSX, mapping, COL_INDEX)

        print("----- Resumen -----")
        print(f"Filas totales en el Excel original: {resumen['total_filas']}")
        print(f"Valores procesados (tercera columna, desde segunda fila): {resumen['total_procesados']}")
        print(f"Reemplazos realizados: {resumen['total_reemplazados']}")
        print(f"Sin coincidencia en el mapeo: {resumen['total_sin_coincidencia']}")
        print(f"Archivo de salida generado: {OUTPUT_XLSX}")

    except Exception as e:
        print("ERROR:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
