#ejercicio 4
def transformar_lista(lista, opcion):
    nueva = []
    for palabra in lista:
        if opcion == 1:
            nueva.append(palabra.upper())
        elif opcion == 2:
            nueva.append(palabra.lower())
        elif opcion == 3:
            nueva.append(palabra.capitalize())
        else:
            return "opcion invalida"
    return nueva

entrada = input("escribe varias palabras separadas por espacios: ")
lista = entrada.split()
opcion = int(input("elige 1, 2 o 3: "))
print(transformar_lista(lista, opcion))