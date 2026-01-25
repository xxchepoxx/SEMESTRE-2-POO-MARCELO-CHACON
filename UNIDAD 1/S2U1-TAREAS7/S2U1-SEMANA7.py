# ======================================================================================================================
print("\n" + "="*30+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*30 + "\n")
print("UNIDAD I")
print("Tarea semana 7 Constructores y Destructores")
print("Este programa simula una conexión a una base de datos")
# ======================================================================================================================
# Tarea semana 7 Constructores y Destructores
# ======================================================================================================================
print("\n" + "="*30+ "Simulación de una conexión a una base de datos  " + "="*30 + "\n")
# ======================================================================================================================
# Este programa simula una conexión a una base de datos
# ----------------------------------------------------------------------------------------------------------------------
#                                CLASE BASE CONEXIONBASEDATOS
# ----------------------------------------------------------------------------------------------------------------------
class ConexionBaseDatos:
    def __init__(self, servidor, usuario):
        """
        Constructor de la clase.
        Se ejecuta automáticamente al crear el objeto.

        :param servidor: Nombre del servidor de la base de datos
        :param usuario: Usuario que se conecta
        """
        self.servidor = servidor
        self.usuario = usuario
        self.conectado = True
        print(f"Conectado al servidor '{self.servidor}' como usuario '{self.usuario}'.")

    def ejecutar_consulta(self, consulta):
# ----------------------------------------------------------------------------------------------------------------------
#                                   SIMULACIÓN DE BASE DE DATOS
# ----------------------------------------------------------------------------------------------------------------------
        """
        Método que simula la ejecución de una consulta SQL.
        """
        if self.conectado:
            print(f"Ejecutando consulta: {consulta}")
        else:
            print("No hay conexión a la base de datos.")

    def __del__(self):
        """
        Destructor de la clase.
        Se ejecuta cuando el objeto es eliminado o al finalizar el programa.
        """
        if self.conectado:
            self.conectado = False
            print(f"Conexión al servidor '{self.servidor}' cerrada correctamente.")
# ----------------------------------------------------------------------------------------------------------------------
#                                               ARRANQUE
# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    # Creación del objeto (constructor)
    conexion = ConexionBaseDatos("UEA", "PCMarceloCHF")

    # Uso del objeto
    conexion.ejecutar_consulta("SELECT * FROM usuarios")

    # Eliminación del objeto (destructor)
    del conexion

    print("Programa finalizado.")