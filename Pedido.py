from Clientes import Cliente
from Productos import Productos

class Pedido :
    def __init__(self, id_pedido: str , cliente : Cliente , fecha :str):
        """__init__

        Args:
            id_pedido (str): es el id del pedido
            cliente (Cliente): es el cliente del pedido
            fecha (str): es la fecha del pedido
        """
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha 
    
    #Get y set id pedido

    def get_id_pedido(self):
        """get_id_pedido

        Returns:
            str : devuelve el id del pedido
        """
        return self.__id_pedido
    
    def set_id_pedido(self ,id_pedido) :
        """set_id_pedido

        Args:
            id_pedido (str): es el nuevo id que se le va a dar al pedido
        """
        self.__id_pedido = id_pedido

    #Get y set productos

    def get_productos(self):
        """get_productos

        Returns:
            list : devuelve los productos que tiene el pedido
        """
        return self.__productos
    
    def set_productos(self ,producto) :
        """set_productos
        Args:
            producto (objet): es el un producto que se va a añadir a la lista de productos
        """
        self.__productos.append(producto)

    #Get y set cliente

    def get_cliente(self):
        """get_cliente

        Returns:
            objet: devuelve el cliente que hizo el pedido
        """
        return self.__cliente
    
    def set_cliente(self ,cliente) :
        """set_cliente

        Args:
            cliente (objet): cambia el cliente del pedido
        """
        self.__cliente = cliente
    
    #Get y set fecha 

    def get_fecha (self):
        """get_fecha

        Returns:
            str: devuelve la fecha del pedido
        """
        return self.__fecha 
    
    def set_id_pedido(self ,fecha ) :
        """set_id_pedido

        Args:
            fecha (str): cabia la fecha del pedido
        """
        self.__fecha  = fecha 

    def agregar_producto(self, producto : Productos) :
        """agregar_producto

        Args:
            producto (Productos): Es el producto que se va a agregar
        """
        self.__productos.append(producto)
    
    def __str__(self):
        """__str__

        Returns:
            str: cadena de texto con toda la informacion del pedido
        """
        return f' -ID_Pedido: {self.__id_pedido} \n -Cliente: {self.__cliente} \n -Productos: {self.__productos} \n -Fecha: {self.__fecha}'