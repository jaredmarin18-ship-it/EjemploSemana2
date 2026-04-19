compra = int(input("Ingrese el monto de compra "))

if compra > 100:
    print("Usted tiene 20 prociento de descuento")
elif compra > 50 and compra < 100 :
    print("Usted tiene 10 prociento de descuento")
elif compra < 50 :
    print("Usted no tiene descuento")