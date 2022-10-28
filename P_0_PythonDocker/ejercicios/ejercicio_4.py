import re

def primerApartado(num):
	primo = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):
		if (primo[p] == True):
			for i in range(p * p, num+1, p):
				primo[i] = False
		p += 1

	for p in range(2, num+1):
		if primo[p]:
			print(p)


# Identificar cualquier palabra seguida de un espacio y una única letra mayúscula (por ejemplo: Apellido N).
def segundoApartado():
    mensaje_1 = "El chic0 N llamado Joselito A guiterfiltrados iba por la calle numero A"
    filtrado = (mensaje_1.split())
    for i in range(len(filtrado)-1):
        if(filtrado[i].isalpha() and filtrado[i+1].isupper() and len(filtrado[i+1])==1):
            print("Composiciones: ", filtrado[i], "", filtrado[i+1])

# Identificar correos electrónicos válidos (empieza por una expresión genérica y ve refinándola todo lo posible).
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
 
def tercerApartado(email):
    if(re.fullmatch(regex, email)):
        print("Correo valido")
    else:
        print("Correo invalido")


def cuartoApartado(tarjeta):
    contador = 0
    for i in range(len(tarjeta)):
        if(i==4 or i==9 or i ==14 or i==19):
            if(tarjeta[i]==" " or tarjeta[i]=="-"):
                sigue=True
            else:
                sigue=False
                break
        elif (re.match(r'\d',tarjeta[i])):
            sigue=True
        else:
            sigue=False
            break
    return sigue

def main():
    primerApartado(50)
    segundoApartado()
    tercerApartado("zapato.com")
    tercerApartado("zapato@¬¬¬.com")
    tercerApartado("zapato@gmail.com")
    print(cuartoApartado("1324 5214 9658 6325"))
    print(cuartoApartado("1324-5244-9758-6325"))
    print(cuartoApartado("1324/5244-9758 6325"))
    print(cuartoApartado("1324 52d4 9&58 63m5"))

main()