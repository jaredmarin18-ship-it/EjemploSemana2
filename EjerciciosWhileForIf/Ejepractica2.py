edad = int(input("ingrese la edad: "))

if edad < 18:
    print("Esta persona es menor de edad")
elif edad > 18 and edad < 60 : 
    print("está persona es mayor de edad")
elif edad == 60 or edad > 60 : 
    print("Es un adulto mayor")

