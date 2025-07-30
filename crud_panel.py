# 

import tkinter as tk
from tkinter import ttk, messagebox
import importlib
import sys
import pyodbc

# --- Colores institucionales ---
ROJO_OSCURO = "#780000"
ROJO = "#C1121F"
CREMA = "#FDF0D5"
AZUL_OSCURO = "#003049"
AZUL_CLARO = "#669BBC"

# --- Conexión según nodo (desde sys.argv) ---
nodo = sys.argv[1] if len(sys.argv) > 1 else "Principal"

if nodo == "Principal":
    cadena = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DAYA;DATABASE=QRAccessControl;UID=sa;PWD=P@ssw0rd;Encrypt=yes;TrustServerCertificate=yes;'
else:
    cadena = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DELL-DANIEL\\DANIELIFE;DATABASE=QRAccessControl_Campus02;UID=sa;PWD=P@ssw0rd;Encrypt=yes;TrustServerCertificate=yes;'

conn = pyodbc.connect(cadena)

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

# --- Título y Dropdown Tabla ---
titulo_y_menu_frame = tk.Frame(header, bg=ROJO)
titulo_y_menu_frame.pack(expand=True)

label = tk.Label(titulo_y_menu_frame, text="EPN - SISTEMA CONTROL ACCESO", bg=ROJO, fg="white", font=("Arial", 20, "bold"))
label.pack(anchor="center", pady=(5, 0))

menu_tabla_frame = tk.Frame(titulo_y_menu_frame, bg=ROJO)
menu_tabla_frame.pack(anchor="center", pady=(0, 5))

tk.Label(menu_tabla_frame, text="TABLA:", bg=ROJO, fg="white", font=("Arial", 11, "bold")).pack(side="left")
tabla_seleccionada = tk.StringVar(value="Usuario")
tablas_disponibles = ["Campus", "Ingresar", "DispositivoEntrada", "Credencial", "RegistroAcceso", "Usuario", "TipoUsuario"]
tabla_menu = ttk.Combobox(menu_tabla_frame, textvariable=tabla_seleccionada, values=tablas_disponibles, state="readonly", font=("Arial", 10))
tabla_menu.pack(side="left", padx=5)

# --- Tabla con estilo ---
panel_tabla = tk.Frame(contenedor, bg=CREMA, bd=0)
panel_tabla.pack(fill="both", expand=True, padx=20, pady=(20, 0))

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("Custom.Treeview", font=("Arial", 10), rowheight=28, background=CREMA, fieldbackground=CREMA, borderwidth=0)
estilo.configure("Custom.Treeview.Heading", font=("Arial", 10, "bold"), background=AZUL_CLARO, foreground="white")

# tabla = ttk.Treeview(panel_tabla, style="Custom.Treeview", show="headings")
# Scrollbars
scroll_y = ttk.Scrollbar(panel_tabla, orient="vertical")
scroll_x = ttk.Scrollbar(panel_tabla, orient="horizontal")

tabla = ttk.Treeview(
    panel_tabla,
    style="Custom.Treeview",
    show="headings",
    yscrollcommand=scroll_y.set,
    xscrollcommand=scroll_x.set
)

scroll_y.config(command=tabla.yview)
scroll_x.config(command=tabla.xview)

# Empaquetar todo
scroll_y.pack(side="right", fill="y")
scroll_x.pack(side="bottom", fill="x")
tabla.pack(fill="both", expand=True)
tabla.pack(fill="both", expand=True)

# --- Panel de botones CRUD ---
panel_botones = tk.Frame(contenedor, bg=CREMA)
panel_botones.pack(pady=15)

# --- Panel de botones CRUD ---
panel_botones = tk.Frame(contenedor, bg=CREMA)
panel_botones.pack(pady=15)

def crear_boton(texto, comando, columna):
    boton = tk.Button(
        panel_botones,
        text=texto,
        command=comando,
        font=("Arial", 11, "bold"),
        bg=AZUL_CLARO,
        fg="white",
        activebackground=ROJO_OSCURO,
        relief="flat",
        bd=0,
        padx=15,
        pady=10
    )
    boton.grid(row=0, column=columna, padx=15)

