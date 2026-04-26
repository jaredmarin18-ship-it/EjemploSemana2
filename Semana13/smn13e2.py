pos, neg = 0, 0
while True:
    num = int(input("Ingresa un número (0 para finalizar): "))
    if num == 0: break
    if num > 0: pos += 1
    elif num < 0: neg += 1

resumen = ["Positivos: " + str(pos), "Negativos: " + str(neg)]
for r in resumen:
    print(r)