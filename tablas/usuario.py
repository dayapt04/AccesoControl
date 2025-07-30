def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaUsuario")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=fila)

def insertar(cursor, valores):
    cursor.execute("EXEC spInsertarUsuario ?,?,?,?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarUsuario ?,?,?,?,?", valores)

def eliminar(cursor, id_usuario):
    cursor.execute("EXEC spEliminarUsuario ?", (id_usuario,))