def abrir_ventana_crear():
    top = tk.Toplevel(root)
    top.title(f"Crear en {tabla_seleccionada.get()}")
    top.geometry("400x500")
    top.configure(bg=CREMA)

    tk.Label(top, text="📝 Crear Nuevo Registro", bg=CREMA, fg=AZUL_OSCURO,
             font=("Arial", 16, "bold")).pack(pady=(15, 10))

    entradas = {}
    excluir = {"fecha", "hora"}
    for campo in tabla["columns"]:
        if campo in excluir:
            continue
        tk.Label(top, text=campo + ":", bg=CREMA, fg="black", font=("Arial", 11)).pack()
        entrada = tk.Entry(top, font=("Arial", 10))
        entrada.pack(pady=5)
        entradas[campo] = entrada

    def guardar():
        # datos = {campo: entradas[campo].get() for campo in entradas}
        # if not all(datos.values()):
        #     messagebox.showwarning("Advertencia", "Complete todos los campos.")
        #     return

        # try:
        #     modulo = importlib.import_module(f"tablas.{tabla_seleccionada.get().lower()}")
        #     with conn.cursor() as cur:
        #         modulo.crear(cur, datos)
        campos = [campo for campo in tabla["columns"] if campo not in excluir]
        valores = [entradas[campo].get() for campo in campos]

        if not all(valores):
            messagebox.showwarning("Advertencia", "Complete todos los campos.")
            return

        try:
            modulo = importlib.import_module(f"tablas.{tabla_seleccionada.get().lower()}")
            with conn.cursor() as cur:
                modulo.crear(cur, valores)
            conn.commit()
            messagebox.showinfo("Éxito", "Registro creado correctamente.")
            actualizar_columnas()
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo crear el registro:\n{e}")

    tk.Button(top, text="Guardar", command=guardar,
              font=("Arial", 11, "bold"), bg=AZUL_CLARO, fg="white",
              activebackground=ROJO_OSCURO, relief="flat").pack(pady=15, ipadx=10, ipady=4)


def abrir_ventana_buscar():
    top = tk.Toplevel(root)
    top.title(f"Buscar en {tabla_seleccionada.get()}")
    top.geometry("400x350")
    top.configure(bg=CREMA)

    # Etiqueta principal
    tk.Label(top, text="🔍 Buscar Registro", bg=CREMA, fg=AZUL_OSCURO,
             font=("Arial", 16, "bold")).pack(pady=(15, 10))

    # Campo (columna) a buscar
    tk.Label(top, text="Campo:", bg=CREMA, fg="black", font=("Arial", 11)).pack()
    combo_campo = ttk.Combobox(top, state="readonly", font=("Arial", 10))
    combo_campo['values'] = tabla["columns"]
    combo_campo.set(tabla["columns"][0])
    combo_campo.pack(pady=5)

    # Valor a buscar
    tk.Label(top, text="Valor:", bg=CREMA, fg="black", font=("Arial", 11)).pack()
    entrada_valor = tk.Entry(top, font=("Arial", 10))
    entrada_valor.pack(pady=5)

    # Botón buscar
    def ejecutar_busqueda():
        campo = combo_campo.get()
        valor = entrada_valor.get()
        if not valor:
            messagebox.showwarning("Advertencia", "Ingrese un valor para buscar.")
            return

        try:
            tabla.delete(*tabla.get_children())
            modulo = importlib.import_module(f"tablas.{tabla_seleccionada.get().lower()}")

            with conn.cursor() as cur:
                resultados = modulo.buscar(cur, campo, valor)
                for fila in resultados:
                    tabla.insert("", "end", values=[str(col) for col in fila])

            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo ejecutar la búsqueda:\n{e}")

    tk.Button(top, text="Buscar", command=ejecutar_busqueda,
              font=("Arial", 11, "bold"), bg=AZUL_CLARO, fg="white",
              activebackground=ROJO_OSCURO, relief="flat").pack(pady=15, ipadx=10, ipady=4)

# def abrir_ventana_actualizar():
#     seleccionado = tabla.focus()
#     if not seleccionado:
#         messagebox.showwarning("Advertencia", "Seleccione un registro para actualizar.")
#         return

#     valores_originales = tabla.item(seleccionado, "values")
#     campos = tabla["columns"]

