import random
secreto = random.randint(1, 50)
intentos = []
print("Adivina el número entre 1 y 50")

while True:
    tiro = int(input("Tu intento: "))
    intentos.append(tiro)
    if tiro == secreto:
        print("¡Ganaste!")
        break
    elif tiro < secreto:
        print("Es mayor")
    else:
        print("Es menor")

for i in range(len(intentos)):
    print("Intento", i + 1, ":", intentos[i])