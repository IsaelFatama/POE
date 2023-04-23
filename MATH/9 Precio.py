# Pedir al usuario la cantidad y el precio de cada producto
num_productos = int(input("¿Cuántos productos va a comprar? "))
total = 0
for i in range(num_productos):
    precio = float(input("Precio del producto {}: ".format(i+1)))
    cantidad = int(input("Cantidad del producto {}: ".format(i+1)))
    total += precio * cantidad

# Mostrar el precio total de la compra
print("El precio total de su compra es: {} soles".format(total))
