#ejercocio 3
def aplicar_transformacion(texto, opcion):
    if opcion == 1:
        return texto.upper()
    elif opcion == 2:
        return texto.lower()
    elif opcion == 3:
        return texto.capitalize()
    else:
        return "opcion invalida"


mi_texto = input("escribe un texto: ")
mi_opcion = int(input("elige opcion (1, 2 o 3): "))


resultado = aplicar_transformacion(mi_texto, mi_opcion)

print(f"el resultado es: {resultado}")