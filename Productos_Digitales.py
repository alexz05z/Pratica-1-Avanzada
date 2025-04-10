from Productos import Productos

class ProductoDigital(Productos):
    def __init__(self, id_producto: str, nombre: str, precio: float, stock: int, formato: str, tamaño: float):
        """_summary_

        Args:
            id_producto (str): id del producto , es unico
            nombre (str): es el nombre del producto
            precio (float): es el precio del producto
            stock (int): es el stock del producto
            formato (str): es el formato del producto
            tamaño (float): es el tamaño del producto
        """
        super().__init__(id_producto, nombre, precio, stock)
        self.__formato = formato
        self.__tamaño = tamaño

    # Set y get de formato

    def get_formato(self):
        """get_formato

        Returns:
            str: devulve el formado del producto
        """
        return self.__formato
    
    def set_formato(self,formato):
        """set_formato

        Args:
            formato (str): es el formato nuevo que se le va a dar
        """
        self.__formato =formato

    # Set y get de tamaño

    def get_tamaño(self):
        """get_tamaño

        Returns:
            float: devuelve el tamaño del producto
        """
        return self.__tamaño
    
    def set_tamaño(self,tamaño):
        """set_tamaño

        Args:
            tamaño (float): es el tamaño nuevo que se le va a dar al producto
        """

        self.__tamaño = tamaño

    def __str__(self):
        """ __str__

        Returns:
            str: cadena de texto con toda la informacion del producto
        """
        return  f'ID : {self.get_id_productos()} Producto: {self.get_nombre()} Precio {self.get_precio()} Stock: {self.get_stock()} Formato {self.get_formato()} Tamaño: {self.get_tamaño()}'