
print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("        EJERCICIO N°13 - PUNTAJES DE VIDEOJUEGO         ")
print("--------------------------------------------------------")


#  Dada la siguiente lista de puntajes de un videojuego:
#  puntajes = [450, 1200, 875, 990, 300, 1500, 640]
#  ● Mostrar el puntaje más alto y el más bajo.
#  ● Mostrar la lista ordenada de mayor a menor (ranking).
#  ● Indicar en qué posición del ranking se encuentra el puntaje 990.

puntajes = [450, 1200, 875, 990, 300, 1500, 640]

# Mostramos el puntaje más alto
for i in puntajes:
    puntaje_alto = max(puntajes)
    puntaje_bajo = min(puntajes)
print("----------------------------------------")
print(f"El Puntaje más Alto fue: {puntaje_alto}")
print(f"El Puntaje más Bajo fue: {puntaje_bajo}")
print("----------------------------------------")

print("\n------Lista Ordenda de Puntajes------")
for i in puntajes:
    lista_ordenada = sorted(puntajes, reverse=True)
print(f"{lista_ordenada}")

# se busca y se Indica en que posición del ranking se encuentra el puntaje 990.
print("\n------Posición del Puntaje 990------")
for i in puntajes:
    posicion = puntajes.index(990)
print(f"El puntaje 990 se encuentra en la posición {posicion}")
    