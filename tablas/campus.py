def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM Campus")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarCampus ?, ?", campo, valor)
    return cursor.fetchall()


def crear(cursor, valores):
    if not isinstance(valores, list):
        raise ValueError("Se esperaba una lista ordenada, no un diccionario")
    cursor.execute("EXEC spInsertarCampus ?,?,?", valores)

def actualizar(cursor, datos):
    cursor.execute("""
        EXEC spActualizarCampus 
            @idCampus = ?,
            @direccionCampus = ?,
            @nombreCampus = ?
    """, (
        datos["idCampus"],
        datos["direccionCampus"],
        datos["nombreCampus"]
    ))
def eliminar(cursor, id_campus):
    cursor.execute("EXEC spEliminarCampus ?", (id_campus,))