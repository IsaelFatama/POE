# Usando una metaclase
class Meta(type):
  def __new__(cls, name, bases, attrs):
    print("Hola mundo")
    return super().__new__(cls, name, bases, attrs)

class Clase(metaclass=Meta):
  pass