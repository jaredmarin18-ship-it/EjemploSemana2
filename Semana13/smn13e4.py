impares = []
suma = 0
while True:
    num = int(input("Ingresa número (0 para salir): "))
    if num == 0: break
    if num % 2 != 0:
        suma += num
        impares.append(num)

print("Suma total:", suma)
for n in impares:
    print("Número impar ingresado:", n)