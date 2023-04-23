# Usando un contexto
class Contexto:
  def __enter__(self):
    print("Hola mundo")
  
  def __exit__(self, exc_type, exc_value, traceback):
    pass

with Contexto():
  pass