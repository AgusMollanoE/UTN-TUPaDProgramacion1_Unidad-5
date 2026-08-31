print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("          EJERCICIO N°6 - ROTAR ELEMENTOS             ")
print("--------------------------------------------------------")

#6) Dada una lista con 7 números, rotar todos los elementos una posición hacia la derecha
# (el último pasa a ser el primero).

#se crea la lista con 7 números y se utiliza end=" " para imprimir los elementos en la misma línea
numeros = [1, 2, 3, 4, 5, 6, 7]
print("Lista original de números: ")
for num in numeros:
    print(num, end=" ")

# rotacion de la lista hacia la derecha donde el último elemento pasa a ser el primero 
# y los demás se desplazan una posición hacia la derecha

lista_rotada = [numeros[-1]] + numeros[:-1]
print("\n----------------------------------------") 
print("Lista rotada una posición hacia la derecha:")
for num in lista_rotada:
    print(num, end=" ")     
    