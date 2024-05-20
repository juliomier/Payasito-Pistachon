import consulta_api.consultador_api
import datos.borrar_datos
import datos.estadisticas
import Graficas.graficas

def consultar_web():
    while True:
        print("Menú:")
        print("1. Mostrar datos por fecha")
        print("2. Mostrar todos los datos")
        print("3. Consultar por estado")
        print("4. Consultar por continente")
        print("5. Consultar por país")
        print("6. Salir")
        eleccion = input("Selecciona una opción: ").strip()

        if eleccion == '1':
            consulta_api.consultador_api.obtener_y_mostrar_datos_por_fecha()
        elif eleccion == '2':
            datos = consulta_api.consultador_api.obtener_datos_covid()
            if datos:
                consulta_api.consultador_api.mostrar_todos_los_datos(datos)
            else:
                print("No se encontraron datos locales.")
        elif eleccion == '3':
            estado = input("Introduce el nombre del estado (en inglés): ").strip()
            consulta_api.consultador_api.obtener_datos_por_estado(estado)
        elif eleccion == '4':
            continente = input("Introduce el nombre del continente: ").strip()
            consulta_api.consultador_api.obtener_datos_por_continente(continente)
        elif eleccion == '5':
            pais = input("Introduce el nombre del país: ").strip()
            consulta_api.consultador_api.obtener_datos_por_pais(pais)
        elif eleccion == '6':
            print("Saliendo del submenú...")
            break
        else:
            print("Opción no válida.")

def consultar_registros():
    datos = consulta_api.consultador_api.cargar_datos_locales()
    if datos:
        consulta_api.consultador_api.mostrar_todos_los_datos(datos)
    else:
        print("No hay registros.")

def estadisticas_covid():
    datos.estadisticas.mostrar_estadisticas()

def graficas_covid():
    Graficas.graficas.crear_graficas()

def borrar_todo():
    datos.borrar_datos.borrar_archivos()
    print("Registros borrados")

def main():
    while True:
        print("Menú:")
        print("1. Consultar web")
        print("2. Consultar registros")
        print("3. Estadísticas")
        print("4. Gráficas")
        print("5. Borrar todo")
        print("6. Salir")
        opcion = input("Selecciona una opción: ").strip()
        
        if opcion == '1':
            consultar_web()
        elif opcion == '2':
            consultar_registros()
        elif opcion == '3':
            estadisticas_covid()
        elif opcion == '4':
            graficas_covid()
        elif opcion == '5':
            borrar_todo()
        elif opcion == '6':
            print("Saliendo...")
            break
        else:
            print("Opción no válida")

if __name__ == "__main__":
    main()
