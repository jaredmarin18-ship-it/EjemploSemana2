nombre = "ING. Jared Emanuel Marin Rodriguez .txt"

remover = nombre.removesuffix(".txt")

prefijo = remover.removeprefix("ING.")

separar = prefijo.lower().split()

print("resultado",separar)




