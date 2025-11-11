#Ejercicio dos. Porgramación Básica - Unidad 3. 
#Nombre: Daniel Carvajal Garcia. 
#Fecha: Noviembre de 2025. 

#Contexto
#En una empresa de marketing, se necesitan analizar 
#textos de los clientes para conocer su extensión
#y su frecuencia de ciertas palabras. 

 #Función propia definida 

def agradecimiento():
    print("\n Gracias por utilizar el pograma para el control del inventario. Espero hacerte ayudado mucho.")

#Se solicita una cadena de texto 

texto_ingresado=""
ana_realizado= False 
rem_realizado= False
RESULTADO={}
texto_reemplzado=""

while True: 
    print("\n Menu de opciones")
    print("1. Ingresar texto")
    print("2. Analizar texto")
    print("3. Reemplazar palabra")
    print("4. Mostrar analisis")
    print("5. Salir")

    try: 
        option=int(input("\n Selecciona una opción del 1 - 5:"))
    except ValueError: 
        print("\n Por favor, ingresa un valor númerico ")
        continue

#Opción 1, donde el ususario elige ingresar texto

    if option==1:
        texto_ingresado= input("\n Por favor ingresa un texto (puede ser una opinión o una reseña):").strip()
        if texto_ingresado:
            print("Texto registrado de manera correcta")
            ana_realizado=False
            rem_realizado=False
            RESULTADO={}
            texto_reemplzado=""
        else: 
            print("Por favor, ingresa el texto. NO debe quedar vacío")

#Opción 2, analizar el texto ingresado 

    elif option==2: 
        if not texto_ingresado:
            print("Por favor, primera regitra tu comentario u opinion")
        else:
            if not isinstance(texto_ingresado, str): 
                texto_ingresado = str(texto_ingresado)
                
            texto_limpio= str(texto_ingresado).split()
            palabras=texto_limpio
            num_palabras= len(palabras)
            num_caracteres= len(texto_ingresado)

            palabra_bus= input("\n Por favor ingresa una palabara para saber cuantas veces aparece:")

            palabras_nor=[p.lower() for p in palabras]
            palabra_bus_nor= palabra_bus.lower()
            con_palabra=palabras_nor.count(palabra_bus_nor)

            RESULTADO= { 
                "Texto":texto_ingresado,
                "Numero de palabras": num_palabras,
                "Numero de caracteres": num_caracteres,
                "Texto MAYUSCULA": texto_ingresado.upper(),
                "Texto minuscula": texto_ingresado.lower(), 
                "Buscar palabra": palabra_bus, 
                "Conteo de palabras":con_palabra
            }

            ana_realizado= True
            print("\n Analisis realizado correctamente")

#Opción 3 ,reemplzar palabras 

    elif option==3: 
        if not texto_ingresado:
            print("Por favor, primera regitra tu comentario u opinion y después analizalo")
        else:
            palabra_antigua= input("\n Por favor, ingresa la palabra que deseas reemplzar:")
            palabra_nueva= input("Ingresa la nueva palabra: ")

            texto_reemplzado= texto_ingresado.replace (palabra_antigua, palabra_nueva)
            resultados =texto_reemplzado
            rem_realizado= True

            print("\n Palabras reemplzada correctamente ")

#Opción 4, mostrar análisis completo 
   
    elif option==4: 
        if not texto_ingresado:
            print("Por favor, primera regitra tu comentario u opinion y después analizalo, por último registra la palabras que desees reemplazar")
        elif not ana_realizado: 
            print("Aún no has realizado el análisis de manera correcta")
        else: 
            print("\n===ANALISIS DE RESULTADOS===")
            print(f"Texto original: {RESULTADO ['Texto']}")
            print(f"Número de palabras: {RESULTADO['Numero de palabras']}")
            print(f"Números de caracteres: {RESULTADO ['Numero de caracteres']}")
            print(f"En MAYUSCULAS {RESULTADO ['Texto MAYUSCULA']}")
            print(f"En minusculas {RESULTADO['Texto minuscula']}")
            print(f"La palabra {RESULTADO ['Buscar palabra']} aparece {RESULTADO ['Conteo de palabras']} veces")

            if rem_realizado: 
                print(f"Texto reemplazado: {texto_reemplzado}")
            else:
                print("NO se ha realizado algún plazo")

#Opción 5, salir del programa

    elif option==5: 
        agradecimiento()
        break 