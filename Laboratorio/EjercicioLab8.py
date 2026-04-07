# ejercicio 8
def menu():
    texto = input("escribe tu texto: ")
    print("1: mayusculas, 2: minusculas, 3: primera mayuscula")
    opcion = int(input("que quieres hacer?: "))
    
    if opcion == 1:
        print(texto.upper())
    elif opcion == 2:
        print(texto.lower())
    elif opcion == 3:
        print(texto.capitalize())
    else:
        print("opcion no valida")

menu()