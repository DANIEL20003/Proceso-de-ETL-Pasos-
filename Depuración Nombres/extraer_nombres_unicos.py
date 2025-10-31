# -*- coding: utf-8 -*-
"""
Script: extraer_nombres_unicos.py
Descripción:
    Lee el archivo 'datos_sucios.xlsx' (misma carpeta), toma la tercera columna (col index 2)
    empezando desde la segunda fila del archivo (es decir, se salta la fila 0),
    extrae los valores únicos manteniendo sensibilidad a mayúsculas/minúsculas, acentos y espacios,
    y guarda los nombres únicos en 'nombres_unicos.xlsx'.
Requisitos: pandas, openpyxl
    pip install pandas openpyxl
"""

from pathlib import Path
import sys
import pandas as pd

# Nombre del archivo de entrada y salida
INPUT_FILE = Path("datos_sucios.xlsx")
OUTPUT_FILE = Path("nombres_unicos.xlsx")

# Índice de la columna a leer (tercera columna -> índice 2, 0-based)
COL_INDEX = 2

def main():
    # Verificar que el archivo exista en la misma carpeta
    if not INPUT_FILE.exists():
        print(f"ERROR: No se encontró el archivo '{INPUT_FILE}'. Asegúrate de que esté en la misma carpeta.")
        sys.exit(1)

    try:
        # Leer el Excel sin interpretar ninguna fila como encabezado (header=None)
        # para poder indexar exactamente por filas (así 'segunda fila' = index 1).
        # Se especifica engine='openpyxl' para compatibilidad con archivos .xlsx.
        df = pd.read_excel(INPUT_FILE, header=None, engine="openpyxl")
    except Exception as e:
        print(f"ERROR al leer '{INPUT_FILE}': {e}")
        sys.exit(1)

    # Comprobar que la DataFrame tenga al menos 3 columnas
    if df.shape[1] <= COL_INDEX:
        print(f"ERROR: El archivo tiene {df.shape[1]} columnas; se requiere al menos 3 columnas.")
        sys.exit(1)

    # Tomar la tercera columna (índice 2) **empezando desde la segunda fila** -> iloc[1:, 2]
    # Nota: no hacemos .str.lower(), .strip() ni normalizaciones — la comparación debe ser exacta.
    col_series = df.iloc[1:, COL_INDEX]

    # Eliminar valores nulos (NaN). Importante: si quieres tratar valores vacíos como nombres válidos,
    # elimina esta línea. Por defecto los ignoramos.
    col_non_na = col_series[~col_series.isna()]

    # Convertir a string para asegurar consistencia al guardar (no se realizan transformaciones)
    # -> la comparación/duplicado será sensible a mayúsculas, acentos y espacios porque no normalizamos.
    col_as_str = col_non_na.astype(str)

    # Extraer valores únicos preservando el orden de aparición.
    # pandas.Series.drop_duplicates() preserva el primer orden de aparición.
    uniques_series = col_as_str.drop_duplicates().reset_index(drop=True)

    # Crear DataFrame con una columna cuyo nombre puedes cambiar si lo deseas
    uniques_df = uniques_series.to_frame(name="Nombres_unicos")

    try:
        # Guardar a Excel sin el índice
        uniques_df.to_excel(OUTPUT_FILE, index=False, engine="openpyxl")
        print(f"Listo: se guardaron {len(uniques_df)} nombres únicos en '{OUTPUT_FILE}'.")
    except Exception as e:
        print(f"ERROR al guardar '{OUTPUT_FILE}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
