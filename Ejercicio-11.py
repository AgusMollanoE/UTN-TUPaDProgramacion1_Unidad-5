print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("        EJERCICIO N°11 - BÚSQUEDA DE ESTUDIANTES        ")
print("--------------------------------------------------------")

# 11. Crea una lista con los nombres de 10 estudiantes
# Solicitar al usuario que ingrese un nombre a buscar, indicar si el nombre se encuentra en la lista
# Mostrar en la posición en la que aparece.
# Sino se encuentra informar que no está en la lista.

estudiantes = ["Ian", "Mateo", "Lia", "Sofia", "Neo", "Gabriel", "Mia", "Lucia", "Agustin", "Misael"]

nombre_buscar = input("\nIngrese el nombre del estudiante a buscar: ").lower().strip()
encontrado = False

# Se recorre la lista de estudiantes y se compara cada nombre con el nombre ingresado por el usuario
for i in range(len(estudiantes)):
    if estudiantes[i].lower() == nombre_buscar:
        print(f"El estudiante {nombre_buscar.strip().title()} se encuentra en la posición {i}.")
        encontrado = True
        break

# Si el nombre no se encuentra en la lista, se le pide al usuario que ingrese otro nombre 
# hasta que se encuentre uno válido
while not encontrado:
    print(f"El estudiante {nombre_buscar.strip().title()} no está en la lista.")
    nombre_buscar = input("\nIngrese el nombre del estudiante a buscar: ").lower().strip()
    for i in range(len(estudiantes)):
        if estudiantes[i].lower() == nombre_buscar:
            print(f"El estudiante {nombre_buscar.strip().title()} se encuentra en la posición {i}.")
            encontrado = True
            break

