import pandas as pd 

class Producto:
    def __init__(self, categoria, producto, precio, cantidad, descripcion):
        self.categoria = categoria
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad
        self.descripcion = descripcion

    def crear_producto(self):
        obj = {
            'categoria': self.categoria,
            'producto': self.producto,
            'precio': self.precio,
            'cantidad': self.cantidad,
            'descripcion': self.descripcion
        }
        array = self.get_producto()
        array.append(obj)
        df = pd.DataFrame(array)
        df.to_csv('files\producto.csv')
        return "Se registró correctamente."
    
    @staticmethod
    def get_producto():
        try:
            df = pd.read_csv('files\producto.csv')
        except:
            df = pd.DataFrame()
        array = list()
        for key, value in df.iterrows():
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