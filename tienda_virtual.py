class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def mostrar_info(self):
        print(f"producto: {self.nombre}")
        print(f"precio: ${self.precio:.2f}")
        print(f"stock disponible: {self.stock}")
        print("-" * 30)
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []
    def agregar_al_carrito(self, producto, cantidad):
        if producto.stock >= cantidad:
            self.carrito.append((producto, cantidad))
            producto.stock -= cantidad
            print(f"{cantidad} unidad(es) de {producto.nombre} agregadas al carrito.")
        else:
            print("no hay suficiente stock disponible.")
    def calcular_total(self):
        total = 0
        for producto, cantidad in self.carrito:
            total += producto.precio * cantidad
        return total
    def mostrar_factura(self):
        print("\n factura")
        print(f"cliente: {self.nombre}")
        print("-" * 30)
        for producto, cantidad in self.carrito:
            subtotal = producto.precio * cantidad
            print(f"{producto.nombre} x{cantidad} = ${subtotal:.2f}")
        print("-" * 30)
        print(f"total a pagar: ${self.calcular_total():.2f}")
class Tienda:
    def __init__(self):
        self.productos = []
    def agregar_producto(self, producto):
        self.productos.append(producto)
    def mostrar_productos(self):
        print("\n productos disponibles")
        print("=" * 30)
        for producto in self.productos:
            producto.mostrar_info()
    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None
tienda = Tienda()
p1 = Producto("laptop", 2500, 5)
p2 = Producto("mouse", 50, 20)
p3 = Producto("teclado", 120, 10)
tienda.agregar_producto(p1)
tienda.agregar_producto(p2)
tienda.agregar_producto(p3)
tienda.mostrar_productos()
cliente1 = Cliente("genis")
producto_encontrado = tienda.buscar_producto("laptop")
if producto_encontrado:
    cliente1.agregar_al_carrito(producto_encontrado, 1)
producto_encontrado = tienda.buscar_producto("mouse")
if producto_encontrado:
    cliente1.agregar_al_carrito(producto_encontrado, 2)
cliente1.mostrar_factura()