# Pedir al usuario la velocidad y el tiempo
velocidad = float(input("Introduce la velocidad del coche en km/h: "))
tiempo = float(input("Introduce el tiempo de viaje en horas: "))

# Calcular la distancia recorrida
distancia = velocidad * tiempo

# Mostrar el resultado al usuario
print("El coche ha recorrido una distancia de", distancia, "kilómetros")
