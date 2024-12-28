# validacion de registro


def validacion_nombre():
    while True:
        nombre = input("Nombre: ").strip()  # elimina espacios
        if nombre:
            break
        else:
            print("No se admite dato nulo. Ingrese el nombre: ")  # NOT NULL
    return nombre


def validacion_descripcion():
    descripcion = input("Descripción: ").strip()
    return descripcion


def validacion_categoria():
    while True:
        categoria = input("Varietal: ").strip()
        if not categoria:
            print("No se admite dato nulo. Ingrese el varietal: ")  # NOT NULL
        else:
            return categoria


# Validar cantidad
def validacion_cantidad(mensaje="Cantidad: "):
    while True:
        try:
            cantidad = int(input(f"{mensaje} ").strip())
            if not cantidad:
                print("No se admite dato nulo. Ingrese la cantidad: ")  # NOT NULL
            elif cantidad <= 0:
                print("La cantidad debe ser mayor a 0. Ingrese la cantidad: ")
            else:
                return cantidad

        except ValueError:
            print("Tipo de dato no valido. Ingrese la cantidad: ")


# Validar el precio
def validacion_precio():
    while True:
        try:
            precio = float(input("Precio: ").strip())
            if not precio:
                print("No se admite dato nulo. Ingrese el precio: ")
            else:
                return precio

        except ValueError:
            print("Tipo de dato no valido. Ingrese el precio: ")
