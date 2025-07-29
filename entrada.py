# # # import tkinter as tk
# # # from tkinter import ttk
# # # import threading
# # # import time

# # # # --- Funciones ---
# # # def efecto_carga():
# # #     progreso.start()
# # #     label_estado.config(text="Cargando datos...")
# # #     threading.Thread(target=carga_rapida).start()

# # # def carga_rapida():
# # #     time.sleep(2)  # Simula una carga breve
# # #     progreso.stop()
# # #     label_estado.config(text="¡Bienvenido al Sistema de Gestión de Accesos!")
# # #     boton_continuar.config(state=tk.NORMAL)

# # # def continuar():
# # #     ventana.destroy()
# # #     # Aquí se abriría la siguiente pantalla real

# # # # --- Interfaz ---
# # # ventana = tk.Tk()
# # # ventana.title("Gestión de Accesos - EPN")
# # # ventana.geometry("600x400")
# # # ventana.configure(bg="#0a2e44")
# # # ventana.resizable(False, False)

# # # # --- Título ---
# # # label_titulo = tk.Label(ventana, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg="white", bg="#0a2e44")
# # # label_titulo.pack(pady=30)

# # # # --- Mensaje bienvenida ---
# # # label_estado = tk.Label(ventana, text="Iniciando...", font=("Arial", 14), fg="white", bg="#0a2e44")
# # # label_estado.pack(pady=10)

# # # # --- Barra de progreso ---
# # # progreso = ttk.Progressbar(ventana, orient="horizontal", length=300, mode="indeterminate")
# # # progreso.pack(pady=20)

# # # # --- Botón para continuar ---
# # # boton_continuar = tk.Button(ventana, text="CONTINUAR", font=("Arial", 12, "bold"), bg="#c62828", fg="white", command=continuar, state=tk.DISABLED)
# # # boton_continuar.pack(pady=10)

# # # # Inicia carga automática
# # # ventana.after(500, efecto_carga)
# # # ventana.mainloop()
# # import tkinter as tk
# # from tkinter import ttk
# # from tkinter import Canvas

# # # --- Colores institucionales ---
# # ROJO_OSCURO = "#780000"
# # ROJO = "#C1121F"
# # CREMA = "#FDF0D5"
# # AZUL_OSCURO = "#003049"
# # AZUL_CLARO = "#669BBC"

# # # --- Interfaz ---
# # ventana = tk.Tk()
# # ventana.title("Gestión de Accesos - EPN")
# # ventana.geometry("600x400")
# # ventana.configure(bg=AZUL_OSCURO)
# # ventana.resizable(False, False)

# # # --- Canvas para bordes redondeados (estética moderna) ---
# # canvas = Canvas(ventana, width=600, height=400, bg=AZUL_OSCURO, highlightthickness=0)
# # canvas.place(x=0, y=0)
# # canvas.create_rectangle(20, 20, 580, 380, outline="", fill=CREMA, width=0)

# # # --- Marco principal redondeado ---
# # frame_principal = tk.Frame(ventana, bg=CREMA)
# # frame_principal.place(relx=0.5, rely=0.5, anchor="center")

# # # --- Título ---
# # label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg=AZUL_OSCURO, bg=CREMA)
# # label_titulo.pack(pady=(30, 10))

# # # --- Bienvenida ---
# # label_bienvenida = tk.Label(frame_principal, text="¡Bienvenido al Sistema!", font=("Arial", 14), fg=ROJO_OSCURO, bg=CREMA)
# # label_bienvenida.pack(pady=10)

# # # --- Botón continuar ---
# # def continuar():
# #     ventana.destroy()

# # boton_continuar = tk.Button(
# #     frame_principal,
# #     text="CONTINUAR",
# #     font=("Arial", 12, "bold"),
# #     bg=ROJO,
# #     fg="white",
# #     activebackground=ROJO_OSCURO,
# #     relief="flat",
# #     command=continuar
# # )
# # boton_continuar.pack(pady=20, ipadx=10, ipady=5)
# # boton_continuar.configure(highlightthickness=0, bd=0)

# # ventana.mainloop()

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

# # --- Canvas para bordes redondeados (estética moderna) ---
# canvas = Canvas(ventana, width=600, height=400, bg=AZUL_OSCURO, highlightthickness=0)
# canvas.place(x=0, y=0)
# canvas.create_rectangle(20, 20, 580, 380, outline="", fill=CREMA, width=0)

# # --- Imagen del búho (cargada con Pillow) ---
# try:
#     imagen_buho = Image.open("./buho2.png")
#     imagen_buho = imagen_buho.resize((80, 80), Image.ANTIALIAS)
#     buho_tk = ImageTk.PhotoImage(imagen_buho)
#     canvas.create_image(550, 340, image=buho_tk, anchor="center")
# except Exception as e:
#     print("No se pudo cargar la imagen del búho:", e)

# # --- Marco principal redondeado ---
# frame_principal = tk.Frame(ventana, bg=CREMA)
# frame_principal.place(relx=0.5, rely=0.5, anchor="center")

# # --- Título ---
# label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg=AZUL_OSCURO, bg=CREMA)
# label_titulo.pack(pady=(30, 10))

# # --- Bienvenida ---
# label_bienvenida = tk.Label(frame_principal, text="¡Bienvenido al Sistema!", font=("Arial", 14), fg=ROJO_OSCURO, bg=CREMA)
# label_bienvenida.pack(pady=10)

# # --- Botón continuar ---
# def continuar():
#     ventana.destroy()

