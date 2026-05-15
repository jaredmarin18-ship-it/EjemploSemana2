etiqueta = input("Ingrese el código de rastreo (AÑO-CATEGORÍA-PAÍS): ")

if not etiqueta:
    print("Error: La entrada está vacía o es nula. Finalizando programa.")
else:
    categoria = etiqueta[5:-3]
    print("Categoría: " + categoria)

    ruta = "Ruta Local" if etiqueta.endswith("SV") else "Ruta Internacional"
    print("Resultado: " + ruta)