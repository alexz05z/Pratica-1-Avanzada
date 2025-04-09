#Importaciones

from Productos import Productos
from Clientes import Cliente
from Productos_Digitales import ProductoDigital
from Pedido import Pedido
from reseña import Reseña
import os

#Variables
productos = []
clientes = {}
pedidos = []
reseñas = []

#Producto
pro1 = Productos("P000", "0", 0.0, 0)
productos.append(pro1)

pro1 = Productos("P001", "Disco", 120.25, 20)
productos.append(pro1)

pro1 = Productos("P002", "Portatil", 250.50, 8)
productos.append(pro1)


#Cliente
cli1 = Cliente("C000", "0", "0", "0")
clientes[cli1.get_id_cliente()]=cli1

cli1 = Cliente("C001", "Jose", "prueba@correo.com", "Adra")
clientes[cli1.get_id_cliente()]=cli1

cli1 = Cliente("C002", "Juan", "prueba3@correo.com", "Balanegra")
clientes[cli1.get_id_cliente()]=cli1

#Producto digital
prodi1 = ProductoDigital("P003", "juego" ,60.0 ,7,"juego" , 500.0)
productos.append(prodi1)

#Pedido
pedido = Pedido("PED000" , clientes["C000"] , "0")
pedido.agregar_producto(productos[0])
pedidos.append(pedido)

pedido = Pedido("PED001" , clientes["C001"] , "14-02-2025")
pedido.agregar_producto(productos[1])
pedidos.append(pedido)

#Resaña

reseña = Reseña("R000" , productos[0] , clientes["C000"] , "0" , 0)
reseñas.append(reseña)

#Menu

