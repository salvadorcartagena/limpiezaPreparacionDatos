import pandas as pd

def procesar_datos(dataframe):
    # Verificar valores faltantes
    if dataframe.isnull().values.any():
        print("Existen valores faltantes. Realizando imputación.")
        dataframe = dataframe.dropna()

    # Verificar filas duplicadas
    if dataframe.duplicated().any():
        print("Existen filas duplicadas. Eliminando duplicados.")
        dataframe = dataframe.drop_duplicates()

    # Verificar y eliminar valores atípicos (usando, por ejemplo, el rango intercuartílico)
    Q1 = dataframe.quantile(0.25)
    Q3 = dataframe.quantile(0.75)
    IQR = Q3 - Q1
    dataframe = dataframe[~((dataframe < (Q1 - 1.5 * IQR)) | (dataframe > (Q3 + 1.5 * IQR))).any(axis=1)]

    # Crear columna de categoría por edades
    bins = [0, 12, 19, 39, 59, float('inf')]
    labels = ['Niño', 'Adolescente', 'Jóvenes adulto', 'Adulto', 'Adulto mayor']
    dataframe['Edad_Categoria'] = pd.cut(dataframe['age'], bins=bins, labels=labels, right=False)

    return dataframe

