notas = []
while True:
    nota = float(input("Ingresa nota (-1 para calcular): "))
    if nota == -1: break
    if 0 <= nota <= 10:
        notas.append(nota)
    else:
        print("Nota inválida")

suma = 0
for n in notas:
    suma += n

if len(notas) > 0:
    print("Promedio:", suma / len(notas))
else:
    print("No se ingresaron notas válidas")