import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
os.chdir(ROOT)

import tkinter as tk
from tkinter import ttk

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio
from ui.login_view import LoginView
from ui.main_view import MainView


def main() -> None:
    raiz = tk.Tk()
    raiz.title("Restaurante App | Gestión del menú")
    raiz.geometry("960x600")
    raiz.minsize(800, 500)
    raiz.configure(background="#edf2f7")

    estilo = ttk.Style()
    if "clam" in estilo.theme_names():
        estilo.theme_use("clam")

    estilo.configure(
        "Modern.TFrame",
        background="#edf2f7",
    )
    estilo.configure(
        "Card.TFrame",
        background="#ffffff",
    )
    estilo.configure(
        "Sidebar.TFrame",
        background="#f8fafc",
    )
    estilo.configure(
        "Primary.TButton",
        background="#ff7a59",
        foreground="#ffffff",
        borderwidth=0,
        focusthickness=0,
        padding=(14, 10),
    )
    estilo.map(
        "Primary.TButton",
        background=[("active", "#f06d4a"), ("pressed", "#ea623f")],
        foreground=[("pressed", "#ffffff")],
    )
    estilo.configure(
        "Secondary.TButton",
        background="#e2e8f0",
        foreground="#1f2937",
        borderwidth=0,
        focusthickness=0,
        padding=(12, 8),
    )
    estilo.map(
        "Secondary.TButton",
        background=[("active", "#cbd5e1"), ("pressed", "#b8c3d1")],
    )
    estilo.configure("TEntry", fieldbackground="#ffffff", foreground="#1f2937", borderwidth=1, lightcolor="#dbeafe")
    estilo.configure("TLabel", foreground="#1f2937")

    servicio = RestauranteServicio()
    servicio.cargar_datos()

    def mostrar_login() -> None:
        for widget in raiz.winfo_children():
            widget.destroy()
        LoginView(raiz, servicio, mostrar_panel).pack(fill="both", expand=True)

    def mostrar_panel(usuario: Usuario) -> None:
        for widget in raiz.winfo_children():
            widget.destroy()
        MainView(raiz, servicio, usuario, mostrar_login).pack(fill="both", expand=True)

    mostrar_login()
    raiz.mainloop()


if __name__ == "__main__":
    main()