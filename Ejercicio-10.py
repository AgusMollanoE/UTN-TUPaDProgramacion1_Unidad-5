print("========================================================")
print("       BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN        ")
print("========================================================")
print("           EJERCICIO N°10 - REGISTRO DE VENTAS          ")
print("--------------------------------------------------------")

# 10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
# ● Mostrar el total vendido por cada producto.
# ● Mostrar el día con mayores ventas totales.
# ● Indicar cuál fue el producto más vendido en la semana.

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
productos = ["Producto A", "Producto B", "Producto C", "Producto D"]

ventas = []
# Se solicita al usuario que ingrese las ventas de cada producto para cada día de la semana
for i in range(len(productos)):
    fila_producto = []
    print(f"Ingrese cantidad de ventas para {productos[i]}:")
    for j in range(len(dias)):
        venta = int(input(f"  {dias[j]}: "))
        fila_producto.append(venta)
    ventas.append(fila_producto)
 # Se muestra el total vendido por cada producto  
print("\n--------Total vendido por cada producto--------")
totales_productos = []
for i in range(len(productos)):
    total = sum(ventas[i])
    totales_productos.append(total)
    print(f"Total vendido por {productos[i]}: {total}")
    
# Se determina cual fue el producto mas vendido de la semana
print("\n----------El producto más vendido en la semana----------")
max_producto = max(totales_productos)
posicion_prod_max = totales_productos.index(max_producto)
print(f"El producto más vendido fue: {productos[posicion_prod_max]} con {max_producto} de unidades")

# Se determina cual fue el día con mayores ventas totales
totales_dias = []
for j in range(len(dias)):
    total_dia = 0
    for i in range(len(productos)):
        total_dia += ventas[i][j]
    totales_dias.append(total_dia)

# Se muestra el día con mayores ventas totales
print("\n--------Total vendido por cada día--------")
max_dia = max(totales_dias)
posicion_dia_max = totales_dias.index(max_dia)  
print(f"El día con mayores ventas totales fue: {dias[posicion_dia_max]} con {max_dia} de unidades")