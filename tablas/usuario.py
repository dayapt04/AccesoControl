def cargar_datos(tabla, cursor):
    cursor.execute("SELECT * FROM vistaUsuario")
    for fila in cursor.fetchall():
        tabla.insert("", "end", values=[str(col) for col in fila])

def buscar(cursor, campo, valor):
    cursor.execute("EXEC spBuscarUsuario ?, ?", campo, valor)
    return cursor.fetchall()

def crear(cursor, valores):
    if not isinstance(valores, list):
        raise ValueError("Se esperaba una lista ordenada, no un diccionario")
    cursor.execute("EXEC spInsertarUsuario ?,?,?,?,?,?,?", valores)

def actualizar(cursor, datos):
    id_usuario = datos["idUsuario"]
    id_campus = datos["idCampus"]

    # Ejecutar spActualizarUsuario para los datos
    cursor.execute("""
        EXEC spActualizarUsuario
            @idUsuario=?,
            @campo1=?, @valor1=?,
            @campo2=?, @valor2=?,
            @campo3=?, @valor3=?,
            @idCampus=?
    """, (
        id_usuario,
        "nombre", datos["nombre"],
        "apellido", datos["apellido"],
        "correo", datos["correo"],
        id_campus
    ))

    # Luego actualizar estadoUsuario (UsuarioValidacion)
    cursor.execute("""
        EXEC spActualizarUsuarioValidacion
            @idUsuario=?, @estadoUsuario=?, @idCampus=?
    """, (
        id_usuario,
        datos["estadoUsuario"],
        id_campus
    ))



def eliminar(cursor, id_usuario):
    cursor.execute("EXEC spEliminarUsuario ?", (id_usuario,))
