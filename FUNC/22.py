# Usando una base de datos
import sqlite3
conexion = sqlite3.connect("hola.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE saludo (palabra TEXT)")
cursor.execute("INSERT INTO saludo VALUES ('Hola')")
cursor.execute("INSERT INTO saludo VALUES ('mundo')")
cursor.execute("SELECT * FROM saludo")
for fila in cursor.fetchall():
  print(fila[0])
conexion.close()