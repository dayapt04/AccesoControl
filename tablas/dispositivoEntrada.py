def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaDispositivoEntrada")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarDispositivoEntrada ?, ?", campo, valor)
    return cursor.fetchall()

def crear(cursor, valores):
    cursor.execute("EXEC spInsertarDispositivoEntrada ?,?,?,?", valores)

def actualizar(cursor, datos):
    cursor.execute(
        "EXEC spActualizarDispositivoEntrada ?, ?, ?",
        datos["idDispositivo"],
        datos["tipoDispositivo"],
        datos["ubicacion"]
    )


def eliminar(cursor, id_dispositivo_entrada, idCampus):
    cursor.execute("EXEC spEliminarDispositivoEntrada ?, ?", (id_dispositivo_entrada, idCampus))