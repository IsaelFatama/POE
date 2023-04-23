# Usando un archivo
with open("hola.txt", "w") as archivo:
  archivo.write("Hola mundo")

with open("hola.txt", "r") as archivo:
  print(archivo.read())