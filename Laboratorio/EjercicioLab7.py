# ejercicio7
def aplicar_varias(texto, lista_numeros):
    resultado = texto
    for n in lista_numeros:
        if n == 1:
            resultado = resultado.upper()
        elif n == 2:
            resultado = resultado.lower()
        elif n == 3:
            resultado = resultado.capitalize()
    return resultado

texto = input("escribe un texto: ")

numeros = [int(n) for n in input("escribe los numeros (ejemplo 1,3): ").split(",")]
print("resultado final:", aplicar_varias(texto, numeros))