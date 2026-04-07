#ejercicio 2
def mostrar_transformacion(palabra, numero):
    if numero == 1:
        print(palabra.upper())
    elif numero == 2:
        print(palabra.lower())
    elif numero == 3:
        print(palabra.capitalize())
    else:
        print("opcion invalida")

p = input("escribe una palabra: ")
n = int(input("escribe el número de transformacion: "))


mostrar_transformacion(p, n)