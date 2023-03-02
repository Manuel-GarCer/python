# Aplicación para hacer operaciones matemáticas
# Tendra opciones para hacer cada una de las operaciones

def inicio_app():
    print("===================================================")
    print("               APLICACION CALCULADORA              ")
    print("===================================================")
    print("Ingrese el código de las opciones mostradas:")
    print("Opción01: Sumar       (1)")
    print("Opción02: Restar      (2)")
    print("Opción03: Multiplicar (3)")
    print("Opción04: Salir       (0)")


def validar_decimal(num):
    contador = str(num).count('.')
    if contador <= 1:
        return True
    else:
        return False


def validar_numero(posicion):
    while True:
        num01 = input(f"Ingrese el {posicion} número: ")
        if str(str(num01).replace('.', '')).isnumeric() and validar_decimal(num01):
            return float(num01)
        else:
            print("El dato ingresado es incorrecto, vuelva a escribir un valor numérico.")


def operacion_matematica(operador):
    num01 = validar_numero('primer')
    num02 = validar_numero('segundo')
    if operador == '+':
        return (num01) + (num02)
    elif operador == '-':
        return (num01) - (num02)
    elif operador == '*':
        return (num01) * (num02)
    else:
        print("El operador ingresado es incorrecto.")


while True:
    inicio_app()
    opcion = input("Ingrese una de las opciones mostradas: ")
    if opcion == '1':
        resultado = operacion_matematica('+')
        print(f"El resultado de la suma es: {resultado}")
    elif opcion == '2':
        resultado = operacion_matematica("-")
        print(f"El resultado de la resta es: {resultado}")
    elif opcion == '3':
        resultado = operacion_matematica("*")
        print(f"El resultado de la multiplicación es: {resultado}")
    elif opcion == '0':
        print(f"\nUsted finalizó la aplicación. Bye\n")
        break
    else:
        print(f"\nUsted ingreso una opción incorrecta. Vuelva a ingresar.\n")
    