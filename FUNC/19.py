# Usando una cola
from queue import Queue
cola = Queue()
cola.put("Hola")
cola.put("mundo")
while not cola.empty():
  print(cola.get())