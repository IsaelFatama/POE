import math

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
mcm = (a*b) // math.gcd(a, b)
print(mcm)
