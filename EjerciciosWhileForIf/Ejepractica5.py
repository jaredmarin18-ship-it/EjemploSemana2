num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("1. Suma")
print("2. Resta")
print("3. Multiplicación")
print("4. División")
opcion = input("Seleccione opción: ")

if opcion == "1":
    resultado = num1 + num2
    print("Resultado:", resultado)
elif opcion == "2":
    resultado = num1 - num2
    print("Resultado:", resultado)
elif opcion == "3":
    resultado = num1 * num2
    print("Resultado:", resultado)
elif opcion == "4":
    if num2 != 0:
        # La división con / siempre devuelve decimales, 
        # usamos // para división entera si quieres evitar el .0
        resultado = num1 // num2
        print("Resultado:", resultado)
    else:
        print("Error: División por cero")
else:
    print("Opción no válida")