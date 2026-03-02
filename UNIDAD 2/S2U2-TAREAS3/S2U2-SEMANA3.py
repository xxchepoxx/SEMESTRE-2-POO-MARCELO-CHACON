# ======================================================================================================================
print("\n" + "="*27+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*170 + "\n")
print("UNIDAD II")
print("Tarea semana 3 Sistema Avanzado de Gestión de Inventario")
print("Desarrollar un sistema avanzado de gestión de inventarios para una tienda, que incorpore las colecciones en POO")
print("para un manejo eficiente de los ítems del inventario y almacene la información del inventario en archivos.")
# ======================================================================================================================
# Tarea semana 3 Fundamentos de colecciones (POO)
# ======================================================================================================================
# Sistema Avanzado de Gestión de Inventario
# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
#                Se crea modulos para almacenar datos que agregemos en nuestro codigo
# ----------------------------------------------------------------------------------------------------------------------
import json
import os


class Producto:
# ----------------------------------------------------------------------------------------------------------------------
#                Clase que representa un producto en el inventario.
# ----------------------------------------------------------------------------------------------------------------------
    def __init__(self, id_producto, nombre, cantidad, precio):
        self._id = id_producto
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

# Getters
    def get_id(self):
        return self._id

    def get_nombre(self):
        return self._nombre

    def get_cantidad(self):
        return self._cantidad

    def get_precio(self):
        return self._precio

# Setters
    def set_nombre(self, nombre):
        self._nombre = nombre

    def set_cantidad(self, cantidad):
        self._cantidad = cantidad

    def set_precio(self, precio):
        self._precio = precio

    def to_dict(self):
# ----------------------------------------------------------------------------------------------------------------------
#                Convierte el objeto Producto en un diccionario para guardarlo en JSON.
# ----------------------------------------------------------------------------------------------------------------------
        return {
            "id": self._id,
            "nombre": self._nombre,
            "cantidad": self._cantidad,
            "precio": self._precio
        }

    @staticmethod
    def from_dict(data):
# ----------------------------------------------------------------------------------------------------------------------
#                Crea un objeto Producto desde un diccionario.
# ----------------------------------------------------------------------------------------------------------------------
        return Producto(
            data["id"],
            data["nombre"],
            data["cantidad"],
            data["precio"]
        )

    def __str__(self):
        return f"ID: {self._id} | Nombre: {self._nombre} | Cantidad: {self._cantidad} | Precio por unidad: ${self._precio:.2f}"


class Inventario:
# ----------------------------------------------------------------------------------------------------------------------
#                Clase que gestiona el inventario usando un diccionario.
# ----------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto):
        if producto.get_id() in self.productos:
            print("Ya existe un producto con ese ID.")
        else:
            self.productos[producto.get_id()] = producto
            print("Producto agregado correctamente.")

    def eliminar_producto(self, id_producto):
        if id_producto in self.productos:
            del self.productos[id_producto]
            print("Producto eliminado.")
        else:
            print("Producto no encontrado.")

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        if id_producto in self.productos:
            if cantidad is not None:
                self.productos[id_producto].set_cantidad(cantidad)
            if precio is not None:
                self.productos[id_producto].set_precio(precio)
            print("Producto actualizado.")
        else:
            print("Producto no encontrado.")

    def buscar_por_nombre(self, nombre):
        encontrados = [
            producto for producto in self.productos.values()
            if nombre.lower() in producto.get_nombre().lower()
        ]

        if encontrados:
            for producto in encontrados:
                print(producto)
        else:
            print("No se encontraron productos con ese nombre.")

    def mostrar_todos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)


    def guardar_en_archivo(self, nombre_archivo="inventario.json"):
       with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        json.dump(
            [producto.to_dict() for producto in self.productos.values()],
            archivo,
            indent=4
        )
        print("Inventario guardado correctamente.")

    def cargar_desde_archivo(self, nombre_archivo="inventario.json"):
        if os.path.exists(nombre_archivo):
            with open(nombre_archivo, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                for item in datos:
                    producto = Producto.from_dict(item)
                    self.productos[producto.get_id()] = producto
            print("Inventario cargado correctamente.")
        else:
            print("No existe un archivo previo. Se creará uno nuevo.")

def menu():
    inventario = Inventario()
    inventario.cargar_desde_archivo()

    while True:
        print("\n=== MENÚ INVENTARIO ===")
        print("1. Añadir producto")
        print("2. Eliminar producto")
        print("3. Actualizar producto")
        print("4. Buscar producto por nombre")
        print("5. Mostrar todos los productos")
        print("6. Guardar y salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id_producto = input("ID: ")
            nombre = input("Nombre: ")
            cantidad = int(input("Cantidad: "))
            precio = float(input("Precio: "))
            producto = Producto(id_producto, nombre, cantidad, precio)
            inventario.agregar_producto(producto)

        elif opcion == "2":
            id_producto = input("ID del producto a eliminar: ")
            inventario.eliminar_producto(id_producto)

        elif opcion == "3":
            id_producto = input("ID del producto a actualizar: ")
            cantidad = input("Nueva cantidad (Enter para omitir): ")
            precio = input("Nuevo precio por unidad (Enter para omitir): ")

            cantidad = int(cantidad) if cantidad else None
            precio = float(precio) if precio else None

            inventario.actualizar_producto(id_producto, cantidad, precio)

        elif opcion == "4":
            nombre = input("Nombre a buscar: ")
            inventario.buscar_por_nombre(nombre)

        elif opcion == "5":
            inventario.mostrar_todos()

        elif opcion == "6":
            inventario.guardar_en_archivo()
            print("Saliendo del programa...")
            break

        else:
            print("Opción inválida seleccione una de las opciones que estan presentes del 1-6.")


if __name__ == "__main__":
    menu()