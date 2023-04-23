vertices = int(input("Ingrese la cantidad de vértices de la figura: "))

if vertices < 3:
    print("No se puede formar una figura con menos de 3 vértices")
elif vertices == 3:
    print("La figura es un triángulo")
elif vertices == 4:
    print("La figura es un cuadrilátero")
elif vertices == 5:
    print("La figura es un pentágono")
elif vertices == 6:
    print("La figura es un hexágono")
elif vertices == 7:
    print("La figura es un heptágono")
elif vertices == 8:
    print("La figura es un octógono")
else:
    print("La figura tiene demasiados vértices para contar los lados")
