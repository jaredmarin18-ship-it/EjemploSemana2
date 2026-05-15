lecturas = []

for i in range(5):
    dato = int(input("Ingrese la temperatura: "))
    lecturas.append(dato)

print("--- RESULTADOS DEL MONITOREO ---")

for t in lecturas:
    match t:
        case 0:
            print("Temperatura " + str(t) + ": Alerta: Punto de Congelación")
        case 100:
            print("Temperatura " + str(t) + ": Alerta: Punto de Ebullición")
        case _:
            estado = "Estable" if 10 <= t <= 30 else "Fuera de Rango"
            print("Temperatura " + str(t) + ": " + estado)