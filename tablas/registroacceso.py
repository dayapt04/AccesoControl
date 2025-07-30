# def cargar_datos(tabla, cursor):
#     cursor.execute("SELECT idRegistro, idCampus, idCredencial, idDispositivo, evento, fecha, hora FROM vistaRegistroAcceso")
#     for fila in cursor.fetchall():
#         tabla.insert("", "end", values=fila)

def cargar_datos(tabla, cursor):
    cursor.execute("SELECT idRegistro, idCampus, idCredencial, idDispositivo, evento, fecha, hora FROM vistaRegistroAcceso")
    for fila in cursor.fetchall():
        idRegistro, idCampus, idCredencial, idDispositivo, evento, fecha, hora = fila

        fecha_str = fecha.strftime("%d/%m/%Y") if fecha else ""
        hora_str = hora.strftime("%H:%M:%S") if hora else ""

        fila_formateada = [
            str(idRegistro),
            str(idCampus),
            str(idCredencial),
            str(idDispositivo),
            str(evento),
            fecha_str,
            hora_str
        ]

        tabla.insert("", "end", values=fila_formateada)

# def buscar(tabla, cursor, campo, valor):
#     """
#     Ejecuta el procedimiento almacenado de búsqueda y llena la tabla con los resultados.
#     """
#     try:
#         tabla.delete(*tabla.get_children())
#         cursor.execute("EXEC spBuscarRegistroAcceso ?, ?", (campo, valor))
#         for fila in cursor.fetchall():
#             tabla.insert("", "end", values=[str(col) for col in fila])
#     except Exception as e:
#         from tkinter import messagebox
#         messagebox.showerror("Error al buscar", f"No se pudo ejecutar la búsqueda:\n{e}")

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarRegistroAcceso ?, ?", campo, valor)
    return cursor.fetchall()
# tablas/registroacceso.py

def crear(cursor, valores):
    if not isinstance(valores, list):
        raise ValueError("Se esperaba una lista ordenada, no un diccionario")
    cursor.execute("EXEC spInsertarRegistroAcceso ?, ?, ?, ?, ?", valores)

def eliminar(cursor, id_registro, id_campus):
    cursor.execute("EXEC spEliminarRegistroAcceso ?, ?", (id_registro, id_campus))