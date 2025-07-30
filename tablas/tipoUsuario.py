def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM TipoUsuario")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarTipoUsuario ?, ?", campo, valor)
    return cursor.fetchall()

def insertar(cursor, valores):
    cursor.execute("EXEC spInsertarTipoUsuario ?,?,?,?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarTipoUsuario ?,?,?,?,?", valores)

def eliminar(cursor, id_tipo_usuario):
    cursor.execute("EXEC spEliminarTipoUsuario ?", (id_tipo_usuario,))