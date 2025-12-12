# ======================================================================================================================
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("UNIDAD I")
print("Tarea semana 3 Comparación de Programación Tradicional y POO en Python")
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("Se ah desarrollado habilidades prácticas en la Programación Tradicional y ")
print( "la Programación Orientada a Objetos (POO) mediante la implementación ")
print("de un programa en Python para determinar el promedio semanal del clima.")
# ======================================================================================================================
# Tarea semana 3 Comparación de Programación Tradicional y POO en Python
# ======================================================================================================================
# Programación Tradicional
#Se va a desarrollar una matriz 3d respecto ciudades del Ecuador, semana y días
#Se utilizará valores aleatorios entre 10 y 29 con respecto las temperaturas
#Al final se mostrará el promedio de las dos semanas en las diferentes ciudades del Ecuador
#con datos aleatorios respecto a las temperaturas
# ======================================================================================================================
print("\n" + "="*30+ " Con Programación Tradicional " + "="*30 + "\n")
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
#                Se importa el modulo que permite generar números pseudoaleatorios
# ----------------------------------------------------------------------------------------------------------------------
import random
# ----------------------------------------------------------------------------------------------------------------------
#                       Se genera una matriz 3D utilizando bucles anidados
# ----------------------------------------------------------------------------------------------------------------------

def generar_temperaturas(ciudades, semanas, dias):
    temperaturas = []
    for _ in ciudades:                     # Recorre cada ciudad
        semanas_ciudad = []
        for _ in range(semanas):           # Recorre cada semana
            dias_semana = []
            for _ in dias:                 # Recorre cada día
# ----------- utilizamos el modulo (import random ), para generar temperaturas aleatorias entre ( 10-29 )---------------

                valor = random.randint(10, 29)  # Temperatura aleatoria
                dias_semana.append(valor)
            semanas_ciudad.append(dias_semana)
        temperaturas.append(semanas_ciudad)
    return temperaturas
# ----------------------------------------------------------------------------------------------------------------------
#                      Se calculo el promedio de las 2 semanas de manera individual por ciudad
# ----------------------------------------------------------------------------------------------------------------------

def calcular_promedios(ciudades, dias, semanas, temperaturas):
    for i in range(len(ciudades)):
        print(f"\nCiudad: {ciudades[i]}")
        for j in range(semanas):
            suma = sum(temperaturas[i][j])     # Suma las temperaturas de la semana
            promedio = suma / len(dias)
            print(f"  Semana {j+1}: Promedio = {promedio:.2f}°C")
# -------------------------- Muestra todas las temperaturas generadas para verificación --------------------------------

def mostrar_temperaturas(ciudades, semanas, dias, temperaturas):
    print("\n=== Temperaturas generadas (matriz 3D) ===")
    for i in range(len(ciudades)):
        print(f"\nCiudad: {ciudades[i]}")
        for j in range(semanas):
            print(f"  Semana {j+1}: {temperaturas[i][j]}")
def main():
    # Listas base
    ciudades = ["Quito", "Cuenca", "Puyo"]
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    semanas = 2

    # Generar matriz 3D de temperaturas
    temperaturas = generar_temperaturas(ciudades, semanas, dias)

    # Mostrar temperaturas generadas en consola
    mostrar_temperaturas(ciudades, semanas, dias, temperaturas)

    # Calcular y mostrar promedios
    calcular_promedios(ciudades, dias, semanas, temperaturas)

# Ejecutar programa
if __name__ == "__main__":
    main()

print("\n" + "="*30+ " Con Programación Orientada a Objetos (POO) " + "="*30 + "\n")
# ======================================================================================================================
# Programación orientada a objetos
#Se va a desarrollar un registro climático semanal
#Se aplicará conceptos como encapsulamiento, herencia o polimorfismo según sea apropiado.
#Al final se mostrará el promedio semanal
# ======================================================================================================================

# ----------------------------------------------------------------------------------------------------------------------
#                                          CLASE REGISTRO CLIMA
# ----------------------------------------------------------------------------------------------------------------------

class RegistroClima:
    """
    Clase que representa el registro climático semanal.
    Aplica encapsulamiento almacenando la lista de temperaturas como atributo privado.
    """

    def __init__(self):
        # Atributo encapsulado (privado)
        self.__temperaturas = []
        self.dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    def ingresar_datos(self):
# --------------- utilizamos el metodo "temp ", que permite crear archivos y directorios temporales --------------------

        """
        Método que solicita al usuario ingresar las temperaturas del clima para cada día.
        """
        print("================== Ingreso de temperaturas usando Programación Orientada a Objetos =====================")
        for dia in self.dias:
            temp = float(input(f"Ingrese la temperatura del {dia}: "))
            self.__temperaturas.append(temp)
# ----------------------------------------------------------------------------------------------------------------------
#                             Se calcula el promedio semanal de las temperaturas
# ----------------------------------------------------------------------------------------------------------------------

    def calcular_promedio(self):

        if len(self.__temperaturas) == 0:
            return 0
        return sum(self.__temperaturas) / len(self.__temperaturas)

# ----------------------------------------------------------------------------------------------------------------------
#                                CLASE RegistroClimaExtendido(RegistroClima)
# ----------------------------------------------------------------------------------------------------------------------
# Clase hija que demuestra herencia (opcional pero solicitado)
class RegistroClimaExtendido(RegistroClima):
    """
    Clase que hereda de RegistroClima y agrega funcionalidad adicional.
    Ejemplo de herencia y polimorfismo.
    """

    def mostrar_resumen(self):
        """
        Muestra el promedio semanal utilizando el método heredado.
        """
        promedio = self.calcular_promedio()
        print(f"\nPromedio semanal (desde clase extendida): {promedio:.2f}°C")

# Ejecución
if __name__ == "__main__":
    registro = RegistroClimaExtendido()
    registro.ingresar_datos()
    registro.mostrar_resumen()