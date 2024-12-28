from funciones_db import *
from funciones_validacion import *


def menu_opciones():
    print("-" * 30)
    print(" MENU PRINCIPAL ")
    print("-" * 30)
    print(
        """
          1. Agregar producto
          2. Mostrar producto
          3. Actualizar
          4. Eliminar
          5. Buscar producto
          6. Reporte bajo Stock
          7. Salir
        """
    )
    opcion = input("Ingrese la opción deseada: ")
    return opcion


def registrar_producto():
    print("\nIngrese los siguientes datos del producto:")
    nombre = validacion_nombre()
    descripcion = validacion_cantidad()
    categoria = validacion_categoria()
    cantidad = validacion_cantidad()
    precio = validacion_precio()

    # Diccionario
    producto = {
        "nombre": nombre,
        "descripcion": descripcion,
        "cateroria": categoria,
        "cantidad": cantidad,
        "precio": precio,
    }

    db_registrar_producto(producto)
    print("Registro insertado exitosamente!")


def mostrar_productos():
    lista_productos = db_mostrar_productos()

    if lista_productos:
        for producto in lista_productos:
            print(producto)
    else:
        print("No hay productos que mostrar")


def actualizar_producto():
    idproductos = int(input("\nIngrese el id del producto a actualizar"))
    get_producto = db_actualizar_producto(idproductos)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(f"Cantidad actual {get_producto[4]} ")
        nueva_cantidad = validacion_cantidad("Nueva cantidad")
        db_actualizar_producto(idproductos, nueva_cantidad)
        print("Registro actualizado exitosamente!")


def eliminar_producto():
    idproductos = int(input("\nIngrese el id del producto a eliminar: "))
    get_producto = db_eliminar_producto(idproductos)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print("\nATENCION: se eliminará el siguiente registro:")
        print(get_producto)
        confirmacion = input(
            "\nIngrese 's' para confirmar o cualquier otro para cancelar: "
        ).lower()
        if confirmacion == "s":
            db_eliminar_producto(id)
            print("Registro eliminado exitosamente!")
        else:
            print("Operación cancelada.")


def buscar_producto():
    idproductos = int(input("\nIngrese el id del producto que desea consultar: "))
    get_producto = db_buscar_producto(idproductos)
    if not get_producto:
        print("ERROR: no se ha encontrado ningún producto con el id {id}")
    else:
        print(get_producto)


def reporte_bajo_stock():
    minimo_stock = int(input("\nIngrese el unmbral de mínimo stock:"))
    lista_productos = db_reporte_bajo_stock(minimo_stock)
    if not lista_productos:
        print("No se ha encontrado ningún producto con stock menor a {minimo_stock}")
    else:
        for producto in lista_productos:
            print(producto)
