while True:
    num = int(input("Tabla del ( -1 para salir): "))
    if num == -1: break
    for i in range(1, 11):
        res = num * i
        if res > 20:
            print(num, "x", i, "=", res)