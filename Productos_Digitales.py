from Productos import Productos

class ProductoDigital(Productos):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamaño: float):
        super().__init__(id_producto, nombre, precio, stock)
        self.__formato = formato
        self.__tamaño = tamaño

    # Set y get de formato

    def get_formato(self):
        return self.__formato
    
    def set_formato(self,formato):
        self.__formato =formato

    # Set y get de tamaño

    def get_tamaño(self):
        return self.__tamaño
    
    def set_tamaño(self,tamaño):
        self.__tamaño = tamaño

    def __str__(self):
        return  f'ID : {self.get_id_productos()} Producto: {self.get_nombre()} Precio {self.get_precio()} Stock: {self.get_stock()} Formato {self.get_formato()} Tamaño: {self.get_tamaño()}'