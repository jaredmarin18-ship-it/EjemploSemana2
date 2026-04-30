equipo = ["Audifono", "Celulares", "Cargadores"]
stock_individual = [0, 0, 0]

while True:
    print("1- Ver, 2- Añadir, 3- Salir")
    opcion = input("Opcion: ")

    if opcion == "3":
        break

    if opcion == "2":
        print("0- Audifono, 1- Celulares, 2- Cargadores")
        indice = int(input("Numero de producto: "))
        cantidad = int(input("Cantidad: "))
        stock_individual[indice] = stock_individual[indice] + cantidad

    if opcion == "1":
        for i in range(len(equipo)):
            nombre = equipo[i]
            cantidad = stock_individual[i]
            print("Equipo:", nombre, "- Cantidad:", cantidad)
            
            match nombre:
                case "Audifono":
                    print("Tipo: Accesorio")
                case "Celulares":
                    print("Tipo: Dispositivo")
                case "Cargador":
                    print("Tipo: Accesorio")