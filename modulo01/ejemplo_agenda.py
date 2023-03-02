# Aplicación para simular el almacenamiento de una agenda
# Tendra opciones para hacer cada una de las operaciones


def inicio_app():
    print("===================================================")
    print("               APLICACION AGENDA                   ")
    print("===================================================")
    print("Ingrese el código de las opciones mostradas:")
    print("Opción01: Registrar agenda   (1)")
    print("Opción02: Listar agenda      (2)")
    print("Opción03: Salir              (3)")


def registrar_usuario():
    while True:
        nombre = input("Ingrese nombres y apellidos completos: ")
        if nombre != '':
            while True:
                telefono = input("Ingrese un número de teléfono o celular: ")
                if telefono != '':
                    obj = {
                        'nombre': str(nombre).title(),
                        'telefono': telefono
                        }
                    return obj
                else:
                    print("No se permiten campos vacios. Vuelva a ingresar el teléfono/celular.")
        else:
            print("No se permiten campos vacios. Vuelva a ingresar el nombre.")


list_agenda = list()
while True:
    inicio_app()
    opcion = input("Ingrese una de las opciones mostradas: ")
    if opcion == '1':
        registro = registrar_usuario()
        list_agenda.append(registro)
        print(f"Se registró correctamente la persona: {registro['nombre']} con el teléfono: {registro['telefono']}")
    elif opcion == '2':
        print("\n=========================================================")
        print("Personas registradas:")
        print("=========================================================")
        for dato in list_agenda:
            print(f"Nombre: {dato['nombre']} - Nro. Tel/Cel: {dato['telefono']}\n")
    elif opcion == '3':
        print(f"\nUsted finalizó la aplicación. Bye\n")
        break
    else:
        print(f"\nUsted ingreso una opción incorrecta. Vuelva a ingresar.\n")