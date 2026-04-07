#ejercicio 5
def transformar(texto, numero):
    if numero == 1:
        return texto.upper()
    elif numero == 2:
        return texto.lower()
    elif numero == 3:
        return texto.capitalize()
    else:
        return "opcion invalida"

texto = input("escribe algo: ")
num = int(input("elige 1, 2 o 3: "))
print(transformar(texto, num))