# # import tkinter as tk
# # from tkinter import ttk

# # # --- Colores institucionales ---
# # ROJO_OSCURO = "#780000"
# # ROJO = "#C1121F"
# # CREMA = "#FDF0D5"
# # AZUL_OSCURO = "#003049"
# # AZUL_CLARO = "#669BBC"

# # # --- Ventana principal ---
# # root = tk.Tk()
# # root.title("Módulo de Registros - EPN")
# # root.geometry("950x550")
# # root.configure(bg=AZUL_OSCURO)
# # root.resizable(False, False)

# # # --- Contenedor principal con estilo más limpio ---
# # contenedor = tk.Frame(root, bg=CREMA, bd=0, relief="flat")
# # contenedor.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

# # # --- Header simplificado con estilo institucional ---
# # header = tk.Frame(contenedor, bg=ROJO, height=55)
# # header.pack(side="top", fill="x")

# # # --- Dropdown para seleccionar tabla ---
# # tabla_seleccionada = tk.StringVar(value="RegistroAcceso")
# # tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
# # tabla_menu = ttk.Combobox(header, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
# # tabla_menu.pack(side="left", padx=20, pady=10)

# # # --- Opciones de sede alineadas a la derecha ---
# # frame_sedes = tk.Frame(header, bg=ROJO)
# # frame_sedes.pack(side="right", padx=10)
# # tk.Button(frame_sedes, text="El Bosque", bg=ROJO, fg="white", font=("Arial", 10), relief="flat", padx=10, pady=2).pack(side="left", padx=5)
# # tk.Button(frame_sedes, text="Principal", bg=ROJO_OSCURO, fg="white", font=("Arial", 10, "bold"), relief="flat", padx=10, pady=2).pack(side="left", padx=5)

# # # --- Tabla visual con bordes más suaves y estética limpia ---
# # panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
# # panel_tabla.pack(side="top", fill="both", expand=True, padx=20, pady=20)

# # estilo = ttk.Style()
# # estilo.theme_use("clam")
# # estilo.configure("Custom.Treeview",
# #     font=("Arial", 10),
# #     rowheight=28,
# #     background=CREMA,
# #     fieldbackground=CREMA,
# #     borderwidth=0
# # )
# # estilo.configure("Custom.Treeview.Heading",
# #     font=("Arial", 10, "bold"),
# #     background=AZUL_CLARO,
# #     foreground="white"
# # )

# # # Tabla con columnas genéricas
# # tabla = ttk.Treeview(panel_tabla, columns=("Col1", "Col2", "Col3", "Col4"), style="Custom.Treeview", show="headings")
# # for col in tabla["columns"]:
# #     tabla.heading(col, text=col)
# #     tabla.column(col, width=180, anchor="center")
# # tabla.pack(fill="both", expand=True)

# # root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# # --- Colores institucionales ---
# ROJO_OSCURO = "#780000"
# ROJO = "#C1121F"
# CREMA = "#FDF0D5"
# AZUL_OSCURO = "#003049"
# AZUL_CLARO = "#669BBC"

# # --- Ventana principal ---
# root = tk.Tk()
# root.title("Sistema Control Acceso - EPN")
# root.geometry("950x600")
# root.configure(bg=AZUL_OSCURO)
# root.resizable(False, False)

# # --- Contenedor principal ---
# contenedor = tk.Frame(root, bg=CREMA, bd=0, relief="flat")
# contenedor.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

# # --- Header ---
# header = tk.Frame(contenedor, bg=ROJO, height=55)
# header.pack(side="top", fill="x")

# # --- Título + Dropdown tabla ---
# titulo_frame = tk.Frame(header, bg=ROJO)
# titulo_frame.pack(side="left", padx=20)
# tk.Label(titulo_frame, text="EPN - Sistema Control Acceso", bg=ROJO, fg="white", font=("Arial", 13, "bold")).pack(anchor="w")
# tk.Label(titulo_frame, text="Tabla de:", bg=ROJO, fg="white", font=("Arial", 10)).pack(anchor="w")

