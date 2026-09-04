print("======================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN      ")
print("======================================================")
print("   EJERCICIO N°3 - LISTA DE NÚMEROS ENTEROS AL AZAR   ")
print("------------------------------------------------------")

#3) Generar una lista con 15 números enteros al azar entre 1 y 100.
# ● Crear una lista con los pares y otra con los impares.
# ● Mostrar cuántos números tiene cada lista.

import random

# Se crea una lista con 15 numeros entenros al azar:
num = []
for i in range(15):
    num.append(random.randint(1, 100))

print(f"Lista de números generados al azar: {num}")
print("------------------------------------------")

# Se crean listas para los números pares e impares:
pares = []
impares = []

for numero in num:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("\n------------------------------------------")  
print(f"Lista de números pares: {pares}")
print(f"Cantidad de números pares: {len(pares)}")
print("------------------------------------------")
print(f"Lista de números impares: {impares}")
print(f"Cantidad de números impares: {len(impares)}")
print("------------------------------------------")
