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

    # Métodos Get y Set para el atributo id_producto
    def get_id_productos(self):
        """get_id_productos

        Returns:
            str: devueve el id producto
        """
        return self.__id_productos  # Devuelve el id del producto

    def set_id_productos(self , id_producto):
        """set_id_productos

        Args:
            id_producto (str): es el id del producto que se le pasa para que modifique el parametro
        """
        self.__id_productos = id_producto  # Modifica el id del producto

    # Métodos Get y Set para el atributo nombre
    def get_nombre(self):
        """get_nombre

        Returns:
            str: devuelve el nombre del producto
        """
        return self.__nombre  # Devuelve el nombre del producto

    def set_nombre(self , nombre):
        """set_nombre

        Args:
            nombre (str): es el nombre del producto que se le pasa para que modifique el parametro
        """
        self.__nombre = nombre  # Modifica el nombre del producto

    # Métodos Get y Set para el atributo precio
    def get_precio(self):
        """get_precio

        Returns:
            float: devuelve el precio del producto
        """
        return self.__precio  # Devuelve el precio del producto

    def set_precio(self , precio):
        """set_precio

        Args:
            precio (float): es el precio del producto que se le pasa para cambiarlo
        """
        self.__precio = precio  # Modifica el precio del producto

    # Métodos Get y Set para el atributo stock
    def get_stock(self):
        """get_stock

        Returns:
            int: devuelve el stock del producto
        """
        return self.__stock  # Devuelve el stock del producto

    def set_stock(self , stock):
        """set_stock

        Args:
            stock (int): es el stock del producto que se le pasa para que modifique el parametro
        """
        self.__stock = stock  # Modifica el stock del producto

    def __str__(self):
        """ __str__

        Returns:
            str: cadena de texto con toda la informacion del producto
        """
        # Este método retorna una cadena de texto con la información del producto
        return f'-Nombre: {self.__nombre} \n -ID: {self.__id_productos} \n -Precio: {self.__precio} \n -Stock: {self.__stock}'
