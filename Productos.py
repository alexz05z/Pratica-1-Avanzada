class Productos :
    def __init__(self ,id_producto :str , nombre : str , precio : float , stock :int):
        self.__id_productos = id_producto
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def __str__(self):
        pass

    #Get y set  id_productos

    def get_id_productos(self):
        return self.__id_productos

    def set_id_productos(self , id_producto) :
        self.__id_productos = id_producto
    
    #Get y set  nombre

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self , nombre ) :
        self.__nombre = nombre
    
    #Get y set  precio

    def get_precio(self):
        return self.__precio

    def set_precio(self , precio) :
        self.__precio = precio
    
    #Get y set  id_productos

    def get_stock(self):
        return self.__stock

    def set_stock(self , stock) :
        self.__stock = stock

    def __str__(self):
        return f'-Nombre: {self.__nombre} \n -ID: {self.__id_productos} \n -Precio: {self.__precio} \n -Stock: {self.__stock}'