# ======================================================================================================================
print("\n" + "="*27+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*170 + "\n")
print("UNIDAD I")
print("Tarea semana 2 Técnicas de Programación (POO)")
print("DEMOSTRACIÓN DE 2 EJEMPLOS APLICANDO CADA TIPO DE TÉCNICAS DE PROGRAMACION")
# ======================================================================================================================
# Tarea semana 2 Técnicas de Programación (POO)
# ======================================================================================================================
# SE VA A DESARROLLAS 2 EJEMPLOS APLICANDO CADA TIPO DE TÉCNICAS DE PROGRAMACION
# TÉCNICAS DE POO: abstracción, encapsulación, herencia, polimorfismo.
# ======================================================================================================================
# EJEMPLO 1: SISTEMA DE ANIMALES
# Demostración de conceptos de Programación Orientada a Objetos:
# - Abstracción: Clase Animal como modelo general.
# - Encapsulación: Atributos privados con getters y setters.
# - Herencia: Perro y Mono heredan de Animal.
# - Polimorfismo: Cada clase implementa su propia versión de describir().
# ======================================================================================================================
print("\n" + "="*30+ " EJEMPLO 1: SIS.ANIMALES " + "="*170 + "\n")
from abc import ABC, abstractmethod

# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE ABSTRACTA ANIMAL
# ----------------------------------------------------------------------------------------------------------------------
class Animal(ABC):
    """
    Clase abstracta que representa un animal.
    Es abstracta porque no describe un animal específico, sino un modelo general
    que sirve de base para otras clases concretas (Perro, Mono).
    Contiene atributos esenciales como tipo, dieta y tamaño.
    """

    def __init__(self, tipo, dieta, tamaño):
        # Encapsulamos las propiedades usando doble guion bajo (__)
        # para evitar acceso directo desde fuera de la clase.
        self.__tipo = tipo
        self.__dieta = dieta
        self.__tamaño = tamaño

# ------------------------------------------ GETTERS Y SETTERS ---------------------------------------------------------
    """
    Los getters y setters permiten controlar cómo se accede y modifica
    la información interna (encapsulación), protegiendo el estado del objeto.
    """

    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, nuevo_tipo):
        self.__tipo = nuevo_tipo

    def get_dieta(self):
        return self.__dieta

    def set_dieta(self, nueva_dieta):
        self.__dieta = nueva_dieta

    def get_tamaño(self):
        return self.__tamaño

    def set_tamaño(self, nuevo_tamaño):
        self.__tamaño = nuevo_tamaño

# ------------------------------------------- MÉTODO ABSTRACTO ---------------------------------------------------------
    @abstractmethod
    def describir(self):
        """
        Método abstracto que obliga a las clases hijas a implementar su propia descripción.
        Representa el polimorfismo.
        """
        pass

# ----------------------------------------------------------------------------------------------------------------------
#                                              CLASE PERRO
# ----------------------------------------------------------------------------------------------------------------------
class Perro(Animal):
    """
    Clase concreta que representa un perro.
    Hereda atributos y métodos de Animal, pero añade detalle propio como tipo de perro.
    """

    def __init__(self, tipo, dieta, tamaño):
        # Fijamos "Perro" como tipo general y enviamos dieta y tamaño al padre.
        super().__init__("Perro", dieta, tamaño)
        self.tipo = tipo  # Tipo específico del perro (doméstico, salvaje, etc.)

    def describir(self):
        """Descripción personalizada del perro."""
        return f"Soy un {self.get_tipo()} {self.tipo}, como {self.get_dieta()} y soy de un tamaño {self.get_tamaño()}."

# ----------------------------------------------------------------------------------------------------------------------
#                                               CLASE MONO
# ----------------------------------------------------------------------------------------------------------------------
class Mono(Animal):
    """
    Clase concreta que representa un mono.
    También hereda de Animal y define su propia descripción.
    """

    def __init__(self, tipo, dieta, tamaño):
        super().__init__("mono", dieta, tamaño)
        self.tipo = tipo  # Tipo específico del mono (doméstico/no doméstico, etc.)

    def describir(self):
        """Descripción personalizada del mono."""
        return f"Soy un {self.get_tipo()} {self.tipo}, como {self.get_dieta()} y soy de un tamaño {self.get_tamaño()}."

