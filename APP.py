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

reseña = Reseña("R000" , productos[0] , clientes["C000"] , "0" , 0)
reseñas.append(reseña)

def menu():

    verdad = True

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

        if opcion == "1":

            print("Que quieres hacer")
            print("1. Añadir producto")
            print("2. Listar productos")
            print("3. Actualizar stock")
            print()
            opcion1 = input("Introduce opcion: ")

            if opcion1 == "1" :

                print("Es Fisico (F) o Digital (D) el producto")
                opcion1_2 = input("Introduce F o D: ")
                opcion1_2 = opcion1_2.lower()

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

                    nom = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio del producto: "))
                    stock = int(input("Introduce el stock del producto: "))

                    productof = Productos(idef,nom,precio,stock)

                    productos.append(productof)

                    input("pulsa para continuar")
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

                    nom = input("Introduce el nombre del producto: ")
                    precio = float(input("Introduce el precio del producto: "))
                    stock = int(input("Introduce el stock del producto: "))
                    form = input("Introduce el formato: ")
                    tamaño = input("Introduce el tamaño: ")

                    productod = ProductoDigital(ided,nom,precio,stock,form,tamaño)
                    productos.append(productod)
                    
                    input("pulsa para continuar")
                    os.system("clear")
                    
                else : 
                    print("Esa opcion no existe")

            elif opcion1 == "2" :

                for i in productos:
                    print(i)

                input("pulsa para continuar")
                os.system("clear")

            elif opcion1 == "3" :

                pregunta = input("Pon el id del producto que quieres cambiar su stock: ")

                for i in productos :

                    if pregunta == i.get_id_productos():
                        stock = int(input("Introduce el stock que quieres poner: ")) 
                        i.set_stock(stock)   

                input("pulsa para continuar")
                os.system("clear")

            else : 
                print("Esa opcion no esta ")

        elif opcion == "2":

            print("Que quieres hacer")
            print("1. Añadir cliente")
            print("2. Listar clientes")
            print()
            opcion2 = input("Introduce opcion: ")

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

                nom = input("Introduce nombre del cliente: ")
                corr = input("Introduce correo@ del cliente: ")
                ubi = input("Introduce la ubicacion del cliente: ")

                clie1 = Cliente(idc,nom,corr,ubi)
                clientes[clie1.get_id_cliente()]=clie1


                input("pulsa para continuar")
                os.system("clear")
            
            elif opcion2 == "2":

                for id , cliente in clientes.items():
                    print(f' \n-Id del cliente : {id} \n\n-Informacion del cliente: \n -Nombre cliente: {cliente.get_nombre()} \n -Email: {cliente.get_email()} \n -Direccion: {cliente.get_direccion()}')

                input("pulsa para continuar")
                os.system("clear")
                

            
            else : 
                print("Esa opcion no existe")

        elif opcion == "3":

            print("Que quieres hacer")
            print("1. Crear pedido")
            print("2. Listar pedidos")
            print("3. Calcular total")
            print("4. Añadir producto")
            print()
            opcion3 = input("Introduce opcion: ")

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

                cliente = input("Introduce el id del cliente: ")
                fecha = input("Introduce la fecha: ")

                pedido = Pedido(id_pedido , clientes[cliente] , fecha)
                pedidos.append(pedido)

                input("pulsa para continuar")
                os.system("clear")

            elif opcion3 == "2" :

                for i in pedidos :
                    print(i)
                
                input("pulsa para continuar")
                os.system("clear")

            elif opcion3 == "3" :

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
                if entra :
                    print (f'El valor total del pedido es {valor_total}')
                
                else :
                    print("Ese id de pedido no existe pruebe otra vez")
                input("pulsa para continuar")
                os.system("clear")

            elif opcion3 == "4" :

                id_producto = input("Introduce el id del producto que vas a añadir (P###)")
                id_pedido = input("Introduce el id del pedido (PED###): ")

                comprobacion = True
                comprobacion1 = True
                comprobacion2 =  False

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
                
                input("pulsa para continuar")
                os.system("clear")

            else :
                print("Esa opcion no existe")

               
            
        elif opcion == "4":

            print("Que quieres hacer")
            print("1. Añadir reseña")
            print("2. Listar reseñas")
            print()
            opcion4 = input("Introduce opcion: ")

            if opcion4 == "1":
                
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

                id_producto = input("Introduce el id del producto: ")
                id_cliente = input("Introduce el id del cliente: ")
                comentario = input("Introduce el comentario: ")
                puntacion = input("Introduce la puntuacion ")

                producto = ""

                comprobacion3 = False

                for i in productos :
                    if id_producto == i.get_id_productos() :
                        producto = i

                for j in clientes.keys() :
                    if j == id_cliente:
                        comprobacion3 = True
                
                if producto != "" and comprobacion3 :               
                    reseña = Reseña(id_reseña , producto , clientes[id_cliente] , comentario , puntacion)
                    reseñas.append(reseña)

            elif opcion4 == "2":

                for i in reseñas:
                    print(i)

            else : 
                print("Esa opcion no existe")

        elif opcion == "5":
            verdad =False

        else :
            print("Esa opcion no esta en el menu")  

menu()