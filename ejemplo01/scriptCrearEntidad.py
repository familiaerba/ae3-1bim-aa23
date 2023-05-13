from scriptBaseDatos import conexion

sql_crear_entidad = 'CREATE TABLE Equipo (codigo TEXT, nombre TEXT, ciudad TEXT)'

print ("Ejecucion de sql para creacion de Equipo")

cursor = conexion.cursor()

cursor.execute(sql_crear_entidad)

cursor.close()

print ("Ejecucion finalizada")