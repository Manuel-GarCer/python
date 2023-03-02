
agenda = []

while True:
    
    print("1. Registrar contacto")
    print("2. Listar contactos")
    print("3. Salir")
    opcion = input()

    if opcion == "1":
        nombre = input("Ingrese el nombre del contacto: ")
        while nombre == "" or nombre[0].islower() or not nombre.isalpha():
            nombre = input("Nombre inválido. Ingrese nuevamente el nombre del contacto: ")
        nombre = nombre.capitalize()

        direccion = input("Ingrese la dirección del contacto: ")
        while direccion == "" or direccion[0].islower():
            direccion = input("Dirección inválida. Ingrese nuevamente la dirección del contacto: ")
        direccion = direccion.capitalize()

        telefono = input("Ingrese el número de teléfono o celular del contacto: ")
        while not telefono.isdigit():
            telefono = input("Número inválido. Ingrese nuevamente el número de teléfono o celular del contacto: ")

        contacto = {"nombre": nombre, "direccion": direccion, "telefono": telefono}
        agenda.append(contacto)
        print("Contacto registrado con éxito.\n")

    elif opcion == "2":
        if len(agenda) == 0:
            print("No hay contactos registrados.\n")
        else:
            print("Lista de contactos:")
            for contacto in agenda:
                print(f"Nombre: {contacto['nombre']}")
                print(f"Dirección: {contacto['direccion']}")
                print(f"Teléfono: {contacto['telefono']}\n")
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción inválida. Por favor seleccione una opción válida.\n")
