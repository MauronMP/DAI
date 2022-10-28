def fibonacci(n):
    if(n>1):
        return fibonacci(n-1) + fibonacci(n-2)
    elif(n==1):
        return 1
    elif (n==0):
        return 0
    else:
        print("Escribe un numero positivo")

def mostrarLista(limite):
    for i in range(limite):
        print(fibonacci(i))

def main():
    f = open('numeroFibonacci.txt', 'rt', encoding='utf-8')
    for line in f:   ## iterates over the lines of the file
        limite = int(line)
    f.close()
    mostrarLista(limite)

main()