from tienda_virtual.cliente import Cliente
from tienda_virtual.producto import Producto
from tienda_virtual.utilidades import mostrar_menu

# Crear productos
productos = [
    Producto("Laptop", 1200.00),
    Producto("Mouse", 50.00),
    Producto("Teclado", 80.00)
]

# Crear cliente
nombre = input("Nombre del cliente: ")
correo = input("Correo del cliente: ")
cliente = Cliente(nombre, correo)

# Interacción básica
while True:
    mostrar_menu()
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        for i, p in enumerate(productos, start=1):
            print(f"{i}. {p}")
    elif opcion == "2":
        eleccion = int(input("Número de producto: ")) - 1
        if 0 <= eleccion < len(productos):
            cliente.agregar_producto(productos[eleccion])
        else:
            print("Opción inválida")
    elif opcion == "3":
        cliente.mostrar_carrito()
    elif opcion == "4":
        print("Gracias por usar la tienda.")
        break
    else:
        print("Opción inválida")
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}"