# # --- Dropdown para seleccionar tabla ---
# tabla_seleccionada = tk.StringVar(value="RegistroAcceso")
# tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
# tabla_menu = ttk.Combobox(titulo_frame, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
# tabla_menu.pack(anchor="w")

# # --- Opciones de sede ---
# frame_sedes = tk.Frame(header, bg=ROJO)
# frame_sedes.pack(side="right", padx=10)
# tk.Button(frame_sedes, text="El Bosque", bg=ROJO, fg="white", font=("Arial", 10), relief="flat", padx=10, pady=2).pack(side="left", padx=5)
# tk.Button(frame_sedes, text="Principal", bg=ROJO_OSCURO, fg="white", font=("Arial", 10, "bold"), relief="flat", padx=10, pady=2).pack(side="left", padx=5)

# # --- Filtro superior ---
# filtro_frame = tk.Frame(contenedor, bg=CREMA)
# filtro_frame.pack(fill="x", padx=20, pady=(10, 0))
# tk.Label(filtro_frame, text="Filtrar por:", bg=CREMA, font=("Arial", 10)).pack(side="left")
# filtro_menu = ttk.Combobox(filtro_frame, values=["ID", "Nombre", "Fecha"], state="readonly", font=("Arial", 10))
# filtro_menu.pack(side="left", padx=10)

# # --- Tabla con estilo ---
# panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
# panel_tabla.pack(fill="both", expand=True, padx=20, pady=10)

# estilo = ttk.Style()
# estilo.theme_use("clam")
# estilo.configure("Custom.Treeview",
#     font=("Arial", 10),
#     rowheight=28,
#     background=CREMA,
#     fieldbackground=CREMA,
#     borderwidth=0
# )
# estilo.configure("Custom.Treeview.Heading",
#     font=("Arial", 10, "bold"),
#     background=AZUL_CLARO,
#     foreground="white"
# )

# tabla = ttk.Treeview(panel_tabla, columns=("Col1", "Col2", "Col3", "Col4"), style="Custom.Treeview", show="headings")
# for col in tabla["columns"]:
#     tabla.heading(col, text=col)
#     tabla.column(col, width=180, anchor="center")
# tabla.pack(fill="both", expand=True)

# # --- Botones CRUD inferiores ---
# botones_frame = tk.Frame(contenedor, bg=CREMA)
# botones_frame.pack(fill="x", pady=10)

# boton_estilo = {"font": ("Arial", 10, "bold"), "padx": 10, "pady": 5, "width": 12, "relief": "ridge", "borderwidth": 2}
# tk.Button(botones_frame, text="Crear", **boton_estilo).pack(side="left", padx=40)
# tk.Button(botones_frame, text="Actualizar", **boton_estilo).pack(side="left", padx=40)
# tk.Button(botones_frame, text="Eliminar", **boton_estilo).pack(side="left", padx=40)

# root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# # --- Colores institucionales ---
# ROJO_OSCURO = "#780000"
# ROJO = "#C1121F"
# CREMA = "#FDF0D5"
# AZUL_OSCURO = "#003049"
# AZUL_CLARO = "#669BBC"

# # --- Ventana principal ---
# root = tk.Tk()
# root.title("Sistema Control Acceso - EPN")
# root.geometry("950x600")
# root.configure(bg=AZUL_OSCURO)
# root.resizable(False, False)

# # --- Contenedor principal ---
# contenedor = tk.Frame(root, bg=CREMA, bd=0, relief="flat")
# contenedor.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

# # --- Header ---
# header = tk.Frame(contenedor, bg=ROJO, height=65)
# header.pack(side="top", fill="x")

# # --- Título y Dropdown Tabla ---
# titulo_frame = tk.Frame(header, bg=ROJO)
# titulo_frame.pack(side="left", padx=20, pady=5)
# tk.Label(titulo_frame, text="EPN - SISTEMA CONTROL ACCESO", bg=ROJO, fg="white", font=("Arial", 16, "bold")).pack(anchor="w")

