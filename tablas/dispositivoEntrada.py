def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaDispositivoEntrada")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarDispositivoEntrada ?, ?", campo, valor)
    return cursor.fetchall()

def insertar(cursor, valores):
    cursor.execute("EXEC spInsertarDispositivoEntrada ?,?,?,?,?", valores)

def actualizar(cursor, valores):
    cursor.execute("EXEC spActualizarDispositivoEntrada ?,?,?,?,?", valores)

def eliminar(cursor, id_dispositivo_entrada):
    cursor.execute("EXEC spEliminarDispositivoEntrada ?", (id_dispositivo_entrada,))