# ------------------------------------------- ARRANQUE DEL SISTEMA -----------------------------------------------------
# Creamos objetos de tipo Perro y Mono para probar el sistema.
animales = [
    Perro("domestico", "croquetas", "mediano"),
    Mono("no domestico", "bananas", "pequeño")
]

# Se aplica polimorfismo: cada objeto ejecuta su propia versión de describir().
for animal in animales:
    print(animal.describir())

print("\n" + "="*30+ " EJEMPLO 2: SIS.EMPLEADOS " + "="*170 + "\n")

# ======================================================================================================================
# EJEMPLO 2: SISTEMA DE EMPLEADOS
# Demostración de POO:
# - Abstracción: Clase Empleado como plantilla general.
# - Encapsulación: Datos privados como nombre, cédula y nacionalidad.
# - Herencia: EmpleadoTiempoCompleto y EmpleadoPorHoras.
# - Polimorfismo: calcular_salario() implementado diferente en cada clase hija.
# ======================================================================================================================
from abc import ABC, abstractmethod

# ----------------------------------------------------------------------------------------------------------------------
#                                           CLASE ABSTRACTA EMPLEADO
# ----------------------------------------------------------------------------------------------------------------------
class Empleado(ABC):
    """
    Clase abstracta que representa a un empleado.
    Provee los atributos básicos y obliga a las clases hijas a definir
    cómo calcular el salario.
    """

    def __init__(self, nombre, cedula, nacionalidad):
        # Encapsulación de los atributos usando __ para evitar acceso directo.
        self.__nombre = nombre
        self.__cedula = cedula
        self.__nacionalidad = nacionalidad

# ---------------------------------------------- GETTERS Y SETTERS -----------------------------------------------------
    """
    Permiten acceder y modificar los atributos de manera controlada.
    """

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre

    def get_cedula(self):
        return self.__cedula

    def set_cedula(self, nueva_cedula):
        self.__cedula = nueva_cedula

    def get_nacionalidad(self):
        return self.__nacionalidad

    def set_nacionalidad(self, nueva_nacionalidad):
        self.__nacionalidad = nueva_nacionalidad

# --------------------------------------------- MÉTODO ABSTRACTO -------------------------------------------------------
    @abstractmethod
    def calcular_salario(self):
        """
        Método abstracto que define una interface obligatoria para las clases hijas.
        Cada tipo de empleado calcula el salario de manera distinta.
        """
        pass

# ----------------------------------------------------------------------------------------------------------------------
#                                        CLASE EMPLEADO TIEMPO COMPLETO
# ----------------------------------------------------------------------------------------------------------------------
class EmpleadoTiempoCompleto(Empleado):
    """
    Representa a un empleado con salario mensual fijo.
    """

    def __init__(self, nombre, cedula, nacionalidad, salario_mensual):
        super().__init__(nombre, cedula, nacionalidad)
        self.salario_mensual = salario_mensual

    def calcular_salario(self):
        """El salario es siempre el mensual fijo."""
        return self.salario_mensual

# ----------------------------------------------------------------------------------------------------------------------
#                                           CLASE EMPLEADO POR HORAS
# ----------------------------------------------------------------------------------------------------------------------
class EmpleadoPorHoras(Empleado):
    """
    Representa a un empleado que cobra según las horas trabajadas.
    """

    def __init__(self, nombre, cedula, nacionalidad, horas, valor_hora):
        super().__init__(nombre, cedula, nacionalidad)
        self.horas = horas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        """El salario se calcula multiplicando por las horas trabajadas por el valor de cada hora."""
        return self.horas * self.valor_hora

# ------------------------------------------- ARRANQUE DEL SISTEMA -----------------------------------------------------
empleados = [
    EmpleadoTiempoCompleto("Andreina Lopez", "2200113244", "Ecuatoriana", 720),
    EmpleadoPorHoras("Marcelo Chacon", "2200662431", "Ecuatoriano", 150, 3.50)
]

for emp in empleados:
    print(
        f"Empleado: {emp.get_nombre()} || Cedula: {emp.get_cedula()} || "
        f"Nacionalidad: {emp.get_nacionalidad()} || Salario: ${emp.calcular_salario()}"
)