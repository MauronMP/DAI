import random


def setValor(): 
    global cadena
    cadena =  ''.join((random.choice('[]') for i in range(random.randint(2, 10))))
    
def comprobarCadena():
    listaSeparada = list(cadena)
    print(listaSeparada)
    print(len(listaSeparada))
    stack = []
    for i in listaSeparada:
        if i == "[":
            stack.append(i)
        elif i == "]":
            pos = "]"
            if ((len(stack) > 0) and
                ("[" == stack[len(stack)-1])):
                stack.pop()
            else:
                return "Incorrento"
    if len(stack) == 0:
        return "Correcto"
    else:
        return "Incorrento"

def main():
    setValor()
    print(comprobarCadena())

main()