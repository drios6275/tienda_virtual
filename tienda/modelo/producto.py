class Producto:
    def __init__(self,nombre:str,precio:float):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self) -> str:
        return f"el producto {self.nombre} tiene precio de {self.precio}"





