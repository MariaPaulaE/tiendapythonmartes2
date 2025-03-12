nombreVendedor=None 
productos=[]
producto={}

opcion=100

print("Mercado")
print("********")
print("1. Crear lista mercado")
print("2. Ver Lista de mercado")
print("3. Editar producto de la lista")
print("4. Retirar producto de la lista")
print("Presiona 5 para salir")
while opcion != 5:
    opcion=int(input("Digita una opcion: "))
    if opcion == 1:
        print("Bienvenido a la creacion de tu lista de mercado")
        
        #creando claves y valores de un diccionario
        producto["id"]=5
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["precio"]=int(input("Digita el precio del producto: "))
        producto["cantidad"]=int(input("Cuantos elementos de este producto vas a llevar: "))
        producto["presentacion"]=input("Cual presentacion llevaras? ")
        
        #mostrando mi diccionario
        #print(producto)
        
        #poblando una lista (agrgando elementos a una lista)
        productos.append(producto)
        print(productos)
        
        
        
    elif opcion==2:
        #Utilizando ciclos FOR en python para recorrer LISTAS
        for productoSeleccionado in productos:
            print(productoSeleccionado["nombre"])
            
    elif opcion==3:
        #0. preguntar a quien se quiere eliminar o editar
        productoCambio=int(input("Digita el id del producto a cambiar: "))
        
        #1. Buscar el producto que quiero editar
        for productoBuscado in productos:
            if productoBuscado["id"]==productoCambio:
                print("Producto encontrado")
                break
            else:
                print("Producto no encontrado")
        #2. seleccionar el elemento
        #3. accedo a las propiedades que quiero o puedo modificar
        
    elif opcion==4:
        print("estoy en la 4")
    else:
        print("Opcion no valida")
        