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
    producto = input(f"ingrese Un Producto: {i + 1}: ")
    
    while not producto.isalpha():
        print("Error: El nombre del producto debe contener solo letras.")
        producto = input(f"Ingrese un producto válido: {i + 1}: ")
    
    lista_productos.append(producto)
    
    # Mostrar la lista actual y el producto agregado
    print("----------------------------------------------")
    print(f"Producto '{producto}' agregado a la lista.")
    print(f"\nLista actual de productos: {lista_productos}")
    print("----------------------------------------------")
    
    #Lista ordenada alfabéticamente
    lista_ordenada = sorted(lista_productos)
print("====================================================")
print(f"Lista ordenada alfabéticamente: {lista_ordenada}")
print("====================================================")
    
    # Preguntar al usuario qué producto desea eliminar.
eliminar_producto = input("Ingrese el nombre del Producto que desea Eliminar: ")
if eliminar_producto in lista_productos:
    lista_productos.remove(eliminar_producto)
    print(f"Producto {eliminar_producto} ha sido eliminado de la lista.")
else:
    print(f"Producto {eliminar_producto} no se encuentra en la lista.")

#lista actualizada después de la eliminación
print("====================================================")   
print(f"Lista actualizada de productos: {lista_productos}")
print("====================================================")