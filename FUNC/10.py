# Usando un decorador
def decorar(func):
  def envolver():
    print("Hola mundo")
    func()
  return envolver

@decorar
def adios():
  print("Adiós mundo")

adios()