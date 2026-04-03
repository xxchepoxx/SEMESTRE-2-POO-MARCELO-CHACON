# ======================================================================================================================
print("\n" + "="*27+ " UNIVERSIDAD ESTATAL AMAZÓNICA " + "="*170 + "\n")
print("UNIDAD II")
print("Tarea semana 8 - Aplicación GUI para Gestión de Tareas con Atajos de Teclado")
print("Gestor de Tareas con Interfaz Gráfica Tkinter")
# ======================================================================================================================
# Tarea semana 8 - Manejadores de eventos
# ======================================================================================================================
# Gestor de Tareas (Lista de tareas pendientes y completadas)
# ======================================================================================================================
#                Importación de librerías necesarias
# ----------------------------------------------------------------------------------------------------------------------
import tkinter as tk
from tkinter import messagebox


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que representa una Tarea
# ----------------------------------------------------------------------------------------------------------------------
class Tarea:
    """Clase que representa una tarea con su estado."""

    def __init__(self, texto, completada=False):
        """Constructor de la clase Tarea.

        Args:
            texto: Descripción de la tarea
            completada: Estado de completado (False por defecto)
        """
        self._texto = texto
        self._completada = completada

    def get_texto(self):
        """Retorna el texto de la tarea."""
        return self._texto

    def set_texto(self, texto):
        """Establece el texto de la tarea."""
        self._texto = texto

    def get_completada(self):
        """Retorna el estado de completado."""
        return self._completada

    def marcar_completada(self):
        """Marca la tarea como completada."""
        self._completada = True

    def desmarcar_completada(self):
        """Desmarca la tarea como completada."""
        self._completada = False

    def alternar_estado(self):
        """Alterna el estado de completado."""
        self._completada = not self._completada

    def __str__(self):
        """Representación en cadena de la tarea."""
        estado = "[✓]" if self._completada else "[ ]"
        return f"{estado} {self._texto}"


# ----------------------------------------------------------------------------------------------------------------------
#                Clase que gestiona la lista de tareas
# ----------------------------------------------------------------------------------------------------------------------
class GestorTareasModelo:
    """Clase que gestiona la lista de tareas (lógica del negocio)."""

    def __init__(self):
        """Constructor: inicializa la lista de tareas."""
        self._tareas = []

    # --------------------------------------------------------------------------------------------------------------
    #                Agregar tarea
    # --------------------------------------------------------------------------------------------------------------
    def agregar_tarea(self, tarea):
        """Agrega una nueva tarea a la lista.

        Args:
            tarea: Objeto de tipo Tarea
        """
        self._tareas.append(tarea)

    # --------------------------------------------------------------------------------------------------------------
    #                Eliminar tarea
    # --------------------------------------------------------------------------------------------------------------
    def eliminar_tarea(self, indice):
        """Elimina una tarea por índice.

        Args:
            indice: Índice de la tarea a eliminar

        Returns:
            True si se eliminó correctamente, False si el índice es inválido
        """
        if 0 <= indice < len(self._tareas):
            del self._tareas[indice]
            return True
        return False

    # --------------------------------------------------------------------------------------------------------------
    #                Alternar estado de tarea
    # --------------------------------------------------------------------------------------------------------------
    def alternar_estado_tarea(self, indice):
        """Alterna el estado de completado de una tarea.

        Args:
            indice: Índice de la tarea

        Returns:
            True si se alternó correctamente, False si el índice es inválido
        """
        if 0 <= indice < len(self._tareas):
            self._tareas[indice].alternar_estado()
            return True
        return False

    # --------------------------------------------------------------------------------------------------------------
    #                Obtener lista de tareas
    # --------------------------------------------------------------------------------------------------------------
    def obtener_tareas(self):
        """Retorna la lista de tareas."""
        return self._tareas

    # --------------------------------------------------------------------------------------------------------------
    #                Obtener cantidad de tareas
    # --------------------------------------------------------------------------------------------------------------
    def cantidad_tareas(self):
        """Retorna la cantidad total de tareas."""
        return len(self._tareas)

    # --------------------------------------------------------------------------------------------------------------
    #                Obtener tarea por índice
    # --------------------------------------------------------------------------------------------------------------
    def obtener_tarea(self, indice):
        """Obtiene una tarea por su índice.

        Args:
            indice: Índice de la tarea

        Returns:
            Objeto Tarea o None si el índice es inválido
        """
        if 0 <= indice < len(self._tareas):
            return self._tareas[indice]
        return None


