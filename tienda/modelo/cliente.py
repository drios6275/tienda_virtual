from tienda.modelo.producto import Producto


class Cliente:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.carrito:list[str]=[]

    def agregar_producto(self,producto:Producto):
        self.carrito.append(producto)


    def mostrar_carrito(self) -> list[str] | str:
        if not self.carrito:
            return "no hay productos en el carrito"

        return self.carrito










