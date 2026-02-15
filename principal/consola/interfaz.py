

from principal.modelo.producto import Producto
from principal.modelo.cliente import Cliente
from principal.modelo.tienda import Tienda

class Interfaz:
    def __init__(self):
        self.producto: Producto | None = None
        self.cliente: Cliente | None = None
        self.tienda: Tienda | None = None



    def mostar_menu(self):
        print("\n" + "=" * 40)
        print(f"{self.tienda.nombre}")
        print("\n" + "=" * 40)
        print("1. Agregar un producto a la principal")
        print("2. Mostrar Productos de la principal")
        print("3. Agregar Productos al carrito")
        print("4. Mostar Carrito de compras")
        print("5. Calcular total de compra")
        print("6. salir")



    def datos_productos(self):
        producto = input("Ingrese el nombre del producto: ")

        precio = int(input("Ingrese el precio del producto: "))

        return producto, precio

    def datos_cliente(self):
        cliente = input("Ingrese el nombre del cliente: ")
        return cliente


    def registro_cliente(self):
        print(f"Hola bienvenido {self.tienda.nombre}" )
        nombre_cliente = input("Ingrese el nombre del cliente: ")
        return nombre_cliente


    def mensaje_registro_exitoso_prodcutos(self):
        print("Producto Registrado con exito acontunuacion encontraras la infomacion completa")
        print(self.producto.mostrar_info())


    def mensaje_agregar_carrito(self):
        print("PRODUCTOS DISPONIBLES PARA AGREGAR AL CARRITO,")
        print("EL INDICE VA EN ORDEN DECENDENTE INCIANDO DESDE 0")
        print(self.tienda.mostrar_productos())
        indice_producto = int(input("Ingrese el indice del producto que desea agregar: "))
        self.cliente.agregar_producto(self.tienda.productos[indice_producto])




    def ejecutar(self):
        self.tienda = Tienda()
        self.cliente = Cliente()


        while True:
            self.mostar_menu()
            opcion = input("seleccione una opcion:")
            if opcion == "1":
                self.nombre_producto , self.precio= self.datos_productos()
                self.producto = Producto(self.nombre_producto , self.precio)
                self.tienda.agregar_producto(self.producto)
                self.mensaje_registro_exitoso_prodcutos()


            elif opcion == "2":
                print(self.tienda.mostrar_productos())

            elif opcion == "3":
                self.mensaje_agregar_carrito()
            elif opcion == "4":
                print(self.cliente.mostrar_carrito())

            elif opcion == "5":
                print(self.cliente.calcular_total())



















