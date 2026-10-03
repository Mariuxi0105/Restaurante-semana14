import tkinter as tk
from tkinter import messagebox, ttk
from typing import Callable

from modelos.usuario import Usuario
from servicios.restaurante_servicio import RestauranteServicio


class LoginView(ttk.Frame):
    """Pantalla de acceso simulado."""

    def __init__(
        self,
        master: tk.Misc,
        servicio: RestauranteServicio,
        al_ingresar: Callable[[Usuario], None],
    ) -> None:
        super().__init__(master, padding=24, style="Modern.TFrame")
        self.servicio = servicio
        self.al_ingresar = al_ingresar
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        tarjeta = ttk.Frame(self, padding=0, style="Card.TFrame")
        tarjeta.grid(row=0, column=0, padx=20, pady=20)
        tarjeta.columnconfigure(0, weight=1)

        encabezado = ttk.Frame(tarjeta, padding=(32, 20, 32, 14), style="Card.TFrame")
        encabezado.grid(row=0, column=0, sticky="ew")
        ttk.Label(
            encabezado,
            text="🍽️ Restaurante App",
            font=("Segoe UI", 24, "bold"),
            foreground="#1f2937",
            background="#ffffff",
        ).pack()
        ttk.Label(
            encabezado,
            text="Ingresa para consultar el menú",
            foreground="#64748b",
            background="#ffffff",
            font=("Segoe UI", 10),
        ).pack(pady=(6, 0))

        formulario = ttk.Frame(tarjeta, padding=(32, 18, 32, 24), style="Card.TFrame")
        formulario.grid(row=1, column=0, sticky="ew")
        formulario.columnconfigure(0, weight=1)

        ttk.Label(formulario, text="Usuario", foreground="#334155", background="#ffffff", font=("Segoe UI", 10, "bold")).grid(
            row=0, column=0, sticky="w", pady=(0, 5)
        )
        self.usuario_var = tk.StringVar()
        usuario_entry = ttk.Entry(formulario, textvariable=self.usuario_var, width=30)
        usuario_entry.grid(row=1, column=0, sticky="ew", pady=(0, 14), ipady=6)

        ttk.Label(formulario, text="Contraseña", foreground="#334155", background="#ffffff", font=("Segoe UI", 10, "bold")).grid(
            row=2, column=0, sticky="w", pady=(0, 5)
        )
        self.contrasena_var = tk.StringVar()
        contrasena_entry = ttk.Entry(formulario, textvariable=self.contrasena_var, show="*", width=30)
        contrasena_entry.grid(row=3, column=0, sticky="ew", pady=(0, 18), ipady=6)

        ttk.Button(
            formulario,
            text="Ingresar al panel",
            command=self._intentar_ingreso,
            style="Primary.TButton",
        ).grid(
            row=4, column=0, sticky="ew", pady=(0, 10), ipady=3
        )
        ttk.Label(
            formulario,
            text="Acceso de prueba: admin / 1234",
            foreground="#64748b",
            background="#ffffff",
            font=("Segoe UI", 9),
        ).grid(row=5, column=0, pady=(4, 0))
        usuario_entry.focus_set()
        contrasena_entry.bind("<Return>", lambda _evento: self._intentar_ingreso())

    def _intentar_ingreso(self) -> None:
        if not self.usuario_var.get().strip() or not self.contrasena_var.get().strip():
            messagebox.showwarning("Datos incompletos", "Ingrese usuario y contraseña.")
            return

        usuario = self.servicio.validar_acceso(
            self.usuario_var.get(), self.contrasena_var.get()
        )
        if usuario is None:
            messagebox.showerror("Acceso denegado", "Las credenciales no son válidas.")
            return
        self.al_ingresar(usuario)
