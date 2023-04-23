# Usando un generador
def generar():
  yield "Hola"
  yield "mundo"

for palabra in generar():
  print(palabra)