#     top = tk.Toplevel(root)
#     top.title(f"Actualizar {tabla_seleccionada.get()}")
#     top.geometry("400x500")
#     top.configure(bg=CREMA)

#     tk.Label(top, text="✏️ Actualizar Registro", bg=CREMA, fg=AZUL_OSCURO,
#              font=("Arial", 16, "bold")).pack(pady=(15, 10))

#     entradas = {}

#     for i, campo in enumerate(campos):
#         tk.Label(top, text=f"{campo}:", bg=CREMA, fg="black", font=("Arial", 11)).pack()
#         entrada = tk.Entry(top, font=("Arial", 10))
#         entrada.insert(0, valores_originales[i])
#         entrada.pack(pady=5)
#         entradas[campo] = entrada

#     def guardar_cambios():
#         nuevos_valores = {
#             campo: entradas[campo].get()
#             for campo in campos
#             if entradas[campo].get().strip() != "" and entradas[campo].get() != valores_originales[campos.index(campo)]
#         }

#         if not nuevos_valores:
#             messagebox.showinfo("Sin cambios", "No se ha modificado ningún campo.")
#             return

#         try:
#             # Suponemos que siempre hay id único + fragmento como primeras columnas
#             id_valor = valores_originales[0]
#             id_fragmento = valores_originales[1]

#             set_clause = ", ".join(
#                 f"{campo} = '{valor}'"
#                 for campo, valor in nuevos_valores.items()
#             )

#             modulo = importlib.import_module(f"tablas.{tabla_seleccionada.get().lower()}")
#             with conn.cursor() as cur:
#                 modulo.actualizar(cur, id_valor, id_fragmento, set_clause)

#             conn.commit()
#             messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
#             actualizar_columnas()
#             top.destroy()
#         except Exception as e:
#             messagebox.showerror("Error", f"No se pudo actualizar el registro:\n{e}")

#     tk.Button(top, text="Guardar Cambios", command=guardar_cambios,
#               font=("Arial", 11, "bold"), bg=AZUL_CLARO, fg="white",
#               activebackground=ROJO_OSCURO, relief="flat").pack(pady=15, ipadx=10, ipady=4)

def abrir_ventana_actualizar():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Seleccione un registro para actualizar.")
        return

    valores = tabla.item(seleccionado, "values")
    campos = tabla["columns"]

    top = tk.Toplevel(root)
    top.title(f"Actualizar {tabla_seleccionada.get()}")
    top.geometry("400x500")
    top.configure(bg=CREMA)

    tk.Label(top, text="✏️ Actualizar Registro", bg=CREMA, fg=AZUL_OSCURO,
             font=("Arial", 16, "bold")).pack(pady=(15, 10))

    entradas = {}

    for i, campo in enumerate(campos):
        tk.Label(top, text=f"{campo}:", bg=CREMA, fg="black", font=("Arial", 11)).pack()
        entrada = tk.Entry(top, font=("Arial", 10))
        entrada.insert(0, valores[i])
        entrada.pack(pady=5)
        entradas[campo] = entrada

    def guardar_cambios():
        nuevos_valores = {campo: entradas[campo].get() for campo in campos}
        if not all(nuevos_valores.values()):
            messagebox.showwarning("Advertencia", "Complete todos los campos.")
            return

        try:
            modulo = importlib.import_module(f"tablas.{tabla_seleccionada.get().lower()}")
            with conn.cursor() as cur:
                modulo.actualizar(cur, nuevos_valores)
            conn.commit()
            messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
            actualizar_columnas()
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo actualizar el registro:\n{e}")

    tk.Button(top, text="Guardar cambios", command=guardar_cambios,
              font=("Arial", 11, "bold"), bg=AZUL_CLARO, fg="white",
              activebackground=ROJO_OSCURO, relief="flat").pack(pady=15, ipadx=10, ipady=4)

# Columnas necesarias para eliminar registros por tabla
columnas_para_eliminar = {
    "RegistroAcceso": ["idRegistro", "idCampus"],
    "Ingresar": ["idCredencial", "idCampus"],
    "Usuario": ["idUsuario"],
    "DispositivoEntrada": ["idDispositivo"],
    "TipoUsuario": ["idTipo"],
    "Campus": ["idCampus"],
    "Credencial": ["idCredencial"]
    # Puedes incluir más según tu criterio, no hace falta que tengan PK real
}