# boton_continuar = tk.Button(
#     frame_principal,
#     text="CONTINUAR",
#     font=("Arial", 12, "bold"),
#     bg=ROJO,
#     fg="white",
#     activebackground=ROJO_OSCURO,
#     relief="flat",
#     command=continuar
# )
# boton_continuar.pack(pady=20, ipadx=10, ipady=5)
# boton_continuar.configure(highlightthickness=0, bd=0)

# ventana.mainloop()

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

# # --- Canvas para bordes redondeados (estética moderna) ---
# canvas = Canvas(ventana, width=600, height=400, bg=AZUL_OSCURO, highlightthickness=0)
# canvas.place(x=0, y=0)
# canvas.create_rectangle(20, 20, 580, 380, outline="", fill=CREMA, width=0)

# # --- Imagen del búho (cargada con Pillow) ---
# try:
#     imagen_buho = Image.open("./buho2.png")
#     imagen_buho = imagen_buho.resize((80, 80), Image.Resampling.LANCZOS)
#     buho_tk = ImageTk.PhotoImage(imagen_buho)
#     canvas.create_image(550, 340, image=buho_tk, anchor="center")
# except Exception as e:
#     print("No se pudo cargar la imagen del búho:", e)

# # --- Marco principal redondeado ---
# frame_principal = tk.Frame(ventana, bg=CREMA)
# frame_principal.place(relx=0.5, rely=0.5, anchor="center")

# # --- Título ---
# label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg=AZUL_OSCURO, bg=CREMA)
# label_titulo.pack(pady=(30, 10))

# # --- Bienvenida ---
# label_bienvenida = tk.Label(frame_principal, text="¡Bienvenido al Sistema!", font=("Arial", 14), fg=ROJO_OSCURO, bg=CREMA)
# label_bienvenida.pack(pady=10)

# # --- Botón continuar ---
# def continuar():
#     ventana.destroy()

# boton_continuar = tk.Button(
#     frame_principal,
#     text="CONTINUAR",
#     font=("Arial", 12, "bold"),
#     bg=ROJO,
#     fg="white",
#     activebackground=ROJO_OSCURO,
#     relief="flat",
#     command=continuar
# )
# boton_continuar.pack(pady=20, ipadx=10, ipady=5)
# boton_continuar.configure(highlightthickness=0, bd=0)

# ventana.mainloop()

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

# # --- Canvas para bordes redondeados (estética moderna) ---
# canvas = Canvas(ventana, width=600, height=400, bg=AZUL_OSCURO, highlightthickness=0)
# canvas.place(x=0, y=0)
# canvas.create_rectangle(20, 20, 580, 380, outline="", fill=CREMA, width=0)

# # --- Imagen del búho (cargada con Pillow) ---
# try:
#     imagen_buho = Image.open("./buho2.png")
#     imagen_buho = imagen_buho.resize((130, 130), Image.Resampling.LANCZOS)
#     # buho_tk = ImageTk.PhotoImage(imagen_buho)
#     # canvas.create_image(520, 310, image=buho_tk, anchor="center")
#     buho_tk = ImageTk.PhotoImage(imagen_buho)
#     canvas.buho_img = buho_tk  # <- evitar que se elimine por garbage collection
#     canvas.create_image(520, 310, image=canvas.buho_img, anchor="center")

# except Exception as e:
#     print("No se pudo cargar la imagen del búho:", e)

# # --- Marco principal redondeado ---
# frame_principal = tk.Frame(ventana, bg=CREMA)
# frame_principal.place(relx=0.5, rely=0.5, anchor="center")

# # --- Título ---
# label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg=AZUL_OSCURO, bg=CREMA)
# label_titulo.pack(pady=(30, 10))

# # --- Bienvenida ---
# label_bienvenida = tk.Label(frame_principal, text="¡Bienvenido al Sistema!", font=("Arial", 14), fg=ROJO_OSCURO, bg=CREMA)
# label_bienvenida.pack(pady=10)

# # --- Botón continuar ---
# def continuar():
#     ventana.destroy()

# boton_continuar = tk.Button(
#     frame_principal,
#     text="CONTINUAR",
#     font=("Arial", 12, "bold"),
#     bg=ROJO,
#     fg="white",
#     activebackground=ROJO_OSCURO,
#     relief="flat",
#     command=continuar
# )
# boton_continuar.pack(pady=20, ipadx=10, ipady=5)
# boton_continuar.configure(highlightthickness=0, bd=0)

# ventana.mainloop()



import tkinter as tk
from tkinter import ttk
from tkinter import Canvas
from PIL import Image, ImageTk

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

# --- Marco principal sin panel crema ---
frame_principal = tk.Frame(ventana, bg=AZUL_OSCURO)
frame_principal.place(relx=0.5, rely=0.4, anchor="center")

# --- Título ---
label_titulo = tk.Label(frame_principal, text="ESCUELA POLITÉCNICA NACIONAL\nGESTIÓN DE ACCESOS", font=("Arial", 18, "bold"), fg="white", bg=AZUL_OSCURO)
label_titulo.pack(pady=(30, 10))

# --- Bienvenida ---
label_bienvenida = tk.Label(frame_principal, text="¡Bienvenido al Sistema!", font=("Arial", 14), fg=CREMA, bg=AZUL_OSCURO)
label_bienvenida.pack(pady=10)

# --- Botón continuar ---
def continuar():
    ventana.destroy()

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
    ventana.buho_img = buho_tk  # Referencia persistente
    label_buho = tk.Label(ventana, image=ventana.buho_img, bg=AZUL_OSCURO, borderwidth=0)
    label_buho.place(x=430, y=240)
    label_buho.lift()  # <-- asegurar que el búho esté al frente
except Exception as e:
    print("No se pudo cargar la imagen del búho:", e)

ventana.mainloop()
