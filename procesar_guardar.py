import pandas as pd
from Limpieza_preparacion import procesar_datos

def procesar_y_guardar_csv(nombre_archivo_cargar, nombre_archivo_guardar):
    # Leer el CSV en un DataFrame
    df = pd.read_csv(nombre_archivo_cargar)

    # Procesar los datos
    df_procesado = procesar_datos(df)

    # Guardar el resultado como CSV
    df_procesado.to_csv(nombre_archivo_guardar, index=False)

    print(f"Datos procesados y guardados correctamente en '{nombre_archivo_guardar}'.")
