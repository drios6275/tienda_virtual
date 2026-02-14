from tienda.modelo import cliente
from tienda.modelo.producto import Producto


class Tienda:

    def __init__(self , nombre = "La tienda de david"):
        self.nombre = nombre
        self.productos :list[str] = []



