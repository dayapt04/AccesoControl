def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaCredencial")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarCredencial ?, ?", campo, valor)
    return cursor.fetchall()

def crear(cursor, valores):
    cursor.execute("EXEC spInsertarCredencial ?,?,?,?", valores)

def actualizar(cursor, datos):
    cursor.execute("""
        EXEC spActualizarCredencial 
            @idCredencial = ?, 
            @tipoCredencial = ?, 
            @idUsuario = ?, 
            @estadoCredencial = ?
    """, (
        datos["idCredencial"],
        datos["tipoCredencial"],
        datos["idUsuario"],
        datos["estadoCredencial"]
    ))

def eliminar(cursor, id_credencial):
    cursor.execute("EXEC spEliminarCredencial ?", (id_credencial,))