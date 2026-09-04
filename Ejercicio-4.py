print("===========================================================")
print("         BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN         ")
print("===========================================================")
print("EJERCICIO N°4 - LISTA DE NÚMEROS REPETIDOS Y SIN REPETICIÓN")
print("-----------------------------------------------------------")

#4) Dada una lista con valores repetidos:
#  
#  DATOS = [1,3,5,3,7,1,9,5,3]
# 
# ● Crear una nueva lista sin elementos repetidos.
# ● Mostrar el resultado


datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
#mostramos la lista original
print(f"\nLista original: {datos}")

# Crear nueva lista sin elementos repatidos
lista_repetidos = []
for elemento in datos:
    if elemento not in lista_repetidos:
        lista_repetidos.append(elemento)
        
#mostramos la lista sin elementos repetidos
print(f"Lista sin elementos repetidos: {lista_repetidos}\n")
print("-----------------------------------------------------------")