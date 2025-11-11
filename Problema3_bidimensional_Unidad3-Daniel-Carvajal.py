#Ejercicio tres. Porgramación Básica - Unidad 3. 
#Nombre: Daniel Carvajal Garcia. 
#Fecha: Noviembre de 2025. 

#Calificaciones de grupo 
#Contexto: 
#Un docente quiere registrar las calificaciones de su grupo 
#de sus alumnos en tres evaluaciones y calcular su promedio 

#Definir una función propia 

def agradecimiento():
    print("\n Gracias por utilizar el pograma para el control del inventario. Espero hacerte ayudado mucho.")

#Definir una función para la captura de datos

def captu_datos():
    lista_nombres=[]
    lista_calificaciones=[]
    print("\n Captura de Datos")
    while True: 
        try: 
            n = int(input("¿Cuántos alumnos deseas evaluar?"))
            if n < 10:
                print("Debes ingresar más alumnos, tomalo en cuenta")
                continue
            break
        except ValueError: 
            print("Ingresa un  valor númerico")

    for i in range(n): 
        print(f"\n Alumno {i + 1}:")
        nombre= input("Nombre del alumno:").strip()
        while nombre=="":
            print("El nombre no puede estar vacío")
            nombre= input("Nombre del alumno").strip()
        lista_nombres.append(nombre)

        calificaciones=[]
        for j in range(5):
            while True:
                try: 
                    cali=float(input(f"Calificaciones {j +1} (0 - 10):"))
                    if 0 <= cali <=10:
                        calificaciones.append(cali)
                        break
                    else:
                        print("La calificacion debe ser un valor de 0 - 10")
                except ValueError: 
                    print("Ingresa un valor númerico ")
        lista_calificaciones.append(calificaciones)
    print("\n Datos capturados corectamente \n")
    return lista_nombres, lista_calificaciones

#Definir una función  para calcular los promedios 

def promedio(lista_calificaciones): 
    promedios=[]
    for calificaciones in lista_calificaciones:
        promedio=sum(calificaciones)/len (calificaciones)
        promedios.append(promedio)
    return promedios

#Definir una función para mostrar resultados 

def mos_resultado(lista_nombres, lista_calificaciones, promedios):
    print("RESULTADOS")
    APROBADOS=0
    REPROBADOS=0
    for i in range(len(lista_nombres)):
        felicidades= "Aprobaste el curso" if promedios[i] >= 6.0 else "Lo siento mucho, reprobaste el curso"
        print(f"Alumnos: {lista_nombres[i]} con promedio: - promedio: {promedios[i]:.1f} {felicidades}")
        if promedios[i] >= 6.0:
            APROBADOS += 1
        else:
            REPROBADOS +=1
    promedio_general= sum(promedios)/ len(promedios)
    print(f"\n Promedio general del grupo {promedio_general:.1f}")
    print(f"Aprobados: {APROBADOS}")
    print(f"Reprobados: {REPROBADOS} \n")

#Se definio una función para registra el nombre del alumno

    lista_nombres=[]
    lista_calificaciones=[]
    promedios=[]

#Se crea una lista para que sea más fácil el registro de calificaiones

while True: 
    print("\n Menú principal")
    print("1. Ingresa el nombre y calificación del alumno")
    print("2. Calcular promedios")
    print("3. Mostrar resultados")
    print("4. Salir")
    option= input("Por favor, seleccione una opción númerica").strip()

#Escoger una opción 

    if option=="1":
        lista_nombres, lista_calificiones=captu_datos()

    elif option=="2":
        if not captu_datos:
            print("Por favor, primero ingresa el nombre y la calificación de cada alumno")
        else: 
            promedios= promedio(lista_calificiones)
            print("Promedios calculados correctamente")

    elif option=="3":
        if not promedio:
            print("Por favor, primera calcula los promedios. Punto 2")
        else: 
            mos_resultado(lista_nombres, lista_calificiones, promedios)

    elif option=="4":
        agradecimiento()
        break
    else:
        print("Opción invalida")