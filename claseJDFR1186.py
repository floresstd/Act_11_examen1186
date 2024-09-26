class Alumno1186: 
    def __init__(self):
        self.productos = ["Pizza", "Hamburguesa", "Ensalada", "Pasta", "Tacos", "Sushi", "Gyoza"]
        self.precios = [8.99, 5.99, 4.50, 7.50, 6.00, 12.00, 9.50]
        self.stock = [10, 15, 20, 8, 25, 5, 12]
        self.tipos = ("Comida", "Comida", "Comida", "Comida", "Comida", "Comida", "Comida")
        self.fecha_añadido = {
            "Pizza": "2023-01-15",
            "Hamburguesa": "2023-01-20",
            "Ensalada": "2023-01-22",
            "Pasta": "2023-02-05",
            "Tacos": "2023-02-10",
            "Sushi": "2023-02-15",
            "Gyoza": "2023-02-20"
        }
        self.ids = {1186, 1187, 1188, 1189, 1190, 1191, 1192}  # IDs únicos de los productos

    def altas0777(self):
        print("La operación se realizó correctamente para los datos del alumno.")

    def bajas077(self):
        print("La operación se realizó correctamente para los datos del alumno.")

    def Lista_ID_Producto1186(self):
        print("Lista de IDs de Productos:")
        for id_producto in self.ids:
            print(id_producto)

    def Nombre1186(self):
        print("Nombres de productos:")
        for producto in self.productos:
            print(producto)

    def Descripcion1186(self):
        descripciones = {
            "Pizza": "Deliciosa pizza de pepperoni.",
            "Hamburguesa": "Hamburguesa con carne de res.",
            "Ensalada": "Ensalada fresca con vegetales.",
            "Pasta": "Pasta al dente con salsa marinara.",
            "Tacos": "Tacos con carne asada y guacamole.",
            "Sushi": "Sushi fresco con pescado crudo.",
            "Gyoza": "Empanadillas japonesas rellenas."
        }
        print("Descripciones de productos:")
        for producto in self.productos:
            print(f"{producto}: {descripciones[producto]}")

    def Precio1186(self):
        print("Precios de productos:")
        for producto, precio in zip(self.productos, self.precios):
            print(f"{producto}: ${precio:.2f}")

    def Stock1186(self):
        print("Stock de productos:")
        for producto, cantidad in zip(self.productos, self.stock):
            print(f"{producto}: {cantidad} disponibles")

    def Tipo1186(self):
        print("Tipos de productos:")
        for tipo in self.tipos:
            print(tipo)

    def Fecha_Añadido1186(self):
        print("Fechas de añadido de productos:")
        for producto, fecha in self.fecha_añadido.items():
            print(f"{producto}: {fecha}")

# Crear la instancia de la clase
info = Alumno1186()

# Llamar a las funciones
info.Lista_ID_Producto1186()
info.Nombre1186()
info.Descripcion1186()
info.Precio1186()
info.Stock1186()
info.Tipo1186()
info.Fecha_Añadido1186()

# Llamar a las nuevas funciones
info.altas0777()
info.bajas077()
