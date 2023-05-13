from scriptBaseDatos import conexion

cursor = conexion.cursor()

codigo = "Equipo01"
nombre = "Barcelona"
ciudad = "Guayaquil"
sql = """INSERT INTO Equipo (codigo, nombre, ciudad) \
VALUES ('%s', '%s', '%s');""" % (codigo, nombre, ciudad)

cursor.execute(sql)

codigo = "Equipo02"
nombre = "Emelec"
ciudad = "Guayaquil"
sql = """INSERT INTO Equipo (codigo, nombre, ciudad) \
VALUES ('%s', '%s', '%s');""" % (codigo, nombre, ciudad)

cursor.execute(sql)

codigo = "Equipo03"
nombre = "Nacional"
ciudad = "Quito"
sql = """INSERT INTO Equipo (codigo, nombre, ciudad) \
VALUES ('%s', '%s', '%s');""" % (codigo, nombre, ciudad)

print("Informacion almacenada")

cursor.execute(sql)
conexion.commit()
cursor.close()