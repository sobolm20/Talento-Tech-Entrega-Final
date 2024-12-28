import mysql.connector
from core import config


def db_crear_tabla_productos():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar accion
    query = """CREATE TABLE IF NOT EXISTS productos (
    idproductos int PRIMARY,
    nombre varchar(45) NOT NULL, 
    descripcion varchar(100), 
    categoria varchar(30) NOT NULL, 
    cantidad int NOT NULL, 
    precio decimal(2,0) NOT NULL)
    """
    cursor.execute(query)

    # almacenar los datos
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


db_crear_tabla_productos()


def db_registrar_producto(producto):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar accion
    query = (
        "INSERT INTO productos (nombre, descripcion, categoria, cantidad, precio) VALUES (?, ?, ?, ?, ?)",
        (
            producto["nombre"],
            producto["descripcion"],
            producto["categoria"],
            producto["cantidad"],
            producto["precio"],
        ),
    )

    cursor.execute(query)

    # almacenar los datos
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


db_registrar_producto()


def db_mostrar_productos():
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar consulta
    query = "SELECT * FROM productos"
    cursor.execute(query)

    # almacenar los datos
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


db_mostrar_productos()


def db_actualizar_producto(nueva_cantidad, idproductos):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar accion
    query = "UPDATE productos SET cantidad = ? WHERE idproductos = ?"
    placeholders = (nueva_cantidad, idproductos)
    cursor.execute(query, placeholders)

    # almacenar los datos
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


db_actualizar_producto()


def db_eliminar_producto(idproductos):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar accion
    query = "DELETE FROM productos WHERE idproductos = ?"
    placeholders = idproductos
    cursor.execute(query, placeholders)

    cursor.close()
    connection.close()


db_eliminar_producto()


def db_buscar_producto(idproductos):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar consulta
    query = "SELECT * FROM productos WHERE idproductos = ?"
    placeholders = idproductos
    cursor.execute(query, placeholders)

    # almacenar dato
    producto = cursor.fetchone()

    cursor.close()
    connection.close()
    return producto


db_buscar_producto()


def db_reporte_bajo_stock(minimo_stock):
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor

    # ejecutar consulta
    query = "SELECT * FROM productos WHERE cantidad < ?"
    placeholders = minimo_stock
    cursor.execute(query, placeholders)

    # almacenar los datos
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    connection.close()


db_reporte_bajo_stock()
