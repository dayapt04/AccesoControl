def cargar_datos(tabla, cursor):
    cursor.execute("SELECT idCredencial, idCampus FROM vistaIngresar")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarIngresar ?, ?", campo, valor)
    return cursor.fetchall()

def insertar(cursor, valores):
    cursor.execute("EXEC spInsertarIngresar ?,?,?,?,?", valores)

def crear(cursor, valores):
    if not isinstance(valores, list):
        raise ValueError("Se esperaba una lista ordenada, no un diccionario")
    cursor.execute("EXEC spInsertarIngresar ?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarIngresar ?,?", valores)

def eliminar(cursor, id_credencial, id_campus):
    cursor.execute("EXEC spEliminarIngresar ?, ?", (id_credencial, id_campus))