# menu_tabla_frame = tk.Frame(titulo_frame, bg=ROJO)
# menu_tabla_frame.pack(anchor="w")
# tk.Label(menu_tabla_frame, text="Tabla de:", bg=ROJO, fg="white", font=("Arial", 10)).pack(side="left")
# tabla_seleccionada = tk.StringVar(value="RegistroAcceso")
# tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
# tabla_menu = ttk.Combobox(menu_tabla_frame, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
# tabla_menu.pack(side="left", padx=5)

# # --- Opciones de sede ---
# frame_sedes = tk.Frame(header, bg=ROJO)
# frame_sedes.pack(side="right", padx=10, pady=10)
# tk.Button(frame_sedes, text="El Bosque", bg=ROJO, fg="white", font=("Arial", 10), relief="flat", padx=10, pady=2).pack(side="left", padx=5)
# tk.Button(frame_sedes, text="Principal", bg=ROJO_OSCURO, fg="white", font=("Arial", 10, "bold"), relief="flat", padx=10, pady=2).pack(side="left", padx=5)

# # --- Filtro superior ---
# filtro_frame = tk.Frame(contenedor, bg=CREMA)
# filtro_frame.pack(fill="x", padx=20, pady=(10, 0))
# tk.Label(filtro_frame, text="Filtrar por:", bg=CREMA, font=("Arial", 10)).pack(side="left")
# filtro_menu = ttk.Combobox(filtro_frame, values=["ID", "Nombre", "Fecha"], state="readonly", font=("Arial", 10))
# filtro_menu.pack(side="left", padx=10)

# # --- Tabla con estilo ---
# panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
# panel_tabla.pack(fill="both", expand=True, padx=20, pady=10)

# estilo = ttk.Style()
# estilo.theme_use("clam")
# estilo.configure("Custom.Treeview",
#     font=("Arial", 10),
#     rowheight=28,
#     background=CREMA,
#     fieldbackground=CREMA,
#     borderwidth=0
# )
# estilo.configure("Custom.Treeview.Heading",
#     font=("Arial", 10, "bold"),
#     background=AZUL_CLARO,
#     foreground="white"
# )

# tabla = ttk.Treeview(panel_tabla, columns=("Col1", "Col2", "Col3", "Col4"), style="Custom.Treeview", show="headings")
# for col in tabla["columns"]:
#     tabla.heading(col, text=col)
#     tabla.column(col, width=180, anchor="center")
# tabla.pack(fill="both", expand=True)

# # --- Botones CRUD inferiores ---
# botones_frame = tk.Frame(contenedor, bg=AZUL_OSCURO)
# botones_frame.pack(fill="x", pady=15)

# boton_estilo = {
#     "font": ("Arial", 10, "bold"),
#     "padx": 10,
#     "pady": 5,
#     "width": 12,
#     "bg": AZUL_CLARO,
#     "fg": "white",
#     "activebackground": ROJO_OSCURO,
#     "relief": "flat",
#     "borderwidth": 0,
#     "highlightthickness": 0
# }
# tk.Button(botones_frame, text="Crear", **boton_estilo).pack(side="left", padx=40, ipadx=10, ipady=5)
# tk.Button(botones_frame, text="Actualizar", **boton_estilo).pack(side="left", padx=40, ipadx=10, ipady=5)
# tk.Button(botones_frame, text="Eliminar", **boton_estilo).pack(side="left", padx=40, ipadx=10, ipady=5)

# root.mainloop()


# import tkinter as tk
# from tkinter import ttk

# # --- Colores institucionales ---
# ROJO_OSCURO = "#780000"
# ROJO = "#C1121F"
# CREMA = "#FDF0D5"
# AZUL_OSCURO = "#003049"
# AZUL_CLARO = "#669BBC"

# # --- Ventana principal ---
# root = tk.Tk()
# root.title("Sistema Control Acceso - EPN")
# root.geometry("950x600")
# root.configure(bg=AZUL_OSCURO)
# root.resizable(False, False)

