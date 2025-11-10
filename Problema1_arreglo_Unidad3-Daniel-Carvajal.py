#Ejercicio uno. Porgramación Básica - Unidad 3. 
#Nombre: Daniel Carvajal Garcia. 
#Fecha: Noviembre de 2025. 

#Control de inventario.
#Contexto: 
#Una tienda desea mantener un control básico de su inventario.
#Cada producto tiene un nombre y precio. El programa debe permitir:
#registrar, ordenar y buscar productos. 

 #Función propia definida 

def agradecimiento():
    print("\n Gracias por utilizar el pograma para el control del inventario. Espero hacerte ayudado mucho.")

#Definir la función Bubble sort 

def bubble_sort(lista_producto, lista_precios):
    n = len (lista_producto) 
    for i in range ( n - 1): 
        for j in range ( n - 1 - i): 
            if lista_producto[j].lower() > lista_producto [j + 1].lower():
                lista_producto[j], lista_producto [j + 1] = lista_producto [j + 1], lista_producto[j]
                lista_precios[j], lista_precios [j +1] = lista_precios [j + 1], lista_precios [j]
                print("\n Productos ordenados alfabeticamente. \n ")

#Creación de las dos lista paralelas 

lista_productos= []
lista_precios= []

#Definir una función para buscar el producto (Busqueda lineal)

def buscar_producto(lista_productos, lista_precios, nombre_buscar): 
    nombre_bus= nombre_buscar.strip().lower()
    for i, prod in enumerate(lista_productos):
            if nombre_bus in prod.lower(): 
                return i
    return -1

#Creación de un menú principal, esto , para tener una mejor presentación 

while True: 
    print("\n===Menú principal===")
    print("1. Registro de los productos")
    print("2. Registro de los precios")
    print("3. Productos ordenados alfabeticamente")
    print("4. Buscar un producto")
    print("5. Salir")

    try: 
        option=int(input("\n Selecciona una opción del 1 -5:"))
    except ValueError: 
        print("\n Por favor, ingresa un valor númerico ")
        continue

#Registrar los productos de manera correcta 

    if option==1: 
        print("\n Registro de Productos \n")
        for i in range(20): 
            while True: 
                nombre=input(f"Por favor ingresa el nombre del producto correctamente {i +1}").strip()
                if nombre=="": 
                    print("Por favor ingresa un nombre y no dejes vacio el espacio")
                    continue
                
#Comando para leer el tipo de letra, si es Mayuscula, minuscula o ambas

                if nombre.isupper():  
                    print("El NOMBRE ESTA EN MAYUSCULAS")
                elif nombre.islower(): 
                    print("el nombre esta en minusculas")
                else: 
                    print("el nombre combina ambos caracteres")
                lista_productos.append(nombre)
                break
        print("\n Los nombre de los productos se registraron correctamente")

#Elegir la opción 2 
     
    elif option==2: 
        if not lista_productos:
            print("Por favor, primera regitra el nombre del producto ")
        else: 
            lista_precios.clear()
            print("Lista de productos y precios")
            for i in range(len(lista_productos)):
                while True: 
                    try: 
                        precio= float(input(f"Ingresa correctamente el precio del producto '{lista_productos [i]}':").strip())
                        if precio < 0: 
                            print("El precio no puede ser negativo")
                            continue
                        if precio.is_integer(): 
                            print("El precio ingresado en un número entero")
                        else:
                            print("El precio ingresado contiene números decimales")
                        lista_precios.append(precio)
                        print(f"Producto '{lista_productos [i]}' con precio ${precio:.2f} registrado correctamente. \n")
                        break
                    except ValueError: 
                        print("Por favor ingresa un valor númerico")
                        continue

#Elegir la opción 3, productos ordenados alfabeticamente

    elif option==3: 
        if not lista_productos: 
            print("Por favor, primero registra el nombre del producto")
        else: 
            bubble_sort(lista_productos, lista_precios)
            for i in range(len(lista_productos)): 
                print(f"{lista_productos [i]} - ${lista_precios [i]:.2f}")

#Buscar un producto en especifico 

    elif option==4: 
        if not lista_productos: 
            print("Por favor, primero registra el nombre del producto")
        else: 
            nombre_a_buscar=input("Ingresa el nombre del producto que deseas buscar: ")
            resultado= buscar_producto(lista_productos, lista_precios, nombre_a_buscar)
            if  resultado !=-1: 
                print(f" Producto encontrado {lista_productos [resultado]} - precio: ${lista_precios [resultado]:.2f}")
            else: 
                print("Producto NO encontrado")
    
#Opción Salir del programa 

    elif option==5: 
        agradecimiento()
        break