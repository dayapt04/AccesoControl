def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaUsuario")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarUsuario ?, ?", campo, valor)
    return cursor.fetchall()

def crear(cursor, valores):
    if not isinstance(valores, list):
        raise ValueError("Se esperaba una lista ordenada, no un diccionario")
    cursor.execute("EXEC spInsertarUsuario ?,?,?,?,?,?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarUsuario ?,?,?,?,?,?,?", valores)

def eliminar(cursor, id_usuario):
    cursor.execute("EXEC spEliminarUsuario ?", (id_usuario,))
