# ======================================================================================================================
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("UNIDAD I")
print("Tarea semana 4 Características de la Programación Orientada a Objetos")
print("Se va realizar unu programa que compara fuerzas entre 3 diferentes personajes")
print("los personajes van hacer un mago eléctrico, luchador, caballero")
print("se va medir fuerzas para ver quien queda con poca salud o vida el que tenga mas vida ganara")
# ======================================================================================================================
# Tarea semana 4 Características de la Programación Orientada a Objetos
# ======================================================================================================================
#comentario
# ======================================================================================================================
print("\n" + "="*30+ " Programa compara fuerzas entre personajes  " + "="*30 + "\n")
# ======================================================================================================================
# Programación orientada a objetos
#Se va a realizar unu programa que compara fuerzas entre 3 diferentes personajes
#los personajes van a hacer un mago eléctrico, luchador, caballero
#se va a medir fuerzas para ver quien queda con poca salud o vida el que tenga mas vida ganara
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE BASE PERSONAJES
# ----------------------------------------------------------------------------------------------------------------------
class Personaje:
    def __init__(self, nombre, vida):
        self.nombre = nombre
        self.vida = vida

    def mostrar_estado(self):
        print(f"{self.nombre} tiene {self.vida} de vida.")
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE MAGO ELÉCTRICO
# ----------------------------------------------------------------------------------------------------------------------
class MagoElectrico(Personaje):
    def __init__(self):
        super().__init__("Mago Eléctrico", vida=100)
        self.daño_magia = 30
    """
    Daño por magia eléctrica (30)
    """

    def atacar(self, otro_personaje):
        otro_personaje.vida -= self.daño_magia
        print(f"{self.nombre} lanza un rayo eléctrico y causa {self.daño_magia} de daño a {otro_personaje.nombre}.")
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE LUCHADOR
# ----------------------------------------------------------------------------------------------------------------------
class Luchador(Personaje):
    def __init__(self):
        super().__init__("Luchador", vida=100)
        self.daño_fuerza = 20
    """
    Daño por fuerza bruta (20)
    """

    def atacar(self, otro_personaje):
        otro_personaje.vida -= self.daño_fuerza
        print(f"{self.nombre} golpea con fuerza bruta y causa {self.daño_fuerza} de daño a {otro_personaje.nombre}.")
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE CABALLERO
# ----------------------------------------------------------------------------------------------------------------------
class Caballero(Personaje):
    def __init__(self):
        super().__init__("Caballero", vida=100)
        self.daño_espada = 25
    """
    Daño con espada (25)
    """

    def atacar(self, otro_personaje):
        otro_personaje.vida -= self.daño_espada
        print(f"{self.nombre} ataca con su espada y causa {self.daño_espada} de daño a {otro_personaje.nombre}.")

# Creación de los personajes
mago = MagoElectrico()
luchador = Luchador()
caballero = Caballero()

# Simulación de ataques
mago.atacar(luchador)
luchador.atacar(caballero)
caballero.atacar(mago)
print("\n" + "="*30+ " Estado final de los personajes:  " + "="*30 + "\n")
mago.mostrar_estado()
luchador.mostrar_estado()
caballero.mostrar_estado()

# Determinar el ganador
personajes = [mago, luchador, caballero]
ganador = max(personajes, key=lambda p: p.vida)

print(f"\nEl ganador es {ganador.nombre} con {ganador.vida} puntos de vida.")