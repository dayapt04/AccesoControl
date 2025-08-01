def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM TipoUsuario")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarTipoUsuario ?, ?", campo, valor)
    return cursor.fetchall()

def crear(cursor, valores):
    cursor.execute("EXEC spInsertarTipoUsuario ?,?", valores)

def actualizar(cursor, datos):
    cursor.execute("""
        EXEC spActualizarTipoUsuario 
            @idTipoUsuario = ?,
            @descripcionTipo = ?
    """, (
        datos["idTipoUsuario"],
        datos["descripcionTipo"]
    ))

def eliminar(cursor, id_tipo_usuario):
    cursor.execute("EXEC spEliminarTipoUsuario ?", (id_tipo_usuario,))