# ejercicio 6
def transformar_y_contar(texto, num):
    if num == 1:
        res = texto.upper()
    elif num == 2:
        res = texto.lower()
    elif num == 3:
        res = texto.capitalize()
    else:
        return "opcion invalida"
    return len(res)

texto = input("escribe un texto: ")
num = int(input("elige 1, 2 o 3: "))
print("la longitud es:", transformar_y_contar(texto, num))