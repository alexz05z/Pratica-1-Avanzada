from Clientes import Cliente
from Productos import Productos

class Pedido :
    def __init__(self, id_pedido: str , cliente : Cliente , fecha :str):
        self.__id_pedido = id_pedido
        self.__cliente = cliente
        self.__productos = []
        self.__fecha = fecha 
    
    #Get y set id pedido

    def get_id_pedido(self):
        return self.__id_pedido
    
    def set_id_pedido(self ,id_pedido) :
        self.__id_pedido = id_pedido

    #Get y set productos

    def get_productos(self):
        return self.__productos
    
    def set_productos(self ,producto) :
        self.__productos.append(producto)

    #Get y set cliente

    def get_cliente(self):
        return self.__cliente
    
    def set_cliente(self ,cliente) :
        self.__cliente = cliente
    
    #Get y set fecha 

    def get_fecha (self):
        return self.__fecha 
    
    def set_id_pedido(self ,fecha ) :
        self.__fecha  = fecha 

    def agregar_producto(self, producto : Productos) :
        self.__productos.append(producto)
    
    def __str__(self):
        return f' -ID_Pedido: {self.__id_pedido} \n -Cliente: {self.__cliente} \n -Productos: {self.__productos} \n -Fecha: {self.__fecha}'