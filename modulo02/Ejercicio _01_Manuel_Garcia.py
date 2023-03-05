# Crear una clase Auto que me permita ingresar los datos necesarios para hallar la velocidad mediante un metodo
#velocidad = d/t


#ASUNTO: Modulo02 - Ejercicio POO 01
#CORREO: itolentinos@continental.edu.pe


class Auto:
    def __init__(self, distancia, tiempo):
        self.distancia = distancia
        self.tiempo = tiempo
    
    def calcular_velocidad(self):
        velocidad = self.distancia / self.tiempo
        return f'La velocidad del auto para la distacia ({self.distancia}) entre el tiempo ({self.tiempo}) es de {velocidad} km/h'

# Crear una instancia de Auto con una distancia de 100 y un tiempo de 10
auto = Auto(100, 10)

# Calcular la velocidad
velocidad = auto.calcular_velocidad()

# Imprimir el resultado
#print("La velocidad es:", velocidad)
print(auto.calcular_velocidad())