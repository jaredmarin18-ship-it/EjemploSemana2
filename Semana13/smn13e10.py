acumulado = 0
numeros = []
while acumulado <= 100:
    print("Llevas", acumulado)
    n = int(input("Suma otro: "))
    if n >= 0:
        acumulado += n
        numeros.append(n)
    else:
        print("Negativo ignorado")

print("Números válidos que sumaste:")
for n in numeros:
    print(n)