import mysql.connector

config = {
    "host": "127.0.0.1",
    "port": "3306",
    "database": "inventario",
    "user": "root",
    "password": "root3306",
}

# crear coneccion y cursor para interactuar
connection = mysql.connector.connect(**config)


cursor = connection.cursor
# ejecutar accion

cursor.execute("SELECT * FROM inventario.productos")

# almacenar los datos
result = cursor.fetchall()

for row in result:
    print(row)
cursor.close()


connection.close()
