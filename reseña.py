from Productos import Productos
from Clientes import Cliente

class Reseña (Productos , Cliente) :

    def __init__(self, id_reseña : str , producto : Productos , cliente : Cliente , comentario :str , puntuacion : int ):
        """_summary_

        Args:
            id_reseña (str): es el identificador de la reseña, es unico para cada una
            producto (Productos): es el producto al cual se le esta haciendo la reseña
            cliente (Cliente): es el cliente el cual esta haciendo la reseña
            comentario (str): 
            puntuacion (int): _description_
        """
        

        Productos.__init__(self , producto.get_id_productos() , producto.get_nombre(), producto.get_precio(), producto.get_stock )

        Cliente.__init__(self,cliente.get_id_cliente(), cliente.get_nombre(), cliente.get_email(), cliente.get_direccion())

        self.__id_reseña = id_reseña
        self.__comentario = comentario
        self.__puntuacion = puntuacion

    #Get y set de id reseña

    def get_id_reseña(self):
        return self.__id_reseña

    def set_id_reseña(self , id_reseña):
        self.__id_reseña = id_reseña
    
    #Get y set de comentario

    def get_comentario(self):
        return self.__comentario

    def set_comentario(self , comentario):
        self.__comentario = comentario
    
    #Get y set de puntuacion

    def get_puntuacion(self):
        return self.__puntuacion

    def set_puntuacion(self , puntuacion):
        self.__puntuacion = puntuacion
    
    def __str__(self):
        return f'ID: {self.get_id_reseña()} Producto: {self.get_id_productos()} Cliente: {self.get_id_cliente()} Comentario: {self.get_comentario()} Puntuacion: {self.get_puntuacion()}'