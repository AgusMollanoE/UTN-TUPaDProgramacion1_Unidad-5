print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("          EJERCICIO N°5 - LISTA DE ESTUDIANTES          ")
print("--------------------------------------------------------")

#5) Crear una lista con los nombres de 8 estudiantes presentes en clase.
# ● Preguntar al usuario si quiere agregar un nuevo estudiante o eliminar uno existente.
# ● Mostrar la lista final actualizada.

# Creamos una lista con los nombres de 8 estudiantes
estudiantes = ["Misael", "Brenda", "Juan", "Agustin", "Sofia", "Lucia", "Matias", "Valentina"]

# Mostramos la Lista de estudiantes actual
print("========================================================")
print("Lista de estudiantes actual:")
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")
    
# Se le pregunta al usuario si desea agregar o elimar un estudante
# se utiliza lower() para convertir la entrada a minúsculas y 
# strip() para eliminar espacios en blanco al inicio y al final

opcion = input("¿Qué acción desea realizar? (Agregar/Eliminar): ").lower().strip()

# opcion para agregar un nuevo estudiante a la lista
if opcion == "agregar":
    nuevo_estudiante = input("Ingrese el nombre del Estudiante: ").strip().title()
    estudiantes.append(nuevo_estudiante)
    print(f"Estudiante {nuevo_estudiante} agregado a la lista.")
#opcion para eliminar un estudiante de la lista    
elif opcion == "eliminar":
    eliminar_estudiante = input("Ingrese el nombre que desea eliminar: ").strip().title()
    if eliminar_estudiante in estudiantes:
        estudiantes.remove(eliminar_estudiante)
        print(f"Estudiante {eliminar_estudiante} eliminado de la lista.")
    else:
        print(f"Estudiante {eliminar_estudiante} no se encuentra en la lista.")
else:
    print("Opción no válida. No se realizaron cambios en la lista.")

# Mostramos la lista final de estudiantes
print("========================================================")
print("Lista final de estudiantes:")
for estudiante in estudiantes:
    print(f"Estudiante: {estudiante}")