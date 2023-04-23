# Encontrar el máximo y mínimo de una lista de números
lista = [5, 2, 8, 1, 9]
maximo = lista[0]
minimo = lista[0]
for numero in lista:
    if numero > maximo:
        maximo = numero
    if numero < minimo:
        minimo = numero
print("El máximo es:", maximo)
print("El mínimo es:", minimo)
