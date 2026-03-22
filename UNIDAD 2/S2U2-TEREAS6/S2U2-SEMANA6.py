# ======================================================================================================================
print("\n" + "="*27+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*170 + "\n")
print("UNIDAD II")
print("Tarea semana 6 Creación de una Aplicación GUI Básica")
print("Agenda Personal para gestión de eventos y tareas.")
# ======================================================================================================================
# Tarea semana 5 GUI con Tkinter
# ======================================================================================================================
# Agenda Personal (Eventos y tareas)
# ======================================================================================================================
# ----------------------------------------------------------------------------------------------------------------------
#                Importación de librerías necesarias
# ----------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry   # Necesita instalación: pip install tkcalendar
import json
import os


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que representa un Evento
# ----------------------------------------------------------------------------------------------------------------------
class Evento:

    def __init__(self, fecha, hora, descripcion):

        self._fecha = fecha
        self._hora = hora
        self._descripcion = descripcion

    def get_fecha(self):
        return self._fecha

    def get_hora(self):
        return self._hora

    def get_descripcion(self):
        return self._descripcion

    def to_dict(self):
        return {
            "fecha": self._fecha,
            "hora": self._hora,
            "descripcion": self._descripcion
        }

    @classmethod
    def from_dict(cls, d):
        return cls(d.get("fecha"), d.get("hora"), d.get("descripcion"))

    def __eq__(self, other):
        if not isinstance(other, Evento):
            return False
        return (self._fecha, self._hora, self._descripcion) == (other._fecha, other._hora, other._descripcion)

    def __str__(self):
        return f"{self._fecha} | {self._hora} | {self._descripcion}"


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que gestiona la Agenda
# ----------------------------------------------------------------------------------------------------------------------
class Agenda:

    def __init__(self):

        self.eventos = []

    # --------------------------------------------------------------------------------------------------------------
    #                Agregar evento
    # --------------------------------------------------------------------------------------------------------------
    def agregar_evento(self, evento):

        self.eventos.append(evento)

    # --------------------------------------------------------------------------------------------------------------
    #                Eliminar evento
    # --------------------------------------------------------------------------------------------------------------
    def eliminar_evento(self, evento):

        if evento in self.eventos:
            self.eventos.remove(evento)
            return True
        return False

    def to_dict_list(self):
        return [e.to_dict() for e in self.eventos]

    def save_to_file(self, filepath):
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.to_dict_list(), f, ensure_ascii=False, indent=4)
            return True
        except Exception:
            return False

    def load_from_file(self, filepath):
        if not os.path.exists(filepath):
            return False
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.eventos = [Evento.from_dict(d) for d in data]
            return True
        except Exception:
            return False


# ----------------------------------------------------------------------------------------------------------------------
#                Clase principal que crea la interfaz gráfica
# ----------------------------------------------------------------------------------------------------------------------
class AppAgenda:

    def __init__(self, root):

        self.agenda = Agenda()

        # Archivo para persistencia (mismo directorio del script)
        self.filepath = os.path.join(os.path.dirname(__file__), 'agenda.json')
        # Cargar si existe
        self.agenda.load_from_file(self.filepath)

        self.root = root
        self.root.title("Agenda Personal - UEA")
        self.root.geometry("700x500")

# ----------------------------------------------------------------------------------------------------------
#                Frame de entrada de datos
# ----------------------------------------------------------------------------------------------------------
        frame_entrada = tk.Frame(root)
        frame_entrada.pack(pady=10)

        tk.Label(frame_entrada, text="Fecha").grid(row=0, column=0, padx=10, pady=5)

        self.entry_fecha = DateEntry(frame_entrada, date_pattern='yyyy-mm-dd')
        self.entry_fecha.grid(row=0, column=1)

        tk.Label(frame_entrada, text="Hora (HH:MM)").grid(row=1, column=0, padx=10, pady=5)

        self.entry_hora = tk.Entry(frame_entrada)
        self.entry_hora.grid(row=1, column=1)

        tk.Label(frame_entrada, text="Descripción").grid(row=2, column=0, padx=10, pady=5)

        self.entry_desc = tk.Entry(frame_entrada, width=30)
        self.entry_desc.grid(row=2, column=1)

# ----------------------------------------------------------------------------------------------------------
#                Frame de botones
# ----------------------------------------------------------------------------------------------------------
        frame_botones = tk.Frame(root)
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones,
            text="Agregar Evento",
            command=self.agregar_evento
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            frame_botones,
            text="Eliminar Evento",
            command=self.eliminar_evento
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            frame_botones,
            text="Salir",
            command=root.quit
        ).grid(row=0, column=2, padx=10)

# ----------------------------------------------------------------------------------------------------------
#                Frame de tabla
# ----------------------------------------------------------------------------------------------------------
        frame_tabla = tk.Frame(root)
        frame_tabla.pack(pady=20)

        columnas = ("Fecha", "Hora", "Descripción")

        self.tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")

        for col in columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=150)

        self.tabla.pack()

        # Poblar tabla con eventos cargados
        for evento in self.agenda.eventos:
            self.tabla.insert("", "end", values=(evento.get_fecha(), evento.get_hora(), evento.get_descripcion()))

# ------------------------------------------------------------------------------------------------------------------
#                Función para agregar evento
# ------------------------------------------------------------------------------------------------------------------
    def agregar_evento(self):

        fecha = self.entry_fecha.get()
        hora = self.entry_hora.get()
        descripcion = self.entry_desc.get()

        if fecha == "" or hora == "" or descripcion == "":
            messagebox.showwarning("Error", "Debe completar todos los campos")
            return

        evento = Evento(fecha, hora, descripcion)

        self.agenda.agregar_evento(evento)

        self.tabla.insert("", "end", values=(fecha, hora, descripcion))

        self.limpiar_campos()

        # Guardar cambios
        self.agenda.save_to_file(self.filepath)

# ------------------------------------------------------------------------------------------------------------------
#                Función para eliminar evento
# ------------------------------------------------------------------------------------------------------------------
    def eliminar_evento(self):

        seleccionado = self.tabla.selection()

        if not seleccionado:
            messagebox.showwarning("Error", "Seleccione un evento")
            return

        confirmar = messagebox.askyesno("Confirmar", "¿Desea eliminar el evento seleccionado?")

        if not confirmar:
            return

        for item in seleccionado:

            valores = self.tabla.item(item)["values"]

            evento = Evento(valores[0], valores[1], valores[2])

            self.agenda.eliminar_evento(evento)

            self.tabla.delete(item)

        # Guardar cambios
        self.agenda.save_to_file(self.filepath)

# ------------------------------------------------------------------------------------------------------------------
#                Limpiar campos
# ------------------------------------------------------------------------------------------------------------------
    def limpiar_campos(self):

        self.entry_hora.delete(0, tk.END)
        self.entry_desc.delete(0, tk.END)


# ----------------------------------------------------------------------------------------------------------------------
#                Función principal
# ----------------------------------------------------------------------------------------------------------------------
def main():

    root = tk.Tk()

    app = AppAgenda(root)

    root.mainloop()

if __name__ == "__main__":
    main()