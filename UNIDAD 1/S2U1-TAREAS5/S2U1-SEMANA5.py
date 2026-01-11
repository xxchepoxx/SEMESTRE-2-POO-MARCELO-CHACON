# ======================================================================================================================
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("UNIDAD I")
print("Tarea semana 5 Tipos de datos, Identificadores")
print("Se va realizar un programa que convierta unidades de medidas")
print("según como lo desee la persona que use el programa")
# ======================================================================================================================
# Tarea semana 5 Tipos de datos, Identificadores
# ======================================================================================================================
print("\n" + "="*30+ " Programa que convierte unidades  " + "="*30 + "\n")
# ======================================================================================================================
# Este programa permite convertir diferentes unidades de longitud
# entre metros, pies, centímetros, kilómetros y pulgadas.
# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE BASE "ConversorUnidades"
# ----------------------------------------------------------------------------------------------------------------------
class ConversorUnidades:
    """
    Esta clase representa un conversor de unidades de longitud.
    Contiene métodos que realizan las diferentes conversiones.
    """

    # Constructor de la clase
    def __init__(self):
        """
        El constructor inicializa el objeto ConversorUnidades.
        En este caso no se requieren atributos, pero el método
        se incluye para demostrar la estructura de una clase en POO.
        """
        pass

    # Métodos de conversión de unidades
    def pies_a_metros(self, pies):
        # Convierte pies a metros
        return pies * 0.3048

    def centimetros_a_metros(self, centimetros):
        # Convierte centímetros a metros
        return centimetros / 100

    def kilometros_a_metros(self, kilometros):
        # Convierte kilómetros a metros
        return kilometros * 1000

    def pulgadas_a_metros(self, pulgadas):
        # Convierte pulgadas a metros
        return pulgadas * 0.0254

    def metros_a_centimetros(self, metros):
        # Convierte metros a centímetros
        return metros * 100

    def metros_a_pies(self, metros):
        # Convierte metros a pies
        return metros / 0.3048

    def metros_a_kilometros(self, metros):
        # Convierte metros a kilómetros
        return metros / 1000

    def metros_a_pulgadas(self, metros):
        # Convierte metros a pulgadas
        return metros / 0.0254
# ---------------------------------------- -----------------------------------------------------------------------------
#                                              MENU
# ----------------------------------------------------------------------------------------------------------------------
# Función que muestra el menú al usuario
def mostrar_menu():
    """
    Muestra en pantalla el menú de opciones disponibles.
    Esta función separa la lógica de presentación,
    facilitando la organización del código.
    """
    print("\n--- MENÚ DE CONVERSIÓN DE UNIDADES ---")
    print("1. Pies a metros")
    print("2. Centímetros a metros")
    print("3. Kilómetros a metros")
    print("4. Pulgadas a metros")
    print("5. Metros a centímetros")
    print("6. Metros a pies")
    print("7. Metros a kilómetros")
    print("8. Metros a pulgadas")
    print("9. Salir")
# ----------------------------------------------------------------------------------------------------------------------
#                               CREACIÓN DE UN OBJETO DE LA CLASE "ConversorUnidades"
# ----------------------------------------------------------------------------------------------------------------------
conversor = ConversorUnidades()

# Variable booleana que controla la ejecución del programa
# Se utiliza para manejar el ciclo while
ejecutar_programa = True

# Ciclo principal del programa
while ejecutar_programa:
    mostrar_menu()

    # Se solicita al usuario seleccionar una opción del menú
    opcion = int(input("Seleccione una opción del menú: "))

    # Estructura condicional que determina qué método de la clase usar
    if opcion == 1:
        valor = float(input("Ingrese la cantidad en pies: "))
        resultado = conversor.pies_a_metros(valor)
        print(f"Resultado: {resultado} metros")

    elif opcion == 2:
        valor = float(input("Ingrese la cantidad en centímetros: "))
        resultado = conversor.centimetros_a_metros(valor)
        print(f"Resultado: {resultado} metros")

    elif opcion == 3:
        valor = float(input("Ingrese la cantidad en kilómetros: "))
        resultado = conversor.kilometros_a_metros(valor)
        print(f"Resultado: {resultado} metros")

    elif opcion == 4:
        valor = float(input("Ingrese la cantidad en pulgadas: "))
        resultado = conversor.pulgadas_a_metros(valor)
        print(f"Resultado: {resultado} metros")

    elif opcion == 5:
        valor = float(input("Ingrese la cantidad en metros: "))
        resultado = conversor.metros_a_centimetros(valor)
        print(f"Resultado: {resultado} centímetros")

    elif opcion == 6:
        valor = float(input("Ingrese la cantidad en metros: "))
        resultado = conversor.metros_a_pies(valor)
        print(f"Resultado: {resultado} pies")

    elif opcion == 7:
        valor = float(input("Ingrese la cantidad en metros: "))
        resultado = conversor.metros_a_kilometros(valor)
        print(f"Resultado: {resultado} kilómetros")

    elif opcion == 8:
        valor = float(input("Ingrese la cantidad en metros: "))
        resultado = conversor.metros_a_pulgadas(valor)
        print(f"Resultado: {resultado} pulgadas")

    elif opcion == 9:
        # Opción para finalizar el programa
        print("Gracias por utilizar el programa.")
        ejecutar_programa = False

    else:
        # Manejo de opciones inválidas
        print("Opción inválida. Por favor, seleccione una opción correcta.")