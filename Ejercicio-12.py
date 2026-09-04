
print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("           EJERCICIO N°12 - LISTA DE NÚMEROS          ")
print("--------------------------------------------------------")


# Pedir al usuario que ingrese 8 números enteros y almacenarlos en una lista.
# ● Mostrar la lista original.
# ● Mostrar la lista ordenada de menor a mayor.
# ● Mostrar la lista ordenada de mayor a menor.
# ● Investigar el uso de sorted() y del parámetro reverse

lista_num = []

# Se le pide al usuario ingresar 8 numero, y se indica cuantos numeros va ingresando hasta llegar al 8
for i in range(8):
    numero = int(input(f"{i + 1} Ingrese Numero: "))
    lista_num.append(numero)

# Se muestra por consola atravez de un for los numeros ingresados en la lista
print("------Lista Original ------")
for i in lista_num:
    print(f"{i}")

# Se usa la funcion sorted() para modificar la lista original y mostarla ordenada  
print("\n------Lista Ordenada de Menor a Mayor------")
for j in lista_num:
    lista_ordenada = sorted(lista_num)
print(f"{lista_ordenada}")
 
# Se usa el parametro reverse para mostrar la lista ordenada al reves
print("\n------Lista ordenada de Mayor a Menor------")    
for k in lista_ordenada:
    lista_invertida = sorted(lista_ordenada, reverse=True)
print(f"{lista_invertida}")
