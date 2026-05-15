nombre_completo = input("Ingrese su nombre y apellido: ")

palabras = nombre_completo.split()
lista_invertida = palabras[::-1]

for palabra in lista_invertida:
    resultado_palabra = ""
    
    for i in range(len(palabra)):
        letra = palabra[i]
        if i < len(palabra) - 1:
            resultado_palabra = resultado_palabra + letra + "."
        else:
            resultado_palabra = resultado_palabra + letra
            
    print(resultado_palabra)