def abrir_ventana_eliminar():
    seleccionado = tabla.focus()
    if not seleccionado:
        messagebox.showwarning("Advertencia", "Seleccione un registro para eliminar.")
        return

    valores = tabla.item(seleccionado, "values")
    tabla_actual = tabla_seleccionada.get()

    claves = columnas_para_eliminar.get(tabla_actual, tabla["columns"][:1])  # usa al menos la 1.ª columna
    valores_clave = [valores[tabla["columns"].index(col)] for col in claves]

    # Ventana de confirmación
    top = tk.Toplevel(root)
    top.title("Confirmar Eliminación")
    top.geometry("420x280")
    top.configure(bg=CREMA)
    top.grab_set()

    tk.Label(top, text="🗑️ Confirmar Eliminación", bg=CREMA, fg=ROJO_OSCURO,
             font=("Arial", 16, "bold")).pack(pady=(20, 10))

    tk.Label(top, text=f"¿Deseas eliminar de la tabla '{tabla_actual}' este registro?", 
             bg=CREMA, fg="black", font=("Arial", 12)).pack()

    for col, val in zip(claves, valores_clave):
        tk.Label(top, text=f"{col} = {val}", bg=CREMA, fg=AZUL_OSCURO, font=("Arial", 11)).pack()

    def confirmar_eliminar():
        try:
            modulo = importlib.import_module(f"tablas.{tabla_actual.lower()}")
            with conn.cursor() as cur:
                modulo.eliminar(cur, *valores_clave)  # se pasan los valores clave definidos
            conn.commit()
            messagebox.showinfo("Éxito", "Registro eliminado correctamente.")
            actualizar_columnas()
            top.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo eliminar el registro:\n{e}")

    botones = tk.Frame(top, bg=CREMA)
    botones.pack(pady=15)
    tk.Button(botones, text="Cancelar", command=top.destroy,
              font=("Arial", 10, "bold"), bg=AZUL_CLARO, fg="white").grid(row=0, column=0, padx=10)
    tk.Button(botones, text="Eliminar", command=confirmar_eliminar,
              font=("Arial", 10, "bold"), bg=ROJO_OSCURO, fg="white").grid(row=0, column=1, padx=10)

# Reemplaza los lambda de prueba por las funciones reales
crear_boton("CREAR", abrir_ventana_crear, 0)
crear_boton("BUSCAR", abrir_ventana_buscar, 1)
crear_boton("ACTUALIZAR", abrir_ventana_actualizar, 2)
crear_boton("ELIMINAR", abrir_ventana_eliminar, 3)



# --- Callback actualizar columnas + cargar datos ---
def actualizar_columnas(*args):
    tabla.delete(*tabla.get_children())

    columnas = {
        "Campus": ["idCampus", "direccionCampus", "nombreCampus"],
        "Ingresar": ["idCredencial", "idCampus"],
        "DispositivoEntrada": ["idDispositivo", "idCampus", "tipoDispositivo", "ubicacion"],
        "Credencial": ["idCredencial", "tipoCredencial", "idUsuario", "estadoCredencial"],
        "RegistroAcceso": ["idRegistro", "idCampus", "idCredencial", "idDispositivo", "evento", "fecha", "hora"],
        "Usuario": ["idUsuario", "nombre", "apellido", "correo", "idTipoUsuario", "estadoUsuario", "idCampus"],
        "TipoUsuario": ["idTipo", "descripcionTipo"]
    }[tabla_seleccionada.get()]

    tabla["columns"] = columnas
    for col in columnas:
        tabla.heading(col, text=col)
        tabla.column(col, width=180, anchor="center")

    try:
        modulo = importlib.import_module(f"tablas.{tabla_seleccionada.get().lower()}")
        with conn.cursor() as cur:
            modulo.cargar_datos(tabla, cur)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo cargar datos: {e}")

# --- Vincular evento ---
tabla_menu.bind("<<ComboboxSelected>>", actualizar_columnas)

# Inicializar columnas
actualizar_columnas()

root.mainloop()
