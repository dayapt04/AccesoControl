def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaCredencial")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarCredencial ?, ?", campo, valor)
    return cursor.fetchall()

def insertar(cursor, valores):
    cursor.execute("EXEC spInsertarCredencial ?,?,?,?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarCredencial ?,?,?,?,?", valores)

def eliminar(cursor, id_credencial):
    cursor.execute("EXEC spEliminarCredencial ?", (id_credencial,))