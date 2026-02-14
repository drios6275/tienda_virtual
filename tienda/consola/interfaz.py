

from tienda.modelo.producto import Producto
from tienda.modelo.cliente import Cliente
from tienda.modelo.tienda import Tienda

class Interfaz:
    def __init__(self):
        self.producto: Producto | None = None
        self.cliente: Cliente | None = None
        self.tienda: Tienda | None = None



    def mostar_menu(self):
        print("\n" + "=" * 40)
        print(f"{self.tienda.nombre}")
        print("\n" + "=" * 40)
        print("1. Agregar un producto a la tienda")
        print("2. Mostrar Productos de la tienda")
        print("3. Agregar Productos al carrito")
        print("4. Mostar Carrito de compras")
        print("5. Calcular total de compra")
        print("6. salir")

