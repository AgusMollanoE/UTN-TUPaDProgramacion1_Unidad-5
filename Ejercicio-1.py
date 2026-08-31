print("==================================================")
print("     BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN    ")
print("==================================================")
print("   EJERCICIO N°1 - CÁLCULO DE PROMEDIO DE NOTAS   ")
print("--------------------------------------------------")

# 1) Crear una lista con las notas de 10 estudiantes.
# ● Mostrar la lista completa.
# ● Calcular y mostrar el promedio.
# ● Indicar la nota más alta y la más baja.

notas = []

for i in range(10):
    nota = float(input(f"Ingrese la nota del estudiante {i + 1}: "))
    
    while nota < 0 or nota > 10:
        print("Error: La nota debe estar entre 0 y 10.")
        nota = float(input(f"Ingrese una nota válida para el estudiante {i + 1}: "))
    notas.append(nota)

print(f"La lista completa de notas es: {notas}")

promedio = sum(notas) / len(notas)
print(f"El promedio de las notas es: {promedio:.2f}")

nota_maxima = max(notas)
nota_minima = min(notas)
print(f"La nota más alta es: {nota_maxima}")
print(f"La nota más baja es: {nota_minima}")
