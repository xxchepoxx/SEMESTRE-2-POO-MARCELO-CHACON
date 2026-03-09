# ======================================================================================================================
print("\n" + "="*27+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*170 + "\n")
print("UNIDAD II")
print("Tarea semana 4 Sistema de Gestión de Biblioteca Digital")
print("Desarrollar un sistema para gestionar una biblioteca digital usando colecciones en POO.")
# ======================================================================================================================
# Tarea semana 4 Fundamentos de colecciones (POO)
# ======================================================================================================================
# Sistema de Gestión de Biblioteca Digital
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
#                Se importan módulos para guardar información en archivos
# ----------------------------------------------------------------------------------------------------------------------
import json
import os


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que representa un libro dentro de la biblioteca
# ----------------------------------------------------------------------------------------------------------------------
class Libro:

    def __init__(self, titulo, autor, categoria, isbn):

        # Tupla para almacenar título y autor (datos que no cambian)
        self._info = (titulo, autor)

        self._categoria = categoria
        self._isbn = isbn
        self._prestado = False

    def get_titulo(self):
        return self._info[0]

    def get_autor(self):
        return self._info[1]

    def get_categoria(self):
        return self._categoria

    def get_isbn(self):
        return self._isbn

    def esta_prestado(self):
        return self._prestado

    def set_prestado(self, estado):
        self._prestado = estado

# ----------------------------------------------------------------------------------------------------------------------
#                Convierte el objeto Libro en diccionario para guardarlo
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):
        return {
            "titulo": self.get_titulo(),
            "autor": self.get_autor(),
            "categoria": self._categoria,
            "isbn": self._isbn,
            "prestado": self._prestado
        }

# ----------------------------------------------------------------------------------------------------------------------
#                Crear objeto Libro desde diccionario
# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def from_dict(data):

        libro = Libro(
            data["titulo"],
            data["autor"],
            data["categoria"],
            data["isbn"]
        )

        libro.set_prestado(data["prestado"])

        return libro

    def __str__(self):
        estado = "Prestado" if self._prestado else "Disponible"
        return f"Título: {self.get_titulo()} | Autor: {self.get_autor()} | Categoría: {self._categoria} | ISBN: {self._isbn} | Estado: {estado}"


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que representa un usuario de la biblioteca
# ----------------------------------------------------------------------------------------------------------------------
class Usuario:

    def __init__(self, nombre, id_usuario):

        self._nombre = nombre
        self._id = id_usuario

        # Lista para guardar libros prestados
        self._libros_prestados = []

    def get_nombre(self):
        return self._nombre

    def get_id(self):
        return self._id

    def prestar_libro(self, libro):
        self._libros_prestados.append(libro)

    def devolver_libro(self, libro):

        if libro in self._libros_prestados:
            self._libros_prestados.remove(libro)

    def listar_libros(self):

        if not self._libros_prestados:
            print("No tiene libros prestados.")
        else:
            for libro in self._libros_prestados:
                print(libro)

# ----------------------------------------------------------------------------------------------------------------------
#                Convertir Usuario a diccionario
# ----------------------------------------------------------------------------------------------------------------------
    def to_dict(self):

        return {
            "nombre": self._nombre,
            "id": self._id
        }

# ----------------------------------------------------------------------------------------------------------------------
#                Crear usuario desde diccionario
# ----------------------------------------------------------------------------------------------------------------------
    @staticmethod
    def from_dict(data):

        return Usuario(
            data["nombre"],
            data["id"]
        )

    def __str__(self):

        return f"Usuario: {self._nombre} | ID: {self._id}"


# ----------------------------------------------------------------------------------------------------------------------
#                Clase principal que gestiona la biblioteca
# ----------------------------------------------------------------------------------------------------------------------
class Biblioteca:

    def __init__(self):

        # Diccionario de libros
        self.libros = {}

        # Diccionario de usuarios
        self.usuarios = {}

        # Conjunto para asegurar IDs únicos
        self.ids_usuarios = set()

# ----------------------------------------------------------------------------------------------------------------------
#                Gestión de libros
# ----------------------------------------------------------------------------------------------------------------------

    def agregar_libro(self, libro):

        if libro.get_isbn() in self.libros:

            print("Ya existe un libro con ese ISBN.")

        else:

            self.libros[libro.get_isbn()] = libro
            print("Libro agregado correctamente.")

    def eliminar_libro(self, isbn):

        if isbn in self.libros:

            del self.libros[isbn]
            print("Libro eliminado.")

        else:

            print("Libro no encontrado.")

# ----------------------------------------------------------------------------------------------------------------------
#                Gestión de usuarios
# ----------------------------------------------------------------------------------------------------------------------

    def registrar_usuario(self, usuario):

        if usuario.get_id() in self.ids_usuarios:

            print("Ya existe un usuario con ese ID.")

        else:

            self.usuarios[usuario.get_id()] = usuario
            self.ids_usuarios.add(usuario.get_id())

            print("Usuario registrado correctamente.")

