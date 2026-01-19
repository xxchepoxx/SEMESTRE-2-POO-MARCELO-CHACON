# ======================================================================================================================
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("UNIDAD I")
print("Tarea semana 6 Tipos de datos, Identificadores")
print("El programa ayuda a modelar animales médiente clases")
print("representando sus características y comportamientos")
# ======================================================================================================================
# Tarea semana 6 Tipos de datos, Identificadores
# ======================================================================================================================
print("\n" + "="*30+ " Sistema que representa un modelo sencillo de animales  " + "="*30 + "\n")
# ======================================================================================================================
# El programa ayuda a modelar animales médiente clases
# representando sus características y comportamientos
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE BASE ANIMAL
# ----------------------------------------------------------------------------------------------------------------------
class Animal:
    def __init__(self, nombre, edad):
        # Atributos encapsulados (privados)
        self.__nombre = nombre
        self.__edad = edad

    # Métodos getters (encapsulación)
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    # Método que será sobrescrito (polimorfismo)
    def hacer_sonido(self):
        return "El animal hace un sonido"

    # Método común
    def describir(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
# ---------------------------------------- -----------------------------------------------------------------------------
#                              CLASE DERIVADA (PUEDE SER CUALQUIER OTRO ANIMAL)
# ----------------------------------------------------------------------------------------------------------------------
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        # Llamada al constructor de la clase base
        super().__init__(nombre, edad)
        self.raza = raza

    # Polimorfismo: sobrescritura de método
    def hacer_sonido(self):
        return "El perro dice: ¡Guau!"
# ----------------------------------------------------------------------------------------------------------------------
#                             CLASE DERIVADA (PUEDE SER CUALQUIER OTRO ANIMAL)
# ----------------------------------------------------------------------------------------------------------------------
class Gato(Animal):
    def hacer_sonido(self):
        return "El gato dice: ¡Miau!"
# ----------------------------------------------------------------------------------------------------------------------
#                                               ARRANQUE
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Crear instancias de las clases
    animal = Animal("Animal genérico", "cualquiera")
    perro = Perro("Max", 3, "Labrador")
    gato = Gato("Luna", 2)

    # Demostración de funcionalidad
    print(animal.describir())
    print(animal.hacer_sonido())

    print(perro.describir())
    print(perro.hacer_sonido())

    print(gato.describir())
    print(gato.hacer_sonido())