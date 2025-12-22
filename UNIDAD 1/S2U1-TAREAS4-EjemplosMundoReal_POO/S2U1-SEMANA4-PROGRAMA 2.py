# ======================================================================================================================
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("UNIDAD I")
print("Tarea semana 4 Características de la Programación Orientada a Objetos")
print("Se va a realizar unu programa que realiza un sistema de reserva")
print("con diferentes habitaciones con su respectivo precio")
# ======================================================================================================================
# Tarea semana 4 Características de la Programación Orientada a Objetos
# ======================================================================================================================
#comentario
# ======================================================================================================================
print("\n" + "="*30+ " Programa compara fuerzas entre personajes  " + "="*30 + "\n")
# ======================================================================================================================
# Programación orientada a objetos
#Se va a realizar unu programa que realiza un sistema de reserva
#con diferentes habitaciones con su respectivo precio
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE BASE HABITACIÓN
# ----------------------------------------------------------------------------------------------------------------------
# Clase que representa una habitación
class Habitacion:
    def __init__(self, numero: int, tipo: str, precio: float):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponible = True  # La habitación comienza disponible

    def reservar(self):
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"La habitación {self.numero} ya está ocupada.")

    def liberar(self):
        if not self.disponible:
            self.disponible = True
            print(f"Habitación {self.numero} ahora está disponible.")
        else:
            print(f"La habitación {self.numero} ya estaba disponible.")

    def mostrar_info(self):
        estado = "Disponible" if self.disponible else "Ocupada"
        print(f"Habitación {self.numero} | Tipo: {self.tipo} | Precio: ${self.precio} | Estado: {estado}")


# Clase que representa el hotel
class Hotel:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.habitaciones = []

    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        print(f"\nHabitaciones del hotel {self.nombre}:")
        for habitacion in self.habitaciones:
            habitacion.mostrar_info()

    def buscar_habitacion(self, numero: int):
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                return habitacion
        return None


# ===============================
# PROGRAMA PRINCIPAL
# ===============================

# Crear hotel
hotel = Hotel("Hotel Paraíso")

# Crear habitaciones
hotel.agregar_habitacion(Habitacion(101, "Sencilla", 50))
hotel.agregar_habitacion(Habitacion(102, "Doble", 80))
hotel.agregar_habitacion(Habitacion(103, "Suite", 120))
hotel.agregar_habitacion(Habitacion(104, "Suite Premium", 180))


# Menú interactivo
while True:
    print("\n===== SISTEMA DE RESERVAS =====")
    print("1. Ver habitaciones")
    print("2. Reservar habitación")
    print("3. Liberar habitación")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        hotel.mostrar_habitaciones()

    elif opcion == "2":
        numero = int(input("Ingrese el número de la habitación a reservar: "))
        habitacion = hotel.buscar_habitacion(numero)

        if habitacion:
            habitacion.reservar()
        else:
            print("Habitación no encontrada.")

    elif opcion == "3":
        numero = int(input("Ingrese el número de la habitación a liberar: "))
        habitacion = hotel.buscar_habitacion(numero)

        if habitacion:
            habitacion.liberar()
        else:
            print("Habitación no encontrada.")

    elif opcion == "4":
        print("Gracias por usar el sistema de reservas.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")