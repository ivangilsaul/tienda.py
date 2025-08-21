from tienda_virtual.producto import Producto

class Cliente:
    clientes_registrados = 0  # Atributo de clase

    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.carrito = []
        Cliente.clientes_registrados += 1

    def agregar_producto(self, producto: Producto):
        self.carrito.append(producto)

    def mostrar_carrito(self):
        total = 0
        for producto in self.carrito:
            print(f"- {producto}")
            total += producto.precio
        print(f"Total: ${total:.2f}")
