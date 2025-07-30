def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM Campus")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarCampus ?, ?", campo, valor)
    return cursor.fetchall()

def insertar(cursor, valores):
    cursor.execute("EXEC spInsertarCampus ?,?,?,?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarCampus ?,?,?,?,?", valores)

def eliminar(cursor, id_campus):
    cursor.execute("EXEC spEliminarCampus ?", (id_campus,))