def menu():

    verdad = True # Varibla para manejar el bucle del menu

    while verdad:
        print("Menu")
        print()
        print("1. Gestionar productos")
        print("2. Gestionar clientes")
        print("3. Gestionar pedidos")
        print("4. Gestionar reseñas")
        print("5. Salir")
        print()
        opcion = input("Elige una opcion: ")

        #Print para ver el menu con un input para pedir la opcion

        if opcion == "1":

            #Menu productos

            print("Que quieres hacer")
            print("1. Añadir producto")
            print("2. Listar productos")
            print("3. Actualizar stock")
            print()
            opcion1 = input("Introduce opcion: ")

            #Print para ver el menu con un input para pedir la opcion

            if opcion1 == "1" :

                print("Es Fisico (F) o Digital (D) el producto")
                opcion1_2 = input("Introduce F o D: ")
                opcion1_2 = opcion1_2.lower()

                #Pregunta para saber si es fisico o digital

                if opcion1_2 == "f":

                    productof = ""

                    for i in productos :
                        idef = i.get_id_productos()

                    numero = int(idef[1:])
                    
                    numero = str(numero + 1)

                    if len(numero) == 1 :
                        idef = "P" + "0" +"0" + numero
                    
                    elif len(numero) == 2 :
                        idef = "P" + "0"+ numero
                    
                    elif len(numero) == 3 :
                        idef = "P" + numero

                    #Generacion automatica del ID

                    nom = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio del producto: "))
                    stock = int(input("Introduce el stock del producto: "))

                    productof = Productos(idef,nom,precio,stock) #Crea el objejo

                    productos.append(productof) #Añade el producto a la lista de productos

                    input("pulsa para continuar") #Pausa con limpiador de pantalla
                    os.system("clear")
                
                elif opcion1_2 == "d" :

                    productod = ""


                    for i in productos :
                        ided = i.get_id_productos()

                    numero = int(ided[1:])
                    
                    numero = str(numero + 1)

                    if len(numero) == 1 :
                        ided = "P" + "0" +"0" + numero
                    
                    elif len(numero) == 2 :
                        ided = "P" + "0"+ numero
                    
                    elif len(numero) == 3 :
                        ided = "P" + numero

                    #Generacion automatica del ID

                    nom = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio del producto: "))
                    stock = int(input("Introduce el stock del producto: "))
                    form = input("Introduce el formato: ")
                    tamaño = input("Introduce el tamaño: ")

                    productod = ProductoDigital(ided,nom,precio,stock,form,tamaño) #Crea el objejo
                    productos.append(productod) #Añade el producto a la lista de productos
                    
                    input("pulsa para continuar") #Pausa con limpiador de pantalla
                    os.system("clear")
                    
                else : 
                    print("Esa opcion no existe")

            elif opcion1 == "2" :
                #Lista los productos

                for i in productos:
                    print(i)

                input("pulsa para continuar")  #Pausa con limpiador de pantalla
                os.system("clear")

            elif opcion1 == "3" :
                #Cambia el stock de un producto
                pregunta = input("Pon el id del producto que quieres cambiar su stock: ")

                for i in productos :

                    if pregunta == i.get_id_productos(): #Busca el producto que el usuario quiere
                        stock = int(input("Introduce el stock que quieres poner: "))  #Le pide al usuario el nuevo stock
                        i.set_stock(stock)      

                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")

            else : 
                print("Esa opcion no esta ")

        elif opcion == "2":

            #Menu clientes

            print("Que quieres hacer")
            print("1. Añadir cliente")
            print("2. Listar clientes")
            print()
            opcion2 = input("Introduce opcion: ")

            #Print para ver el menu con un input para pedir la opcion

            if opcion2 == "1" :               

                for i in clientes.values() :
                        idc = i.get_id_cliente()

                numero = int(idc[1:])
                    
                numero = str(numero + 1)

                if len(numero) == 1 :
                    idc = "C" + "0" +"0" + numero
                    
                elif len(numero) == 2 :
                    idc = "C" + "0"+ numero
                    
                elif len(numero) == 3 :
                    idc = "C" + numero

                #Generacion automatica del ID

                nom = input("Introduce nombre del cliente: ")
                corr = input("Introduce correo@ del cliente: ")
                ubi = input("Introduce la ubicacion del cliente: ")

                clie1 = Cliente(idc,nom,corr,ubi)
                clientes[clie1.get_id_cliente()]=clie1


                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")
            
            elif opcion2 == "2":

                for id , cliente in clientes.items():
                    print(f' \n-Id del cliente : {id} \n\n-Informacion del cliente: \n -Nombre cliente: {cliente.get_nombre()} \n -Email: {cliente.get_email()} \n -Direccion: {cliente.get_direccion()}')

                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")
                

            
            else : 
                print("Esa opcion no existe")

        elif opcion == "3":

            #Menu pedido

            print("Que quieres hacer")
            print("1. Crear pedido")
            print("2. Listar pedidos")
            print("3. Calcular total")
            print("4. Añadir producto")
            print()
            opcion3 = input("Introduce opcion: ")

            #Print para ver el menu con un input para pedir la opcion


            if opcion3 == "1" :

                pedido = ""

                for i in pedidos :
                        id_pedido = i.get_id_pedido()

                numero = int(id_pedido[3:])
                    
                numero = str(numero + 1)

                if len(numero) == 1 :
                    id_pedido = "PED" + "0" +"0" + numero
                    
                elif len(numero) == 2 :
                    id_pedido = "PED" + "0"+ numero
                    
                elif len(numero) == 3 :
                    id_pedido = "PED" + numero

                #Generacion automatica del ID

                cliente = input("Introduce el id del cliente: ")
                fecha = input("Introduce la fecha: ")

                pedido = Pedido(id_pedido , clientes[cliente] , fecha)
                pedidos.append(pedido)

                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")

            elif opcion3 == "2" :

                for i in pedidos : #Listar los pedidos
                    print(i)
                
                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")

            elif opcion3 == "3" :

                #Calcular total

                entra = False

                id_pedido = input("Introduce el id del pedido PED###: ")

                for i in pedidos:

                    if id_pedido == i.get_id_pedido():
                       entra = True
                       valor_total = 0
                       for j in i.get_productos():
                            if j == "" :

                                pass
                            else :
                                valor_total = valor_total + j.get_precio()

                #Hace comprobaciones para ver si ese id del pedido existe y luego va comprando si tiene productos si tienes los va sumando al total el total empieza en cero
                
                if entra :
                    print (f'El valor total del pedido es {valor_total}')
                
                else :
                    print("Ese id de pedido no existe pruebe otra vez")

                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")

            elif opcion3 == "4" :

                id_producto = input("Introduce el id del producto que vas a añadir (P###)")
                id_pedido = input("Introduce el id del pedido (PED###): ")

                comprobacion = True
                comprobacion1 = True
                comprobacion2 =  False

                #Variables de comprobacion incializadas

                for i in pedidos:
                    if id_pedido == i.get_id_pedido():

                        comprobacion = False

                        for j in productos :
                            if id_producto == j.get_id_productos() :

                                comprobacion1 = False
                                
                                for h in i.get_productos():
                                    if h.get_id_producto == id_producto :

                                        comprobacion2 = True
                            
                                if comprobacion2 :
                                    print("No se puede añadir ese producto porque ya lo tienes en el pedido")
                                else :
                                    i.agregar_producto(j)

                        if comprobacion1:
                            print("Ese id de producto no existe")

                if comprobacion:
                    print("Ese id de pedido no existe")

                #Comprobacion para en caso de que el id de pedido dado no exista te imprima que no existe si existe al cambiar el valor a False y no entra
                #Comprobacion1 para en caso de que el id de producto dado no exista te imprima que no existe si existe al cambiar el valor a False y no entra
                #Comprobacion2 comprueba en el pedido dado que no exista ese producto si existe te dice que ya esta si no esta lo añade
                
                input("pulsa para continuar") #Pausa con limpiador de pantalla
                os.system("clear")

            else :
                print("Esa opcion no existe")

               
            
        elif opcion == "4":

            #Menu Reseñas

            print("Que quieres hacer")
            print("1. Añadir reseña")
            print("2. Listar reseñas")
            print()
            opcion4 = input("Introduce opcion: ")

            #Print para ver el menu con un input para pedir la opcion

            if opcion4 == "1":

                #Crea la reseñas
                
                reseña = ""

                for i in reseñas :
                        id_reseña = i.get_id_reseña()

                numero = int(id_reseña[3:])
                    
                numero = str(numero + 1)

                if len(numero) == 1 :
                    id_reseña = "R" + "0" +"0" + numero
                    
                elif len(numero) == 2 :
                    id_reseña = "R" + "0"+ numero
                    
                elif len(numero) == 3 :
                    id_reseña = "R" + numero

                #Generacion automatica del ID

                id_producto = input("Introduce el id del producto: ")
                id_cliente = input("Introduce el id del cliente: ")
                comentario = input("Introduce el comentario: ")
                puntacion = input("Introduce la puntuacion ")

                producto = ""

                comprobacion3 = False

                for i in productos : #Busca el producto
                    if id_producto == i.get_id_productos() : 
                        producto = i

                for j in clientes.keys() : #Comprueba el cliente
                    if j == id_cliente:
                        comprobacion3 = True
                
                if producto != "" and comprobacion3 :  #Comprueba que el cliente y el producto estan        
                    reseña = Reseña(id_reseña , producto , clientes[id_cliente] , comentario , puntacion) #Crea el objeto
                    reseñas.append(reseña)  #Añade la reseña a la lista resñas

            elif opcion4 == "2":

                #Lista las reseñas

                for i in reseñas:   #Recore la lista e mostrandola por pantaña
                    print(i)

            else : 
                print("Esa opcion no existe")

        elif opcion == "5":
            verdad =False

        else :
            print("Esa opcion no esta en el menu")  

menu()