# Importacion de funciones
from funciones_db import *
from funciones_main import (
    db_crear_tabla_productos,
    menu_opciones,
    registrar_producto,
    mostrar_productos,
    actualizar_producto,
    eliminar_producto,
    buscar_producto,
    reporte_bajo_stock,
)


# funcion principal
def main():
    # inicializar base de datos
    db_crear_tabla_productos()


# funciones de menu
while True:
    opcion = menu_opciones()
    print("Usted selecciono: ", opcion)

    if opcion == "1":
        registrar_producto()
    elif opcion == "2":
        mostrar_productos()
    elif opcion == "3":
        actualizar_producto()
    elif opcion == "4":
        eliminar_producto()
    elif opcion == "5":
        buscar_producto()
    elif opcion == "6":
        reporte_bajo_stock()
    elif opcion == "7":
        print("Gracias por usar nuestra App")
        break
    else:
        print("Opcion no valida, por favor seleccione una opcion valida")

    continuar = input(
        "Ingrese 's' para salir o cualquier tecla para continuar: "
    ).lower()
    if continuar == "s":
        print("n\Gracias por usar nuestra App")
        break

main()
