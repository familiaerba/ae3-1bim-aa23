from scriptBaseDatos import conexion

sql_crear_entidad = 'CREATE TABLE Jugador (codigo INTEGER,nombre TEXT, \
    nombreEquipo TEXT, edad INTEGER)'

print ("Ejecucion de sql para creacion de Jugador")

cursor = conexion.cursor()

cursor.execute(sql_crear_entidad)

cursor.close()

print ("Ejecucion finalizada")