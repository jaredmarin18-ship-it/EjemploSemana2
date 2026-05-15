from decimal import Decimal

total_acumulado = Decimal("0.0")

while True:
    entrada = input("Ingrese el precio del producto (o 0 para finalizar): ")
    
    try:
        precio = Decimal(entrada)
        
        if precio == 0:
            break
            
        total_acumulado = total_acumulado + precio
        
    except:
        print("Advertencia: El valor ingresado no es un número válido. Intente de nuevo.")

print("Cobro finalizado. El total acumulado es: $" + str(total_acumulado))


