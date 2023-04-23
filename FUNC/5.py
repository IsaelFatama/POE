# Usando una clase
class Mundo:
  def __init__(self):
    self.mensaje = "Hola mundo"

  def decir(self):
    print(self.mensaje)

m = Mundo()
m.decir()