# ----------------------------------------------------------------------------------------------------------------------
#                Préstamo de libros
# ----------------------------------------------------------------------------------------------------------------------

    def prestar_libro(self, isbn, id_usuario):

        if isbn not in self.libros:

            print("Libro no encontrado.")
            return

        if id_usuario not in self.usuarios:

            print("Usuario no encontrado.")
            return

        libro = self.libros[isbn]

        if libro.esta_prestado():

            print("El libro ya está prestado.")

        else:

            usuario = self.usuarios[id_usuario]

            libro.set_prestado(True)
            usuario.prestar_libro(libro)

            print("Libro prestado correctamente.")

# ----------------------------------------------------------------------------------------------------------------------
#                Devolver libros
# ----------------------------------------------------------------------------------------------------------------------

    def devolver_libro(self, isbn, id_usuario):

        if isbn in self.libros and id_usuario in self.usuarios:

            libro = self.libros[isbn]
            usuario = self.usuarios[id_usuario]

            libro.set_prestado(False)
            usuario.devolver_libro(libro)

            print("Libro devuelto correctamente.")

        else:

            print("Datos incorrectos.")

# ----------------------------------------------------------------------------------------------------------------------
#                Buscar libros
# ----------------------------------------------------------------------------------------------------------------------

    def buscar_por_titulo(self, titulo):

        for libro in self.libros.values():

            if titulo.lower() in libro.get_titulo().lower():
                print(libro)

    def buscar_por_autor(self, autor):

        for libro in self.libros.values():

            if autor.lower() in libro.get_autor().lower():
                print(libro)

    def buscar_por_categoria(self, categoria):

        for libro in self.libros.values():

            if categoria.lower() in libro.get_categoria().lower():
                print(libro)

# ----------------------------------------------------------------------------------------------------------------------
#                Guardar libros
# ----------------------------------------------------------------------------------------------------------------------

    def guardar_libros(self, archivo="libros.json"):

        with open(archivo, "w", encoding="utf-8") as f:

            json.dump(
                [libro.to_dict() for libro in self.libros.values()],
                f,
                indent=4
            )

# ----------------------------------------------------------------------------------------------------------------------
#                Cargar libros
# ----------------------------------------------------------------------------------------------------------------------

    def cargar_libros(self, archivo="libros.json"):

        if os.path.exists(archivo):

            with open(archivo, "r", encoding="utf-8") as f:

                datos = json.load(f)

                for item in datos:

                    libro = Libro.from_dict(item)

                    self.libros[libro.get_isbn()] = libro

# ----------------------------------------------------------------------------------------------------------------------
#                Guardar usuarios
# ----------------------------------------------------------------------------------------------------------------------

    def guardar_usuarios(self, archivo="usuarios.json"):

        with open(archivo, "w", encoding="utf-8") as f:

            json.dump(
                [usuario.to_dict() for usuario in self.usuarios.values()],
                f,
                indent=4
            )

# ----------------------------------------------------------------------------------------------------------------------
#                Cargar usuarios
# ----------------------------------------------------------------------------------------------------------------------

    def cargar_usuarios(self, archivo="usuarios.json"):

        if os.path.exists(archivo):

            with open(archivo, "r", encoding="utf-8") as f:

                datos = json.load(f)

                for item in datos:

                    usuario = Usuario.from_dict(item)

                    self.usuarios[usuario.get_id()] = usuario
                    self.ids_usuarios.add(usuario.get_id())


# ----------------------------------------------------------------------------------------------------------------------
#                Menú del sistema
# ----------------------------------------------------------------------------------------------------------------------

def menu():

    biblioteca = Biblioteca()

    biblioteca.cargar_libros()
    biblioteca.cargar_usuarios()

    while True:

        print("\n=== MENÚ BIBLIOTECA ===")
        print("1 Registrar usuario")
        print("2 Añadir libro")
        print("3 Prestar libro")
        print("4 Devolver libro")
        print("5 Buscar libro por título")
        print("6 Buscar libro por autor")
        print("7 Buscar libro por categoría")
        print("8 Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            nombre = input("Nombre: ")
            id_usuario = input("ID usuario: ")

            usuario = Usuario(nombre, id_usuario)

            biblioteca.registrar_usuario(usuario)

        elif opcion == "2":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            libro = Libro(titulo, autor, categoria, isbn)

            biblioteca.agregar_libro(libro)

        elif opcion == "3":

            isbn = input("ISBN libro: ")
            id_usuario = input("ID usuario: ")

            biblioteca.prestar_libro(isbn, id_usuario)

        elif opcion == "4":

            isbn = input("ISBN libro: ")
            id_usuario = input("ID usuario: ")

            biblioteca.devolver_libro(isbn, id_usuario)

        elif opcion == "5":

            titulo = input("Título a buscar: ")

            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "6":

            autor = input("Autor a buscar: ")

            biblioteca.buscar_por_autor(autor)

        elif opcion == "7":

            categoria = input("Categoría a buscar: ")

            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "8":

            biblioteca.guardar_libros()
            biblioteca.guardar_usuarios()

            print("Datos guardados correctamente.")
            print("Saliendo del sistema...")

            break

        else:

            print("Opción inválida.")
if __name__ == "__main__":
    menu()