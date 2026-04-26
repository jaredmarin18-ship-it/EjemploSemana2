correcta = "python123"
intentos = []
while True:
    contra = input("Contraseña: ")
    if contra == correcta:
        print("Acceso concedido")
        break
    else:
        print("Incorrecta")
        intentos.append(contra)

for i in range(len(intentos)):
    print("Fallo", i + 1, ":", intentos[i])
    