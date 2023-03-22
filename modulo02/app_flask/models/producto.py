import pandas as pd  #para importar el paquete pandas y "as pd" es un alias q le ponemos

class Producto:
    def __init__(self, categoria, producto, precio, cantidad, descripcion):
        self.categoria = categoria
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion

    def crear_producto(self):  # creamos metodo crear_producto
        obj = {
            'categoria': self.categoria,
            'producto': self.producto,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'descripcion': self.descripcion
        }
        array = self.get_producto()
        array.append(obj) #al array se gregan los objetos
        df = pd.DataFrame(array)
        df.to_csv('files\producto.csv')
        return "Se registró correctamente."
    
    @staticmethod ## decorador para que no herede el self en la funcion que sigue pero si pertenece a la clase persona
    def get_producto():  # hace comunicacion entre csv y pandas
        try:
            df = pd.read_csv('files\producto.csv') #llamo a pandas y su metodo read_csv y entre (la ubicacion de archivo)
        except:
            df = pd.DataFrame() #metdo que usa pandas es DataFrame que es como tablas dinamicas
        array = list()
        for key, value in df.iterrows(): #iterrow itera en cada fila y columna del dataFrame
            #print(value)
            obj = {
                'categoria': value[1],
                'producto': value[2],
                'precio': value[3],
                'cantidad': value[4],
                'descripcion': value[5]
            }
            array.append(obj)
        return array