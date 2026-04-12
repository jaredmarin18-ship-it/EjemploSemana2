texto = "Jared"

texto_preparado = texto.casefold()


analfabeta = texto_preparado.isalpha()

print("Texto normalizado:", texto_preparado)
print("¿Es solo letras?:", analfabeta)