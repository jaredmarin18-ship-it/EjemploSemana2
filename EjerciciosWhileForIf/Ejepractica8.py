lado1 = int(input("ingrese el primer lado: "))
lado2 = int(input("ingrese el segundo lado: "))
lado3 = int(input("ingrese el tercer lado: "))

if lado1 == lado2 and lado2 == lado3:
    print("El triangulo es equilatero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triangulo es isoceles")
else:
    print("El triangulo es escaleno")