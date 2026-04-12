palabra = "CANTANDO"

palabra_minuscula = palabra.lower()
raiz_palabra = palabra_minuscula.removesuffix("ando")
indice_t = raiz_palabra.find("t")

print("Palabra final:", raiz_palabra)
print("La letra 't' está en el índice:", indice_t)