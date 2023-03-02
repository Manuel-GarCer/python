   
def validar_edad(edad):
    # Verificar si el valor ingresado es un número entero positivo
    if not edad.isnumeric():
        return False
    edad = int(edad)
    if edad < 1:
        return False
    return True

import datetime

# Función para validar la fecha de nacimiento
def validar_fecha_nacimiento(fecha):
    try:
        datetime.datetime.strptime(fecha, '%d/%m/%Y')
        return True
    except ValueError:
        return False

# Definición de la función para validar la cantidad
def validar_cantidad(cadena):
    try:
        cantidad = int(cadena)
        if cantidad < 0:
            raise ValueError
        return cantidad
    except ValueError:
        return None

# Definición de la función para validar el precio
def validar_precio(precio):
    # Verificar si el valor ingresado es un número entero o decimal positivo
    try:
        precio = float(precio)
    except ValueError:
        return False
    if precio < 0:
        return False
    return True
    

trabajadores = []
productos = []

while True:
    print("======================")
    print("======================")
    print("Empresa DataCorp SAC  ")
    print("======================")
    print("======================")

# Ingresamos alguna opción valida   
    while True:
        print("Opciones:")
        print("1. Sucursal HYO")
        print("2. Sucursal LIM")
        print("3. Salir")

        opcion = input("Ingrese una opción: ")

    ### INICIO DE PRIMERA PARTE

        if opcion == "1":
            print("====================================")
            print("Bienvenido a la Sucursal de Huancayo")
            while True:
                print("Opciones:")
                print("1. Registrar un trabajador")
                print("2. Mostrar lista de trabajadores")
                print("3. Salir")

                subopcion = input("Ingrese una opción: ")



                if subopcion == "1":
                    print("Ingrese los siguientes datos:")
                    nombre = input("Ingrese el nombre del trabajador: ")
                    apellido = input("Ingrese el apellido del trabajador: ")
                    edad = input("Edad: ")
                    while not validar_edad(edad):
                        print("La edad ingresada no es válida. Intente nuevamente.")
                        edad = input("Edad: ")
                    edad = int(edad)

                    fecha_nacimiento = input("Fecha de nacimiento (en formato dd/mm/yyyy): ")
                    while not validar_fecha_nacimiento(fecha_nacimiento):
                        print("La fecha ingresada no es válida. Intente nuevamente.")
                        fecha_nacimiento = input("Fecha de nacimiento (en formato dd/mm/yyyy): ")

                    nombre = nombre.capitalize()
                    apellido = apellido.capitalize()
                    # Agregar el trabajador a la lista de trabajadores
                    trabajadores.append((nombre, apellido, int(edad), fecha_nacimiento))
                    print("Trabajador registrado correctamente")

                elif subopcion == "2":
                    if len(trabajadores) == 0:
                        print("No se ha registrado ningún trabajador")
                    else:
                        print("Lista de trabajadores:")
                        for i, trabajador in enumerate(trabajadores):
                            print(f"{i+1}. {trabajador[0]} {trabajador[1]}, {trabajador[2]} años, nacido el {trabajador[3]}")
                
                elif subopcion == "3":
                    print("Salir")
                    break
                else:
                    print("Opción inválida")
                

    ### INICIO DE SEGUNDA PARTE           

        elif opcion == "2":
            print("====================================")
            print("Bienvenido a la Sucursal de Lima")
            # Agregar las opciones de la sucursal de Lima aquí
            while True:
                print("Opciones:")
                print("1. Registrar un producto")
                print("2. Mostrar lista de productos")
                print("3. Salir")

                subopcion = input("Ingrese una opción: ")

            
                if subopcion == "1":
                    print("Ingrese los siguientes datos:")
                    nombre = input("Ingrese el nombre del producto: ")
                    nombre = nombre.capitalize()
                    cantidad = input("Cantidad: ")
                    while not validar_cantidad(cantidad):
                        print("La cantidad ingresada no es válida. Intente nuevamente.")
                        cantidad = input("Cantidad: ")
                    cantidad = int(cantidad)
                    precio = input("Precio: ")
                    while not validar_precio(precio):
                        print("El precio ingresado no es válido. Intente nuevamente.")
                        precio = input("precio: ")
                    precio = float(precio)
                    productos.append((nombre, cantidad, precio))
                    print("Producto registrado correctamente")

                elif subopcion == "2":
                    if len(productos) == 0:
                        print("No se ha registrado ningún trabajador")
                    else:
                        print("Lista de productos:")
                        for i, producto in enumerate(productos):
                            print(f"{i+1}. producto: {producto[0]}, cantidad: {producto[1]}, precio: {producto[2]}")
                elif subopcion == "3":
                    print("Salir") 
                    break 
                else:
                    print("Opción inválida")
                

        elif opcion == "3":
            print("Gracias por utilizar nuestro programa. ¡Hasta pronto!")
            break

        else:
            print("Opción inválida")


