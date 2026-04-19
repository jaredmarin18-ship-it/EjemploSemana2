nota = int(input("ingrese su nota: "))

if nota > 8 and nota < 11:
    print("Excelente")
elif nota > 6 and nota < 8 : 
    print("Bueno")
elif nota == 6: 
    print("Aprobado")
elif nota < 6:
    print("Reprobado")
else :
    print("Numero no valido")    