import pandas as pd
import consulta_api.consultador_api

def calcular_estadisticas(datos):
    df = pd.DataFrame(datos['cases'].items(), columns=['Fecha', 'Casos'])
    estadisticas = {
        'Media': df['Casos'].mean(),
        'Mediana': df['Casos'].median(),
        'Máximo': df['Casos'].max(),
        'Mínimo': df['Casos'].min(),
        'Varianza': df['Casos'].var(),
        'Desviación Estándar': df['Casos'].std()
    }
    return estadisticas

def mostrar_estadisticas():
    datos = consulta_api.consultador_api.obtener_datos_covid()
    if datos:
        estadisticas = calcular_estadisticas(datos)
        print("Estadísticas de casos históricos de COVID 19:")
        for key, value in estadisticas.items():
            print(f"{key}: {value}")
    else:
        print("No se encontraron datos locales")
