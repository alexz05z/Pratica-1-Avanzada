class Cliente:
    def __init__(self,id_cliente: str, nombre: str, email: str, direccion: str):
        """Funcion __init__ : Crea el objeto

        Args:
            id_cliente (str): Es el indentificador de cada cliente ; es unico para cada cliente
            nombre (str): Nombre del cliente puede ser principalmente sin apellidos pero en caso necesario se pueden meter
            email (str): Dirrecion de correo del cliente 
            direccion (str): Dirrecion del cliente
        """
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__email = email
        self.__direccion = direccion

    # Set y get de id_cliente

    def get_id_cliente(self):
        """ 
        Cliente get_id_cliente : Es para mostrar el id del cliente de forma correcta , esto es necesario ya que los atributos los tenemos en privados

        Returns:
            id_cliente (str) : Es el indentificador de cada cliente ; es unico para cada cliente
        """

        return self.__id_cliente
    
    def set_id_cliente(self,id_cliente):

        """
        Cliente set_id_cliente : Es para cambiar el id del cliente para esto se le pasa el nuevo id y lo modifica , esto es necesario ya que los atributos los tenemos en privados

        """

        self.__id_cliente = id_cliente

    # Set y get de nombre

    def get_nombre(self):

        """ 
        Cliente get_nombre : Es para mostrar el nombre del cliente de forma correcta , esto es necesario ya que los atributos los tenemos en privados

        Returns:
            nombre (str) : Nombre del cliente puede ser principalmente sin apellidos pero en caso necesario se pueden meter
        """

        return self.__nombre
    
    def set_nombre(self,nombre):

        """
        Cliente set_nombre : Es para cambiar el nombre del cliente para esto se le pasa el nuevo nombre y lo modifica , esto es necesario ya que los atributos los tenemos en privados

        """

        self.__nombre = nombre
    
    # Set y get de email

    def get_email(self):

        """ 
        Cliente get_email : Es para mostrar el correo del cliente de forma correcta , esto es necesario ya que los atributos los tenemos en privados

        Returns:
            email (str) : Dirrecion de correo del cliente
        """

        return self.__email
    
    def set_email(self,email):

        """
        Cliente set_email : Es para cambiar el correo del cliente para esto se le pasa el nuevo correo y lo modifica , esto es necesario ya que los atributos los tenemos en privados

        """

        self.__email = email

    # Set y get de direccion

    def get_direccion(self):

        """ 
        Cliente get_dirrecion : Es para mostrar la dirrecion del cliente de forma correcta , esto es necesario ya que los atributos los tenemos en privados

        Returns:
            direccion (str): Dirrecion del cliente
        """

        return self.__direccion
    
    def set_direccion(self,direccion):

        """
        Cliente set_dirrecion : Es para cambiar la dirrecion del cliente para esto se le pasa la nueva dirrecion y la modifica , esto es necesario ya que los atributos los tenemos en privados

        """

        self.__direccion = direccion

    def __str__(self):

        """__str__

        Returns:
            (str) : Muestrala la informacion del objeto de forma correcta ya que al tenerlos privados no se podrian ver 
        """

        return f' ID: {self.get_id_cliente()} \nNombre: {self.get_nombre()} \nEmail: {self.get_email()} \nDireccion: {self.get_direccion()}'