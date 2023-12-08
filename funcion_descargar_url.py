import requests

def descargar_y_guardar_csv(url: str, nombre_archivo: str) -> None:
    try:
        # Realizar get request
        respuesta = requests.get(url)
        
        # Verificar si la solicitud fue exitosa (código 200)
        if respuesta.status_code == 200:
            # Guardar el contenido en un archivo CSV
            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                archivo.write(respuesta.text)
            print(f"Datos descargados y guardados correctamente en '{nombre_archivo}'.")
        else:
           print(f"Error al descargar datos. Código de estado: {respuesta.status_code}")
    except requests.RequestException as e:
        print(f"Error al realizar la solicitud: {e}")
