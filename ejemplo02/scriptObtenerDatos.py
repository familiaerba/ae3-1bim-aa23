from scriptBaseDatos import conexion

cursor = conexion.cursor()
print("Extraer informacion de entidad Jugador")
consulta_sql = "SELECT * from jugador"
cursor.execute(consulta_sql)
resultado = cursor.fetchall()
print("%s - %s - %s - %s " % ("Codigo", "Nombre", "Equipo", "Edad"))
for dato in resultado:
    print("%d - %s - %s - %d " % (dato[0], dato[1], dato[2], dato[3]))