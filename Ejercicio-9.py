
print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("             EJERCICIO N°9 - TATETI                     ")
print("--------------------------------------------------------")

#Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
# ● Inicializarlo con guiones "-" representando casillas vacías.
# ● Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
# ● Mostrar el tablero después de cada jugada


tablero = [["-", "-", "-"], 
           ["-", "-", "-"], 
           ["-", "-", "-"]]

jugador_x = True

# Visualización del Tablero Vacío
for i in range (len(tablero)):
    print(f"{tablero[i]}")

for turno in range(1, 11):
    print(f"\n-------Turno {turno}----------")
    if jugador_x:
        print("---Turno del Jugador X---")
        fila = int(input("Ingrese posición de una fila (1, 2, 3): "))
        fila -=1
        columna = int(input("Ingrese posición de una columna (1, 2, 3): "))
        columna -= 1
        
    else:
        print("---Turno del Jugador O---")
        fila = int(input("Ingrese posición de una fila (1, 2, 3): "))
        fila -= 1
        columna = int(input("Ingrese posición de una columna (1, 2, 3): "))
        columna -= 1
    
    # Se valida que la casilla no este ocupada
    while tablero[fila][columna] != "-":
        print("\nLa casilla esta ocupada. Intente nuevamente.")
        fila = int(input("Ingrese posición de una fila (1, 2, 3): "))
        fila -=1
        columna = int(input("Ingrese posición de una columna (1, 2, 3): "))
        columna -= 1
     
     # Se actualiza el tablero   
    if jugador_x:
        tablero[fila][columna] = "X"
        
    else:
        tablero[fila][columna] = "O"
    
    #Cambio de jugador
    jugador_x = not jugador_x
    
    # Visualizar jugada
    for fila in tablero:
        print(" | ".join(fila))
        
        
    # Valido por filas para declarar al ganador
    if tablero[0][0] != "-" and tablero[0][0] == tablero[0][1] == tablero[0][2]:
        print(f"¡El jugador {tablero[0][0]} ha ganado!")
        break    
    if tablero[1][0] != "-" and tablero[1][0] == tablero[1][1] == tablero[1][2]:
        print(f"¡El jugador {tablero[1][0]} ha ganado!")
        break    
    if tablero[2][0] != "-" and tablero[2][0] == tablero[2][1] == tablero[2][2]:
        print(f"¡El jugador {tablero[2][0]} ha ganado!")
        break    
            
     # Valido por columnas para declara al ganador      
    if tablero[0][0] != "-" and tablero[0][0] == tablero[1][0] == tablero[2][0]:
        print(f"¡El jugador {tablero[0][0]} ha ganado!")
        break        
    if tablero[0][1] != "-" and tablero[0][1] == tablero[1][1] == tablero[2][1]:
        print(f"¡El jugador {tablero[0][1]} ha ganado!")
        break        
    if tablero[0][2] != "-" and tablero[0][2] == tablero[1][2] == tablero[2][2]:
        print(f"¡El jugador {tablero[0][2]} ha ganado!")
        break        
        
    # Valido por diagonales para declarar al ganador
    if tablero[0][0] != "-" and tablero[0][0] == tablero[1][1] == tablero[2][2]:
        print(f"¡El jugador {tablero[0][0]} ha ganado!")
        break        
    if tablero[2][0] != "-" and tablero[2][0] == tablero[1][1] == tablero[0][2]:
        print(f"¡El jugador {tablero[2][0]} ha ganado!")
        break
    
    # Declaramos empate
    if turno == 9:
        print("¡Empate! El juego ha terminado.")
        break   
    