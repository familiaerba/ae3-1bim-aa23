from scriptBaseDatos import conexion

cursor = conexion.cursor()

codigo = 1
nombre = "Damian Diaz"
nombreEquipo = "Barcelona"
edad = 37
sql = """INSERT INTO Jugador (codigo, nombre, nombreEquipo, edad) \
VALUES ('%d', '%s', '%s', '%d');""" % (codigo, nombre, nombreEquipo,edad)

cursor.execute(sql)

codigo = 2
nombre = "Luis Leon"
nombreEquipo = "Emelec"
edad = 30
sql = """INSERT INTO Jugador (codigo, nombre, nombreEquipo, edad) \
VALUES ('%d', '%s', '%s', '%d');""" % (codigo, nombre, nombreEquipo,edad)

cursor.execute(sql)

codigo = 3
nombre = "Ronie Carrillo"
nombreEquipo = "Nacional"
edad = 26
sql = """INSERT INTO Jugador (codigo, nombre, nombreEquipo, edad) \
VALUES ('%d', '%s', '%s', '%d');""" % (codigo, nombre, nombreEquipo,edad)
print("Informacion almacenada")

cursor.execute(sql)
conexion.commit()
cursor.close()