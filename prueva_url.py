from funcion_descargar_url import descargar_y_guardar_csv
# Ejemplo de uso:
url_descargar = 'https://huggingface.co/datasets/mstz/heart_failure/raw/main/heart_failure_clinical_records_dataset.csv'
nombre_archivo_guardar = 'heart_failure_dataset.csv'
descargar_y_guardar_csv(url_descargar, nombre_archivo_guardar)
