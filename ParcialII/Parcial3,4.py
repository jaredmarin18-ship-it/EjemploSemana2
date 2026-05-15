for registro in range(1, 50):
    if registro % 3 == 0:
        continue
    
    if registro == 42:
        print("AMENAZA DETECTADA: Protocolo de parada activado en ID 42.")
        break
        
    print("Procesando registro ID: " + str(registro))