#ejrcicio1
def transformar_texto(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "opcion no valida"


mi_text = input("introduce el texto: ")


mi_opcion = int(input("introduce la opción (1: MAYUS, 2: minuscula, 3: Capital): "))


resultado_final = transformar_texto(mi_text, mi_opcion)


print("Resultado:", resultado_final)