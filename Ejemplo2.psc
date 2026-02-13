Algoritmo Ejemplo2
	Definir cajero, cuentaDeAhorro, numeroDeCuenta, cantidadSaliente, Saldo, preguntar Como Entero
	cuentaDeAhorro = 1000
	numeroDeCuenta = 12345
	Escribir "Bienvenido"
	Escribir "Actividad que desea relizar"
	Escribir "1 para consultar"
	Escribir "2 para retirar dinero de la cuenta de ahorro"
	
	Escribir "Escriba el nùmero de cuenta a operar"
	Leer preguntar

	si preguntar == 1
		Escribir "Escriba el nùmero de cuenta a operar"
		Leer preguntar
		
		si preguntar ==numeroDeCuenta
		Escribir "Su saldo es" , cuentaDeAhorro
		FinSi
	FinSi
	si preguntar == 2
		Escribir "Escriba el nùmero de cuenta a operar"
		Leer preguntar
		
		si preguntar <= cuentaDeAhorro
			Escribir "procesando" 
			Escribir "Su saldo actual es de" , Saldo
		FinSi
	FinSi

	
FinAlgoritmo
