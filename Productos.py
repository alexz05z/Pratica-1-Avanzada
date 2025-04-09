class Productos :
    def __init__(self ,id_producto :str , nombre : str , precio : float , stock :int):
        """Funcion __init__ : Crea el objeto

        Args:
            id_producto (str):Id del producto es unica
            nombre (str): nombre del producto
            precio (float): precio del producto
            stock (int): stock del producto
        """
        self.__id_productos = id_producto  # Aquí se inicializa el id del producto
        self.__nombre = nombre            # Aquí se inicializa el nombre del producto
        self.__precio = precio            # Aquí se inicializa el precio del producto
        self.__stock = stock              # Aquí se inicializa la cantidad disponible de stock

    def __str__(self):
        pass  # Método que se utiliza para representar el objeto como un string. Aquí no está implementado, pero generalmente se usa para mostrar una descripción de la instancia del objeto.

    # Métodos Get y Set para el atributo id_producto
    def get_id_productos(self):
        return self.__id_productos  # Devuelve el id del producto

    def set_id_productos(self , id_producto):
        self.__id_productos = id_producto  # Modifica el id del producto

    # Métodos Get y Set para el atributo nombre
    def get_nombre(self):
        return self.__nombre  # Devuelve el nombre del producto

    def set_nombre(self , nombre):
        self.__nombre = nombre  # Modifica el nombre del producto

    # Métodos Get y Set para el atributo precio
    def get_precio(self):
        return self.__precio  # Devuelve el precio del producto

    def set_precio(self , precio):
        self.__precio = precio  # Modifica el precio del producto

    # Métodos Get y Set para el atributo stock
    def get_stock(self):
        return self.__stock  # Devuelve el stock del producto

    def set_stock(self , stock):
        self.__stock = stock  # Modifica el stock del producto

    # Este método debería devolver una representación del objeto como un string.
    # Sin embargo, el método no está implementado correctamente. Aquí está la implementación que debería tener:
    def __str__(self):
        # Este método retorna una cadena de texto con la información del producto
        return f'-Nombre: {self.__nombre} \n -ID: {self.__id_productos} \n -Precio: {self.__precio} \n -Stock: {self.__stock}'
