import tkinter as tk
from tkinter import messagebox, scrolledtext
from respaldo_controlador import RespaldoControlador
import os

class InterfazRespaldo:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Respaldo de Base de Datos")
        self.root.geometry("700x500")
        self.root.config(bg="#f4f4f4")

        # Instancia del controlador
        self.controlador = RespaldoControlador()

        # --- Título principal ---
        tk.Label(
            root, text="Sistema de Respaldo MySQL",
            font=("Arial", 18, "bold"),
            bg="#f4f4f4", fg="#2c3e50"
        ).pack(pady=10)

        # --- Botones principales ---
        frame_botones = tk.Frame(root, bg="#f4f4f4")
        frame_botones.pack(pady=10)

        tk.Button(
            frame_botones, text="🗄 Crear Respaldo",
            command=self.crear_respaldo,
            bg="#27ae60", fg="white",
            font=("Arial", 12, "bold"),
            padx=15, pady=8
        ).grid(row=0, column=0, padx=10)

        tk.Button(
            frame_botones, text="📂 Ver Respaldos",
            command=self.mostrar_respaldos,
            bg="#2980b9", fg="white",
            font=("Arial", 12, "bold"),
            padx=15, pady=8
        ).grid(row=0, column=1, padx=10)

        tk.Button(
            frame_botones, text="🧾 Ver Log",
            command=self.mostrar_log,
            bg="#8e44ad", fg="white",
            font=("Arial", 12, "bold"),
            padx=15, pady=8
        ).grid(row=0, column=2, padx=10)

        # --- Área de salida / resultados ---
        self.salida = scrolledtext.ScrolledText(
            root, width=80, height=20, font=("Consolas", 10)
        )
        self.salida.pack(pady=15)

        self.mostrar_bienvenida()

    # ----- Funciones -----
    def crear_respaldo(self):
        """Ejecuta la creación del respaldo"""
        exito = self.controlador.crear_respaldo()
        if exito:
            messagebox.showinfo("Éxito", "Respaldo creado correctamente.")
        else:
            messagebox.showerror("Error", "No se pudo crear el respaldo.")

    def mostrar_respaldos(self):
        """Muestra los respaldos existentes en la carpeta"""
        self.salida.delete(1.0, tk.END)
        archivos = os.listdir(self.controlador.carpeta_respaldo)
        if archivos:
            self.salida.insert(tk.END, "📦 Respaldos encontrados:\n\n")
            for archivo in archivos:
                self.salida.insert(tk.END, f" - {archivo}\n")
        else:
            self.salida.insert(tk.END, "❌ No hay respaldos registrados.\n")

    def mostrar_log(self):
        """Muestra el contenido del archivo de logs"""
        self.salida.delete(1.0, tk.END)
        log_path = os.path.join(self.controlador.carpeta_logs, "respaldo_log.txt")
        if os.path.exists(log_path):
            with open(log_path, "r", encoding="utf-8") as log:
                contenido = log.read()
                self.salida.insert(tk.END, contenido)
        else:
            self.salida.insert(tk.END, "❌ No hay registros de log.\n")

    def mostrar_bienvenida(self):
        """Mensaje inicial"""
        self.salida.insert(
            tk.END,
            "👋 Bienvenido al Sistema de Respaldo MySQL\n"
            "Use los botones de arriba para crear y consultar respaldos.\n"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazRespaldo(root)
    root.mainloop()
