import pandas as pd 

class Persona:
    def __init__(self, nombre, apellido, genero):
        self.nombre = nombre
        self.apellido = apellido
        self.genero = genero

    def crear_persona(self):
        obj = {
            'nombre': self.nombre,
            'apellido': self.apellido,
            'genero': self.genero
        }
        array = self.get_persona()
        array.append(obj)
        df = pd.DataFrame(array)
        df.to_csv('files\persona.csv')
        return "Se registró correctamente."
    
    @staticmethod
    def get_persona():
        try:
            df = pd.read_csv('files\persona.csv')
        except:
            df = pd.DataFrame()
        array = list()
        for key, value in df.iterrows():
            #print(value)
            obj = {
                'nombre': value[1],
                'apellido': value[2],
                'genero': value[3]
            }
            array.append(obj)
        return array