# # --- Contenedor principal ---
# contenedor = tk.Frame(root, bg=CREMA, bd=0, relief="flat")
# contenedor.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

# # --- Header ---
# header = tk.Frame(contenedor, bg=ROJO, height=65)
# header.pack(side="top", fill="x")

# # --- Título y Dropdown Tabla ---
# titulo_frame = tk.Frame(header, bg=ROJO)
# titulo_frame.pack(side="left", padx=20, pady=5)
# tk.Label(titulo_frame, text="EPN - SISTEMA CONTROL ACCESO", bg=ROJO, fg="white", font=("Arial", 18, "bold")).pack(anchor="w")

# menu_tabla_frame = tk.Frame(titulo_frame, bg=ROJO)
# menu_tabla_frame.pack(anchor="w")
# tk.Label(menu_tabla_frame, text="Tabla de:", bg=ROJO, fg="white", font=("Arial", 10)).pack(side="left")
# tabla_seleccionada = tk.StringVar(value="RegistroAcceso")
# tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
# tabla_menu = ttk.Combobox(menu_tabla_frame, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
# tabla_menu.pack(side="left", padx=5)

# # --- Opciones de sede ---
# frame_sedes = tk.Frame(header, bg=ROJO)
# frame_sedes.pack(side="right", padx=10, pady=10)
# tk.Button(frame_sedes, text="El Bosque", bg=ROJO, fg="white", font=("Arial", 10), relief="flat", padx=10, pady=2).pack(side="left", padx=5)
# tk.Button(frame_sedes, text="Principal", bg=ROJO_OSCURO, fg="white", font=("Arial", 10, "bold"), relief="flat", padx=10, pady=2).pack(side="left", padx=5)

# # --- Tabla con estilo ---
# panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
# panel_tabla.pack(fill="both", expand=True, padx=20, pady=(20, 0))

# estilo = ttk.Style()
# estilo.theme_use("clam")
# estilo.configure("Custom.Treeview",
#     font=("Arial", 10),
#     rowheight=28,
#     background=CREMA,
#     fieldbackground=CREMA,
#     borderwidth=0
# )
# estilo.configure("Custom.Treeview.Heading",
#     font=("Arial", 10, "bold"),
#     background=AZUL_CLARO,
#     foreground="white"
# )

# tabla = ttk.Treeview(panel_tabla, columns=("Col1", "Col2", "Col3", "Col4"), style="Custom.Treeview", show="headings")
# for col in tabla["columns"]:
#     tabla.heading(col, text=col)
#     tabla.column(col, width=180, anchor="center")
# tabla.pack(fill="both", expand=True)

# # --- Botones CRUD inferiores ---
# botones_frame = tk.Frame(contenedor, bg=AZUL_OSCURO)
# botones_frame.pack(fill="x", pady=20)

# boton_estilo = {
#     "font": ("Arial", 11, "bold"),
#     "padx": 12,
#     "pady": 8,
#     "bg": AZUL_CLARO,
#     "fg": "white",
#     "activebackground": ROJO_OSCURO,
#     "relief": "flat",
#     "borderwidth": 0,
#     "highlightthickness": 0,
# }

# tk.Button(botones_frame, text="CREAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)
# tk.Button(botones_frame, text="ACTUALIZAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)
# tk.Button(botones_frame, text="ELIMINAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)

# root.mainloop()

# import tkinter as tk
# from tkinter import ttk

# # --- Colores institucionales ---
# ROJO_OSCURO = "#780000"
# ROJO = "#C1121F"
# CREMA = "#FDF0D5"
# AZUL_OSCURO = "#003049"
# AZUL_CLARO = "#669BBC"

# # --- Ventana principal ---
# root = tk.Tk()
# root.title("Sistema Control Acceso - EPN")
# root.geometry("950x600")
# root.configure(bg=AZUL_OSCURO)
# root.resizable(False, False)

# # --- Contenedor principal ---
# contenedor = tk.Frame(root, bg=CREMA, bd=0, relief="flat")
# contenedor.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

