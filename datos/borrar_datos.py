import os

CARPETA_DATOS = 'datos_covid'

def borrar_archivos(ruta_txt=None, ruta_excel=None, rutas_graficas=None):
    if rutas_graficas is None:
        rutas_graficas = ['grafica_linea.png', 'grafica_barras.png', 'histograma.png']
    
    if ruta_txt is None:
        ruta_txt = os.path.join(CARPETA_DATOS, 'datos_covid.txt')
    
    if ruta_excel is None:
        ruta_excel = os.path.join(CARPETA_DATOS, 'datos_covid.xlsx')
    
    try:
        os.remove(ruta_txt)
        print(f"Archivo de texto '{ruta_txt}' borrado exitosamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo de texto '{ruta_txt}' para borrar.")
    
    try:
        os.remove(ruta_excel)
        print(f"Archivo de Excel '{ruta_excel}' borrado exitosamente.")
    except FileNotFoundError:
        print(f"No se encontró el archivo de Excel '{ruta_excel}' para borrar.")
    
    for ruta_grafica in rutas_graficas:
        try:
            os.remove(ruta_grafica)
            print(f"Archivo de gráfica '{ruta_grafica}' borrado exitosamente.")
        except FileNotFoundError:
            print(f"No se encontró el archivo de gráfica '{ruta_grafica}' para borrar.")
    
    # Borrar archivos individuales
    for archivo in os.listdir(CARPETA_DATOS):
        archivo_path = os.path.join(CARPETA_DATOS, archivo)
        try:
            os.remove(archivo_path)
            print(f"Archivo '{archivo_path}' borrado exitosamente.")
        except FileNotFoundError:
            print(f"No se encontró el archivo '{archivo_path}' para borrar.")
    
    # Intentar borrar la carpeta si está vacía
    try:
        os.rmdir(CARPETA_DATOS)
        print(f"Carpeta '{CARPETA_DATOS}' borrada exitosamente.")
    except OSError:
        print(f"No se pudo borrar la carpeta '{CARPETA_DATOS}' porque no está vacía o no existe.")
