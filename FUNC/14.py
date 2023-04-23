# Usando un descriptor
class Descriptor:
  def __get__(self, instance, owner):
    print("Hola mundo")

class Clase:
  atributo = Descriptor()

c = Clase()
c.atributo