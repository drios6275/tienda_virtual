
from principal.modelo.producto import Producto


class Tienda:

    def __init__(self , nombre = "La principal de david"):
        self.nombre = nombre
        self.productos :list[str] = []

    def agregar_producto(self, producto:Producto):
        self.productos.append(producto)

    def mostrar_productos(self) ->list[str] | str:
        if not self.productos:
            return"No hay productos en la lista"

        for producto in self.productos:
            print(producto)






