print("======================================================")
print("        BIENVENIDOS AL TRABAJO PRÁCTICO N°5 - UTN     ")
print("======================================================")
print("   EJERCICIO N°2 - CARGA Y ELIMINACIÓN DE PRODUCTOS   ")
print("------------------------------------------------------")

#2) Pedir al usuario que cargue 5 productos en una lista.
# ● Mostrar la lista ordenada alfabéticamente. Investigue el uso del método sorted().
# ● Preguntar al usuario qué producto desea eliminar y actualizar la lista.

lista_productos = []

for i in range(5):
    producto = input(f"Ingrese el nombre del producto Nro. {i + 1}: ")
    
    while not producto.isalpha():
        print("\nERROR: El nombre del producto debe contener solo letras.")
        producto = input(f"Ingrese un nombre de producto válido para el producto Nro. {i + 1}: ")
    
    lista_productos.append(producto)
    
    # Mostrar la lista actual y el producto agregado
    print("\n----------------------------------------------")
    print(f"Producto '{producto}' agregado a la lista.")
    print(f"\nLista actual de productos: {lista_productos}")
    print("----------------------------------------------\n")
    
    #Lista ordenada alfabéticamente
    lista_ordenada = sorted(lista_productos)
print("====================================================")
print(f"Lista ordenada alfabéticamente: {lista_ordenada}")
print("====================================================\n")
    
    # Preguntar al usuario qué producto desea eliminar.
eliminar_producto = input("Ingrese el nombre del producto que desea eliminar: ")
if eliminar_producto in lista_productos:
    lista_productos.remove(eliminar_producto)
    print(f"Producto {eliminar_producto} ha sido eliminado de la lista.")
else:
    print(f"Producto {eliminar_producto} no se encuentra en la lista.")

#lista actualizada después de la eliminación
print("\n====================================================")   
print(f"Lista actualizada de productos: {lista_productos}")
print("====================================================")