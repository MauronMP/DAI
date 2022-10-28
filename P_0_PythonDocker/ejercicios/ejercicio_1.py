#Criba de Eratóstenes
#Obtener las lista de números a evaluar
try:
	limite = int(input("Limite: "))
	primos = []
	numeros= []

	for i in range(1,limite+1):
		numeros.append(True)
	#Recorrer los números y para cada uno
	for n in range(2, limite):
		#Si es primo recorrer los múltiplos y marcarlos como no primo
		if numeros[n]:
			for i in range(n*n,limite,n):
				numeros[i] = False
	#Mostrar la lista de los primos
	print("Primos: ")
	for n in range(2, limite):
		if numeros[n]:
			print(str(n)+" ")
except ValueError:
	print("Escribe un numero, te has equivocado")