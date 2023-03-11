cadena = "Esta es una cadena"

IP_SERVIDOR = "14.159.45"
VER_SISTEMA = "1.1.1"

def suma(num01, num02):
    return num01 + num02

def resta(num01, num02):
    return num01 - num02

def multiplicacion(num01, num02):
    return num01 * num02

def division(num01, num02):
    return num01 / num02



class Operaciom:
    def __init__(self, num01, num02):
        self.num01 = num01
        self.num02 = num02

    def suma(self):
        return self.num01 + self.num02

    def resta(self):
        return self.num01 - self.num02

    def multiplicacion(self):
        return self.num01 * self.num02

    def division(self):
        return self.num01 / self.num02

operacion = Operaciom(10, 5)
print(operacion.suma())
print(operacion.resta())
