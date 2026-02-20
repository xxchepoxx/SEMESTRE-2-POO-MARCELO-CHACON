"""
Sistema de Inventario
"""

import os


# =========================
# Clase Producto
# =========================
class Producto:
    def __init__(self, id_producto: str, nombre: str, cantidad: int, precio: float):
        """
        Constructor del producto.
        """
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

    def to_line(self):
        """
        Convierte el objeto a una línea para guardar en archivo.
        """
        return f"{self._id},{self._nombre},{self._cantidad},{self._precio}\n"

    @staticmethod
    def from_line(linea):
        """
        Crea un producto desde una línea del archivo.
        Maneja posibles líneas corruptas.
        """
        try:
            id_producto, nombre, cantidad, precio = linea.strip().split(",")
            return Producto(id_producto, nombre, int(cantidad), float(precio))
        except ValueError:
            return None


# =========================
# Clase Inventario
# =========================
class Inventario:
    def __init__(self, archivo="inventario.txt"):
        """
        Inicializa el inventario y carga los datos del archivo.
        """
        self.archivo = archivo
        self.productos = []
        self.cargar_desde_archivo()

    def cargar_desde_archivo(self):
        """
        Carga productos desde el archivo.
        Si no existe, lo crea.
        """
        try:
            if not os.path.exists(self.archivo):
                open(self.archivo, "w").close()

            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    producto = Producto.from_line(linea)
                    if producto:
                        self.productos.append(producto)

        except PermissionError:
            print(" No tienes permisos para leer el archivo.")
        except Exception as e:
            print(f" Error al cargar archivo: {e}")

    def guardar_en_archivo(self):
        """
        Guarda todos los productos en el archivo.
        """
        try:
            with open(self.archivo, "w", encoding="utf-8") as f:
                for producto in self.productos:
                    f.write(producto.to_line())
            return True
        except PermissionError:
            print(" No tienes permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f" Error al guardar archivo: {e}")
            return False

    def añadir_producto(self, producto):
        """
        Añade un producto asegurando ID único.
        """
        for p in self.productos:
            if p.get_id() == producto.get_id():
                print(" El ID ya existe.")
                return False

        self.productos.append(producto)
        return self.guardar_en_archivo()

    def eliminar_producto(self, id_producto):
        """
        Elimina producto por ID.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                self.productos.remove(p)
                return self.guardar_en_archivo()

        print(" Producto no encontrado.")
        return False

    def actualizar_producto(self, id_producto, cantidad=None, precio=None):
        """
        Actualiza cantidad o precio.
        """
        for p in self.productos:
            if p.get_id() == id_producto:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return self.guardar_en_archivo()

        print(" Producto no encontrado.")
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos por coincidencia parcial de nombre.
        """
        return [p for p in self.productos if nombre.lower() in p.get_nombre().lower()]

    def mostrar_todos(self):
        """
        Muestra todos los productos.
        """
        if not self.productos:
            print("Inventario vacío.")
            return

        for p in self.productos:
            print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                  f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")


# =========================
# Interfaz de Usuario
# =========================
def menu():
    print("\n===== SISTEMA DE INVENTARIO =====")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar producto")
    print("4. Buscar producto")
    print("5. Mostrar todos")
    print("6. Salir")


def main():
    inventario = Inventario()

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        try:
            if opcion == "1":
                id_producto = input("ID: ")
                nombre = input("Nombre: ")
                cantidad = int(input("Cantidad: "))
                precio = float(input("Precio: "))

                producto = Producto(id_producto, nombre, cantidad, precio)

                if inventario.añadir_producto(producto):
                    print(" Producto añadido correctamente.")

            elif opcion == "2":
                id_producto = input("ID a eliminar: ")
                if inventario.eliminar_producto(id_producto):
                    print(" Producto eliminado correctamente.")

            elif opcion == "3":
                id_producto = input("ID del producto: ")
                cantidad = input("Nueva cantidad (Enter para omitir): ")
                precio = input("Nuevo precio (Enter para omitir): ")

                cantidad = int(cantidad) if cantidad else None
                precio = float(precio) if precio else None

                if inventario.actualizar_producto(id_producto, cantidad, precio):
                    print(" Producto actualizado correctamente.")

            elif opcion == "4":
                nombre = input("Nombre a buscar: ")
                resultados = inventario.buscar_por_nombre(nombre)

                if resultados:
                    for p in resultados:
                        print(f"ID: {p.get_id()} | Nombre: {p.get_nombre()} | "
                              f"Cantidad: {p.get_cantidad()} | Precio: ${p.get_precio():.2f}")
                else:
                    print(" No se encontraron productos.")

            elif opcion == "5":
                inventario.mostrar_todos()

            elif opcion == "6":
                print("Saliendo del sistema...")
                break

            else:
                print(" Opción inválida.")

        except ValueError:
            print(" Error: Debes ingresar números válidos para cantidad y precio.")
        except Exception as e:
            print(f" Error inesperado: {e}")


if __name__ == "__main__":
    main()