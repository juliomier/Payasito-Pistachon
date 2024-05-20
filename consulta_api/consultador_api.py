import requests
import datetime
import json
import os
import pandas as pd

CARPETA_DATOS = 'datos_covid'

def crear_carpeta_datos():
    if not os.path.exists(CARPETA_DATOS):
        os.makedirs(CARPETA_DATOS)

def obtener_datos_covid():
    url = "https://disease.sh/v3/covid-19/historical/all?lastdays=all"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        guardar_datos_locales(datos)
        return datos
    except requests.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}, utilizando datos locales si están disponibles.")
        return cargar_datos_locales()

def guardar_datos_locales(datos):
    crear_carpeta_datos()
    try:
        ruta_txt = os.path.join(CARPETA_DATOS, 'datos_covid.txt')
        ruta_excel = os.path.join(CARPETA_DATOS, 'datos_covid.xlsx')
        
        # Guardar en un archivo de texto JSON
        with open(ruta_txt, 'w') as archivo_txt:
            json.dump(datos, archivo_txt)
        print(f"Datos guardados en {ruta_txt}")

        # Guardar en un archivo Excel
        df = pd.DataFrame(datos['cases'].items(), columns=['Fecha', 'Casos'])
        with pd.ExcelWriter(ruta_excel, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)
        print(f"Datos guardados en {ruta_excel}")
    except Exception as e:
        print(f"Error al guardar los datos locales: {e}")

def cargar_datos_locales():
    ruta_txt = os.path.join(CARPETA_DATOS, 'datos_covid.txt')
    ruta_excel = os.path.join(CARPETA_DATOS, 'datos_covid.xlsx')
    datos = cargar_datos_desde_txt(ruta_txt) or cargar_datos_desde_excel(ruta_excel)
    if datos:
        return datos
    else:
        print("No se encontraron datos locales")
        return None

def cargar_datos_desde_txt(ruta_txt):
    if os.path.exists(ruta_txt):
        with open(ruta_txt, 'r') as archivo_txt:
            datos = json.load(archivo_txt)
        return datos
    else:
        return None

def cargar_datos_desde_excel(ruta_excel):
    if os.path.exists(ruta_excel):
        df = pd.read_excel(ruta_excel, engine='openpyxl')
        datos = dict(zip(df['Fecha'], df['Casos']))
        return {'cases': datos}
    else:
        return None

def mostrar_datos_por_fecha(datos, fecha):
    casos = datos.get('cases', {}).get(fecha)
    if casos is not None:
        print(f"{fecha}: {casos}")
    else:
        print("No hay datos disponibles para esa fecha")

def mostrar_todos_los_datos(datos):
    print("Número de casos históricos:")
    for fecha, casos in datos.get('cases', {}).items():
        print(f"{fecha}: {casos}")

def obtener_y_mostrar_datos_por_fecha():
    datos = obtener_datos_covid()
    if datos:
        fecha = input("Introduce una fecha (MM/DD/YY) para ver el número de casos: ").strip()
        try:
            datetime.datetime.strptime(fecha, '%m/%d/%y')
            mostrar_datos_por_fecha(datos, fecha)
        except ValueError:
            print("Formato de fecha incorrecto")
        except KeyError:
            print("Fecha no encontrada en los datos")

def guardar_datos_individuales(tipo, nombre, datos):
    crear_carpeta_datos()
    ruta = os.path.join(CARPETA_DATOS, f'datos_{tipo}_{nombre}.json')
    try:
        with open(ruta, 'w') as archivo:
            json.dump(datos, archivo)
        print(f"Datos guardados en {ruta}")
    except Exception as e:
        print(f"Error al guardar los datos locales: {e}")

def cargar_datos_individuales(tipo, nombre):
    ruta = os.path.join(CARPETA_DATOS, f'datos_{tipo}_{nombre}.json')
    if os.path.exists(ruta):
        with open(ruta, 'r') as archivo:
            datos = json.load(archivo)
        return datos
    else:
        print(f"No se encontraron datos locales para {tipo} {nombre}")
        return None

def mostrar_datos_individuales(tipo, nombre, datos):
    print(f"Datos para {tipo} {nombre}:")
    print(json.dumps(datos, indent=4))

def obtener_datos_por_estado(estado):
    url = f"https://disease.sh/v3/covid-19/states/{estado}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        guardar_datos_individuales('estado', estado, datos)
    except requests.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}, utilizando datos locales si están disponibles.")
        datos = cargar_datos_individuales('estado', estado)
    
    if datos:
        mostrar_datos_individuales('estado', estado, datos)
    return datos

def obtener_datos_por_continente(continente):
    url = f"https://disease.sh/v3/covid-19/continents/{continente}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        guardar_datos_individuales('continente', continente, datos)
    except requests.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}, utilizando datos locales si están disponibles.")
        datos = cargar_datos_individuales('continente', continente)
    
    if datos:
        mostrar_datos_individuales('continente', continente, datos)
    return datos

def obtener_datos_por_pais(pais):
    url = f"https://disease.sh/v3/covid-19/countries/{pais}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        datos = response.json()
        guardar_datos_individuales('pais', pais, datos)
    except requests.RequestException as e:
        print(f"Error al obtener los datos de la API: {e}, utilizando datos locales si están disponibles.")
        datos = cargar_datos_individuales('pais', pais)
    
    if datos:
        mostrar_datos_individuales('pais', pais, datos)
    return datos