# ----------------------------------------------------------------------------------------------------------------------
#                Clase principal que crea la interfaz gráfica
# ----------------------------------------------------------------------------------------------------------------------
class AppGestorTareas:
    """Clase principal de la aplicación con interfaz gráfica."""

    def __init__(self, root):
        """Constructor: inicializa la interfaz gráfica.

        Args:
            root: Ventana principal de Tkinter
        """
        # Modelo de datos
        self.modelo = GestorTareasModelo()

        # Configuración de la ventana principal
        self.root = root
        self.root.title("Gestor de Tareas - UEA")
        self.root.geometry("500x450")
        self.root.resizable(True, True)

        # ----------------------------------------------------------------------------------------------------------
        #                Frame de entrada de datos
        # ----------------------------------------------------------------------------------------------------------
        frame_entrada = tk.Frame(root, padx=10, pady=10)
        frame_entrada.pack(fill=tk.X)

        tk.Label(frame_entrada, text="Nueva Tarea:").pack(side=tk.LEFT, padx=(0, 5))

        self.entry_tarea = tk.Entry(frame_entrada, width=40)
        self.entry_tarea.pack(side=tk.LEFT, fill=tk.X, expand=True)

        # Evento Enter para añadir tarea
        self.entry_tarea.bind("<Return>", self._evento_enter)

        # ----------------------------------------------------------------------------------------------------------
        #                Frame de botones
        # ----------------------------------------------------------------------------------------------------------
        frame_botones = tk.Frame(root, padx=10, pady=5)
        frame_botones.pack(fill=tk.X)

        tk.Button(
            frame_botones,
            text="Añadir Tarea",
            command=self.anadir_tarea,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_botones,
            text="Marcar Completada",
            command=self.marcar_completada,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        tk.Button(
            frame_botones,
            text="Eliminar Tarea",
            command=self.eliminar_tarea,
            width=15
        ).pack(side=tk.LEFT, padx=5)

        # ----------------------------------------------------------------------------------------------------------
        #                Frame de lista de tareas
        # ----------------------------------------------------------------------------------------------------------
        frame_lista = tk.Frame(root, padx=10, pady=10)
        frame_lista.pack(fill=tk.BOTH, expand=True)

        tk.Label(frame_lista, text="Lista de Tareas:").pack(anchor=tk.W)

        # Scrollbar para la lista
        scrollbar = tk.Scrollbar(frame_lista)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Listbox para mostrar tareas
        self.lista_tareas = tk.Listbox(
            frame_lista,
            yscrollcommand=scrollbar.set,
            font=("Arial", 11),
            height=15
        )
        self.lista_tareas.pack(fill=tk.BOTH, expand=True)
        scrollbar.config(command=self.lista_tareas.yview)

        # Evento doble clic para marcar como completada
        self.lista_tareas.bind("<Double-Button-1>", self._evento_doble_clic)

        # ----------------------------------------------------------------------------------------------------------
        #                Configuración de atajos de teclado
        # ----------------------------------------------------------------------------------------------------------
        self.root.bind("<Delete>", self._evento_tecla_delete)
        self.root.bind("<d>", self._evento_tecla_d)
        self.root.bind("<D>", self._evento_tecla_d)
        self.root.bind("<c>", self._evento_tecla_c)
        self.root.bind("<C>", self._evento_tecla_c)
        self.root.bind("<Escape>", self._evento_tecla_escape)

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para evento Enter
    # ------------------------------------------------------------------------------------------------------------------
    def _evento_enter(self, event):
        """Manejador del evento tecla Enter."""
        self.anadir_tarea()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para evento doble clic
    # ------------------------------------------------------------------------------------------------------------------
    def _evento_doble_clic(self, event):
        """Manejador del evento doble clic."""
        self.marcar_completada()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para evento tecla Delete
    # ------------------------------------------------------------------------------------------------------------------
    def _evento_tecla_delete(self, event):
        """Manejador del evento tecla Delete."""
        self.eliminar_tarea()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para evento tecla D
    # ------------------------------------------------------------------------------------------------------------------
    def _evento_tecla_d(self, event):
        """Manejador del evento tecla D para eliminar tarea."""
        self.eliminar_tarea()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para evento tecla C
    # ------------------------------------------------------------------------------------------------------------------
    def _evento_tecla_c(self, event):
        """Manejador del evento tecla C."""
        self.marcar_completada()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para evento tecla Escape
    # ------------------------------------------------------------------------------------------------------------------
    def _evento_tecla_escape(self, event):
        """Manejador del evento tecla Escape para cerrar la aplicación."""
        self.root.quit()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para actualizar la lista visual
    # ------------------------------------------------------------------------------------------------------------------
    def _actualizar_lista(self):
        """Actualiza el Listbox con las tareas del modelo."""
        self.lista_tareas.delete(0, tk.END)

        for i, tarea in enumerate(self.modelo.obtener_tareas()):
            texto = str(tarea)
            self.lista_tareas.insert(tk.END, texto)

            # Cambiar color según el estado - feedback visual
            if tarea.get_completada():
                self.lista_tareas.itemconfig(i, fg="gray")
            else:
                self.lista_tareas.itemconfig(i, fg="black")

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para añadir tarea
    # ------------------------------------------------------------------------------------------------------------------
    def anadir_tarea(self):
        """Añade una nueva tarea a la lista."""
        texto = self.entry_tarea.get().strip()

        if texto == "":
            messagebox.showwarning("Advertencia", "Por favor, escribe una tarea.")
            return

        tarea = Tarea(texto)
        self.modelo.agregar_tarea(tarea)
        self._actualizar_lista()

        # Limpiar campo de entrada
        self.entry_tarea.delete(0, tk.END)
        self.entry_tarea.focus_set()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para marcar tarea como completada
    # ------------------------------------------------------------------------------------------------------------------
    def marcar_completada(self):
        """Marca o desmarca la tarea seleccionada como completada."""
        seleccion = self.lista_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
            return

        indice = seleccion[0]
        self.modelo.alternar_estado_tarea(indice)
        self._actualizar_lista()

    # ------------------------------------------------------------------------------------------------------------------
    #                Función para eliminar tarea
    # ------------------------------------------------------------------------------------------------------------------
    def eliminar_tarea(self):
        """Elimina la tarea seleccionada de la lista."""
        seleccion = self.lista_tareas.curselection()

        if not seleccion:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
            return

        indice = seleccion[0]
        tarea = self.modelo.obtener_tarea(indice)

        confirmar = messagebox.askyesno(
            "Confirmar",
            f"¿Estás seguro de eliminar la tarea?\n'{tarea.get_texto()}'"
        )

        if confirmar:
            self.modelo.eliminar_tarea(indice)
            self._actualizar_lista()


# ----------------------------------------------------------------------------------------------------------------------
#                Función principal
# ----------------------------------------------------------------------------------------------------------------------
def main():
    """Función principal que inicia la aplicación."""
    root = tk.Tk()
    app = AppGestorTareas(root)
    root.mainloop()


if __name__ == "__main__":
    main()