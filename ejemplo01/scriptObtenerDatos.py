from scriptBaseDatos import conexion

cursor = conexion.cursor()
print("Extraer informacion de entidad Equipo")
consulta_sql = "SELECT * from Equipo"
cursor.execute(consulta_sql)
resultado = cursor.fetchall()
print("%s - %s - %s " % ("Codigo", "Nombre", "Ciudad"))
for dato in resultado:
    print("%s - %s - %s " % (dato[0], dato[1], dato[2]))