from principal.modelo.producto import Producto


class Cliente:
    def __init__(self,nombre:str="Usuario"):
        self.nombre = nombre
        self.carrito:list[str]=[]

    def agregar_producto(self,producto:Producto):
        self.carrito.append(producto)


    def mostrar_carrito(self) -> list[str] | str:
        if not self.carrito:
            return "no hay productos en el carrito"

        return self.carrito


    def calcular_total(self):
        suma = 0
        for iteracion in self.carrito:
            suma += iteracion.precio
            return suma