# # --- Header ---
# header = tk.Frame(contenedor, bg=ROJO, height=65)
# header.pack(side="top", fill="x")

# # --- Título y Dropdown Tabla centrado y mejorado ---
# titulo_y_menu_frame = tk.Frame(header, bg=ROJO)
# titulo_y_menu_frame.pack(expand=True)

# titulo_label = tk.Label(titulo_y_menu_frame, text="EPN - SISTEMA CONTROL ACCESO", bg=ROJO, fg="white", font=("Arial", 20, "bold"))
# titulo_label.pack(anchor="center", pady=(5, 0))

# menu_tabla_frame = tk.Frame(titulo_y_menu_frame, bg=ROJO)
# menu_tabla_frame.pack(anchor="center", pady=(0, 5))
# tk.Label(menu_tabla_frame, text="TABLA:", bg=ROJO, fg="white", font=("Arial", 11, "bold")).pack(side="left")
# tabla_seleccionada = tk.StringVar(value="RegistroAcceso")
# tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
# tabla_menu = ttk.Combobox(menu_tabla_frame, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
# tabla_menu.pack(side="left", padx=5)

# # --- Tabla con estilo ---
# panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
# panel_tabla.pack(fill="both", expand=True, padx=20, pady=(20, 0))

# estilo = ttk.Style()
# estilo.theme_use("clam")
# estilo.configure("Custom.Treeview",
#     font=("Arial", 10),
#     rowheight=28,
#     background=CREMA,
#     fieldbackground=CREMA,
#     borderwidth=0
# )
# estilo.configure("Custom.Treeview.Heading",
#     font=("Arial", 10, "bold"),
#     background=AZUL_CLARO,
#     foreground="white"
# )

# tabla = ttk.Treeview(panel_tabla, columns=("Col1", "Col2", "Col3", "Col4"), style="Custom.Treeview", show="headings")
# for col in tabla["columns"]:
#     tabla.heading(col, text=col)
#     tabla.column(col, width=180, anchor="center")
# tabla.pack(fill="both", expand=True)

# # --- Botones CRUD inferiores ---
# botones_frame = tk.Frame(contenedor, bg=CREMA)
# botones_frame.pack(fill="x", pady=20)

# boton_estilo = {
#     "font": ("Arial", 11, "bold"),
#     "padx": 12,
#     "pady": 8,
#     "bg": AZUL_CLARO,
#     "fg": "white",
#     "activebackground": ROJO_OSCURO,
#     "relief": "flat",
#     "borderwidth": 0,
#     "highlightthickness": 0,
# }

# tk.Button(botones_frame, text="CREAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)
# tk.Button(botones_frame, text="ACTUALIZAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)
# tk.Button(botones_frame, text="ELIMINAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)

# root.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# --- Colores institucionales ---
ROJO_OSCURO = "#780000"
ROJO = "#C1121F"
CREMA = "#FDF0D5"
AZUL_OSCURO = "#003049"
AZUL_CLARO = "#669BBC"

# --- Ventana principal ---
root = tk.Tk()
root.title("Sistema Control Acceso - EPN")
root.geometry("950x600")
root.configure(bg=AZUL_OSCURO)
root.resizable(False, False)

# --- Contenedor principal ---
contenedor = tk.Frame(root, bg=CREMA, bd=0, relief="flat")
contenedor.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.95, relheight=0.9)

# --- Header ---
header = tk.Frame(contenedor, bg=ROJO, height=65)
header.pack(side="top", fill="x")

# --- Título y Dropdown Tabla centrado y mejorado ---
titulo_y_menu_frame = tk.Frame(header, bg=ROJO)
titulo_y_menu_frame.pack(expand=True)

titulo_label = tk.Label(titulo_y_menu_frame, text="EPN - SISTEMA CONTROL ACCESO", bg=ROJO, fg="white", font=("Arial", 20, "bold"))
titulo_label.pack(anchor="center", pady=(5, 0))

