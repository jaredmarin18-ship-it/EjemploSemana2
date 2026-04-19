añoo = int(input("Ingrese un año: "))

if añoo % 4 == 0 and añoo % 100 != 0 or añoo % 400 == 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")