# Calcular el descuento en una compra según el monto total
monto = float(input("Ingrese el monto: "))
descuentoEspecifico = float(input("Ingrese el descuento en decimales: "))
if monto >= 1000:
    descuento = descuentoEspecifico * monto
monto_descuento = monto - descuento
print(monto_descuento)