menu_tabla_frame = tk.Frame(titulo_y_menu_frame, bg=ROJO)
menu_tabla_frame.pack(anchor="center", pady=(0, 5))
tk.Label(menu_tabla_frame, text="TABLA:", bg=ROJO, fg="white", font=("Arial", 11, "bold")).pack(side="left")
tabla_seleccionada = tk.StringVar(value="RegistroAcceso")
tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
tabla_menu = ttk.Combobox(menu_tabla_frame, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
tabla_menu.pack(side="left", padx=5)

# --- Callback para actualizar columnas dinámicamente ---
def actualizar_columnas(*args):
    columnas_dinamicas = {
        "Campus": ["idCampus", "nombre"],
        "Ingresar": ["idIngreso", "idUsuario", "idDispositivo", "fecha", "hora"],
        "DispositivoEntrada": ["idDispositivo", "tipo", "ubicacion"],
        "Credencial": ["idCredencial", "tipo", "estado"],
        "RegistroAcceso": ["idRegistro", "idCredencial", "idDispositivo", "fecha", "hora"],
        "Usuario": ["idUsuario", "nombre", "apellido", "correo"],
        "TipoUsuario": ["idTipo", "descripcion"]
    }

    tabla.delete(*tabla.get_children())
    tabla["columns"] = columnas_dinamicas.get(tabla_seleccionada.get(), [])

    for col in tabla["columns"]:
        tabla.heading(col, text=col)
        tabla.column(col, width=180, anchor="center")

# --- Vincular selección de tabla al callback ---
tabla_menu.bind("<<ComboboxSelected>>", actualizar_columnas)

# --- Tabla con estilo ---
panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
panel_tabla.pack(fill="both", expand=True, padx=20, pady=(20, 0))

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Custom.Treeview",
    font=("Arial", 10),
    rowheight=28,
    background=CREMA,
    fieldbackground=CREMA,
    borderwidth=0
)
estilo.configure("Custom.Treeview.Heading",
    font=("Arial", 10, "bold"),
    background=AZUL_CLARO,
    foreground="white"
)

tabla = ttk.Treeview(panel_tabla, columns=("Col1", "Col2", "Col3", "Col4"), style="Custom.Treeview", show="headings")
for col in tabla["columns"]:
    tabla.heading(col, text=col)
    tabla.column(col, width=180, anchor="center")
tabla.pack(fill="both", expand=True)

# --- Funciones CRUD ---
def abrir_ventana_crear():
    top = tk.Toplevel(root)
    top.title(f"Crear registro en {tabla_seleccionada.get()}")
    top.geometry("400x400")

    campos = tabla["columns"]
    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(top, text=campo, font=("Arial", 10)).pack(pady=(10 if i == 0 else 5, 0))
        entrada = tk.Entry(top, font=("Arial", 10))
        entrada.pack(pady=5)
        entradas[campo] = entrada

    def guardar():
        valores = {campo: entradas[campo].get() for campo in campos}
        messagebox.showinfo("Registro", f"Datos ingresados:\n{valores}")
        top.destroy()

    tk.Button(top, text="Guardar", command=guardar, bg=AZUL_CLARO, fg="white", font=("Arial", 10, "bold"), relief="flat").pack(pady=20)

# --- Botones CRUD inferiores ---
botones_frame = tk.Frame(contenedor, bg=CREMA)
botones_frame.pack(fill="x", pady=20)

boton_estilo = {
    "font": ("Arial", 11, "bold"),
    "padx": 12,
    "pady": 8,
    "bg": AZUL_CLARO,
    "fg": "white",
    "activebackground": ROJO_OSCURO,
    "relief": "flat",
    "borderwidth": 0,
    "highlightthickness": 0,
}

tk.Button(botones_frame, text="CREAR", command=abrir_ventana_crear, **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)
tk.Button(botones_frame, text="ACTUALIZAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)
tk.Button(botones_frame, text="ELIMINAR", **boton_estilo).pack(side="left", expand=True, padx=30, ipadx=15, ipady=5)

# Inicializar columnas al inicio
actualizar_columnas()

root.mainloop()