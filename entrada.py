# import tkinter as tk
# from tkinter import ttk
# from tkinter import Canvas
# from PIL import Image, ImageTk

# # --- Colores institucionales ---
# ROJO_OSCURO = "#780000"
# ROJO = "#C1121F"
# CREMA = "#FDF0D5"
# AZUL_OSCURO = "#003049"
# AZUL_CLARO = "#669BBC"

# # --- Interfaz ---
# ventana = tk.Tk()
# ventana.title("Gestión de Accesos - EPN")
# ventana.geometry("600x400")
# ventana.configure(bg=AZUL_OSCURO)
# ventana.resizable(False, False)

# # --- Marco principal sin panel crema ---
# frame_principal = tk.Frame(ventana, bg=AZUL_OSCURO)
# frame_principal.place(relx=0.5, rely=0.4, anchor="center")

# # --- Título ---
# label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg="white", bg=AZUL_OSCURO)
# label_titulo.pack(pady=(30, 10))

# # --- Bienvenida ---
# label_bienvenida = tk.Label(frame_principal, text="¡Bienvenido al Sistema!", font=("Arial", 14), fg=CREMA, bg=AZUL_OSCURO)
# label_bienvenida.pack(pady=10)

# # --- Botón continuar ---
# def continuar():
#     ventana.destroy()

# boton_continuar = tk.Button(
#     frame_principal,
#     text="CONTINUAR",
#     font=("Arial", 12, "bold"),
#     bg=ROJO_OSCURO,
#     fg="white",
#     activebackground=ROJO_OSCURO,
#     relief="flat",
#     command=continuar
# )
# boton_continuar.pack(pady=20, ipadx=10, ipady=5)
# boton_continuar.configure(highlightthickness=0, bd=0)

# # --- Imagen del búho (cargada con Pillow) ---
# try:
#     imagen_buho = Image.open("./buho2.png")
#     imagen_buho = imagen_buho.resize((160, 160), Image.Resampling.LANCZOS)
#     buho_tk = ImageTk.PhotoImage(imagen_buho)
#     ventana.buho_img = buho_tk  # Referencia persistente
#     label_buho = tk.Label(ventana, image=ventana.buho_img, bg=AZUL_OSCURO, borderwidth=0)
#     label_buho.place(x=430, y=240)
#     label_buho.lift()  # <-- asegurar que el búho esté al frente
# except Exception as e:
#     print("No se pudo cargar la imagen del búho:", e)

# ventana.mainloop()

import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from PIL import Image, ImageTk
import pyodbc
import subprocess

# --- Colores institucionales ---
ROJO_OSCURO = "#780000"
ROJO = "#C1121F"
CREMA = "#FDF0D5"
AZUL_OSCURO = "#003049"
AZUL_CLARO = "#669BBC"

# --- Interfaz ---
ventana = tk.Tk()
ventana.title("Gestión de Accesos - EPN")
ventana.geometry("600x400")
ventana.configure(bg=AZUL_OSCURO)
ventana.resizable(False, False)

# --- Marco principal ---
frame_principal = tk.Frame(ventana, bg=AZUL_OSCURO)
frame_principal.place(relx=0.5, rely=0.35, anchor="center")

# --- Título ---
label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg="white", bg=AZUL_OSCURO)
label_titulo.pack(pady=(30, 10))

# --- Bienvenida ---
label_bienvenida = tk.Label(frame_principal, text="Seleccione el nodo para continuar", font=("Arial", 14), fg=CREMA, bg=AZUL_OSCURO)
label_bienvenida.pack(pady=10)

# --- Selección de nodo ---
frame_login = tk.Frame(frame_principal, bg=AZUL_OSCURO)
frame_login.pack(pady=5)

tk.Label(frame_login, text="Nodo:", font=("Arial", 12), fg=CREMA, bg=AZUL_OSCURO).pack(side="left", padx=5)
nodo_var = tk.StringVar(value="Principal")
combo_nodo = ttk.Combobox(frame_login, textvariable=nodo_var, values=["Principal", "El Bosque"], state="readonly", font=("Arial", 11))
combo_nodo.pack(side="left")

# --- Botón continuar ---
def continuar():
    nodo = nodo_var.get()
    if nodo == "Principal":
        cadena = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DAYA;DATABASE=QRAccessControl;UID=sa;PWD=P@ssw0rd;Encrypt=yes;TrustServerCertificate=yes;'
    else:
        cadena = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=DELL-DANIEL\\DANIELIFE;DATABASE=QRAccessControl_Campus02;UID=sa;PWD=P@ssw0rd;Encrypt=yes;TrustServerCertificate=yes;'
    
    try:
        conn = pyodbc.connect(cadena)
        conn.close()
        ventana.destroy()
        subprocess.Popen(["python", "crud_panel.py", nodo])
    except Exception as e:
        tk.messagebox.showerror("Error de conexión", f"No se pudo conectar al nodo seleccionado:\n{e}")

boton_continuar = tk.Button(
    frame_principal,
    text="CONTINUAR",
    font=("Arial", 12, "bold"),
    bg=ROJO_OSCURO,
    fg="white",
    activebackground=ROJO_OSCURO,
    relief="flat",
    command=continuar
)
boton_continuar.pack(pady=20, ipadx=10, ipady=5)
boton_continuar.configure(highlightthickness=0, bd=0)

# --- Imagen del búho (cargada con Pillow) ---
try:
    imagen_buho = Image.open("./buho2.png")
    imagen_buho = imagen_buho.resize((160, 160), Image.Resampling.LANCZOS)
    buho_tk = ImageTk.PhotoImage(imagen_buho)
    ventana.buho_img = buho_tk
    label_buho = tk.Label(ventana, image=ventana.buho_img, bg=AZUL_OSCURO, borderwidth=0)
    label_buho.place(x=430, y=240)
    label_buho.lift()
except Exception as e:
    print("No se pudo cargar la imagen del búho:", e)

ventana.mainloop()
