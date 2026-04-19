usuario_correcto = "admin"
clave_correcta = "1234"


usuario_ingresado = input("Ingrese su usuario: ")
clave_ingresada = input("Ingrese su contraseña: ")


if usuario_ingresado == usuario_correcto and clave_ingresada == clave_correcta:
    print("Acceso permitido")
else:
    print("Acceso denegado")
