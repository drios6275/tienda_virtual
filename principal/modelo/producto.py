

class Producto:
    def __init__(self,nombre:str,precio:float):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):

            return f"-{self.nombre} - ${self.precio}"

    def mostrar_info(self) -> str:
        return f"el producto {self.nombre} tiene precio de {self.precio}"


