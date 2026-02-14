class Cliente:
    def __init__(self,nombre:str):
        self.nombre = nombre
        self.carrito:list[str]=[]

    def agregar_producto(self,producto):
        self.carrito.append(producto)








