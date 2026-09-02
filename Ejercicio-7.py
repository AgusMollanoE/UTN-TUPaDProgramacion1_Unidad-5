print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("             EJERCICIO N°7 - TEMPERATURAS               ")
print("--------------------------------------------------------")


#7) Crear una matriz (lista anidada) de 7x2 con las temperaturas mínimas y máximas de
# una semana.
# ● Calcular el promedio de las mínimas y el de las máximas.
# ● Mostrar en qué día se registró la mayor amplitud térmica.

dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
temperaturas = [
                [15, 25], #lunes
                [17, 28], #martes
                [15, 23], #miércoles
                [20, 30], #jueves
                [18, 27], #viernes
                [16, 26], #sábado
                [19, 29], #domingo
                ]

suma_minimas = 0
suma_maximas = 0
mayor_amplitud = 0
dia_mayor_amplitud = ""

for contador in range(len(temperaturas)):
    minimas = temperaturas[contador][0]
    maximas = temperaturas[contador][1]
    
    #Acumulamos las termperaturas para calular el promedio
    suma_minimas += minimas
    suma_maximas += maximas
    
    #Calculamos la amplitud térmica del día actual
    amplitud = maximas - minimas
    
    if amplitud >= mayor_amplitud:
        mayor_amplitud = amplitud
        dia_mayor_amplitud = dias_semana[contador]
        
# Calculamos los promedios de las temperaturas mínimas y máximas
promedio_minimas = suma_minimas / len(temperaturas)
promedio_maximas = suma_maximas / len(temperaturas)

# Mostramos los resultados
print("\n--------------------------------------------------------")
print(f"Promedio de temperaturas mínimas: {promedio_minimas:.2f}°C")
print(f"Promedio de temperaturas máximas: {promedio_maximas:.2f}°C")
print(f"Día con mayor amplitud térmica: {dia_mayor_amplitud}")
print(f"Amplitud térmica: {mayor_amplitud}°C")
print("--------------------------------------------------------\n")


