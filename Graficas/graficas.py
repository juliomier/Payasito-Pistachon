import matplotlib.pyplot as plt
import pandas as pd
import consulta_api.consultador_api

def grafica_linea(df):
    plt.figure(figsize=(10, 5))
    plt.plot(df['Fecha'], df['Casos'], label='Casos de COVID-19', color='blue')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Casos')
    plt.title('Casos de COVID-19 a lo largo del tiempo')
    plt.legend()
    plt.grid(True)
    plt.savefig('grafica_linea.png')
    plt.show()

def grafica_barras(df):
    plt.figure(figsize=(10, 5))
    plt.bar(df['Fecha'], df['Casos'], color='green')
    plt.xlabel('Fecha')
    plt.ylabel('Número de Casos')
    plt.title('Casos de COVID-19 a lo largo del tiempo')
    plt.grid(True)
    plt.savefig('grafica_barras.png')
    plt.show()

def histograma(df):
    plt.figure(figsize=(10, 5))
    plt.hist(df['Casos'], bins=20, color='red')
    plt.xlabel('Número de Casos')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Casos de COVID-19')
    plt.grid(True)
    plt.savefig('histograma.png')
    plt.show()

def crear_graficas():
    datos = consulta_api.consultador_api.obtener_datos_covid()
    if datos:
        df = pd.DataFrame(datos['cases'].items(), columns=['Fecha', 'Casos'])
        df['Fecha'] = pd.to_datetime(df['Fecha'], format='%m/%d/%y')

        while True:
            print("Submenú de Gráficas:")
            print("1. Gráfica de Línea")
            print("2. Gráfica de Barras")
            print("3. Histograma")
            print("4. Salir")
            eleccion = input("Selecciona una opción: ").strip()

            if eleccion == '1':
                grafica_linea(df)
            elif eleccion == '2':
                grafica_barras(df)
            elif eleccion == '3':
                histograma(df)
            elif eleccion == '4':
                print("Saliendo")
                break
            else:
                print("Opción no válida")
    else:
        print("No se encontraron datos locales")

if __name__ == "__main__":
    crear_graficas()
