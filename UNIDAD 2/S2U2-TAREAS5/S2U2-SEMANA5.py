# ======================================================================================================================
print("\n" + "="*27+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*170 + "\n")
print("UNIDAD II")
print("Tarea semana 5 Creación de una Aplicación GUI Básica")
print("Sistema para registrar personas en un evento y controlar pago de cuotas.")
# ======================================================================================================================
# Tarea semana 5 GUI con Tkinter
# ======================================================================================================================
# Sistema para registrar personas en un evento y controlar pago de cuotas
# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
#                Importación de librerías necesarias
# ----------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que representa una persona dentro del evento
# ----------------------------------------------------------------------------------------------------------------------
class Persona:

    def __init__(self, nombre, cedula, pago):

        self._nombre = nombre
        self._cedula = cedula
        self._pago = pago

    def get_nombre(self):
        return self._nombre

    def get_cedula(self):
        return self._cedula

    def get_pago(self):
        return self._pago

    def __str__(self):

        estado = "Pagó" if self._pago else "No pagó"

        return f"{self._nombre} | {self._cedula} | {estado}"


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que gestiona el evento
# ----------------------------------------------------------------------------------------------------------------------
class Evento:

    def __init__(self):

        # Lista para almacenar personas registradas
        self.personas = []

# --------------------------------------------------------------------------------------------------------------
#                Agregar persona al evento
# --------------------------------------------------------------------------------------------------------------
    def agregar_persona(self, persona):

        self.personas.append(persona)

# --------------------------------------------------------------------------------------------------------------
#                Eliminar persona del evento
# --------------------------------------------------------------------------------------------------------------
    def eliminar_persona(self, cedula):

        for persona in self.personas:

            if persona.get_cedula() == cedula:

                self.personas.remove(persona)
                return True

        return False


# ----------------------------------------------------------------------------------------------------------------------
#                Clase principal que crea la interfaz gráfica
# ----------------------------------------------------------------------------------------------------------------------
class AppEvento:

    def __init__(self, root):

        self.evento = Evento()

        self.root = root
        self.root.title("Sistema de Gestión de Eventos para la universidad UEA")
        self.root.geometry("630x500")

# ----------------------------------------------------------------------------------------------------------
#                Etiquetas y campos de entrada
# ----------------------------------------------------------------------------------------------------------
        tk.Label(root, text="Nombre de la persona invitada").grid(row=0, column=0, padx=10, pady=10)

        self.entry_nombre = tk.Entry(root)
        self.entry_nombre.grid(row=0, column=1)

        tk.Label(root, text="Cédula de la persona invitada").grid(row=1, column=0, padx=10, pady=10)

        self.entry_cedula = tk.Entry(root)
        self.entry_cedula.grid(row=1, column=1)

# ----------------------------------------------------------------------------------------------------------
#                Checkbox para pago
# ----------------------------------------------------------------------------------------------------------
        self.pago_var = tk.BooleanVar()

        tk.Checkbutton(
            root,
            text="Pagó la cuota indicada",
            variable=self.pago_var
        ).grid(row=2, column=1, pady=5)

# ----------------------------------------------------------------------------------------------------------
#                Botones
# ----------------------------------------------------------------------------------------------------------
        tk.Button(
            root,
            text="Agregar persona",
            command=self.agregar_persona
        ).grid(row=3, column=0, pady=10)

        tk.Button(
            root,
            text="Eliminar persona",
            command=self.eliminar_persona
        ).grid(row=3, column=1)

        tk.Button(
            root,
            text="Limpiar",
            command=self.limpiar_campos
        ).grid(row=3, column=2)

# ----------------------------------------------------------------------------------------------------------
#                Tabla para mostrar datos
# ----------------------------------------------------------------------------------------------------------
        columnas = ("Nombre", "Cédula", "Pago")

        self.tabla = ttk.Treeview(root, columns=columnas, show="headings")

        for col in columnas:

            self.tabla.heading(col, text=col)

        self.tabla.grid(row=4, column=0, columnspan=3, padx=10, pady=20)

# ------------------------------------------------------------------------------------------------------------------
#                Función para agregar persona
# ------------------------------------------------------------------------------------------------------------------
    def agregar_persona(self):

        nombre = self.entry_nombre.get()
        cedula = self.entry_cedula.get()
        pago = self.pago_var.get()

        if nombre == "" or cedula == "":

            messagebox.showwarning("Error", "Debe ingresar todos los datos")
            return

        persona = Persona(nombre, cedula, pago)

        self.evento.agregar_persona(persona)

        estado = "Pagó" if pago else "No pagó"

        self.tabla.insert("", "end", values=(nombre, cedula, estado))

        self.limpiar_campos()

# ------------------------------------------------------------------------------------------------------------------
#                Función para eliminar persona
# ------------------------------------------------------------------------------------------------------------------
    def eliminar_persona(self):

        seleccionado = self.tabla.selection()

        if not seleccionado:

            messagebox.showwarning("Error", "Seleccione una persona")
            return

        for item in seleccionado:

            cedula = self.tabla.item(item)["values"][1]

            self.evento.eliminar_persona(cedula)

            self.tabla.delete(item)

# ------------------------------------------------------------------------------------------------------------------
#                Limpiar campos
# ------------------------------------------------------------------------------------------------------------------
    def limpiar_campos(self):

        self.entry_nombre.delete(0, tk.END)
        self.entry_cedula.delete(0, tk.END)
        self.pago_var.set(False)


# ----------------------------------------------------------------------------------------------------------------------
#                Función principal
# ----------------------------------------------------------------------------------------------------------------------
def main():

    root = tk.Tk()

    app = AppEvento(root)

    root.mainloop()
if __name__ == "__main__":
    main()