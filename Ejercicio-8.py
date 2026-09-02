
print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("             EJERCICIO N°8 - NOTAS                      ")
print("--------------------------------------------------------")


#8) Crear una matriz con las notas de 5 estudiantes en 3 materias.
# ● Mostrar el promedio de cada estudiante.
# ● Mostrar el promedio de cada materia.

materias = ["Matemática", "Programación I", "AySO"]
estudiantes = []
notas = []

# En este primer for se pide al Usuario que ingrese los nombres de cada estudiante
for i in range(5):
    nombre = input(f"Ingrese el Nombre del estudiante {i + 1}: ").strip()
    estudiantes.append(nombre)
print(f"Estudiantes: {estudiantes}")

# En este segundo for se muestran los alumnos de la matriz estudiante para luego pedirle al usuario 
# que carge las tres notas correspondientes.

for j in range(5):
    print(f"\nCargando nota del Alumno: {estudiantes[j]} ")
    fila_estudiante = []
    
    for k in range(3):
        nota = float(input(f"Ingrese Nota de {materias[k]}: "))
        fila_estudiante.append(nota)

    notas.append(fila_estudiante)

print("\n-----------Promedios por estudiantes------------------------")
for l in range(len(notas)):
    suma_notas = sum(notas[l])
    cantida_notas = len(notas[l])
    promedio = suma_notas / cantida_notas
    
    print(f"{estudiantes[l]}: {notas[l]} Promedio del estudiante: {promedio:.2f}")

print("\n-----------Promedios por materias------------------------")
for m in range(len(materias)):
    suma_materias = 0
    cantidad_estudiantes = len(estudiantes)
    promedio_materia = 0
    
    for n in range(cantidad_estudiantes):
        suma_materias += notas[n][m]
        promedio_materia = suma_materias / cantidad_estudiantes
    
    print(f"El promedio para {materias[m]} es: {promedio_materia:.2f}")
